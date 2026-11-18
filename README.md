# Research Template

Use this template to run an evidence-backed research project. The sample report uses fictional observations about library guide preferences.

1. Select **Use this template** on GitHub to start your project.
2. Define the research question and scope in `report/main.tex`.
3. Register evidence in `data/sources.csv` and add cited sources to `report/sources.bib`. Use the same source IDs in both files.
4. Keep collection methods and open questions in `notes/`. Use LaTeX's `\cite{source-id}` for claims supported by an entry in the bibliography.

## Customize the cover and style

Edit the title, subtitle, short title, author, and status at the top of `report/main.tex`. Set the accent color in `report/style.tex`, which also defines the cover, headings, captions, and running page headers and footers.

The cover artwork is drawn in TikZ. To use a photograph, add `report/cover.jpg` cropped to the US Letter aspect ratio (8.5:11). The cover applies a dark tint to keep the title readable.

## Label evidence

The sample findings show three inline labels. Use `\PrimaryRecord{}` for a direct record of an observation or event, `\FirstPartyStatement{}` for a statement from an organization or person involved, and `\SecondaryReporting{}` for secondary reporting. Cite the underlying source alongside the label and state any limit on what the source establishes.

## Build the PDF

Install a TeX distribution with `latexmk`, `pdflatex`, BibTeX, and the packages listed in `report/style.tex`. On Ubuntu, install `latexmk texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended`. From the repository root, run:

```sh
latexmk -cd -pdf -Werror -interaction=nonstopmode -halt-on-error -outdir=build report/main.tex
```

Open `report/build/main.pdf`. GitHub Actions runs the same command on pushes, pull requests, and manual requests. Download **report-pdf** from the completed **Build report** run.
