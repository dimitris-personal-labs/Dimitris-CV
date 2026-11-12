#!/usr/bin/env python3
"""Build the English and Greek CVs (Word .docx) from the website's data files.

Usage (from the repository folder):

    python3 tools/build_cv.py            # writes assets/dimitrios-asimopoulos-cv-{en,el}.docx
    python3 tools/build_cv.py --pdf      # also converts them to PDF with Microsoft Word

The content comes from data/profile.js, data/projects.js and
data/publications.js, so the CV always matches the website.
Requires: python-docx, Node.js (to read the data files).
"""

import datetime
import json
import os
import re
import subprocess
import sys
import unicodedata

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_TAB_ALIGNMENT, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.shared import Cm, Pt, RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCENT = RGBColor(0x0F, 0x77, 0x69)
INK = RGBColor(0x15, 0x21, 0x1D)
MUTED = RGBColor(0x55, 0x60, 0x5C)
FONT = "Calibri"
OWN_NAME = re.compile(r"D\. (?:C\. )?Asimopoulos")

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
MONTHS_EL = ["Ιανουάριος", "Φεβρουάριος", "Μάρτιος", "Απρίλιος", "Μάιος", "Ιούνιος",
             "Ιούλιος", "Αύγουστος", "Σεπτέμβριος", "Οκτώβριος", "Νοέμβριος", "Δεκέμβριος"]

LABELS = {
    "en": {
        "cv": "Curriculum Vitae",
        "summary": "Professional Summary",
        "experience": "Work Experience",
        "education": "Education",
        "projects": "EU Research Projects",
        "publications": "Publications",
        "skills": "Digital Skills",
        "languages": "Languages",
        "certifications": "Certifications",
        "ongoing": "ongoing",
        "phone": "Phone",
        "updated": "Last updated",
        "page": "Page",
        "of": "of",
        "projects_intro": "Through MetaMind Innovations P.C.",
        "publications_intro": "{n} peer-reviewed publications, newest first.",
    },
    "el": {
        "cv": "Βιογραφικό Σημείωμα",
        "summary": "Επαγγελματικό Προφίλ",
        "experience": "Επαγγελματική Εμπειρία",
        "education": "Εκπαίδευση",
        "projects": "Ευρωπαϊκά Ερευνητικά Έργα",
        "publications": "Δημοσιεύσεις",
        "skills": "Ψηφιακές Δεξιότητες",
        "languages": "Γλώσσες",
        "certifications": "Πιστοποιήσεις",
        "ongoing": "σε εξέλιξη",
        "phone": "Τηλ.",
        "updated": "Τελευταία ενημέρωση",
        "page": "Σελίδα",
        "of": "από",
        "projects_intro": "Μέσω της MetaMind Innovations P.C.",
        "publications_intro": "{n} δημοσιεύσεις με κρίση, από τις πιο πρόσφατες.",
    },
}


# ---------------------------------------------------------------- data

def load_data():
    js = r"""
      global.window = {};
      const fs = require("fs"), vm = require("vm"), path = require("path");
      for (const f of ["profile.js", "projects.js", "publications.js"]) {
        vm.runInThisContext(fs.readFileSync(path.join(process.argv[1], "data", f), "utf8"));
      }
      process.stdout.write(JSON.stringify({
        profile: window.CV_PROFILE, projects: window.CV_PROJECTS, publications: window.CV_PUBLICATIONS
      }));
    """
    out = subprocess.run(["node", "-e", js, ROOT], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def month_value(mm_yyyy):
    month, year = mm_yyyy.split("/")
    return int(year) * 100 + int(month)


def sorted_publications(pubs):
    def key(p):
        m = MONTHS.index(p["month"]) if p.get("month") in MONTHS else -1
        return (-p["year"], -m)
    return sorted(pubs, key=key)


# ---------------------------------------------------------------- docx helpers

def set_run(run, size=None, bold=None, italic=None, color=None):
    run.font.name = FONT
    run._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    run._element.rPr.rFonts.set(qn("w:cs"), FONT)
    if size: run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if italic is not None: run.italic = italic
    if color is not None: run.font.color.rgb = color
    return run


def add_text(par, text, **fmt):
    return set_run(par.add_run(text), **fmt)


def add_link(par, text, url, size=None, bold=False, color=ACCENT, underline=True):
    r_id = par.part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        fonts.set(qn(attr), FONT)
    rpr.append(fonts)
    if bold:
        rpr.append(OxmlElement("w:b"))
    col = OxmlElement("w:color")
    col.set(qn("w:val"), str(color))
    rpr.append(col)
    if underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        rpr.append(u)
    if size:
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), str(int(size * 2)))
        rpr.append(sz)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    par._p.append(link)


