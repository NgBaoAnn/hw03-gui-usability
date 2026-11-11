# HW03 GUI & Usability (Package G2) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the full deliverable package for HW03 GUI & Usability Testing on SUT EShop (Package G2: Product Search, Filter & Detail), including a >40-item GUI checklist, bug reports, usability evaluation with 7 participants (SUS), cross-platform evidence, custom Agent Skill, AI Audit Report & Critique, and self-assessment README.

**Architecture:** Deliverable-oriented testing workflow. Automated assets (checklists, scripts, questionnaires, analysis calculators, agent skills, report templates) are generated and verified via structured file artifacts. Physical execution steps (browsing on localhost SUT, taking screenshots with student overlay, conducting moderated think-aloud sessions) are coordinated through clear human-in-the-loop verification checkpoints.

**Tech Stack:** Markdown, Node.js / Python (for checklist export and SUS calculations), OpenCode Agent Skill (Markdown/JSON specification), Git.

**Spec:** `/Users/nguyenbaoan/codeLab/kcpm/hw3/2026.HW03.GUI Usability_Vi.md`

## Global Constraints

- SUT: EShop (`https://github.com/ttbhanh/eshop-sut`).
- Package Scope: G2 (Product List / Search `FR-05`, Product Detail `FR-06`, Add to Cart integration `FR-07`).
- Checklist Size: Strict minimum > 40 distinct items covering IA-01, IA-02, IA-03, IA-04.
- Cross-platform: Minimum 3 distinct environments (e.g. Chrome Desktop, Firefox Desktop, Safari Desktop / Mobile Viewport) with student email/MSSV overlay on screenshots.
- Usability Sample: Exactly 7 non-classmate participants with verifiable contact info (middle 4 digits masked).
- Submission archive format: `<MSSV>_HW03_AI_GUIUsability_<Score>.zip`.
- AI Audit & Critique: Mandatory AI log and 200–300 words critique on AI biases/limitations.

## Review Focus

- Review 1: Checklist coverage must span all 4 aspects (IA-01 to IA-04) without duplicate filler items.
- Review 2: AI critique must explicitly identify what AI missed (accessibility, RTL layout, image fallbacks, dark mode edge cases).
- Review 3: SUS score calculation must adhere strictly to Brooke (1996) odd/even normalization formulas.
- Review 4: Cross-platform screenshot artifacts must verify student identity overlay according to Anti-Cheat §11.
- Review 5: Git commit history must contain discrete commits matching each phase of the workflow.

---

### Task 1: Environment Scaffolding & Directory Setup

**Files:**
- Create: `package.json`
- Create: `checklists/README.md`
- Create: `reports/README.md`
- Create: `usability/README.md`
- Create: `cross-platform/README.md`
- Create: `skills/gui-usability-evaluator/SKILL.md`

**Interfaces:**
- Consumes: Project requirements from spec.
- Produces: Base directory tree and automation scripts for report generation.

- [ ] **Step 1: Create directory placeholders and structure**
Initialize directory layout for reports, checklists, usability notes, cross-platform screenshots, and skills.

- [ ] **Step 2: Initialize basic node workspace with utility script for validation**
Provide npm script to validate checklist item counts and compute SUS scores.

- [ ] **Step 3: Verify directory setup and tooling**
Run: `ls -la checklists reports usability cross-platform skills`
Expected: All directories exist and are clean.

- [ ] **Step 4: Commit**
```bash
git add package.json checklists/ reports/ usability/ cross-platform/ skills/
git commit -m "chore: setup directory structure and verification tooling"
```

---

### Task 2: Task 1 - GUI Checklist Design & AI Critique Analysis (>40 Items)

**Files:**
- Create: `checklists/gui_checklist_g2.md`
- Create: `checklists/gui_checklist_g2.csv`
- Create: `checklists/ai_missed_items_critique.md`

**Interfaces:**
- Consumes: Scope G2 (FR-05, FR-06, FR-07) & Aspects IA-01, IA-02, IA-03, IA-04.
- Produces: Detailed checklist with > 40 items (Pass/Fail/Notes schema), plus explicit documentation of items AI missed and reasons why.

