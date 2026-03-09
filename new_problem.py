import argparse
import re
from pathlib import Path


TEMPLATE = """from time import perf_counter


def solve():
    # TODO: implement solution
    return None


if __name__ == "__main__":
    start = perf_counter()
    answer = solve()
    elapsed_ms = (perf_counter() - start) * 1000

    print(answer)
    print(f"Time: {elapsed_ms:.3f} ms")
"""


def next_problem_number(base_dir: Path) -> int:
    pattern = re.compile(r"^p(\d{3})\.py$")
    existing = []

    for path in base_dir.iterdir():
        match = pattern.match(path.name)
        if match:
            existing.append(int(match.group(1)))

    if not existing:
        return 1
    return max(existing) + 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create next Project Euler problem file with timer template."
    )
    parser.add_argument(
        "--number",
        type=int,
        help="Optional explicit problem number (e.g., 9 creates p009.py).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show file that would be created without writing it.",
    )
    args = parser.parse_args()

    base_dir = Path(".").resolve()
    number = args.number if args.number is not None else next_problem_number(base_dir)

    if number < 1:
        raise ValueError("Problem number must be >= 1.")

    target = base_dir / f"p{number:03d}.py"

    if args.dry_run:
        print(target.name)
        return

    if target.exists():
        raise FileExistsError(f"{target.name} already exists.")

    target.write_text(TEMPLATE, encoding="utf-8")
    print(f"Created {target.name}")


if __name__ == "__main__":
    main()
