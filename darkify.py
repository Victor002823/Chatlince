import re
import sys
from pathlib import Path

SCAN_DIRS = ["src/screens", "src/components-next"]
EXCLUDE_SUFFIXES = [".stories.tsx"]

COLOR_NAMES = [
    "gray", "mauve", "slate", "sage", "olive", "sand", "tomato", "red", "ruby",
    "crimson", "pink", "plum", "purple", "violet", "iris", "indigo", "blue",
    "cyan", "teal", "jade", "green", "grass", "brown", "bronze", "gold", "sky",
    "mint", "lime", "yellow", "amber", "orange",
]

PROPS = ["bg", "text", "border", "fill", "stroke", "divide", "ring"]

TOKEN_RE = re.compile(
    r"(?<!dark:)\b(" + "|".join(PROPS) + r")-(white|black|" + "|".join(COLOR_NAMES) + r")(?!Dark)(A)?-?([A-Za-z0-9]+)?\b"
)


def compute_dark_token(prop, color, is_alpha, shade):
    if color == "white":
        dark_color, dark_shade = "grayDark", "50"
    elif color == "black":
        dark_color, dark_shade = "grayDark", "950"
    elif color == "whiteA":
        dark_color, dark_shade = "blackA", shade
    elif color == "blackA":
        dark_color, dark_shade = "whiteA", shade
    elif is_alpha:
        dark_color, dark_shade = f"{color}DarkA", shade
    else:
        dark_color, dark_shade = f"{color}Dark", shade

    if dark_shade:
        return f"dark:{prop}-{dark_color}-{dark_shade}"
    return f"dark:{prop}-{dark_color}"


def process_file(path: Path, apply_changes: bool):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    changed = False
    report = []

    for i, line in enumerate(lines):
        if "colorScheme" in line:
            continue
        if "dark:" not in line and TOKEN_RE.search(line) is None:
            continue

        matches = list(TOKEN_RE.finditer(line))
        if not matches:
            continue

        insertions = []
        for m in matches:
            prop, color, alpha_flag, shade = m.groups()
            is_alpha = bool(alpha_flag)
            full_color = color + ("A" if is_alpha else "")

            dark_token = compute_dark_token(prop, full_color, is_alpha, shade)

            if dark_token in line:
                continue
            if not re.search(r"['\"`]", line):
                continue

            insertions.append((m.end(), " " + dark_token))

        if insertions:
            new_line = line
            for offset, text_to_insert in sorted(insertions, key=lambda x: -x[0]):
                new_line = new_line[:offset] + text_to_insert + new_line[offset:]
            if new_line != line:
                report.append((i + 1, line.strip(), new_line.strip()))
                lines[i] = new_line
                changed = True

    if changed and report:
        if apply_changes:
            path.write_text("\n".join(lines), encoding="utf-8")
        return report
    return []


def main():
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    apply_changes = "--apply" in sys.argv

    total_files = 0
    total_lines = 0
    all_reports = {}

    for scan_dir in SCAN_DIRS:
        d = base / scan_dir
        if not d.exists():
            continue
        for path in d.rglob("*.tsx"):
            if any(str(path).endswith(suf) for suf in EXCLUDE_SUFFIXES):
                continue
            report = process_file(path, apply_changes)
            if report:
                total_files += 1
                total_lines += len(report)
                all_reports[str(path)] = report

    mode = "APLICADO" if apply_changes else "DRY-RUN (nada se escribió)"
    print(f"=== {mode} ===")
    print(f"Archivos afectados: {total_files}")
    print(f"Líneas modificadas: {total_lines}\n")

    for fpath, report in all_reports.items():
        print(f"--- {fpath} ({len(report)} líneas) ---")
        for lineno, before, after in report[:5]:
            print(f"  L{lineno}:")
            print(f"    - {before}")
            print(f"    + {after}")
        if len(report) > 5:
            print(f"  ... y {len(report) - 5} líneas más")
        print()


if __name__ == "__main__":
    main()
