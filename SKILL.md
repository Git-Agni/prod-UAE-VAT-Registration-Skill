---
name: uae-vat-registration
description: Help a user register their UAE company for VAT on the FTA EmaraTax portal by driving the browser through the VAT registration form (V101), preparing the turnover declaration and sample invoices, and handing off for the final declaration. Use when the user wants to register a UAE mainland or free zone company for VAT (mandatory or voluntary), get a VAT TRN, or work out what the EmaraTax VAT form is asking. Not for tax advice, filing VAT returns, or deciding whether supplies are zero-rated.
---

# UAE VAT registration on EmaraTax

You are helping the user register their own company for VAT on the UAE Federal Tax Authority's EmaraTax portal (eservices.tax.gov.ae). You prepare the figures and documents with them, drive the browser through the form, and stop before the final declaration. The user reviews and submits.

## Read this first: what you must and must not do

- **You are not a tax advisor.** Do not decide whether their supplies are zero-rated, whether they should register voluntarily, or whether to apply for an exception. Explain what the form asks and what each option means, then let the user choose. For anything about their tax position, point them to a registered UAE tax agent on the FTA register (tax.gov.ae).
- **Never type the user's password or any OTP,** and never use UAE PASS for them. The user logs in.
- **Never draw, invent or paste a signature.** The turnover declaration and sample invoices must carry the authorised signatory's real signature. You can prepare the documents and leave a signature line; the user signs.
- **Never tick the final declaration or click Submit.** At step 9, summarise and hand off.
- **Personal declarations are the user's.** Questions like "Is the manager a UAE resident?" are answered by the user, not inferred by you.
- **Every number comes from real records:** invoices, bank statements, accounting. Never estimate a month's supplies to get over a threshold. If the figures do not reach the threshold, say so.

## Before you start

Go through `references/before-you-start.md` with the user. The essentials:

- An EmaraTax account with a Taxable Person profile (usually already there if they registered for Corporate Tax).
- Their **taxable supplies by month** since incorporation (or the last 12 months), with the invoice behind each amount, converted to AED.
- PDFs: trade licence, MOA, Emirates ID and passport of the manager / signatory, a **bank account confirmation letter** (IBAN letter), 1 to 3 sample sales invoices, any contracts or purchase orders.
- A company stamp, or a digital seal of their own company (see gotchas: there is no official stamp to apply for).

## Work out which registration it is

Read `references/thresholds-and-timing.md` and explain it to the user in plain words:

- **Mandatory:** taxable supplies (including zero-rated exports) over the last 12 months passed **AED 375,000**, or will within the next 30 days. Apply within 30 days of the obligation. Late registration carries a fixed penalty (AED 10,000 at the time of writing).
- **Voluntary:** supplies or taxable expenses passed **AED 187,500**. Optional; lets the company reclaim input VAT.
- Count supplies by **invoice date** (the date of supply), not when the cash arrived. Invoices issued but not yet paid count. Using cash only can understate the figure and trip the portal's "below threshold" warning.

## The flow

Field-by-field detail is in `references/emaratax-walkthrough.md`. The shape:

1. **Open the form.** Taxable Person dashboard → Registration Overview → *Value Added Tax* row → Action (⋯) → **Register**. (It is not under the VAT menu tiles.) Tick the instructions box, Start. Nine steps, about 45 minutes, free.
2. **Step 1 Entity, Step 2 Identification:** mostly prefilled from the Corporate Tax profile. Check activities, owners, branches / sole establishment / property (usually No).
3. **Step 3 Eligibility:** enter monthly taxable supplies in AED, the next-30-days figure, answer the three questions, upload the signed and stamped turnover declaration and sample invoices. Confirm the *VAT Registration Criteria* box reads **Mandatory** or **Voluntary**, not "Not Applicable".
4. **Step 4 Contact:** prefilled; check address matches the trade licence.
5. **Step 5 Business Relationships:** Designation (CEO or Manager), UAE PASS prefill, residency. "Add Relationships" is only for people involved in *other UAE businesses*.
6. **Step 6 Bank:** IBAN, account holder name (letters, numbers, spaces only), branch, bank letter upload.
7. **Step 7 Additional:** import / export of goods *or services*, customs number.
8. **Step 8 Authorised Signatory:** the person who signs, with proof of authority (usually the MOA).
9. **Step 9 Review and Declaration:** expand all, check every step shows its values (a step can come back blank, fix it with Edit), summarise, hand off.

Save as Draft at the end of every step.

## Documents you can prepare

`tools/turnover_declaration.py` builds the FTA-style turnover declaration letter (and an itemised supplies page) from a small JSON file, with an optional seal of the user's own company and a blank signature line. See `references/documents.md`. Show the user the PDF before they sign.

## Gotchas

`references/gotchas.md` has the full list. The ones that cost the most time:

- The "below voluntary/mandatory threshold" warning ignores the next-30-days field. Fix the monthly figures (invoice basis), do not push through it.
- Changing the threshold date makes **"Reason for change in Obligation Date"** mandatory.
- **Account holder name rejects hyphens** and punctuation ("ACME - FZCO" fails, "ACME FZCO" passes).
- A step can show **empty on the review page** even after you filled it. Re-open it with Edit and re-enter.
- Answer **export of services: Yes** if the company invoices clients abroad. A "No" contradicts zero-rated sales.
- macOS Preview cannot save a signature onto a downloaded (locked) PDF: use File → Export as PDF.

## After submission

Capture the reference number from the confirmation page. The FTA reviews applications (commonly within 20 business days) and may email for more information. On approval the VAT TRN and certificate appear in the EmaraTax account. Remind the user, without advising, that registration is the start: they will be assigned tax periods (usually quarterly), returns are due 28 days after each period ends, and invoices must carry the TRN from the effective date.