def spacing(par, before=0, after=0, line=None, keep_next=False):
    pf = par.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    if line: pf.line_spacing = line
    pf.keep_with_next = keep_next
    return par


def bottom_border(par, color="0F7769", size=8):
    ppr = par._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), str(size))
    b.set(qn("w:space"), "2")
    b.set(qn("w:color"), color)
    bdr.append(b)
    ppr.append(bdr)


def right_tab(par, doc):
    sec = doc.sections[0]
    width = sec.page_width - sec.left_margin - sec.right_margin
    par.paragraph_format.tab_stops.add_tab_stop(width, WD_TAB_ALIGNMENT.RIGHT)


def add_field(par, instr, **fmt):
    for kind, text in (("begin", None), ("instr", instr), ("separate", None), ("text", "1"), ("end", None)):
        run = set_run(par.add_run(), **fmt)
        if kind == "instr":
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = f" {text} "
            run._r.append(el)
        elif kind == "text":
            run.text = text
        else:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
            run._r.append(el)


def heading(doc, text):
    p = spacing(doc.add_paragraph(), before=11, after=5, keep_next=True)
    # Greek capitals are written without accents (ΓΛΏΣΣΕΣ -> ΓΛΩΣΣΕΣ).
    upper = unicodedata.normalize("NFD", text.upper()).replace("́", "")
    add_text(p, unicodedata.normalize("NFC", upper), size=11, bold=True, color=ACCENT)
    bottom_border(p)
    return p


def bullet(doc, text, size=10):
    p = doc.add_paragraph(style="List Bullet")
    spacing(p, after=2, line=1.08)
    p.paragraph_format.left_indent = Cm(0.55)
    p.paragraph_format.first_line_indent = Cm(-0.35)
    add_text(p, text, size=size, color=INK)
    return p


def no_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tbl_pr.append(borders)
    mar = OxmlElement("w:tblCellMar")
    for edge in ("left", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), "0")
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tbl_pr.append(mar)


def entry_header(doc, title, right, sub=None):
    # Title and date side by side in a borderless table, so long titles wrap
    # instead of running into the date.
    sec = doc.sections[0]
    width = sec.page_width - sec.left_margin - sec.right_margin
    date_w = Cm(3.4)
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False
    no_borders(table)
    left, right_cell = table.rows[0].cells
    left.width, right_cell.width = width - date_w, date_w
    p = spacing(left.paragraphs[0], before=4, after=0, keep_next=True)
    add_text(p, title, size=10.5, bold=True, color=INK)
    if sub:
        s = spacing(left.add_paragraph(), after=2, keep_next=True)
        add_text(s, sub, size=10, italic=True, color=MUTED)
    r = spacing(right_cell.paragraphs[0], before=5, after=0, keep_next=True)
    r.alignment = 2  # right
    add_text(r, right, size=9.5, color=MUTED)
    return table


def dash(text):
    return text.replace(" - ", " – ")


# ---------------------------------------------------------------- CV

