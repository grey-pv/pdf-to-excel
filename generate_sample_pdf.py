"""
generate_sample_pdf.py
─────────────────────
Generates a realistic sample PDF with multiple tables for testing the extractor.
Requires: pip install reportlab
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

OUTPUT = "samples/sample_report.pdf"

def build_pdf():
    doc = SimpleDocTemplate(OUTPUT, pagesize=letter,
                            topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    story  = []

    # ── Title ──────────────────────────────────────────────────────────────────
    story.append(Paragraph("Q2 2024 – Financial Summary Report", styles["Title"]))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "This report summarizes revenue, expenses, and product performance "
        "for the second quarter of fiscal year 2024.",
        styles["Normal"]
    ))
    story.append(Spacer(1, 0.3*inch))

    # ── Table 1: Revenue by Region ─────────────────────────────────────────────
    story.append(Paragraph("Table 1 – Revenue by Region (USD)", styles["Heading2"]))
    story.append(Spacer(1, 0.1*inch))

    t1_data = [
        ["Region",        "Q1 Revenue", "Q2 Revenue", "Growth (%)", "Status"],
        ["North America", "$1,240,000", "$1,410,000", "+13.7%",     "On Target"],
        ["Europe",        "$870,000",   "$920,000",   "+5.7%",      "On Target"],
        ["Asia-Pacific",  "$540,000",   "$680,000",   "+25.9%",     "Exceeds"],
        ["Latin America", "$210,000",   "$195,000",   "-7.1%",      "At Risk"],
        ["Middle East",   "$130,000",   "$158,000",   "+21.5%",     "Exceeds"],
        ["TOTAL",         "$2,990,000", "$3,363,000", "+12.5%",     "—"],
    ]

    t1 = Table(t1_data, colWidths=[1.4*inch, 1.2*inch, 1.2*inch, 1.1*inch, 1.1*inch])
    t1.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  colors.HexColor("#1F4E79")),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  colors.white),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, -1), 9),
        ("BACKGROUND",   (0, -1), (-1, -1), colors.HexColor("#BDC3C7")),
        ("FONTNAME",     (0, -1), (-1, -1), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, colors.HexColor("#EBF5FB")]),
        ("GRID",         (0, 0), (-1, -1),  0.5, colors.HexColor("#A9C4D8")),
        ("ALIGN",        (1, 0), (-1, -1),  "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1),  "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1),  5),
        ("BOTTOMPADDING",(0, 0), (-1, -1),  5),
    ]))
    story.append(t1)
    story.append(Spacer(1, 0.4*inch))

    # ── Table 2: Top Products ──────────────────────────────────────────────────
    story.append(Paragraph("Table 2 – Top 5 Products by Units Sold", styles["Heading2"]))
    story.append(Spacer(1, 0.1*inch))

    t2_data = [
        ["Product",          "SKU",      "Units Sold", "Unit Price", "Total Revenue"],
        ["Whey Protein 1kg", "WP-1000",  "4,820",      "$49.90",     "$240,518"],
        ["Creatine 300g",    "CR-300",   "3,610",      "$29.90",     "$107,939"],
        ["BCAA 200 caps",    "BC-200",   "2,940",      "$34.90",     "$102,606"],
        ["Pre-Workout 300g", "PW-300",   "2,100",      "$54.90",     "$115,290"],
        ["Collagen 250g",    "CO-250",   "1,870",      "$39.90",     "$74,613"],
    ]

    t2 = Table(t2_data, colWidths=[1.6*inch, 0.9*inch, 1.0*inch, 1.0*inch, 1.3*inch])
    t2.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  colors.HexColor("#1F4E79")),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  colors.white),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EBF5FB")]),
        ("GRID",         (0, 0), (-1, -1),  0.5, colors.HexColor("#A9C4D8")),
        ("ALIGN",        (2, 0), (-1, -1),  "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1),  "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1),  5),
        ("BOTTOMPADDING",(0, 0), (-1, -1),  5),
    ]))
    story.append(t2)
    story.append(Spacer(1, 0.4*inch))

    # ── Page break + Table 3 ───────────────────────────────────────────────────
    from reportlab.platypus import PageBreak
    story.append(PageBreak())

    story.append(Paragraph("Table 3 – Warehouse Inventory Status", styles["Heading2"]))
    story.append(Spacer(1, 0.1*inch))

    t3_data = [
        ["Warehouse",         "Location",       "Capacity", "Used (%)", "Critical Items"],
        ["WH-01 Dispatch",    "São Paulo, SP",  "500 pallets", "72%",   "3"],
        ["WH-02 Production",  "Pindamonhangaba","300 pallets", "88%",   "7"],
        ["WH-03 Raw Material","Guaratinguetá",  "400 pallets", "61%",   "1"],
    ]

    t3 = Table(t3_data, colWidths=[1.4*inch, 1.5*inch, 1.2*inch, 1.0*inch, 1.2*inch])
    t3.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  colors.HexColor("#1F4E79")),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  colors.white),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EBF5FB")]),
        ("GRID",         (0, 0), (-1, -1),  0.5, colors.HexColor("#A9C4D8")),
        ("ALIGN",        (2, 0), (-1, -1),  "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1),  "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1),  5),
        ("BOTTOMPADDING",(0, 0), (-1, -1),  5),
    ]))
    story.append(t3)

    doc.build(story)
    print(f"✅ Sample PDF created: {OUTPUT}")

if __name__ == "__main__":
    build_pdf()
