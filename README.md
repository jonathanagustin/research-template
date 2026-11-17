# Research Template

Use this template to run an evidence-backed research project. The example follows library visitors choosing between print and digital guides. All example observations are fictional.

1. Select **Use this template** on GitHub to create your project.
2. Define your question and scope in `report/draft.md`.
3. Register evidence in `data/sources.csv`. Give each source a stable ID, a locator, and a short description of what it supports. For local evidence, use a repository-relative path.
4. Keep working notes in `notes/` and cite sources in the draft using `{{cite:SOURCE_ID}}`.
5. Run `python scripts/build_report.py` with Python 3.11 or newer. Open `build/report.md` to review the output. Run `python scripts/build_report.py --check` to validate without writing a report.

GitHub Actions runs the same validation on pushes and pull requests. The project has no third-party Python dependencies or required plugins.