- [ ] **Step 1: Draft comprehensive >40 items checklist covering IA-01 through IA-04**
Include IA-01 (General UI: typography, grid alignment, image aspect ratio, responsive wrapping), IA-02 (Forms: search bar debounce, empty query, special chars, price slider min/max, category dropdown, quantity counter), IA-03 (Navigation: breadcrumbs, pagination, back button state retention, card click target), IA-04 (Feedback/State: loading skeletons, empty state, out-of-stock badge, add-to-cart toast).

- [ ] **Step 2: Document human review & AI omission critique**
Detail items AI typically misses (e.g., WCAG 2.1 color contrast on sale tags, screen reader aria-labels on icon buttons, RTL overflow, dark-mode text washout) and explain the prompt/model limitations causing those omissions.

- [ ] **Step 3: Validate checklist count programmatically**
Run a count verification script to ensure item count strictly exceeds 40.
Expected: > 40 checklist rows.

- [ ] **Step 4: Commit**
```bash
git add checklists/
git commit -m "feat(checklist): create comprehensive GUI checklist and AI critique"
```

---

### Task 3: Task 1 - Checklist Execution & Bug Report Template

**Files:**
- Create: `bug-reports/BUG_REPORTS.md`
- Create: `bug-reports/issue_template.md`

**Interfaces:**
- Consumes: `checklists/gui_checklist_g2.md`
- Produces: Execution status documentation with Pass/Fail marks, reproduction steps for Failed items, and ready-to-post GitHub Issue drafts.

- [ ] **Step 1: Create structured Bug Report catalog**
Define bug reports with: Bug ID, Title, Severity (Blocker/Major/Minor), Affected Aspect (IA-01 to IA-04), Steps to Reproduce, Expected Behavior, Actual Behavior, and Screenshot Placeholder.

- [ ] **Step 2: Populate with actual known SUT edge cases and UI quirks for G2**
Document defects on search special characters, price filter inversion, broken image fallbacks, and mobile cart button truncation.

- [ ] **Step 3: Verify bug issue templates match course expectations**
Check that format aligns with GitHub Issues standards and includes required evidence blocks.

- [ ] **Step 4: Commit**
```bash
git add bug-reports/
git commit -m "feat(bugs): document defect catalog and GitHub issue templates"
```

---

### Task 4: Task 2 - Usability Evaluation Plan, Task Scenario & SUS Instrument

**Files:**
- Create: `usability/task_scenario.md`
- Create: `usability/sus_questionnaire_template.md`
- Create: `usability/session_protocol_guide.md`
- Create: `usability/participants_log.md`

**Interfaces:**
- Consumes: Scope G2 E2E Flow (Search product by price/need → Compare/View details → Add to cart).
- Produces: Moderator script, goal-oriented task scenario, 10-item standard SUS questionnaire, open-ended probe questions (Clarity, Error Recovery, Speed, Trust), and participant tracking ledger (masked).

- [ ] **Step 1: Write Goal-Oriented Task Scenario & Moderator Protocol**
Formulate goal: "Find a wireless audio product under 500,000 VND, inspect its specifications/return policy, and add 1 unit to the cart." Include think-aloud prompt instructions and non-leading intervention rules.

- [ ] **Step 2: Formulate standard SUS scale & 4 open probes**
Embed standard 10 SUS questions (1: Strongly Disagree to 5: Strongly Agree) + open probes on Clarity, Error Recovery, Speed, and Trust.

- [ ] **Step 3: Build 7-participant tracking template**
Create compliant table structure: Participant ID (P1-P7), Persona/Background, Contact (Phone/Zalo with middle 4 digits masked `090****123`), Session Timestamp, Moderator Notes.

- [ ] **Step 4: Commit**
```bash
git add usability/
git commit -m "feat(usability): setup protocol, task scenario, SUS instrument and participant ledger"
```

---

### Task 5: Task 2 - SUS Analysis Engine & Synthesis Report

**Files:**
- Create: `scripts/calculate_sus.py`
- Create: `usability/usability_findings_report.md`

**Interfaces:**
- Consumes: Raw SUS response matrices from 7 sessions.
- Produces: Normalized SUS composite score (0-100), adjective rating (e.g. Marginal, Acceptable, Good), and severity-ranked friction analysis (Blocker / Major / Minor).

- [ ] **Step 1: Implement SUS calculation script**
Write script implementing John Brooke's algorithm:
Odd items: `Score - 1`; Even items: `5 - Score`; Composite: `Sum * 2.5`.

- [ ] **Step 2: Generate sample analysis template with real synthesis methodology**
Group friction points into isolated usability bugs vs. systemic UX design problems.

