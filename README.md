# Dimitrios Christos Asimopoulos CV Website

Static bilingual portfolio / CV website for GitHub Pages.

## Files

- `index.html`: page layout, the rest of the content and the language switcher
- `data/publications.js`: list of publications (edit this to add a paper)
- `data/projects.js`: list of EU research projects, in English and Greek (edit this to add a project)
- `styles.css`: responsive styling
- `assets/dimitrios-asimopoulos-photo.jpg`: profile photo
- `assets/dimitrios-asimopoulos-cv-en.docx`: English CV download
- `assets/dimitrios-asimopoulos-cv-el.docx`: Greek CV download

## Adding a paper

Open `data/publications.js` and add a new block anywhere in the list (the site
sorts papers by year and month automatically):

```js
  {
    authors: "A. Author, D. C. Asimopoulos, B. Author",
    title: "Paper title",
    venue: "Conference or journal name",
    pages: "pp. 1-6",
    month: "June",
    year: 2026,
    type: "conference",
    doi: "10.xxxx/xxxxx"
  },
```

`pages`, `month` and `doi` are optional; delete those lines if you don't have
them. With a `doi`, the title links to the paper; without one you can add
`url: "https://..."` instead (e.g. an arXiv page). `type` is `"journal"`,
`"conference"` or `"preprint"`; preprints are not counted as peer-reviewed.
Your name is shown in bold automatically. Keep the quotes,
the commas between fields and the comma after the closing `}`. The site
builds the citation text from these fields.

## Adding a project

Open `data/projects.js` and add a new block anywhere in the list (the site sorts
projects by start date):

```js
  {
    name: "PROJECT",
    start: "MM/YYYY",
    end: "MM/YYYY",
    description: {
      en: "Short description in English.",
      el: "Σύντομη περιγραφή στα ελληνικά."
    }
  },
```

Use the official project dates. While the end date hasn't passed yet, the site
adds "(ongoing)" / "(σε εξέλιξη)" automatically. `programme` and `url` are
optional extra lines, e.g. `programme: "Horizon Europe",` and
`url: "https://...",`; with a url, the project name becomes a link.

After either change, open `index.html` in a browser to check it, then commit and
push. GitHub Pages republishes the site automatically.

The headline numbers at the top of the page (EU research projects and
peer-reviewed publications) are counted automatically from these two files.

## Preview locally

Open `index.html` directly in a browser.

## Free hosting with GitHub Pages

1. Create a GitHub repository, for example `cv`.
2. Upload everything inside this folder: `index.html`, `styles.css`, `README.md`, and the `assets` folder.
3. Go to `Settings` -> `Pages`.
4. Choose `Deploy from a branch`.
5. Select branch `main` and folder `/root`.
6. Click `Save`.

The site will be available at:

`https://username.github.io/cv/`

If the repository is named exactly `username.github.io`, the site will be:

`https://username.github.io/`

## Privacy note

The webpage shows Thessaloniki, Greece instead of the full street address.
The downloadable DOCX files are copies of the original CV files and may contain
the full contact details from those documents.
