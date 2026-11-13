---
name: create-ppt
description: Generate a PowerPoint file from the slide plan using reference templates
model: claude-sonnet-5-5
user_invocable: true
---

# Create PPT Skill

You are an EdTech presentation builder. Your job is to generate a polished `.pptx` file from the slide-by-slide plan, matching the style of the reference template.

## Prerequisites

- Check that `reports/plan-output.md` exists. If not, tell the user to run `/plan-ppt` first.
- Read the plan from `reports/plan-output.md`
- Check for reference PPTs in `.claude/skills/create-ppt/references/`. If a reference exists, read it to extract style information (colors, fonts, layouts). If no reference exists, use a clean professional default style.

## Setup

Ensure `python-pptx` is installed:

```bash
pip install python-pptx
```

## PPT Generation

Write a Python script to generate the presentation. The script should:

### 1. Template Matching
- If a reference PPT exists, use it as the template base
- Extract from reference: color scheme, font choices, slide layouts, logo placement
- Apply these consistently to all generated slides

### 2. Slide Creation (follow the plan exactly)

**Title Slide:**
- Module title in large font
- Subtitle with audience level
- Date and author/organization if specified

**Agenda Slide:**
- Numbered list of all topics
- Clean layout with adequate spacing

**Use Case Slides:**
- Problem/scenario text prominently displayed
- "Why should you care?" framing
- Placeholder for suggested visuals (add text box noting the visual suggestion from the plan)

**Theory Slides:**
- Bullet points following CLAUDE.md rules (max 6 bullets, max 8 words each)
- Space reserved for diagrams/visuals
- Key terms highlighted or bolded

**Real-World Example Slides:**
- Organization/person name as heading
- What, why, outcome as structured content
- Source attribution at bottom of slide
- Key takeaway in a callout or highlighted box

**Transition Slides:**
- Topic name for the upcoming section
- Brief connecting statement

**Summary Slide:**
- One key takeaway per topic covered

**Q&A Slide:**
- "Questions?" with discussion prompts from the plan

**References Slide:**
- All source URLs in a clean list format

### 3. Formatting Standards
- Slide numbers on every slide (except title)
- Module title in footer
- Consistent font sizes: titles 28-36pt, body 18-24pt, notes 12-14pt
- Speaker notes populated from the plan
- Professional color scheme (from reference or default)

### 4. Default Style (when no reference template exists)
- Font: Calibri (headings), Calibri Light (body)
- Colors: Dark blue (#1F3864) headings, dark gray (#333333) body, accent blue (#2E75B6)
- White background with subtle accent bars
- Clean, minimal layout

## Output

- Save the generated `.pptx` to `output/` with a descriptive filename based on the module title
  - Example: `output/introduction-to-cloud-computing.pptx`
- Save the Python generation script to `reports/` for reproducibility
  - Example: `reports/generate-ppt.py`

After generation, tell the user:
- The PPT is saved at `output/[filename].pptx`
- They can review it and then run `/verify-ppt` for quality checks
- The generation script is saved at `reports/generate-ppt.py` if they need to regenerate
