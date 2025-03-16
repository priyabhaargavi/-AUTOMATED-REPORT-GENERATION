import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    summary = df.describe().T
    return summary

def generate_pdf_report(data_summary, output_pdf="report_reportlab.pdf"):
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    elements = []

    data = [["Metric"] + list(data_summary.columns)]  
    for index, row in data_summary.iterrows():
        data.append([index] + [f"{val:.2f}" for val in row])

    table = Table(data)
    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    elements.append(table)
    doc.build(elements)
    print(f"Report generated: {output_pdf}")

file_path = "data.csv"
summary = analyze_data(file_path)
generate_pdf_report(summary)

