---
title: "I built a Python tool that extracts tables from PDFs and exports to Excel automatically"
published: true
tags: python, automation, productivity, opensource
---

Every week I saw the same thing at work: someone opening a PDF, manually copying a table into Excel, cell by cell. 30 minutes of work that should take 2 seconds.

So I built a tool to fix it.

## What it does

```bash
python extract_tables.py financial_report.pdf
```

That's it. You get a formatted `.xlsx` file with every table from the PDF, organized into separate sheets with styled headers, alternating rows, and auto-fitted columns.

## The tech stack

Three libraries. That's all:

- **pdfplumber** — opens the PDF and extracts table data page by page
- **pandas** — structures the raw data into DataFrames
- **openpyxl** — writes to Excel with formatting

No OCR. No Java. No external APIs. Pure Python.

## The core extraction — 15 lines

```python
import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    results = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()
            for t_idx, raw_table in enumerate(tables, start=1):
                header = raw_table[0]
                rows = raw_table[1:]
                df = pd.DataFrame(rows, columns=header)
                results.append({"page": page_num, "table_index": t_idx, "dataframe": df})
    return results
```

pdfplumber does the heavy lifting. It detects table boundaries from the PDF's internal structure — no guessing, no heuristics for basic cases.

## Why it's useful for real work

PDF reports are everywhere: government data, supplier invoices, financial statements, logistics documents. Most of them have tables. None of them are easy to work with.

This tool is for the analyst who gets a 20-page PDF every Monday morning and needs the data in Excel by 9am.

## Get the full code

GitHub: [github.com/YOUR_USERNAME/pdf-to-excel](https://github.com/YOUR_USERNAME/pdf-to-excel)

Includes the full CLI script, a sample PDF generator for testing, and instructions to run it in under 2 minutes.

## What's coming next

- Batch mode for processing multiple PDFs at once
- Streamlit UI for non-technical users
- OCR support for scanned PDFs

---

This is part of a Python automation toolkit I'm building in public. If you work with PDFs regularly, try it and let me know what breaks — real-world PDFs are always messier than test cases.
