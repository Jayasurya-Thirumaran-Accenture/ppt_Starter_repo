# EdTech PPT Creation Pipeline

## Overview

An automated pipeline for creating high-quality educational PowerPoint presentations. Content creators upload a module outline, and a series of skills and agents transform it into a polished, verified PPT.

---

## Pipeline Stages

### Stage 1: Outline Upload

- The content creator uploads a **module outline** (markdown or text file) to the repo.
- The outline contains:
  - Module title
  - Target audience and level (beginner / intermediate / advanced)
  - List of topics to cover
  - Learning objectives
  - Estimated slide count or duration

### Stage 2: Outline Verify Skill (`/verify-outline`)

**Purpose:** Validate the uploaded outline before any work begins.

**Checks:**
- All required fields are present (title, audience, topics, objectives)
- Topics are scoped appropriately for the stated audience level
- No duplicate or overlapping topics
- Learning objectives follow Bloom's taxonomy verbs (understand, apply, analyze, etc.)
- Estimated slide count is realistic for the number of topics

**Output:** Passes the outline to Stage 3, or returns feedback to the creator with what needs fixing.

---

### Stage 3: Plan Skill (`/plan-ppt`)

**Purpose:** Expand the verified outline into a detailed slide-by-slide plan.

**Structure for each topic:**

```
Topic: [Topic Name]

1. USE CASE SLIDE(S)
   - Open with a relatable problem or scenario
   - "Why should you care?" framing
   - Visual suggestion (diagram, screenshot, or illustration idea)

2. THEORY SLIDES
   - Core concept explanation (keep text minimal, favor visuals)
   - Key terminology with definitions
   - How-it-works breakdown (step-by-step or flowchart)
   - Comparisons / contrasts where relevant
   - Speaker notes with deeper explanation

3. REAL-WORLD EXAMPLE SLIDE(S)
   - Fetched from the internet (NOT synthetic or made-up)
   - Name the actual organization or person
   - What they did, why, and what the outcome was
   - Source URL for attribution
   - Key takeaway connecting the example back to the theory
```

**Additional plan elements:**
- Title slide design notes
- Agenda / table of contents slide
- Transition slides between topics
- Summary / recap slide
- Q&A slide
- References slide (all real-world example sources)

**Rules:**
- Every real-world example must be sourced from the internet with a verifiable URL
- No synthetic, hypothetical, or fabricated case studies
- Examples should be recent and relevant (prefer last 3-5 years)
- Each topic follows the strict order: Use Case -> Theory -> Real-World Example

**Output:** A structured plan document (`plan-output.md`) listing every slide with its content outline, speaker notes summary, and visual suggestions.

---

### Stage 4: Create Skill (`/create-ppt`)

**Purpose:** Generate the actual PowerPoint file from the plan.

**Inputs:**
- The slide-by-slide plan from Stage 3
- Reference PPTs stored in `.claude/skills/create-ppt/references/` for format, style, and branding consistency

**Process:**
- Match the reference PPT's template (fonts, colors, layouts, logo placement)
- Populate slides following the plan exactly
- Apply consistent formatting:
  - Title slides use the reference title layout
  - Content slides use bullet or visual layouts from the reference
  - Example slides use a distinct layout (e.g., case study card style)
- Embed speaker notes from the plan
- Add slide numbers, footers, and branding per the reference

**Output:** A `.pptx` file in the `output/` directory.

---

### Stage 5: Final Verify Agent (`/verify-ppt`)

**Purpose:** Quality-check the generated PPT before delivery.

**Verification checks:**

| Category            | What it checks                                                        |
|---------------------|-----------------------------------------------------------------------|
| Grammar & Language  | Spelling, grammar, punctuation, consistent tense and voice            |
| Theory Correctness  | Technical accuracy of definitions, explanations, and claims           |
| Format Match        | Slides match the reference PPT template (fonts, colors, layouts)      |
| Structure           | Each topic follows Use Case -> Theory -> Real-World Example order     |
| Real-World Examples | Examples are real (not fabricated), sources are valid and accessible   |
| Completeness        | All topics from the outline are covered, no missing slides            |
| Speaker Notes       | Notes are present and align with slide content                        |
| Visual Consistency  | Diagrams, icons, and images are consistent in style                   |
| Accessibility       | Sufficient contrast, alt text on images, readable font sizes          |

**Output:** A verification report (`verify-report.md`) with:
- Pass / Fail status per category
- List of issues found with slide numbers
- Suggested fixes
- Overall verdict: **Approved** or **Needs Revision**

If **Needs Revision**, the report is sent back to Stage 4 for fixes, then re-verified.

---

## CLAUDE.md — Project Instructions

The `CLAUDE.md` file lives at the repo root and serves as the central knowledge base for Claude when working in this project. It tells Claude **what this project is, how to behave, and what rules to follow** across all skills.

### Contents

