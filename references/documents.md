# Preparing the documents

## Turnover declaration letter

The FTA links a Word template (tax.gov.ae → Turnover-Declaration-Letter.docx). It needs:

- Date, "To: Federal Tax Authority", "Subject: Declaration Letter".
- The company's turnover by year and by month from the date of establishment to the date of submission.
- The month taxable supplies started and the date the threshold (mandatory AED 375,000 / voluntary AED 187,500) was reached.
- The standard declaration paragraph.
- Signature and stamp of the authorised signatory.

`tools/turnover_declaration.py` builds this as a 2-page PDF (letter + itemised supplies) from a JSON file:

```bash
pip install reportlab
python tools/turnover_declaration.py tools/example.json declaration.pdf
```

See `tools/example.json` for the format (fictional company). Set `"seal": true` to draw a simple round seal with the company name and licence number, only for the user's own company. The signature line is left blank on purpose: the signatory signs it (on paper and scans, or in Preview / Acrobat).

## Sample sales invoices

Use the real invoices sent to customers (same numbers and dates as in the declaration). Add the stamp and signature (Preview → Markup → Sign; drag the seal image on). Pick invoices that show the zero-rating wording if the sales are exports.

## Bank letter

From the bank (in-app for digital banks): company name, IBAN, account number, bank name. Upload as PDF in Step 6.
