# Agent instructions

- Read the research question and scope before gathering or editing evidence.
- Register each new source in `data/sources.csv`. Record a stable locator, the access date for online sources, and relevant coverage or limitations.
- Cite material claims at the point of use. Verify that a source supports the claim, and distinguish observations, inferences, and open questions.
- Record collection methods and unresolved gaps in `notes/`. Preserve raw material in an approved location and commit only evidence cleared for the repository's audience.
- Keep credentials, personal data, and confidential material out of Git.
- Edit `report/draft.md` and its evidence inputs. Run `python scripts/build_report.py --check` before finishing and inspect the generated Markdown when changing the report.