```markdown
# EdTech PPT Pipeline

## Project Identity
- This repo is an EdTech content creation pipeline.
- Content creators upload module outlines, and Claude skills transform them into
  polished PowerPoint presentations through a multi-stage pipeline.

## Pipeline Order
Always follow this sequence — never skip a stage:
1. `/verify-outline` — validate the uploaded outline
2. `/plan-ppt` — expand outline into slide-by-slide plan
3. `/create-ppt` — generate the .pptx from the plan
4. `/verify-ppt` — final quality check

## Content Rules
- Every topic MUST follow this slide order: Use Case → Theory → Real-World Example
- Real-world examples MUST be sourced from the internet with verifiable URLs
- NEVER use synthetic, hypothetical, or fabricated examples
- Prefer examples from the last 3-5 years
- Learning objectives must use Bloom's taxonomy action verbs

## Slide Design Rules
- Max 6 bullet points per slide
- Max 8 words per bullet point
- Favor visuals over text — diagrams, flowcharts, icons
- Speaker notes carry the detailed explanation, not the slide face
- Always include slide numbers and module title in footer

## Branding & Style
- Match fonts, colors, and layouts from reference PPTs in
  `.claude/skills/create-ppt/references/`
- Title slides: use reference title layout exactly
- Content slides: use reference bullet/visual layouts
- Example slides: use case-study card layout
- Maintain consistent icon style throughout

## Tone & Language
- Professional but approachable — avoid jargon unless the audience level demands it
- Beginner: plain language, analogies, no assumed knowledge
- Intermediate: technical terms with brief context
- Advanced: technical depth, assume foundational knowledge
- Always use active voice on slides

## File Conventions
- Outlines go in `input/`
- Generated PPTs go in `output/`
- Verification reports go in `reports/`
- Reference templates stay in `.claude/skills/create-ppt/references/`
- Plan outputs are saved as `reports/plan-output.md`
```

### Why CLAUDE.md matters

- **Consistency across sessions**: Any creator opening this repo gets the same behavior from Claude — same rules, same ordering, same quality bar.
- **Single source of truth**: Style rules, content policies, and pipeline order live here, not scattered across skill files. Skills reference CLAUDE.md for shared rules.
- **Onboarding**: A new team member reads CLAUDE.md and immediately understands the project workflow without needing a walkthrough.

---

## settings.json — Permissions Configuration

The `.claude/settings.json` file controls what Claude is **allowed to do** in this project. This keeps the pipeline functional while preventing unintended actions.

### Configuration

```json
{
  "permissions": {
    "allow": [
      "WebSearch",
      "WebFetch",
      "Read",
      "Write",
      "Edit",
      "Glob",
      "Grep",
      "Bash(python*)",
      "Bash(pip install python-pptx*)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push*)",
      "Bash(git reset --hard*)"
    ]
  }
}
```

### Permission Rationale

| Permission | Why it's allowed |
|---|---|
| `WebSearch` | `/plan-ppt` needs to find real-world examples from the internet |
| `WebFetch` | Fetch details from URLs found during web search for example slides |
| `Read` | Read outlines, reference PPTs, plan outputs, and reports |
| `Write` | Create plan documents, PPT files, and verification reports |
| `Edit` | Update plans or reports based on verification feedback |
| `Glob` / `Grep` | Navigate the repo — find outlines, references, existing outputs |
| `Bash(python*)` | Run Python scripts for PPT generation via `python-pptx` |
| `Bash(pip install python-pptx*)` | Install the PPT generation library if not present |

| Permission | Why it's denied |
|---|---|
| `Bash(rm -rf *)` | Prevent accidental deletion of outlines, outputs, or references |
| `Bash(git push*)` | Creator should review and push manually — no auto-publishing |
| `Bash(git reset --hard*)` | Protect work-in-progress from being discarded |

### What settings.json does NOT cover

- **No hooks**: Pipeline stages are triggered manually by the creator. This gives full control to review the plan before generating the PPT, and review the PPT before finalizing.
- **No MCP servers**: All tooling runs locally through Claude's built-in tools and Python scripts.

---

## Directory Structure

```
repo/
  input/                        # Module outlines uploaded by creators
    module-outline.md
  output/                       # Generated PPTs
    module-name.pptx
  reports/                      # Verification reports and plan outputs
    verify-report.md
    plan-output.md
  .claude/
    settings.json               # Permissions (allow/deny rules)
    skills/
      verify-outline/           # Stage 2 skill
        skill.md
      plan-ppt/                 # Stage 3 skill
        skill.md
      create-ppt/               # Stage 4 skill
        skill.md
        references/             # Reference PPTs for style matching
          reference-template.pptx
      verify-ppt/               # Stage 5 skill
        skill.md
  plan.md                       # This file
  CLAUDE.md                     # Project-wide rules, style, and pipeline instructions
```

## Workflow Summary

```
[Creator uploads outline]
        |
        v
  /verify-outline  -->  Pass? --No--> Fix outline & re-upload
        |
       Yes
        v
    /plan-ppt      -->  Generates slide-by-slide plan
        |                (Use Case -> Theory -> Real-World Example per topic)
        v                (Real examples fetched from internet)
   /create-ppt     -->  Builds .pptx from plan + reference template
        |
        v
   /verify-ppt     -->  Pass? --No--> Fix & re-verify
        |
       Yes
        v
  [Final PPT delivered]
```