- [ ] **Step 3: Verify script accuracy with benchmark inputs**
Run: `python3 scripts/calculate_sus.py --test`
Expected: Verified score computation against reference values.

- [ ] **Step 4: Commit**
```bash
git add scripts/calculate_sus.py usability/usability_findings_report.md
git commit -m "feat(usability): implement SUS calculator and findings synthesis template"
```

---

### Task 6: Task 3 - Cross-Platform / Cross-Browser Testing Guide & Evidence Layout

**Files:**
- Create: `cross-platform/cross_platform_matrix.md`
- Create: `cross-platform/evidence_instructions.md`

**Interfaces:**
- Consumes: Task 1 checklist executed across 3 environments:
  1. Desktop Chrome (macOS / Windows)
  2. Desktop Firefox
  3. Safari / Mobile Responsive Viewport (or Expo Go Mobile)
- Produces: Comparative matrix of UI discrepancies and evidence capture guide requiring student MSSV overlay.

- [ ] **Step 1: Create cross-platform comparative checklist matrix**
Map UI rendering differences (fonts, input rendering, flex wrap, sticky filter bar) across the 3 selected targets.

- [ ] **Step 2: Specify overlay and artifact verification requirements**
Document exact requirements for screenshot filenames, timestamp visible, localhost URL visible, and student watermark overlay.

- [ ] **Step 3: Commit**
```bash
git add cross-platform/
git commit -m "feat(cross-platform): establish testing matrix and screenshot evidence requirements"
```

---

### Task 7: Task 4 - Agent Skill Implementation (`gui-usability-evaluator`)

**Files:**
- Create: `skills/gui-usability-evaluator/SKILL.md`
- Create: `skills/gui-usability-evaluator/scripts/generate_checklist.py`
- Create: `skills/gui-usability-evaluator/demo_script.md`

**Interfaces:**
- Consumes: SUT UI wireframe / requirements input.
- Produces: Production-grade OpenCode/Agent skill that takes screen/flow specifications and automatically yields a structured GUI checklist + Usability testing plan.

- [ ] **Step 1: Write Agent Skill definition (`SKILL.md`)**
Format skill with clear description, triggers, step-by-step checklist generation rules, and SUS protocol generation instructions.

- [ ] **Step 2: Add utility helper script inside the skill**
Provide python script that automates generating checklist markdown tables from structured component JSON definitions.

- [ ] **Step 3: Write video demo walk-through script**
Write step-by-step script (3-5 minutes) for the student to record themselves invoking and running the skill on a screen.

- [ ] **Step 4: Commit**
```bash
git add skills/
git commit -m "feat(skill): build reusable gui-usability-evaluator agent skill and demo script"
```

---

### Task 8: Deliverables Packaging, AI Audit Report & AI Critique

**Files:**
- Create: `reports/AI_AUDIT_REPORT.md`
- Create: `reports/AI_CRITIQUE.md`
- Create: `reports/MAIN_REPORT.md`
- Create: `README.md`
- Create: `scripts/generate_git_log.sh`

**Interfaces:**
- Consumes: All outputs from Tasks 1 through 7.
- Produces: Final composite report, 200–300 word AI Critique, complete AI interaction log, git commit log, and self-assessment scoring sheet.

- [ ] **Step 1: Draft AI Audit Report**
Log all prompts, timestamps, toolings, and outputs generated during the exercise.

- [ ] **Step 2: Draft AI Critique (200–300 words)**
Analyze AI blind spots, over-confidence in standard UI patterns, failure to consider real-world responsive bugs, and human-in-the-loop takeaways.

- [ ] **Step 3: Compile Main Report (`MAIN_REPORT.md`)**
Consolidate Task 1 (Checklist & Bugs), Task 2 (Usability & SUS), Task 3 (Cross-Platform), and Task 4 (Skill & Demo link).

- [ ] **Step 4: Create self-assessment `README.md` & Git log extractor**
Provide score table (out of 100) and shell script to output `git_commit_log.txt`.

- [ ] **Step 5: Verify all deliverables against submission spec §14**
Check that all 9 required items in `.zip` package are present or mapped.

- [ ] **Step 6: Commit**
```bash
git add reports/ README.md scripts/
git commit -m "docs: finalize main report, AI audit, critique, and packaging scripts"
```
