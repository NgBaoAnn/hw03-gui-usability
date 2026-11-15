---
name: gui-usability-evaluator
description: Design and execute GUI checklists and prepare moderated usability evaluations against a supplied SUT specification. Use for ecommerce screen/flow testing with traceable evidence and genuine participant data.
---

Read the provided specification and inspect the running application before designing checks. Record SUT revision, primary screen and end-to-end flow. Distinguish explicit requirements from usability heuristics. Do not assume filters, sorting, authentication or products exist.

For HW03, design more than 40 distinct checks covering IA-01 general UI, IA-02 forms, IA-03 navigation and IA-04 feedback/state. Each item needs an ID, screen, executable action, observable expectation and requirement/heuristic reference. Use the current project's `checklists/items.json` when present; adapt to other flows rather than copying product-specific expectations.

Preserve the initial AI checklist. Ask the student to review and add their own missing checks with reasons. Label AI additions as AI additions; a generated critique is not proof of human review. Unsupported dark mode/RTL are discussion points unless required, not automatic defects.

Execute on the actual SUT. Capture browser/version, OS, URL, timestamp, raw observation and screenshot for every failure. Wait for navigation, data and rendering before measuring. A tool timeout is Blocked, not a product failure. Declare delayed/failed network simulations explicitly. Never count a mobile viewport as a new browser or Playwright WebKit as Safari. Add the student's verified email/name/ID as a visibly separate evidence annotation after measuring, without changing application behavior.

In this SUT workspace, read `README.md` for requirements, `api_specification.md` for API expectations and `setup_guide.md` only if the services are unavailable. The web frontend is http://localhost:5173 and the backend is http://localhost:3000. Reuse running services: `backend/database.js` reseeds its database on startup.

For a video-demo request, use a visible browser through the available browser/computer tools, explain the current action briefly, and demonstrate one complete user flow. Select relevant criteria from the bundled [51-item G2 checklist](references/gui-checklist-g2.json). Observe the current SUT rather than assuming a recorded bug will recur. Save new observations/screenshots in a separate run under `demo-evidence/`; preserve existing homework evidence. A demo request alone does not request publishing GitHub Issues or submitting Moodle.

This recording is for Nguyễn Bảo An, MSSV 23120207, email 23120207@student.hcmus.edu.vn. Keep these verified details visible in a separate evidence annotation when screenshots are captured. Chrome, Firefox and real Safari remain distinct environments; record actual versions and methods. The optional test runners from the homework repository are not bundled here; use the browser tools available in this workspace.

Group reproducible failures by root cause into Markdown bugs with steps, expected/actual, severity, references and original screenshots. Create GitHub Issues only in the user's authorized repository. Keep local evidence in the archive so links are supplementary. Never alter screenshots to fabricate browser runs or participants.

Prepare one goal-oriented task scenario, pilot protocol, SUS or justified scale, neutral think-aloud moderation and open questions on clarity, recovery, speed and trust. For HW03 collect one pilot and seven independent sessions with people outside the class. Do not create names, contact details, answers, quotes, timing or outcomes. Keep contact originals private; submission contacts are masked. If no genuine data exists, report that limitation and provide blank instruments.

The bundled [SUS scorer](scripts/calculate_sus.py) validates ten integer answers 1–5, sums odd answers minus 1 and 5 minus even answers, then multiplies by 2.5. From the SUT root, run `python3 .agents/skills/gui-usability-evaluator/scripts/calculate_sus.py --test` to check it, or replace `--test` with the genuine response CSV path to calculate scores. Exclude pilot from n=7. Never fill missing answers or interpret SUS as a completion percentage. Synthesise only recorded observations and identify which participants support each finding.

Record real Git commits per completed phase/session, prompt/output audit and limitations. Validate evidence links, consistency of counts, scale arithmetic and archive contents. Mark incomplete packages as drafts; do not claim final submission or a completed participant study when prerequisites are missing.
