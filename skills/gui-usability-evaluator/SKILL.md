---
name: gui-usability-evaluator
description: Design and execute GUI checklists and prepare moderated usability evaluations against a supplied SUT specification. Use for ecommerce screen/flow testing with traceable evidence and genuine participant data.
---

Read the provided specification and inspect the running application before designing checks. Record SUT revision, primary screen and end-to-end flow. Distinguish explicit requirements from usability heuristics. Do not assume filters, sorting, authentication or products exist.

For HW03, design more than 40 distinct checks covering IA-01 general UI, IA-02 forms, IA-03 navigation and IA-04 feedback/state. Each item needs an ID, screen, executable action, observable expectation and requirement/heuristic reference. Use the current project's `checklists/items.json` when present; adapt to other flows rather than copying product-specific expectations.

Preserve the initial AI checklist. Ask the student to review and add their own missing checks with reasons. Label AI additions as AI additions; a generated critique is not proof of human review. Unsupported dark mode/RTL are discussion points unless required, not automatic defects.

Execute on the actual SUT. Capture browser/version, OS, URL, timestamp, raw observation and screenshot for every failure. Wait for navigation, data and rendering before measuring. A tool timeout is Blocked, not a product failure. Declare delayed/failed network simulations explicitly. Never count a mobile viewport as a new browser or Playwright WebKit as Safari. Add the student's verified email/name/ID as a visibly separate evidence annotation after measuring, without changing application behavior.

In this submission repository, `scripts/run_gui.cjs` runs the G2 checklist with an installed Playwright dependency: `node scripts/run_gui.cjs chrome` or `firefox`. Use an available runtime/module path, not a hardcoded path from another computer. Source and network overrides remain recorded in raw JSON.

For real Safari, use `uv run --with selenium python scripts/run_safari.py` with Apple safaridriver listening on port 4444 and the user's authorized remote-automation setting. The same-origin evidence frame supplies exact CSS viewports. Network-error cases explicitly redirect XHR to a localhost fixture; Option-Tab is Safari's all-item navigation when default Tab skips links. Inspect `click_delivery` when SafariDriver only blurs a focused input: repeat a driver command only if zero DOM clicks were delivered, preserving first-click product defects.

Group reproducible failures by root cause into Markdown bugs with steps, expected/actual, severity, references and original screenshots. Create GitHub Issues only in the user's authorized repository. Keep local evidence in the archive so links are supplementary. Never alter screenshots to fabricate browser runs or participants.

Prepare one goal-oriented task scenario, pilot protocol, SUS or justified scale, neutral think-aloud moderation and open questions on clarity, recovery, speed and trust. For HW03 collect one pilot and seven independent sessions with people outside the class. Do not create names, contact details, answers, quotes, timing or outcomes. Keep contact originals private; submission contacts are masked. If no genuine data exists, report that limitation and provide blank instruments.

Use `scripts/calculate_sus.py` if supplied by the project. Otherwise validate ten integer answers 1–5, sum odd answers minus 1 and 5 minus even answers, then multiply by 2.5. Exclude pilot from n=7. Never fill missing answers or interpret SUS as a completion percentage. Synthesise only recorded observations and identify which participants support each finding.

Record real Git commits per completed phase/session, prompt/output audit and limitations. Validate evidence links, consistency of counts, scale arithmetic and archive contents. Mark incomplete packages as drafts; do not claim final submission or a completed participant study when prerequisites are missing.