def build(lang, data, today):
    L = LABELS[lang]
    prof = data["profile"]
    contact = prof["contact"]
    P = prof[lang]
    pubs = sorted_publications(data["publications"])
    peer = [p for p in pubs if p.get("type") != "preprint"]
    projects = sorted(data["projects"], key=lambda p: month_value(p["start"]))
    current = today.year * 100 + today.month

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(1.9)
    sec.top_margin, sec.bottom_margin = Cm(1.6), Cm(1.6)
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(10)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    normal.element.rPr.rFonts.set(qn("w:cs"), FONT)
    doc.core_properties.title = f"{contact['name'][lang]} – {L['cv']}"
    doc.core_properties.author = contact["name"]["en"]
    doc.core_properties.language = "el-GR" if lang == "el" else "en-GB"

    # Header block
    p = spacing(doc.add_paragraph(), after=0)
    add_text(p, contact["name"][lang], size=22, bold=True, color=INK)
    p = spacing(doc.add_paragraph(), after=4)
    phd = "Ph.D. Candidate" if lang == "en" else "Υποψήφιος Διδάκτορας"
    add_text(p, f"{contact['role'][lang]}  ·  {phd}", size=11.5, color=ACCENT, bold=True)

    p = spacing(doc.add_paragraph(), after=0)
    add_text(p, f"{contact['location'][lang]}  ·  ", size=9.5, color=MUTED)
    add_link(p, contact["email"], f"mailto:{contact['email']}", size=9.5, color=MUTED, underline=False)
    add_text(p, f"  ·  {L['phone']} {contact['phone']}", size=9.5, color=MUTED)
    p = spacing(doc.add_paragraph(), after=2)
    add_link(p, "LinkedIn", contact["linkedIn"], size=9.5)
    add_text(p, "  ·  ", size=9.5, color=MUTED)
    add_link(p, "Google Scholar", contact["scholar"], size=9.5)
    add_text(p, "  ·  ORCID ", size=9.5, color=MUTED)
    add_link(p, contact["orcid"], f"https://orcid.org/{contact['orcid']}", size=9.5)

    # Summary
    heading(doc, L["summary"])
    p = spacing(doc.add_paragraph(), after=2, line=1.1)
    add_text(p, P["cvSummary"].replace("{publications}", str(len(peer))), size=10, color=INK)

    # Experience
    heading(doc, L["experience"])
    e = P["experience"]
    entry_header(doc, e["title"], dash(e["date"]), sub=f"{e['company']}, {e['location']}")
    for b in e["bullets"]:
        bullet(doc, b)

    # Education
    heading(doc, L["education"])
    for ed in P["education"]:
        entry_header(doc, ed["title"], dash(ed["date"]), sub=ed["org"])
        if ed.get("body"):
            bullet(doc, ed["body"])

    # Projects
    heading(doc, L["projects"])
    p = spacing(doc.add_paragraph(), after=3)
    add_text(p, L["projects_intro"], size=9.5, italic=True, color=MUTED)
    for pr in projects:
        dates = f"{pr['start']} – {pr['end']}" if pr.get("end") else f"{pr['start']} – {L['ongoing']}"
        if pr.get("end") and month_value(pr["end"]) >= current:
            dates += f" ({L['ongoing']})"
        p = spacing(doc.add_paragraph(), before=2, after=0, keep_next=True)
        right_tab(p, doc)
        if pr.get("url"):
            add_link(p, pr["name"], pr["url"], size=10.5, bold=True, color=INK, underline=False)
        else:
            add_text(p, pr["name"], size=10.5, bold=True, color=INK)
        if pr.get("programme"):
            add_text(p, f"  ·  {pr['programme']}", size=9.5, color=ACCENT)
        add_text(p, "\t" + dates, size=9.5, color=MUTED)
        d = spacing(doc.add_paragraph(), after=3, line=1.05)
        add_text(d, pr["description"][lang], size=9.5, color=INK)

    # Publications
    heading(doc, L["publications"])
    p = spacing(doc.add_paragraph(), after=3)
    add_text(p, L["publications_intro"].replace("{n}", str(len(peer))), size=9.5, italic=True, color=MUTED)
    for i, pub in enumerate(pubs, 1):
        p = spacing(doc.add_paragraph(), after=3, line=1.05)
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.first_line_indent = Cm(-0.8)
        p.paragraph_format.tab_stops.add_tab_stop(Cm(0.8))
        add_text(p, f"[{i}]\t", size=9.5, color=ACCENT, bold=True)
        last = 0
        for m in OWN_NAME.finditer(pub["authors"]):
            add_text(p, pub["authors"][last:m.start()], size=9.5, color=INK)
            add_text(p, m.group(0), size=9.5, color=INK, bold=True)
            last = m.end()
        add_text(p, pub["authors"][last:] + ", “", size=9.5, color=INK)
        add_text(p, pub["title"], size=9.5, color=INK, italic=True)
        details = [pub["venue"]]
        if pub.get("pages"): details.append(pub["pages"])
        details.append(f"{pub['month']} {pub['year']}" if pub.get("month") else str(pub["year"]))
        add_text(p, "”, " + ", ".join(details), size=9.5, color=INK)
        if pub.get("doi"):
            add_text(p, ", doi: ", size=9.5, color=INK)
            add_link(p, pub["doi"], f"https://doi.org/{pub['doi']}", size=9.5)
        elif pub.get("url"):
            add_text(p, ", ", size=9.5, color=INK)
            add_link(p, pub["url"], pub["url"], size=9.5)
        add_text(p, ".", size=9.5, color=INK)

    # Skills
    heading(doc, L["skills"])
    for label, items in P["skillGroups"]:
        p = spacing(doc.add_paragraph(), after=2)
        add_text(p, f"{label}: ", size=10, bold=True, color=INK)
        add_text(p, ", ".join(items), size=10, color=INK)

    # Languages
    heading(doc, L["languages"])
    langs = P["languages"]
    p = spacing(doc.add_paragraph(), after=4, keep_next=True)
    add_text(p, langs["motherTongue"], size=10, color=INK)
    table = doc.add_table(rows=1 + len(langs["rows"]), cols=len(langs["headers"]))
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.style = doc.styles["Table Grid"]
    widths = [Cm(3.4)] + [Cm(2.76)] * (len(langs["headers"]) - 1)
    for r, values in enumerate([langs["headers"]] + langs["rows"]):
        for c, val in enumerate(values):
            cell = table.cell(r, c)
            cell.width = widths[c]
            cp = cell.paragraphs[0]
            spacing(cp, before=1, after=1, keep_next=True)  # keep the table on one page
            add_text(cp, val, size=9, bold=(r == 0 or c == 0), color=INK if r else ACCENT)
            if r == 0:
                shd = OxmlElement("w:shd")
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:color"), "auto")
                shd.set(qn("w:fill"), "E7F1EF")
                cell._tc.get_or_add_tcPr().append(shd)
    borders = table._tbl.tblPr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        table._tbl.tblPr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:color"), "C9D6D2")
        borders.append(el)
    p = spacing(doc.add_paragraph(), before=2, after=0)
    levels = ("Levels: A1/A2 basic user · B1/B2 independent user · C1/C2 proficient user"
              if lang == "en" else
              "Επίπεδα: A1/A2 βασικός χρήστης · B1/B2 ανεξάρτητος χρήστης · C1/C2 ικανός χρήστης")
    add_text(p, levels, size=8.5, italic=True, color=MUTED)

    # Certifications
    heading(doc, L["certifications"])
    for title, detail in P["certifications"]:
        p = spacing(doc.add_paragraph(), after=3)
        add_text(p, title, size=10, bold=True, color=INK)
        add_text(p, f" – {detail}", size=10, color=MUTED)

    # Footer
    months = MONTHS_EL if lang == "el" else MONTHS
    fp = sec.footer.paragraphs[0]
    right_tab(fp, doc)
    add_text(fp, f"{contact['name'][lang]} – {L['cv']}  ·  {L['updated']}: {months[today.month - 1]} {today.year}",
             size=8, color=MUTED)
    add_text(fp, f"\t{L['page']} ", size=8, color=MUTED)
    add_field(fp, "PAGE", size=8, color=MUTED)
    add_text(fp, f" {L['of']} ", size=8, color=MUTED)
    add_field(fp, "NUMPAGES", size=8, color=MUTED)

    return doc


def to_pdf(docx_path):
    pdf_path = docx_path[:-5] + ".pdf"
    script = f'''
      tell application "Microsoft Word"
        set theDoc to open file name (POSIX file "{docx_path}" as text)
        save as theDoc file name (POSIX file "{pdf_path}" as text) file format format PDF
        close theDoc saving no
      end tell
    '''
    subprocess.run(["osascript", "-e", script], check=True)
    return pdf_path


def main():
    data = load_data()
    today = datetime.date.today()
    for lang in ("en", "el"):
        path = os.path.join(ROOT, "assets", f"dimitrios-asimopoulos-cv-{lang}.docx")
        build(lang, data, today).save(path)
        print("wrote", os.path.relpath(path, ROOT))
        if "--pdf" in sys.argv:
            print("wrote", os.path.relpath(to_pdf(path), ROOT))


if __name__ == "__main__":
    main()
