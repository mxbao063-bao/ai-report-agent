# ai-report-agent

Turn a CSV file into a concise business report.

This is a portfolio-ready demo for the offer: "I can turn your spreadsheet into an automated weekly report."

## Demo

```bash
python3 report_agent.py examples/sales.csv --output report.md
```

Open `report.md` to see the generated summary.

Sample output: [`examples/sample-report.md`](examples/sample-report.md)

## What It Does

- Reads CSV files with no required dependencies.
- Detects numeric and categorical columns.
- Summarizes totals, averages, min/max values, and missing data.
- Produces a Markdown report with suggested next actions.
- Includes optional Excel support if `openpyxl` is installed.

## Optional Excel Support

```bash
python3 -m pip install openpyxl
python3 report_agent.py data.xlsx --output report.md
```

## Paid Offer

Fixed-price starter version: `$99`.

Client gets:

- Custom input fields
- Branded Markdown report
- README and demo command
- One small revision after review
- Optional scheduled GitHub Action
