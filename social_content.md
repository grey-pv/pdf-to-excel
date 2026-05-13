# Social Media Content Pack
# PDF to Excel Extractor — Launch Week

---

## TWITTER/X

### Tweet 1 — Launch (text-based hook)
I spent years watching people copy tables from PDFs into Excel by hand.

So I built a Python tool that does it automatically.

One command. Any PDF. Formatted Excel output.

Open source → [LINK]

---

### Tweet 2 — How it works (thread opener)
How I extract tables from PDFs in Python (thread 🧵)

The stack:
• pdfplumber → reads the PDF
• pandas → structures the data
• openpyxl → writes the Excel

15 lines of code. Let me show you:

---

### Tweet 3 — Relatable pain
"Can you get this data from the PDF into Excel?"

Before: 45 minutes of copying
After: python extract_tables.py report.pdf

The file lands in your folder in 3 seconds.

---

### Tweet 4 — Code screenshot post
The core of my PDF extractor is this:

[screenshot of the extract_tables_from_pdf function]

pdfplumber detects the tables.
pandas organizes the rows.
openpyxl writes the Excel.

That's the whole idea. Full script → [LINK]

---

### Tweet 5 — Build in public angle
Day 1 of shipping Python automation tools in public.

Project #1: PDF to Excel Extractor
• 150 lines of code
• 3 dependencies
• Solves a real problem I saw every week at work

GitHub is live. Next: batch mode + Streamlit UI.

Following along → [LINK]

---

## LINKEDIN

### Post 1 — Launch post
I built a Python tool that extracts tables from PDF files and exports them to Excel automatically.

One command:
python extract_tables.py report.pdf

You get a formatted .xlsx with every table — headers styled, rows alternating, columns auto-fitted.

The tech: pdfplumber + pandas + openpyxl. No Java, no external APIs, no config files.

Why I built it: I work in logistics. Every week we receive supplier reports as PDFs. Getting the data into Excel was a manual, error-prone process. Now it's a 3-second script.

Open source, MIT license, beginner-friendly code.

If you work with PDFs regularly, try it → [LINK]

Happy to answer questions in the comments.

---

### Post 2 — Educational angle (2 weeks later)
Most people don't know that Python can extract tables from PDFs automatically.

Here's the library that makes it possible: pdfplumber

It reads the internal structure of a PDF and detects table boundaries — no OCR needed for machine-generated PDFs.

Combined with pandas and openpyxl, you can go from PDF to formatted Excel in about 15 lines of code.

I built a full CLI tool around this. Open source, link in comments.

What's your most painful manual data task right now?

---

## STACK OVERFLOW TARGETS
# Search these queries and answer genuinely — mention the project naturally

- "how to extract table from pdf python"
- "python pdf to excel table"
- "pdfplumber extract table to dataframe"
- "how to read pdf table with pandas"
- "convert pdf table to xlsx python"

