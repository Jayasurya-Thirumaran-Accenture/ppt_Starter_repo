# EdTech PPT Pipeline

## Project Identity

This repo is an EdTech content creation pipeline. Content creators upload module outlines, and Claude skills transform them into polished PowerPoint presentations through a multi-stage pipeline.

## Pipeline Order

Always follow this sequence — never skip a stage:

1. `/verify-outline` — validate the uploaded outline
2. `/plan-ppt` — expand outline into slide-by-slide plan
3. `/create-ppt` — generate the .pptx from the plan
4. `/verify-ppt` — final quality check

## Content Rules

- Every topic MUST follow this slide order: **Use Case → Theory → Real-World Example**
- Real-world examples MUST be sourced from the internet with verifiable URLs
- NEVER use synthetic, hypothetical, or fabricated examples
- Prefer examples from the last 3-5 years
- Learning objectives must use Bloom's taxonomy action verbs (understand, apply, analyze, evaluate, create)

## Slide Design Rules

- Max 6 bullet points per slide
- Max 8 words per bullet point
- Favor visuals over text — diagrams, flowcharts, icons
- Speaker notes carry the detailed explanation, not the slide face
- Always include slide numbers and module title in footer

## Branding & Style

- Match fonts, colors, and layouts from reference PPTs in `.claude/skills/create-ppt/references/`
- Title slides: use reference title layout exactly
- Content slides: use reference bullet/visual layouts
- Example slides: use case-study card layout
- Maintain consistent icon style throughout

## Tone & Language

- Professional but approachable — avoid jargon unless the audience level demands it
- **Beginner**: plain language, analogies, no assumed knowledge
- **Intermediate**: technical terms with brief context
- **Advanced**: technical depth, assume foundational knowledge
- Always use active voice on slides

## File Conventions

- Outlines go in `input/`
- Generated PPTs go in `output/`
- Verification reports and plan outputs go in `reports/`
- Reference templates stay in `.claude/skills/create-ppt/references/`

## Dependencies

- Python library: `python-pptx` (for PPT generation)
- Install with: `pip install python-pptx`
