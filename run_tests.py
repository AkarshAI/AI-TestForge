import argparse
import pathlib
import sys

import pytest


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the AI testing framework with optional environment and marker filters."
    )
    parser.add_argument("--env", default="qa", help="Target environment for API/UI tests.")
    parser.add_argument(
        "--report", default="reports/report.html",
        help="Output path for the HTML report.",
    )
    parser.add_argument(
        "--tags",
        default="",
        help="Optional pytest marker expression to select tests.",
    )
    args = parser.parse_args()

    report_path = pathlib.Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    test_args = [
        "-v",
        "-n",
        "auto",
        f"--target-env={args.env}",
        f"--html={report_path}",
        "--self-contained-html",
    ]
    if args.tags:
        test_args.extend(["-m", args.tags])

    return pytest.main(test_args)


if __name__ == "__main__":
    sys.exit(main())
