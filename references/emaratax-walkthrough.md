# EmaraTax VAT registration (form V101): field-by-field walkthrough

Labels as seen in 2026. Screens change, so read what is on screen. The user must be logged in first.

## Open the form

1. Home → Taxable Person list → **View** on the company.
2. On the dashboard, **Registration Overview** tab → *Value Added Tax* row (status "Not Registered") → Action (**⋯**) → **Register**.
   - The left menu's *VAT* page only shows refund and import forms (VAT 301, 301A, 702). Registration is not there.
3. Intro page: 4 form sections, about 45 minutes, free of charge. Tick "I confirm that I have read the above instructions and guidelines" → **Start**.

The wizard has 9 steps. Click **Save as Draft** before leaving any step.

## Step 1: Entity Details

- Entity Type: prefilled (for example "Legal Person - Incorporated - UAE Private Company").
- Date of Incorporation: prefilled from the CT profile.
- **Do you have a certificate of incorporation?** "No" is acceptable when the company has a UAE trade licence (the licence is the primary document). Free zones often issue a certificate of formation; answering Yes and attaching it is optional.
- **Applying to create or join a Tax Group?** No for a single company.

## Step 2: Identification Details

- Trade licence block: prefilled (issuing authority, number, issue and expiry dates, legal and trade names in English and Arabic). Check against the licence.
- Business Activity Details: prefilled from the CT profile; one row marked Primary.
- Owners List: prefilled.
- **Branches in UAE / Sole Establishment / Own any Property:** usually No for a small company. These radios are not always pre-selected: set them.

## Step 3: Eligibility Details

The step that needs the most preparation.

- **Taxable Supplies table:** one row per month since incorporation. Enter each month in AED (figures by invoice date). The Cumulative column and "Taxable Supplies in any past period of 12 months or less" fill themselves.
- **Taxable Supplies - Next 30 days:** expected supplies.
- **Taxable Expenses table:** optional; leave at 0 unless registering voluntarily on expenses.
- **Uploads** (PDF or DOC, up to 3 files each, 20 MB):
  - *pdf version of the uploaded excel template with signature and seal of the Authorized signatory* → the signed and stamped **turnover declaration letter**.
  - *Purchase orders, contracts* → optional, recommended.
  - *Sample expenses invoices* → optional.
  - *Sample sales invoices* → 1 to 3 signed and stamped invoices.
  - You do not have to use the "Upload Filled Template" Excel buttons if you type the table in directly.
- **VAT Registration Criteria:** turns to **Mandatory** or **Voluntary** once the figures support it. If it says **Not Applicable**, the past 12 months are under AED 187,500: re-check the figures (invoice basis) before going further.
- **Date on which the threshold limit … exceeded / expected to be exceeded:** the date the relevant threshold was passed. Changing it from the portal's default makes **Reason for change in Obligation Date** mandatory; give a short factual reason that matches the declaration letter.
- **On what date would you like to be registered:** optional requested effective date. Changing it can require a reason too.
- **Do you expect the VAT on your expenses to regularly exceed the VAT in your taxable supplies?** If nearly all sales are zero-rated exports, output VAT is about zero, so the honest answer is usually Yes (a refund position). The user decides.
- **Do you expect to make exempt supplies?** Usually No for services businesses.
- **Do you wish to apply for Exception from VAT?** The user's decision (see `thresholds-and-timing.md`).

## Step 4: Contact Details

Prefilled from the CT profile: country, building, street, area, city, emirate, mobile, landline (8-digit cap), email, P.O. Box (optional). Must match the trade licence.

## Step 5: Business Relationships

- **Designation:** CEO or Manager (the person running the company, often the GM named in the MOA).
- **Do you want your UAE Pass profile information to be retrieved?** Yes pulls Emirates ID, passport, names and nationality from the federal record (the user approves in UAE PASS). No means entering them by hand.
- **Is the Manager/CEO a resident in the UAE?** The user answers.
- **Add Relationships:** a separate list for any director or partner who is (or in the last 5 years was) involved in **another business resident in the UAE**. Leave empty if there is none. The relationship-type dropdown inside this dialog does not always keep its value: re-check before clicking Add.

## Step 6: Bank Details (marked optional, fill it anyway)

- Country, **IBAN** (no spaces). Bank Name and Account Number fill from the IBAN.
- **Branch Name:** digital banks have no branches; use the head office (for example "Head Office Abu Dhabi").
- **Account Holder's Name:** letters, numbers and spaces only. Remove hyphens and punctuation from the company name.
- Upload the bank confirmation letter.

## Step 7: Additional Details

- **Do you intend to import goods or services?** Buying software or services from abroad counts as importing services (reverse charge). The user decides.
- **Do you intend to export goods or services?** **Yes** if the company invoices customers outside the UAE. This should match zero-rated sales in Step 3.
- **Customs registration number?** No unless the company trades physical goods across borders.

## Step 8: Authorised Signatory

The person making the declaration: name, Emirates ID, mobile, email, proof of authority (MOA for a GM named in it), and ID / passport uploads. Often prefilled from the CT profile.

## Step 9: Review and Declaration

1. Click **Expand All** and read every section.
2. Any step that shows labels with no values (it happened with Bank Details in testing) needs reopening with **Edit**, re-entering and saving.
3. Summarise for the user: figures and criteria, threshold date, bank, import/export answers, signatory.
4. The Declaration block is prefilled with the signatory and the submission date. **The user** ticks "I declare that all information provided is true, accurate and complete…" and clicks **Submit**.
5. The confirmation page shows **Application Submitted Successfully**, a reference number, the date, and status "In Review." Save that reference.
