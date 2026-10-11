"""Update the progress table in README.md by running each problem's tests.

Usage:  python tools/progress.py

For every problem file it reads the title, link, difficulty and pattern from the
docstring, runs that problem's tests, and marks it as:
  Solved       all tests pass
  Failing      written but some tests fail
  Not started  still raises NotImplementedError (tests skipped)
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- progress:start -->", "<!-- progress:end -->"


def problems() -> list[dict]:
    found = []
    for path in sorted((ROOT / "problems").glob("*/*.py")):
        if path.name in {"__init__.py", "node.py"}:
            continue
        text = path.read_text(encoding="utf-8")
        doc = re.search(r'"""(.*?)"""', text, re.S)
        func = re.search(r"^def (\w+)\(", text, re.M)
        if not doc or not func:
            continue
        lines = [l.strip() for l in doc.group(1).strip().splitlines()]
        meta = re.search(r"Difficulty:\s*(\w+)\s+Pattern:\s*(.+)", doc.group(1))
        found.append({
            "title": lines[0],
            "link": lines[1],
            "difficulty": meta.group(1) if meta else "",
            "pattern": meta.group(2).strip() if meta else "",
            "topic": path.parent.name.replace("_", " ").capitalize(),
            "file": path.relative_to(ROOT).as_posix(),
            "test": f"test_{func.group(1)}",
        })
    return found


def status(test_name: str) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--tb=no", "-p", "no:cacheprovider", "-k", test_name],
        cwd=ROOT, capture_output=True, text=True,
    )
    out = result.stdout
    passed = int(m.group(1)) if (m := re.search(r"(\d+) passed", out)) else 0
    failed = int(m.group(1)) if (m := re.search(r"(\d+) failed", out)) else 0
    if failed:
        return "❌ Failing"
    if passed:
        return "✅ Solved"
    return "⬜ Not started"


def main() -> None:
    rows = []
    solved = 0
    items = problems()
    for p in items:
        s = status(p["test"])
        solved += s.startswith("✅")
        rows.append(f"| [{p['title']}]({p['link']}) | {p['topic']} | {p['pattern']} | {p['difficulty']} | "
                    f"[code]({p['file']}) | {s} |")
    table = "\n".join([
        f"**{solved} of {len(items)} solved**",
        "",
        "| Problem | Topic | Pattern | Difficulty | My solution | Status |",
        "|---|---|---|---|---|---|",
        *rows,
    ])
    readme = README.read_text(encoding="utf-8")
    new = re.sub(f"{re.escape(START)}.*?{re.escape(END)}", f"{START}\n{table}\n{END}", readme, flags=re.S)
    README.write_text(new, encoding="utf-8")
    print(f"{solved} of {len(items)} solved. README.md updated.")


if __name__ == "__main__":
    main()
