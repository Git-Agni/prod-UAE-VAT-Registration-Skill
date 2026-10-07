# Gotchas and troubleshooting

EmaraTax is a SAP UI5 app. These are the snags from real VAT registrations, with the fix. (The general portal snags from the Corporate Tax skill apply too: one file per upload, slow loads, save often.)

## "The provided Taxable Supplies … are below voluntary registration threshold"

Pops up when moving past Step 3 if the 12-month figure is under AED 187,500 (or AED 375,000 for mandatory). The next-30-days figure does not clear it.

**Fix:** re-check the monthly figures. The most common cause is counting cash received instead of invoices issued: unpaid invoices already issued count by their invoice date. If the honest figures are still short, wait until they are not. Do not inflate a month.

## Criteria box says "Not Applicable"

Same cause as above. Once the past figures pass a threshold, it changes to Voluntary or Mandatory and shows the rule text.

## "Please enter reason for change in Obligation Date"

Appears as soon as the threshold date is edited away from the portal's default.

**Fix:** a one-line factual reason that matches the declaration letter, for example "Voluntary threshold exceeded on 3 October 2026 when invoices X and Y were issued, per signed turnover declaration." Some fields reject punctuation; drop commas and hyphens if it complains.

## Account Holder's Name: "Please enter alpha numeric characters only"

The field rejects hyphens and punctuation, so "ACME - FZCO" fails.

**Fix:** "ACME FZCO". The bank letter shows the full legal name; that is fine.

## Branch name for a digital bank

There is no branch. **Fix:** "Head Office" plus the city of the bank's head office (it is on the bank letter or the bank's website).

## A step shows blank on the review page

Step 9 can show only labels for a step you filled (seen with Bank Details), meaning the data did not save.

**Fix:** Edit that step, re-enter, Save as Draft, come back to Review and check the values now show.

## Export of services answered No

If the company invoices clients abroad at 0%, "Do you intend to export goods or services?" must be Yes. A No contradicts the zero-rated sales in Step 3 and the "0% export" invoices.

## Passport issuing country looks wrong

With UAE PASS prefill, "Passport Issuing Country" comes from the federal record, which may store the place of issue (for example a passport issued at an embassy abroad). Leave it matching the official record unless the user knows it is wrong.

## The relationship dropdown in "Add Relationships" resets

Selecting Partner/Director sometimes clears when another radio is clicked.

**Fix:** set the dropdown last, check it still shows the value, then click Add. If the company has no director involved in another UAE business, the list can stay empty.

## Signing PDFs on a Mac: "The file is locked"

Files downloaded from a browser or chat can be locked, so Preview cannot save the signature.

**Fix:** Preview → File → **Export as PDF…** (or Duplicate) and save a new file, then upload that.

## No company stamp

Many small free zone companies never ordered one.

**Fix:** order a self-inking stamp (company name, licence number, emirate) from any stamp shop, or use a digital seal of the company's own details. `tools/turnover_declaration.py` can draw a simple one. Only for the user's own company.

## The agent's own safety checks

Some browser agents refuse to answer personal declarations (residency, the final declaration) or to type certain dates on a government form. That is expected. The user clicks those.
