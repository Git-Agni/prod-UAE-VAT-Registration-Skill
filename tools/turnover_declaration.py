#!/usr/bin/env python3
"""Draft a UAE FTA turnover declaration letter (VAT registration, EmaraTax Step 3) as a PDF.

Usage:  python turnover_declaration.py input.json output.pdf
Needs:  pip install reportlab

Page 1 follows the FTA's Turnover-Declaration-Letter template; page 2 itemises the supplies.
The signature line is left blank: the authorised signatory signs. "seal": true draws a simple
round seal of the company's own name and licence number. Only ever use it for your own company.
"""
import json, math, sys
from collections import OrderedDict
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas

INK = Color(0.10, 0.22, 0.55)
W, H = A4
M = 56  # margin


def money(v):
    return f"{v:,.2f}"


def month_name(ym):
    y, m = map(int, ym.split("-"))
    return date(y, m, 1).strftime("%B %Y")


def seal(c, cx, cy, d, r=46):
    c.saveState()
    c.setStrokeColor(INK); c.setFillColor(INK)
    c.setLineWidth(2); c.circle(cx, cy, r)
    c.setLineWidth(0.8); c.circle(cx, cy, r - 5); c.circle(cx, cy, r - 17)

    def arc(text, radius, start, end, top, size):
        c.setFont("Helvetica-Bold", size)
        n = max(len(text), 1)
        for i, ch in enumerate(text):
            a = math.radians(start + (end - start) * (i + 0.5) / n)
            c.saveState()
            c.translate(cx + radius * math.cos(a), cy + radius * math.sin(a))
            c.rotate(math.degrees(a) - 90 if top else math.degrees(a) + 90)
            c.drawCentredString(0, -size / 3, ch)
            c.restoreState()

    name = d["company"].upper()
    arc(name, r - 11.5, 165, 15, True, 7.5 if len(name) < 18 else 6)
    arc(f"{d.get('emirate', 'DUBAI')} - U.A.E.", r - 11.5, 215, 325, False, 7)
    c.setFont("Helvetica-Bold", 6.5); c.drawCentredString(cx, cy + 6, "LICENCE NO.")
    c.setFont("Helvetica-Bold", 9); c.drawCentredString(cx, cy - 4, d["licence_no"])
    if d.get("licence_authority"):
        c.setFont("Helvetica", 5.5); c.drawCentredString(cx, cy - 13, d["licence_authority"])
    c.restoreState()


def head(c, d, title):
    c.setFont("Helvetica-Bold", 13); c.drawString(M, H - 70, d["company"])
    c.setFont("Helvetica", 8.5)
    c.drawString(M, H - 84, f"{d['address']}  |  Licence No. {d['licence_no']}")
    c.setLineWidth(0.5); c.line(M, H - 92, W - M, H - 92)
    c.setFont("Helvetica-Bold", 11); c.drawString(M, H - 118, title)


def para(c, text, y, size=10):
    c.setFont("Helvetica", size)
    for line in simpleSplit(text, "Helvetica", size, W - 2 * M):
        c.drawString(M, y, line); y -= 14
    return y - 6


def sign(c, d, y):
    c.setFont("Helvetica", 9.5)
    c.drawString(M, y, "Authorized Signatory (Sign and Stamp)")
    c.line(M, y - 42, M + 194, y - 42)
    c.drawString(M, y - 54, d["signatory"])
    if d.get("signatory_id"):
        c.drawString(M, y - 66, d["signatory_id"])
    if d.get("seal"):
        seal(c, W - M - 70, y - 30, d)


def main(src, out):
    d = json.load(open(src))
    rows = sorted(d["supplies"], key=lambda r: r["date"])
    by_month = OrderedDict()
    for r in rows:
        by_month[r["month"]] = by_month.get(r["month"], 0) + r["aed"]
    total = sum(by_month.values())
    limit = "AED 375,000 (mandatory)" if d.get("threshold") == "mandatory" else "AED 187,500 (voluntary)"
    c = canvas.Canvas(out, pagesize=A4)

    head(c, d, "Declaration Letter")
    y = H - 150
    c.setFont("Helvetica", 10)
    for line in [f"Date: {d['letter_date']}", "To: Federal Tax Authority", "Subject: Declaration Letter"]:
        c.drawString(M, y, line); y -= 16
    y -= 8
    y = para(c, f'In reference to the above mentioned subject, kindly note that "{d["company"]}" '
                f'(incorporated {d["incorporated"]}) has the below mentioned turnover:', y)
    y = para(c, f"We started making taxable supplies in {month_name(rows[0]['month'])} and we reached the "
                f"registration threshold of {limit} on {d['threshold_date']}, when our taxable supplies "
                f"reached AED {money(total)} (counted by invoice date). We expect a further "
                f"AED {money(d.get('next_30_days_aed', 0))} of taxable supplies within the next 30 days. "
                f"{d.get('note', '')}", y)
    y = para(c, "I hereby declare that the information related to this disclosure is complete and best to my "
                "knowledge and none of the above information is false or misrepresented as it is supported by "
                "documentary proof such as: signed and stamped monthly taxable supplies for the last 12 months "
                "by the authorized signatory, and supporting financial documents (invoices and contracts).", y)
    c.setFont("Helvetica-Bold", 10); c.drawString(M, y, "Month"); c.drawRightString(M + 280, y, "Amount (AED)"); y -= 15
    c.setFont("Helvetica", 10)
    for m, v in by_month.items():
        c.drawString(M + 14, y, month_name(m)); c.drawRightString(M + 280, y, money(v)); y -= 14
    c.setFont("Helvetica-Bold", 10); c.drawString(M + 14, y, "Total"); c.drawRightString(M + 280, y, money(total)); y -= 40
    sign(c, d, y)
    c.showPage()

    head(c, d, "Monthly taxable supplies - itemised")
    c.setFont("Helvetica", 8.5)
    c.drawString(M, H - 132, "Counted by invoice date. USD at the AED 3.6725 peg; other currencies at the rate of the day.")
    y = H - 156
    cols = [M, M + 70, M + 150, M + 320]
    c.setFont("Helvetica-Bold", 8.5)
    for x, h in zip(cols, ["Date", "Reference", "Customer", "Original amount"]):
        c.drawString(x, y, h)
    c.drawRightString(W - M, y, "AED"); y -= 14
    c.setFont("Helvetica", 8.5)
    for r in rows:
        c.drawString(cols[0], y, r["date"]); c.drawString(cols[1], y, r["ref"])
        c.drawString(cols[2], y, r["customer"][:34]); c.drawString(cols[3], y, r.get("original", ""))
        c.drawRightString(W - M, y, money(r["aed"])); y -= 13
    c.line(M, y + 4, W - M, y + 4); y -= 8
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M, y, "Total taxable supplies to date"); c.drawRightString(W - M, y, money(total)); y -= 13
    c.drawString(M, y, "Expected in the next 30 days"); c.drawRightString(W - M, y, money(d.get("next_30_days_aed", 0))); y -= 40
    sign(c, d, y)
    c.save()
    print(f"Wrote {out}: {len(rows)} supplies, AED {money(total)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
