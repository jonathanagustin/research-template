"""Validate source references and render the Markdown report."""

import argparse
import csv
import re
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FIELDS = ["id", "title", "locator", "accessed", "notes"]
SOURCE_ID = re.compile(r"[a-zA-Z0-9][a-zA-Z0-9_-]*")
CITATION = re.compile(r"\{\{cite:([^{}\r\n]*)\}\}")


def load_sources():
    sources = {}
    with (ROOT / "data/sources.csv").open(encoding="utf-8-sig", newline="") as file:
        rows = csv.DictReader(file)
        if rows.fieldnames != SOURCE_FIELDS:
            raise ValueError("Expected source columns: " + ", ".join(SOURCE_FIELDS))
        for row in rows:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Invalid source row at line {rows.line_num}")
            source_id = row["id"]
            if not SOURCE_ID.fullmatch(source_id) or source_id in sources:
                raise ValueError(f"Invalid or duplicate source ID: {source_id!r}")
            locator = row["locator"].strip()
            if not row["title"].strip() or not locator:
                raise ValueError(f"Source {source_id} needs a title and locator")
            url = urlsplit(locator)
            if url.scheme in {"http", "https"} and url.hostname:
                target = quote(locator, safe=":/?#[]@!$&'()*+,;=%")
            else:
                path = (ROOT / locator).resolve()
                if not path.is_relative_to(ROOT) or not path.is_file():
                    raise ValueError(f"Source {source_id} needs a URL or an existing repository file")
                target = "../" + quote(path.relative_to(ROOT).as_posix())
            title = re.sub(r"([\\\[\]])", r"\\\1", row["title"].strip())
            sources[source_id] = f"[{title}](<{target}>)"
    return sources


def render_report(sources):
    draft = (ROOT / "report/draft.md").read_text(encoding="utf-8")
    cited = {}

    def replace(match):
        source_id = match[1]
        if source_id not in sources:
            raise ValueError(f"Unknown citation: {source_id!r}")
        if source_id not in cited:
            cited[source_id] = len(cited) + 1
        return f"[{cited[source_id]}](#source-{source_id})"

    rendered = CITATION.sub(replace, draft)
    if "{{cite:" in rendered:
        raise ValueError("Malformed citation. Use {{cite:SOURCE_ID}}.")
    if cited:
        references = [
            f'{number}. <a id="source-{source_id}"></a>{sources[source_id]}'
            for source_id, number in cited.items()
        ]
        rendered = rendered.rstrip() + "\n\n## Sources\n\n" + "\n".join(references) + "\n"
    return rendered


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without writing output")
    args = parser.parse_args()
    try:
        report = render_report(load_sources())
        if not args.check:
            output = ROOT / "build/report.md"
            output.parent.mkdir(exist_ok=True)
            output.write_text(report, encoding="utf-8")
        print("Report validated." if args.check else "Wrote build/report.md")
    except (ValueError, OSError, csv.Error) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
