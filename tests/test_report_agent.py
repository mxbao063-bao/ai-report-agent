import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from report_agent import build_report, load_csv, parse_number


class ReportAgentTests(unittest.TestCase):
    def test_parse_number_handles_currency_and_commas(self):
        self.assertEqual(parse_number("$1,200"), 1200)

    def test_build_report_summarizes_numeric_columns(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.csv"
            path.write_text("region,revenue\nNorth,100\nSouth,200\n", encoding="utf-8")
            headers, rows = load_csv(path)
            report = build_report(headers, rows, "sample.csv")

        self.assertIn("Rows analyzed: 2", report)
        self.assertIn("| revenue | 300 | 150 | 100 | 200 |", report)
        self.assertIn("| South | 200 |", report)


if __name__ == "__main__":
    unittest.main()
