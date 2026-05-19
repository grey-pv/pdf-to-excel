<div align="center">

# 📄 → 📊 PDF to Excel Extractor

**Extract tables from any PDF file and export to a formatted Excel spreadsheet — in one command.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange)](CONTRIBUTING.md)
[![pdfplumber](https://img.shields.io/badge/Powered%20by-pdfplumber-blueviolet)](https://github.com/jsvine/pdfplumber)

</div>

---

> **Stop copying tables from PDFs by hand.**
> This Python tool extracts every table from any PDF and exports it to a clean, formatted Excel file automatically.

---

## 🎯 The Problem It Solves

Every week, analysts, assistants, and developers waste hours manually copying data from PDF reports into Excel spreadsheets. This tool eliminates that entirely.

**Who this is for:**
- 📊 Data analysts working with PDF reports
- 🧾 Finance teams extracting invoice or statement data
- 🏢 Office workers dealing with government or supplier PDFs
- 🐍 Python developers who want a simple automation script to study or extend

---

## ✨ Features

- ✅ Extracts **all tables** from every page of a PDF automatically
- ✅ Exports to a **professionally formatted Excel workbook**
- ✅ One **sheet per table**, named by page number and table index
- ✅ **Frozen header row** so long tables stay readable
- ✅ **Auto-fitted column widths** for clean presentation
- ✅ Handles **multi-page PDFs** with no extra configuration
- ✅ **Descriptive terminal output** — see exactly what was found
- ✅ Custom output path via `--output` flag
- ✅ Zero configuration — works out of the box

---

## 🚀 Quick Start

### Requirements

- Python 3.10 or higher
- pip

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/pdf-to-excel.git
cd pdf-to-excel
pip install -r requirements.txt
```

### Usage

```bash
# Extract tables from a PDF (output saved as report.xlsx)
python extract_tables.py report.pdf

# Specify a custom output path
python extract_tables.py report.pdf --output my_data.xlsx

# See all options
python extract_tables.py --help
```

---

## 📸 Example Output

**Terminal:**
```
📄 PDF to Excel Extractor
────────────────────────────────────────
  Input  : financial_report.pdf
  Output : financial_report.xlsx
────────────────────────────────────────
  → Scanning 4 page(s)...
  ✓ Page 1 – Table 1: 12 rows × 5 columns
  ✓ Page 2 – Table 1:  8 rows × 3 columns
  ✓ Page 3 – Table 1: 20 rows × 6 columns

📊 Exporting 3 table(s) to Excel...

✅ Done! File saved to: financial_report.xlsx
   3 table(s) extracted across 3 page(s).
────────────────────────────────────────
```

**Excel result:** dark blue headers, alternating row shading, frozen top row, auto-width columns — ready to share or analyze immediately.

---

## ⚙️ CLI Options

| Option | Short | Description |
|---|---|---|
| `--output FILE` | `-o` | Custom output file path (default: same name as PDF) |
| `--help` | `-h` | Show help message and exit |

---

## 🗂️ Project Structure

```
pdf-to-excel/
├── extract_tables.py        ← Main script — run this
├── generate_sample_pdf.py   ← Creates a demo PDF for testing
├── requirements.txt         ← 3 dependencies only
├── README.md
├── samples/                 ← Place your input PDFs here
└── output/                  ← Suggested folder for results
```

---

## 🧠 How It Works

```
Your PDF file
      │
      ▼
 pdfplumber       ← Opens the PDF, detects and extracts table data page by page
      │
      ▼
   pandas          ← Converts raw table rows into structured DataFrames
      │
      ▼
  openpyxl         ← Writes each table to Excel with formatting applied
      │
      ▼
  output.xlsx      ← Styled spreadsheet, one sheet per table, ready to use
```

**No OCR. No internet connection. No external services. Pure Python.**

> ⚠️ Works best with **machine-generated PDFs** (text-based).
> Scanned or image-based PDFs require an OCR layer — see the Roadmap below.

---

## 🧪 Try It With a Sample PDF

No PDF handy? Generate one in seconds:

```bash
pip install reportlab
python generate_sample_pdf.py
python extract_tables.py samples/sample_report.pdf --output output/result.xlsx
```

This generates a realistic 2-page financial report with 3 tables and immediately extracts them to Excel.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| [pdfplumber](https://github.com/jsvine/pdfplumber) | ≥ 0.10.0 | PDF parsing and table extraction |
| [pandas](https://pandas.pydata.org/) | ≥ 2.0.0 | Data structuring |
| [openpyxl](https://openpyxl.readthedocs.io/) | ≥ 3.1.0 | Excel file creation and formatting |

---

## 🆚 How This Compares

| Feature | This Tool | Copy-Paste | Tabula | Camelot |
|---|---|---|---|---|
| Works from terminal | ✅ | ❌ | ✅ | ✅ |
| Formatted Excel output | ✅ | ❌ | ❌ | ❌ |
| No Java required | ✅ | ✅ | ❌ | ✅ |
| Beginner-friendly code | ✅ | — | ❌ | ❌ |
| Multi-table per page | ✅ | ❌ | ✅ | ✅ |
| Pure Python | ✅ | — | ❌ | ✅ |

---

## 🔮 Roadmap

- [ ] **Batch mode** — process multiple PDFs at once (`*.pdf`)
- [ ] **Summary sheet** — first tab with an index of all tables found
- [ ] **`--no-style` flag** — plain data export without formatting
- [ ] **Streamlit UI** — browser-based drag & drop interface
- [ ] **OCR support** — Tesseract integration for scanned PDFs
- [ ] **REST API** — Flask/FastAPI endpoint for integration into other tools

Want to help build any of these? Open a PR or an issue.

---

## ❓ FAQ

**Does it work on Windows, Mac, and Linux?**
Yes. Pure Python, no OS-specific dependencies.

**What kinds of PDFs work best?**
PDFs generated by software (Excel exports, report generators, government portals). Scanned or handwritten PDFs require OCR and are not supported yet.

**Can it handle PDFs with multiple tables on the same page?**
Yes. Each table gets its own sheet in the Excel output.

**What if a table has merged cells or irregular formatting?**
pdfplumber handles most cases well, but heavily irregular tables may need manual cleanup after extraction.

**Is this free to use in commercial projects?**
Yes. MIT license — use it however you want.

---

## 🤝 Contributing

PRs are welcome. If extraction fails on your PDF, open an issue and attach the file — that's the most useful contribution you can make right now.

Please keep PRs focused and small. One improvement per PR.

---

## 📄 License

MIT — free to use, modify, and distribute. See [LICENSE](LICENSE) for details.

---

## 👤 Author

Built by **Paulo Victor** — shipping Python automation tools in public.

- Twitter/X: [@grey_pv1]
- LinkedIn: [linkedin.com/in/www.linkedin.com/in/paulo-victor-f-gonçalves-6b0b26318]
- GitHub: [@grey-pv]

---

<div align="center">

**Found this useful? Drop a ⭐ — it helps other developers find the project.**

*Part of a growing Python automation toolkit for developers, analysts, and office workers.*

</div>
