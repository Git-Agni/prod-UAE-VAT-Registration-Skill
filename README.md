# UAE VAT Registration Skill

Register your UAE company for VAT on the FTA's EmaraTax portal with an AI agent (Claude Code or OpenAI Codex, with browser control) doing the form for you. You bring the invoices and your login. The agent works out your monthly figures, drafts the turnover declaration, fills all 9 steps, and stops before the declaration so you review and submit.

I built this after registering my own Dubai free zone company for VAT. It took one evening and cost nothing. The same filing usually costs AED 1,500 to 2,500 through an agent or your free zone. This is that evening, packaged, plus every snag I hit so you do not have to.

It is the follow-up to the [UAE Corporate Tax Registration Skill](https://github.com/Git-Agni/prod-UAE-Corporate-Tax-Skill). If you used that one, half of this form fills itself.

> **Not tax advice.** This is an automation helper, not a tax, legal or financial advisory service. It does not decide whether you should register, whether your sales are zero-rated, or whether to ask for an exception. It types the answers you give it into a government portal you could fill in yourself. For anything about your tax position, talk to a registered UAE tax agent (the FTA keeps a public list). Full disclaimer below.

## What it does

- Explains the two thresholds in plain words: **AED 375,000 mandatory**, **AED 187,500 voluntary**, and why your 0% export sales still count.
- Builds your month-by-month taxable supplies table **by invoice date**, the way the FTA counts it (counting only cash received is the most common reason the portal says you are "below threshold").
- Drafts the FTA-style **turnover declaration letter** as a PDF, with an itemised page and an optional seal for your own company (`tools/turnover_declaration.py`).
- Drives the EmaraTax VAT form (V101) step by step: eligibility, contact, business relationships, bank, additional details, signatory.
- Knows the traps: the account holder field that rejects hyphens, the "reason for change in obligation date" box, the review page that silently drops a step, the export question that contradicts your own invoices if you answer it wrong.
- Stops before the legal declaration so you read everything and submit it yourself.

## What it will NOT do

- Type your password, an OTP or use UAE PASS for you.
- Draw or paste your signature. You sign the letter and invoices.
- Tick the declaration or click Submit.
- Inflate a month to get you over a threshold. If your numbers are not there yet, it tells you.
- Give tax advice.

## Who this is for

A UAE company (mainland or free zone) that has crossed, or is about to cross, the VAT threshold, or wants to register voluntarily so it can reclaim VAT on costs. Mandatory registration is due within 30 days of crossing AED 375,000, and the late-registration penalty is AED 10,000, so it pays to be early.

## Requirements

- An AI agent that can control a browser: Claude Code with browser tools, OpenAI Codex, or similar.
- An EmaraTax account (free, eservices.tax.gov.ae), ideally with your company's Corporate Tax registration already done.
- Your invoices for the last 12 months (or since incorporation), and your bank's account confirmation letter.
- Python 3 with `reportlab` if you want the declaration letter drafted for you.

Full checklist: [references/before-you-start.md](references/before-you-start.md).

## How to use it

1. Gather your invoices and documents with the checklist.
2. Log into EmaraTax in your browser yourself.
3. Drop this folder into your Claude Code skills directory (it loads on its own), or paste `SKILL.md` into the chat and say "help me register my company for UAE VAT, I'm logged into EmaraTax."
4. Give it your invoice list. It builds the monthly table, drafts the declaration, and you sign it.
5. Let it drive the form. Answer the personal questions (residency, whether to apply for an exception) yourself.
6. Read the review page, tick the declaration, submit. Keep the reference number.

The FTA's stated processing time is 20 business days. Your VAT TRN and certificate then show up in EmaraTax.

## Files

- `SKILL.md`: the skill, the instructions the agent follows.
- `references/before-you-start.md`: documents and figures checklist.
- `references/thresholds-and-timing.md`: thresholds, invoice-date counting, exceptions, what happens after approval.
- `references/emaratax-walkthrough.md`: field-by-field walkthrough of all 9 steps.
- `references/gotchas.md`: what goes wrong and how to get past it.
- `references/documents.md`: the turnover declaration, sample invoices and bank letter.
- `tools/turnover_declaration.py` + `tools/example.json`: the declaration letter generator, with a fictional example company.

## Disclaimer

Read this before you use the skill.

This project is a free, open-source automation aid, provided as is, with no warranty, under the MIT licence.

It is **not** tax, legal, accounting or financial advice, and using it does not create any advisor or client relationship with the author. Nothing here is a recommendation about whether or how you should register for VAT, how your supplies should be treated, or anything else about your situation. The skill only enters, into a government portal, the information you provide and direct it to enter.

**You are responsible** for the accuracy of everything submitted: the figures, the documents, the declaration letter and the application. The authorised signatory makes a legal declaration to the Federal Tax Authority. That is you, not the tool and not the author. The seal drawn by the letter generator is for your own company only.

For advice on VAT, zero-rating, exceptions, free zone rules or anything specific to your company, consult a **registered UAE tax agent** (the FTA publishes the register at tax.gov.ae) or a qualified professional.

This project is **not affiliated with, endorsed by, or connected to** the Federal Tax Authority, the UAE government, EmaraTax, UAE PASS, any free zone authority, any bank, Anthropic or OpenAI. All product names and trademarks belong to their owners.

You use this skill at your own risk. The author is not liable for any outcome, including rejected applications, penalties or incorrect filings. If you are not comfortable with that, hire an agent.

## Licence

MIT. Use it, fork it, share it. If it saved you the fee, tell someone.
