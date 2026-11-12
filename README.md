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

Open `data/publications.js` and add a new line at the top of the list:

```js
  "A. Author, D. C. Asimopoulos, “Paper title”, Venue name, pp. 1-6, Month Year.",
```

Keep the quotes around the text and the comma at the end of the line.

## Adding a project

Open `data/projects.js` and add a new block at the end of the list:

```js
  {
    name: "PROJECT",
    dates: "MM/YYYY - MM/YYYY",
    description: {
      en: "Short description in English.",
      el: "Σύντομη περιγραφή στα ελληνικά."
    }
  },
```

After either change, open `index.html` in a browser to check it, then commit and
push. GitHub Pages republishes the site automatically.

Note: the headline numbers at the top of the page ("12 EU research projects",
"11 peer-reviewed publications") are still typed by hand in `index.html`.

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
