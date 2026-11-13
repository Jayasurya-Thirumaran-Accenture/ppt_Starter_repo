from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import os

VISUALS_DIR = r"C:\Users\JAYASU~1.THI\AppData\Local\Temp\claude\C--Users-jayasurya-thirumaran-OneDrive---Accenture-Desktop-Learning-session-9-Hands-on-1\d9d5af22-3786-427f-bb5f-4f4cdb28f851\scratchpad\visuals"

def vis_path(name):
    return os.path.join(VISUALS_DIR, name)

# --- STYLE CONSTANTS (matched from reference PPT) ---
PURPLE_DARK = RGBColor(0x6D, 0x28, 0xD9)     # #6D28D9 - section labels, accents
PURPLE_LIGHT = RGBColor(0x8B, 0x5C, 0xF6)     # #8B5CF6 - tag text
PURPLE_BG = RGBColor(0x1E, 0x12, 0x33)         # #1E1233 - dark bg, heading text
PURPLE_PALE = RGBColor(0xE7, 0xDE, 0xFB)       # #E7DEFB - light purple text
PURPLE_CARD_BG = RGBColor(0xF2, 0xEC, 0xFB)    # #F2ECFB - card backgrounds
AMBER = RGBColor(0xF5, 0x9E, 0x0B)             # #F59E0B - highlights, callouts
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK_TEXT = RGBColor(0x1E, 0x12, 0x33)
BODY_GRAY = RGBColor(0x6B, 0x62, 0x80)         # #6B6280 - body text
TEAL = RGBColor(0x0E, 0xA5, 0xA4)              # #0EA5A4 - secondary accent
ACCENT_BLUE = RGBColor(0x2E, 0x75, 0xB6)

HEADING_FONT = "Trebuchet MS"
BODY_FONT = "Calibri"

SLIDE_WIDTH = 12192000   # standard widescreen
SLIDE_HEIGHT = 6858000

prs = Presentation()
prs.slide_width = SLIDE_WIDTH
prs.slide_height = SLIDE_HEIGHT

def emu(inches):
    return Inches(inches)

def add_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_shape_bg(slide, left, top, width, height, color, corner_radius=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    if corner_radius:
        shape.adjustments[0] = corner_radius
    return shape

def add_rect(slide, left, top, width, height, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape

def add_textbox(slide, left, top, width, height):
    return slide.shapes.add_textbox(left, top, width, height)

def set_text(tf, text, font_name=BODY_FONT, size=Pt(14), bold=False, color=DARK_TEXT, align=PP_ALIGN.LEFT):
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color
    return run

def add_para(tf, text, font_name=BODY_FONT, size=Pt(14), bold=False, color=DARK_TEXT, align=PP_ALIGN.LEFT, space_before=Pt(4), space_after=Pt(2)):
    p = tf.add_paragraph()
    p.alignment = align
    p.space_before = space_before
    p.space_after = space_after
    run = p.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = size
    run.font.bold = bold
    run.font.color.rgb = color
    return run

def add_footer(slide, slide_num):
    tb = add_textbox(slide, emu(0.3), emu(7.05), emu(12), emu(0.35))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = "Data Manipulation with Python Pandas  \u00b7  Intermediate  \u00b7  5-Day Python Training"
    run.font.name = BODY_FONT
    run.font.size = Pt(9)
    run.font.color.rgb = BODY_GRAY
    # slide number on right
    tb2 = add_textbox(slide, emu(11.5), emu(7.05), emu(1), emu(0.35))
    tf2 = tb2.text_frame
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.RIGHT
    run2 = p2.add_run()
    run2.text = str(slide_num).zfill(2)
    run2.font.name = HEADING_FONT
    run2.font.size = Pt(12)
    run2.font.bold = True
    run2.font.color.rgb = PURPLE_DARK

def add_speaker_notes(slide, text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = text

def make_title_slide():
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
    add_bg(slide, PURPLE_BG)
    # top accent bar
    add_rect(slide, 0, 0, SLIDE_WIDTH, Emu(80000), PURPLE_DARK)
    # tag line
    tb = add_textbox(slide, emu(0.8), emu(0.8), emu(10), emu(0.4))
    set_text(tb.text_frame, "TECHNOLOGY EDUCATION  \u00b7  PYTHON PANDAS  \u00b7  HANDS-ON TRAINING",
             HEADING_FONT, Pt(13), True, PURPLE_LIGHT, PP_ALIGN.LEFT)
    # main title
    tb = add_textbox(slide, emu(0.8), emu(1.5), emu(9), emu(2.5))
    tf = tb.text_frame
    tf.word_wrap = True
    set_text(tf, "Data Manipulation", HEADING_FONT, Pt(54), True, WHITE)
    add_para(tf, "with Python Pandas", HEADING_FONT, Pt(54), True, WHITE, space_before=Pt(0))
    # subtitle
    tb = add_textbox(slide, emu(0.8), emu(3.8), emu(10), emu(0.6))
    set_text(tb.text_frame, "Intermediate Level \u2014 Part of a 5-Day Python Training Session",
             BODY_FONT, Pt(17), False, PURPLE_PALE)
    # problem statement box
    add_shape_bg(slide, emu(0.8), emu(4.8), emu(10.5), emu(0.7), PURPLE_DARK, 0.05)
    tb = add_textbox(slide, emu(1.0), emu(4.85), emu(10), emu(0.6))
    tf = tb.text_frame
    set_text(tf, "THE GOAL   ", HEADING_FONT, Pt(11.5), True, AMBER)
    run = tf.paragraphs[0].add_run()
    run.text = "Master loading, cleaning, transforming, and merging data with pandas."
    run.font.name = HEADING_FONT
    run.font.size = Pt(15.5)
    run.font.bold = True
    run.font.color.rgb = WHITE
    # three pillars
    pillar_x = [1.0, 4.5, 8.0]
    pillar_labels = ["7 Topics", "40 Slides", "Real Examples"]
    for i, (x, label) in enumerate(zip(pillar_x, pillar_labels)):
        add_shape_bg(slide, emu(x), emu(5.8), emu(2.8), emu(0.7), RGBColor(0x2D, 0x1A, 0x56), 0.08)
        tb = add_textbox(slide, emu(x + 0.1), emu(5.85), emu(2.6), emu(0.6))
        set_text(tb.text_frame, label, HEADING_FONT, Pt(13), True, WHITE, PP_ALIGN.CENTER)
    # bottom text
    tb = add_textbox(slide, emu(0.8), emu(6.7), emu(10), emu(0.4))
    set_text(tb.text_frame, "For Python developers and aspiring data analysts",
             BODY_FONT, Pt(11.5), False, RGBColor(0xC9, 0xB8, 0xEE))
    add_speaker_notes(slide, "Welcome slide. This module covers Python Pandas for data manipulation. Part of a 5-day Python training. Audience: Python developers and aspiring data analysts with basic Python knowledge.")

def make_agenda_slide():
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, WHITE)
    # section label
    tb = add_textbox(slide, emu(0.8), emu(0.5), emu(5), emu(0.35))
    set_text(tb.text_frame, "AGENDA", HEADING_FONT, Pt(11.5), True, PURPLE_DARK)
    # title
    tb = add_textbox(slide, emu(0.8), emu(0.85), emu(10), emu(0.6))
    set_text(tb.text_frame, "What We Will Cover Today", HEADING_FONT, Pt(29), True, DARK_TEXT)
    topics = [
        ("01", "Introduction to Pandas", "What and Why"),
        ("02", "Data Structures", "Series and DataFrame"),
        ("03", "Loading & Inspecting Data", "CSV, Excel, JSON, SQL"),
        ("04", "Selection & Filtering", "loc, iloc, boolean indexing"),
        ("05", "Data Cleaning", "Handling Missing Values"),
        ("06", "Data Transformation", "apply, map, groupby, aggregation"),
        ("07", "Merging & Reshaping", "merge, concat, pivot_table"),
    ]
    y_start = 1.7
    for i, (num, title, subtitle) in enumerate(topics):
        y = y_start + i * 0.72
        # number circle
        add_shape_bg(slide, emu(0.8), emu(y), emu(0.55), emu(0.5), PURPLE_DARK, 0.5)
        tb = add_textbox(slide, emu(0.8), emu(y + 0.05), emu(0.55), emu(0.4))
        set_text(tb.text_frame, num, HEADING_FONT, Pt(12), True, WHITE, PP_ALIGN.CENTER)
        # topic title
        tb = add_textbox(slide, emu(1.6), emu(y - 0.02), emu(5), emu(0.3))
        set_text(tb.text_frame, title, HEADING_FONT, Pt(15.5), True, DARK_TEXT)
        # subtitle
        tb = add_textbox(slide, emu(1.6), emu(y + 0.28), emu(5), emu(0.25))
        set_text(tb.text_frame, subtitle, BODY_FONT, Pt(11), False, BODY_GRAY)
    add_footer(slide, 2)
    add_speaker_notes(slide, "Agenda overview. 7 topics covering pandas end-to-end: from intro and data structures through loading, filtering, cleaning, transformation, and merging. Each topic follows: Use Case, Theory, Real-World Example.")

def make_use_case_slide(slide_num, section_label, title, bullets, visual_note, speaker_notes, image_path=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, WHITE)
    # section label
    tb = add_textbox(slide, emu(0.8), emu(0.5), emu(5), emu(0.35))
    set_text(tb.text_frame, section_label, HEADING_FONT, Pt(11.5), True, PURPLE_DARK)
    # title
    tb = add_textbox(slide, emu(0.8), emu(0.85), emu(10), emu(0.6))
    set_text(tb.text_frame, title, HEADING_FONT, Pt(29), True, DARK_TEXT)
    # use case box
    add_shape_bg(slide, emu(0.6), emu(1.8), emu(7), emu(3.8), PURPLE_BG, 0.03)
    tb = add_textbox(slide, emu(0.9), emu(1.95), emu(6.4), emu(3.5))
    tf = tb.text_frame
    tf.word_wrap = True
    first = True
    for bullet in bullets:
        if first:
            set_text(tf, bullet, BODY_FONT, Pt(17), False, WHITE)
            first = False
        else:
            add_para(tf, bullet, BODY_FONT, Pt(17), False, WHITE, space_before=Pt(14))
    # visual: embedded image or fallback text
    add_shape_bg(slide, emu(8.0), emu(1.8), emu(3.8), emu(3.8), PURPLE_CARD_BG, 0.03)
    if image_path and os.path.exists(image_path):
        slide.shapes.add_picture(image_path, emu(8.1), emu(1.9), emu(3.6), emu(3.6))
    else:
        tb = add_textbox(slide, emu(8.2), emu(2.0), emu(3.4), emu(0.3))
        set_text(tb.text_frame, "VISUAL SUGGESTION", HEADING_FONT, Pt(10), True, PURPLE_DARK)
        tb = add_textbox(slide, emu(8.2), emu(2.5), emu(3.4), emu(2.8))
        set_text(tb.text_frame, visual_note, BODY_FONT, Pt(12), False, BODY_GRAY)
    add_footer(slide, slide_num)
    add_speaker_notes(slide, speaker_notes)

def make_theory_slide(slide_num, section_label, title, bullets, visual_note, speaker_notes, image_path=None):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, WHITE)
    # section label
    tb = add_textbox(slide, emu(0.8), emu(0.5), emu(5), emu(0.35))
    set_text(tb.text_frame, section_label, HEADING_FONT, Pt(11.5), True, PURPLE_DARK)
    # title
    tb = add_textbox(slide, emu(0.8), emu(0.85), emu(10), emu(0.6))
    set_text(tb.text_frame, title, HEADING_FONT, Pt(29), True, DARK_TEXT)
    # content area
    tb = add_textbox(slide, emu(0.8), emu(1.8), emu(7), emu(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    first = True
    for bullet in bullets:
        if first:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.space_before = Pt(8)
        p.space_after = Pt(4)
        # bullet marker
        run = p.add_run()
        run.text = "\u25b8  "
        run.font.name = HEADING_FONT
        run.font.size = Pt(15)
        run.font.color.rgb = PURPLE_DARK
        run.font.bold = True
        # if bullet has bold prefix (before the dash)
        if " \u2014 " in bullet:
            parts = bullet.split(" \u2014 ", 1)
            run2 = p.add_run()
            run2.text = parts[0]
            run2.font.name = HEADING_FONT
            run2.font.size = Pt(15)
            run2.font.bold = True
            run2.font.color.rgb = DARK_TEXT
            run3 = p.add_run()
            run3.text = " \u2014 " + parts[1]
            run3.font.name = BODY_FONT
            run3.font.size = Pt(14)
            run3.font.color.rgb = BODY_GRAY
        else:
            run2 = p.add_run()
            run2.text = bullet
            run2.font.name = BODY_FONT
            run2.font.size = Pt(15)
            run2.font.color.rgb = DARK_TEXT
        first = False
    # visual box on right: embedded image or fallback text
    if image_path and os.path.exists(image_path):
        add_shape_bg(slide, emu(8.2), emu(1.8), emu(3.6), emu(3.5), PURPLE_CARD_BG, 0.03)
        slide.shapes.add_picture(image_path, emu(8.3), emu(1.9), emu(3.4), emu(3.3))
    elif visual_note:
        add_shape_bg(slide, emu(8.2), emu(1.8), emu(3.6), emu(3.5), PURPLE_CARD_BG, 0.03)
        tb = add_textbox(slide, emu(8.4), emu(2.0), emu(3.2), emu(3.2))
        tf2 = tb.text_frame
        tf2.word_wrap = True
        set_text(tf2, visual_note, BODY_FONT, Pt(11), False, BODY_GRAY)
    add_footer(slide, slide_num)
    add_speaker_notes(slide, speaker_notes)

def make_example_slide(slide_num, section_label, org_name, what, why, outcome, source, takeaway, speaker_notes):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, WHITE)
    # section label
    tb = add_textbox(slide, emu(0.8), emu(0.5), emu(5), emu(0.35))
    set_text(tb.text_frame, section_label, HEADING_FONT, Pt(11.5), True, PURPLE_DARK)
    # title
    tb = add_textbox(slide, emu(0.8), emu(0.85), emu(10), emu(0.5))
    set_text(tb.text_frame, "Real-World Example", HEADING_FONT, Pt(29), True, DARK_TEXT)
    # org name card
    add_shape_bg(slide, emu(0.6), emu(1.6), emu(11), emu(1.0), PURPLE_BG, 0.03)
    tb = add_textbox(slide, emu(0.9), emu(1.7), emu(10.5), emu(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    set_text(tf, org_name, HEADING_FONT, Pt(24), True, WHITE)
    # detail cards
    labels = ["WHAT", "WHY", "OUTCOME"]
    values = [what, why, outcome]
    colors = [PURPLE_DARK, TEAL, AMBER]
    y_pos = 2.9
    for i, (label, value, lcolor) in enumerate(zip(labels, values, colors)):
        y = y_pos + i * 1.1
        # label
        tb = add_textbox(slide, emu(0.9), emu(y), emu(1.2), emu(0.3))
        set_text(tb.text_frame, label, HEADING_FONT, Pt(10), True, lcolor)
        # value
        tb = add_textbox(slide, emu(2.1), emu(y), emu(9.3), emu(0.9))
        set_text(tb.text_frame, value, BODY_FONT, Pt(13), False, DARK_TEXT)
    # takeaway bar
    add_shape_bg(slide, emu(0.6), emu(6.0), emu(11), emu(0.65), RGBColor(0xFE, 0xF3, 0xC7), 0.03)
    tb = add_textbox(slide, emu(0.9), emu(6.05), emu(10.5), emu(0.55))
    tf = tb.text_frame
    tf.word_wrap = True
    run = set_text(tf, "KEY TAKEAWAY   ", HEADING_FONT, Pt(9), True, AMBER)
    run2 = tf.paragraphs[0].add_run()
    run2.text = takeaway
    run2.font.name = BODY_FONT
    run2.font.size = Pt(12)
    run2.font.bold = True
    run2.font.color.rgb = DARK_TEXT
    # source
    tb = add_textbox(slide, emu(0.8), emu(6.7), emu(10), emu(0.3))
    set_text(tb.text_frame, "Source: " + source, BODY_FONT, Pt(9), False, BODY_GRAY)
    add_footer(slide, slide_num)
    add_speaker_notes(slide, speaker_notes)

def make_transition_slide(slide_num, topic_title, connecting_text):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide, PURPLE_BG)
    add_rect(slide, 0, 0, SLIDE_WIDTH, Emu(80000), PURPLE_DARK)
    # big text
    tb = add_textbox(slide, emu(1.5), emu(2.5), emu(9.5), emu(1.5))
    tf = tb.text_frame
    tf.word_wrap = True
    set_text(tf, connecting_text, HEADING_FONT, Pt(28), True, WHITE, PP_ALIGN.CENTER)
    # subtle hint
    tb = add_textbox(slide, emu(1.5), emu(4.2), emu(9.5), emu(0.5))
    set_text(tb.text_frame, "UP NEXT: " + topic_title, HEADING_FONT, Pt(13), True, AMBER, PP_ALIGN.CENTER)
    add_footer(slide, slide_num)

# ==================== BUILD ALL 40 SLIDES ====================

# SLIDE 1: Title
make_title_slide()

# SLIDE 2: Agenda
make_agenda_slide()

# SLIDE 3: Topic 1 - Use Case
make_use_case_slide(3, "USE CASE  \u00b7  TOPIC 1",
    "Why Do You Need Pandas?",
    [
        "\u201cYou have 10,000 rows of sales data in a CSV.\u201d",
        "\u201cYour manager wants a summary by region \u2014 by tomorrow.\u201d",
        "\u201cExcel crashes. SQL feels overkill. What do you use?\u201d",
    ],
    "Illustration of an overloaded Excel spreadsheet showing a 'Not Responding' dialog box \u2014 a relatable moment for anyone who's hit Excel's limits.",
    "Frame the problem: raw data is everywhere \u2014 CSVs, databases, APIs. Analysts need a tool that sits between Excel (too limited) and SQL (too rigid for exploration). Pandas fills that gap. It was literally created for this \u2014 Wes McKinney built it at a hedge fund because existing tools couldn't keep up with financial data analysis.",
    image_path=vis_path("excel_crash.png")
)

# SLIDE 4: Topic 1 - Theory
make_theory_slide(4, "THEORY  \u00b7  TOPIC 1",
    "What is Pandas?",
    [
        "Python library for data manipulation",
        "Built on top of NumPy arrays",
        "Handles tabular data (rows and columns)",
        "Read, clean, transform, analyze \u2014 all in one",
        "import pandas as pd \u2014 the universal convention",
    ],
    "Diagram: Raw Data \u2192 Pandas \u2192 Clean Insights\n\nPandas sits in the middle of the Python data ecosystem, connecting data sources to analysis tools.",
    "Pandas provides two core data structures (Series and DataFrame \u2014 covered next). It integrates with the entire Python data ecosystem: NumPy for computation, Matplotlib/Seaborn for visualization, scikit-learn for ML. Created by Wes McKinney in 2008, open-sourced in 2009. The name comes from 'panel data,' an econometrics term.",
    image_path=vis_path("pipeline.png")
)

# SLIDE 5: Topic 1 - Example
make_example_slide(5, "REAL-WORLD EXAMPLE  \u00b7  TOPIC 1",
    "AQR Capital Management",
    "Wes McKinney, a quantitative analyst at AQR, built pandas in 2008 because existing tools couldn't handle the firm's financial data analysis needs efficiently.",
    "The quant research team needed a high-performance, flexible tool for analyzing trading strategies across global macro and credit markets.",
    "Pandas was open-sourced in 2009 and is now used by 77% of Python data professionals (JetBrains/PSF Developer Survey 2024).",
    "Wikipedia \u2014 Pandas (software) | wesmckinney.com/about",
    "Pandas was born from a real business need in finance \u2014 it wasn't an academic project, it was built to solve daily data problems.",
    "McKinney worked at AQR from 2007-2010 on the front office quant research team. He convinced management to allow him to open-source the library before leaving. Chang She, another AQR employee, became the second major contributor in 2012. This origin story shows that pandas was designed for real-world, messy, time-series financial data \u2014 not just clean textbook datasets."
)

# SLIDE 6: Transition
make_transition_slide(6, "Data Structures",
    "Now that you know WHY pandas exists,\nlet\u2019s learn its building blocks")

# SLIDE 7: Topic 2 - Use Case
make_use_case_slide(7, "USE CASE  \u00b7  TOPIC 2",
    "Series vs DataFrame: Know Your Containers",
    [
        "A list of 500 product prices \u2014 that\u2019s a Series.",
        "A full product catalog (names, prices, stock) \u2014 that\u2019s a DataFrame.",
        "Knowing which to use is the first step.",
    ],
    "Side-by-side comparison: a single column (Series) vs. a multi-column table (DataFrame) with clear visual distinction.",
    "Before you can manipulate data, you need to understand how pandas stores it. Think of Series as a single column in a spreadsheet and DataFrame as the entire spreadsheet. Every pandas operation returns one of these two structures.",
    image_path=vis_path("data_structures.png")
)

# SLIDE 8: Topic 2 - Theory (Series)
make_theory_slide(8, "THEORY  \u00b7  TOPIC 2",
    "Series: The 1D Labeled Array",
    [
        "1D labeled array \u2014 one column of data",
        "Holds any data type (int, float, string)",
        "Has an index (labels for each value)",
        "Created from lists, dicts, or NumPy arrays",
        "pd.Series([10, 20, 30], name=\"prices\")",
    ],
    "Diagram: Vertical strip showing index-value pairs\n\nIndex: 0, 1, 2\nValues: 10, 20, 30\n\nLike a Python dict with vectorized math.",
    "A Series is like a Python dictionary with superpowers \u2014 it has an index (like keys) and values, but supports vectorized operations. You can do math on an entire Series at once without loops. The index doesn't have to be integers \u2014 it can be dates, names, or any hashable type.",
    image_path=vis_path("data_structures.png")
)

# SLIDE 9: Topic 2 - Theory (DataFrame)
make_theory_slide(9, "THEORY  \u00b7  TOPIC 2",
    "DataFrame: The 2D Labeled Table",
    [
        "2D labeled table \u2014 collection of Series",
        "Rows = observations, Columns = variables",
        "Most common pandas object you'll use",
        "Supports SQL-like operations with Python flexibility",
        "pd.DataFrame({\"name\": [...], \"price\": [...]})",
    ],
    "Table diagram:\n\n  index | name   | price\n  0     | Widget | 9.99\n  1     | Gadget | 19.99\n  2     | Gizmo  | 14.99\n\nEach column is a Series.",
    "A DataFrame is essentially a dictionary of Series objects that share the same index. Each column is a Series. You can select a single column and get a Series back. DataFrames support SQL-like operations (select, filter, group, join) but with Python's flexibility. Most data you load from files becomes a DataFrame automatically.",
    image_path=vis_path("data_structures.png")
)

# SLIDE 10: Topic 2 - Example
make_example_slide(10, "REAL-WORLD EXAMPLE  \u00b7  TOPIC 2",
    "Two Sigma Investments",
    "Two Sigma built an internal data stack called 'Bamboo' with pandas DataFrames at its core for quantitative research.",
    "Their research teams need to manipulate financial time-series data rapidly; DataFrames provide the natural tabular structure for this.",
    "Jeff Reback, a Two Sigma Managing Director, became one of pandas' most prolific open-source contributors, and Two Sigma actively sponsors pandas development.",
    "twosigma.com/articles/pandas-at-a-crossroads | twosigma.com/articles/the-future-of-pandas",
    "The DataFrame is so central to data work that one of the world's largest hedge funds built its entire research infrastructure around it.",
    "Two Sigma manages over $60 billion and runs thousands of quantitative models. Their 'Bamboo' stack uses pandas for datasets that fit in memory and translates to Apache Spark via Ibis for larger sets. The fact that a Two Sigma MD contributes to pandas core shows how critical the DataFrame abstraction is to real finance workflows."
)

# SLIDE 11: Transition
make_transition_slide(11, "Loading & Inspecting Data",
    "You know the structures \u2014\nnow let\u2019s load real data into them")

# SLIDE 12: Topic 3 - Use Case
make_use_case_slide(12, "USE CASE  \u00b7  TOPIC 3",
    "Getting Data Into Pandas",
    [
        "Your data lives in CSVs, Excel sheets, databases, APIs.",
        "Step one of every analysis: get it into pandas.",
        "Pandas reads 20+ file formats out of the box.",
    ],
    "Icons for CSV, Excel, JSON, SQL all converging with arrows into a single DataFrame table.",
    "No analysis starts without loading data. In practice, you'll encounter messy CSVs with encoding issues, Excel files with multiple sheets, JSON from APIs, and SQL databases. Pandas has a read_* function for each. The most common is read_csv(), which handles 90% of use cases.",
    image_path=vis_path("loading.png")
)

# SLIDE 13: Topic 3 - Theory (Loading)
make_theory_slide(13, "THEORY  \u00b7  TOPIC 3",
    "Loading Data: The read_* Family",
    [
        "pd.read_csv(\"sales.csv\") \u2014 most common",
        "pd.read_excel(\"report.xlsx\", sheet_name=\"Q1\")",
        "pd.read_json(\"api_response.json\")",
        "pd.read_sql(\"SELECT * FROM users\", conn)",
        "Key params: sep, encoding, na_values, parse_dates",
    ],
    "Code flow:\n\npd.read_csv(\"data.csv\",\n  encoding=\"utf-8\",\n  parse_dates=[\"date\"],\n  na_values=[\"N/A\"])\n\n\u2192 DataFrame",
    "read_csv is the workhorse \u2014 it handles delimiters, headers, data types, missing value markers, date parsing, and more. Common gotchas: wrong encoding (use encoding='utf-8' or 'latin1'), dates read as strings (use parse_dates=['date_col']), and custom missing values (use na_values=['N/A', 'missing']). For large files, use chunksize to read in batches.",
    image_path=vis_path("loading.png")
)

# SLIDE 14: Topic 3 - Theory (Inspecting)
make_theory_slide(14, "THEORY  \u00b7  TOPIC 3",
    "Inspecting Data: First Things First",
    [
        ".head() / .tail() \u2014 first/last 5 rows",
        ".shape \u2014 (rows, columns) count",
        ".dtypes \u2014 data type of each column",
        ".describe() \u2014 summary statistics",
        ".info() \u2014 memory usage and non-null counts",
    ],
    "Sample .info() output:\n\nRangeIndex: 1000 entries\nData columns: 8\nColumn  Non-Null  Dtype\nname    1000      object\nprice   987       float64\ndate    1000      datetime64",
    "Always inspect after loading. .info() is your best friend \u2014 it shows column names, non-null counts (reveals missing data), data types, and memory usage in one call. .describe() gives mean, std, min, max, quartiles for numeric columns. If dtypes look wrong (e.g., numbers read as strings), you caught it early.",
    image_path=vis_path("info_output.png")
)

# SLIDE 15: Topic 3 - Example
make_example_slide(15, "REAL-WORLD EXAMPLE  \u00b7  TOPIC 3",
    "Netflix",
    "Netflix's engineering teams use pandas alongside NumPy, SciPy, and other scientific Python libraries for data analysis across their content and streaming operations.",
    "Their CORE team analyzes large volumes of signals after operational alerts, requiring fast data loading and inspection from multiple sources.",
    "Python and pandas are embedded across Netflix's full content lifecycle \u2014 from content analytics to A/B testing to real-time monitoring.",
    "TechRepublic \u2014 How Netflix Uses Python",
    "Even companies processing billions of events daily rely on pandas for exploratory analysis and signal inspection.",
    "Netflix has publicly documented their Python stack. Their teams use Jupyter notebooks with pandas for interactive data exploration before building production pipelines. The key insight: pandas isn't just for small datasets \u2014 it's the starting point for understanding data before scaling up."
)

# SLIDE 16: Transition
make_transition_slide(16, "Selection & Filtering",
    "Data is loaded \u2014\nnow let\u2019s slice and dice it")

# SLIDE 17: Topic 4 - Use Case
make_use_case_slide(17, "USE CASE  \u00b7  TOPIC 4",
    "Asking Questions of Your Data",
    [
        "You have 1 million transactions but only need Q4 sales.",
        "Or only orders above $500 from California.",
        "Filtering is how you ask questions of your data.",
    ],
    "Large table with a highlighted subset \u2014 filtered rows glowing in purple, unselected rows faded to gray.",
    "Filtering and selection are the most frequent operations in data analysis. You rarely analyze an entire dataset \u2014 you zoom into subsets. 'Show me all customers who churned last month,' 'Find transactions over $10K,' 'Get revenue by product for the West region.' All of these are filtering operations.",
    image_path=vis_path("boolean_indexing.png")
)

# SLIDE 18: Topic 4 - Theory (loc/iloc)
make_theory_slide(18, "THEORY  \u00b7  TOPIC 4",
    "Selection with loc and iloc",
    [
        ".loc[] \u2014 select by label (row/column names)",
        ".iloc[] \u2014 select by integer position (0-based)",
        "df.loc[0:5, \"name\":\"price\"] \u2014 label range",
        "df.iloc[0:5, 0:3] \u2014 position range",
        "Both support single values, slices, and lists",
    ],
    "Grid diagram:\n\nloc = labels (what you see)\niloc = integers (position)\n\nloc includes endpoint\niloc excludes endpoint\n(like Python lists)",
    "The #1 confusion in pandas: loc vs iloc. Simple rule \u2014 loc uses labels (what you see), iloc uses positions (0-based integers). loc includes the endpoint in slices, iloc doesn't (like Python lists). When the index is integers, this gets confusing \u2014 that's why being explicit with loc/iloc is better than using df[0:5].",
    image_path=vis_path("loc_iloc.png")
)

# SLIDE 19: Topic 4 - Theory (Boolean Indexing)
make_theory_slide(19, "THEORY  \u00b7  TOPIC 4",
    "Boolean Indexing: Filter by Condition",
    [
        "df[df[\"price\"] > 100] \u2014 filter by condition",
        "df[df[\"city\"] == \"Mumbai\"] \u2014 exact match",
        "Combine: & (and), | (or), ~ (not)",
        ".isin([\"A\", \"B\"]) \u2014 match multiple values",
        ".query(\"price > 100 and city == 'Mumbai'\")",
    ],
    "Flowchart:\n\nCondition\n  \u2193\nBoolean mask (True/False)\n  \u2193\nFiltered rows (only True)",
    "Boolean indexing is the pandas equivalent of SQL's WHERE clause. The expression df['price'] > 100 returns a Series of True/False values \u2014 a 'mask.' Passing that mask into df[...] returns only the True rows. Always wrap multiple conditions in parentheses: df[(df['a'] > 5) & (df['b'] < 10)]. The .query() method is more readable for complex filters.",
    image_path=vis_path("boolean_indexing.png")
)

# SLIDE 20: Topic 4 - Example
make_example_slide(20, "REAL-WORLD EXAMPLE  \u00b7  TOPIC 4",
    "Instacart (Grocery Dataset)",
    "Instacart released a dataset of 3.4 million grocery orders from 200,000 users; analysts worldwide use pandas boolean indexing to uncover shopping patterns.",
    "Understanding which products are reordered, at what time, and in what combinations drives Instacart's recommendation engine and inventory planning.",
    "Analysis revealed bananas are the #1 reordered item (557,763 reorders). Filtering by time-of-day and department exposed distinct shopping behaviors.",
    "instacart.com/datasets/grocery-shopping-2017 | Kaggle Competition",
    "Filtering 3.4M rows to answer 'which products get reordered on weekends?' is exactly what boolean indexing was built for.",
    "The Instacart dataset is one of the most popular real-world datasets for learning pandas filtering. Analysts filter by department, hour of day, days since prior order, and reorder status. A common exercise: filter to only organic products reordered on weekends \u2014 this requires chaining multiple boolean conditions."
)

# SLIDE 21: Transition
make_transition_slide(21, "Data Cleaning",
    "Real data is messy \u2014\nlet\u2019s learn to clean it")

# SLIDE 22: Topic 5 - Use Case
make_use_case_slide(22, "USE CASE  \u00b7  TOPIC 5",
    "The Messy Data Problem",
    [
        "Your dataset has 15% missing values.",
        "Some rows have 'N/A', others have blank cells.",
        "Drop them? Fill them? It depends on the context.",
    ],
    "Table with scattered empty cells highlighted in red, showing the random pattern of missing data across columns.",
    "Missing data is the most common real-world data problem. Surveys have unanswered questions, sensors fail, APIs return partial records, users skip optional fields. How you handle missing values can change your analysis results dramatically. Dropping too aggressively loses information; filling incorrectly introduces bias.",
    image_path=vis_path("missing_data.png")
)

# SLIDE 23: Topic 5 - Theory (Detection)
make_theory_slide(23, "THEORY  \u00b7  TOPIC 5",
    "Detecting Missing Values",
    [
        "df.isna() \u2014 detect missing (True/False grid)",
        "df.isna().sum() \u2014 count missing per column",
        "df.isna().mean() \u2014 percentage missing per column",
        "Non-standard markers: na_values in read_csv",
        "Visualize: df.isna().sum().plot(kind=\"bar\")",
    ],
    "Bar chart showing missing value counts per column:\n\nname:    0\nprice:  13\ndate:    0\nstock:  47\nrating: 89",
    "Always start by measuring the problem. isna().sum() gives you the count, isna().mean() gives the percentage. Rule of thumb: if a column is >50% missing, consider dropping it entirely. If a row is mostly missing, drop the row. For scattered missing values in important columns, filling is usually better.",
    image_path=vis_path("missing_data.png")
)

# SLIDE 24: Topic 5 - Theory (Handling)
make_theory_slide(24, "THEORY  \u00b7  TOPIC 5",
    "Handling Missing Values",
    [
        "df.dropna() \u2014 remove rows with any missing",
        "df.dropna(thresh=3) \u2014 keep rows with 3+ valid",
        "df.fillna(0) \u2014 fill with a constant value",
        "df.fillna(df.mean()) \u2014 fill with column mean",
        "df.interpolate() \u2014 estimate from neighbors",
    ],
    "Before / After:\n\n[NaN, 10, NaN, 30]\n\u2193 fillna(mean)\n[20, 10, 20, 30]\n\n\u2193 dropna\n[10, 30]",
    "dropna() is the simplest but most aggressive approach \u2014 it removes entire rows. Use thresh to be more selective. fillna() with mean/median is common for numeric data, mode for categorical. For time-series data, interpolate() or fillna(method='ffill') preserves trends. The choice depends on context: dropping is fine for analysis, but filling is usually necessary before feeding data into ML models.",
    image_path=vis_path("fill_strategies.png")
)

# SLIDE 25: Topic 5 - Example
make_example_slide(25, "REAL-WORLD EXAMPLE  \u00b7  TOPIC 5",
    "Goldman Sachs (GS Quant)",
    "Goldman Sachs built and open-sourced GS Quant, a Python toolkit for quantitative finance that uses pandas for data manipulation including handling missing market data.",
    "Financial time-series data frequently has gaps \u2014 markets close on holidays, instruments halt trading, data feeds drop \u2014 and these gaps must be handled correctly for accurate risk modeling.",
    "GS Quant provides built-in functions for filling missing financial data, built on top of pandas' fillna and interpolation capabilities.",
    "eFinancialCareers \u2014 Python Libraries for Finance",
    "Even the world's largest investment bank relies on pandas' missing data tools \u2014 the stakes of getting fill strategies wrong are measured in millions.",
    "In finance, missing data isn't just an inconvenience \u2014 it can break risk models. A missing price for a stock on a holiday needs forward-filling (use last known price), not zero-filling (which would imply the stock is worthless). Goldman Sachs built GS Quant to standardize these decisions."
)

# SLIDE 26: Transition
make_transition_slide(26, "Data Transformation",
    "Clean data in hand \u2014\ntime to transform and aggregate")

# SLIDE 27: Topic 6 - Use Case
make_use_case_slide(27, "USE CASE  \u00b7  TOPIC 6",
    "From Raw Data to Business Answers",
    [
        "You have 100K rows of individual transactions.",
        "Boss asks: 'What\u2019s total revenue per region per month?'",
        "That\u2019s a groupby-aggregate operation.",
    ],
    "Funnel diagram: 100K raw transaction rows narrowing down into a compact summary table grouped by region and month.",
    "Transformation is where analysis actually happens. Loading and cleaning are prep work \u2014 groupby and aggregation are where you extract meaning. 'Total sales by store,' 'average salary by department,' 'count of orders by customer' \u2014 these are all split-apply-combine operations.",
    image_path=vis_path("groupby.png")
)

# SLIDE 28: Topic 6 - Theory (groupby)
make_theory_slide(28, "THEORY  \u00b7  TOPIC 6",
    "GroupBy: Split-Apply-Combine",
    [
        "df.groupby(\"region\")[\"sales\"].sum() \u2014 basic",
        "Split \u2192 Apply \u2192 Combine pattern",
        "Multiple columns: groupby([\"region\", \"month\"])",
        ".agg([\"sum\", \"mean\", \"count\"]) \u2014 multiple aggs",
        "Named: .agg(total=(\"sales\", \"sum\"))",
    ],
    "3-step diagram:\n\n1. SPLIT: Group by region\n   [East] [West] [North]\n\n2. APPLY: sum(sales)\n   [150K] [200K] [120K]\n\n3. COMBINE: Result table",
    "The split-apply-combine pattern is the foundation of data aggregation. groupby splits the DataFrame into groups based on column values, applies a function (sum, mean, count, custom), and combines results into a new DataFrame. You can group by multiple columns for nested summaries.",
    image_path=vis_path("groupby.png")
)

# SLIDE 29: Topic 6 - Theory (apply/map)
make_theory_slide(29, "THEORY  \u00b7  TOPIC 6",
    "Transform, Apply, and Map",
    [
        ".apply(func) \u2014 apply any function row/column-wise",
        ".map(dict) \u2014 map values using a dictionary",
        ".transform() \u2014 return same-size output",
        "Method chaining: df.assign().query().groupby()",
        "Lambda: .apply(lambda x: x.upper())",
    ],
    "apply vs transform:\n\napply: flexible, any output\ntransform: same shape back\n\nUse transform for\n'group % of total' patterns",
    "apply is the Swiss army knife \u2014 it can apply any function to rows or columns. It's flexible but slower than built-in methods. Prefer vectorized operations when possible. transform is special \u2014 it returns a result with the same index as the input, making it perfect for group-level calculations assigned back to each row."
)

# SLIDE 30: Topic 6 - Example
make_example_slide(30, "REAL-WORLD EXAMPLE  \u00b7  TOPIC 6",
    "Spotify (Data Platform)",
    "Spotify operates 20,000+ batch data pipelines across 300+ teams; data scientists use pandas groupby and aggregation in Jupyter notebooks for exploratory analysis.",
    "Before building production pipelines, Spotify's analysts prototype aggregations in pandas \u2014 grouping streams by artist, region, and time period to identify trends.",
    "Insights from pandas-based exploration inform Spotify's recommendation algorithms and business decisions for 600M+ users.",
    "engineering.atspotify.com | ByteByteGo \u2014 Spotify Data Platform",
    "Groupby-aggregate is the first analysis step even at massive scale \u2014 Spotify analysts prototype in pandas before building production pipelines.",
    "Spotify's data platform processes petabytes of data, but the analysis journey often starts in a Jupyter notebook with pandas. An analyst might group stream data by country and genre to spot emerging trends, then hand that logic off to a Spark pipeline for production."
)

# SLIDE 31: Transition
make_transition_slide(31, "Merging & Reshaping",
    "Single datasets are useful \u2014\ncombining them is powerful")

# SLIDE 32: Topic 7 - Use Case
make_use_case_slide(32, "USE CASE  \u00b7  TOPIC 7",
    "Combining Data From Multiple Sources",
    [
        "Orders in one table, customers in another, products in a third.",
        "You need a unified view joining all three.",
        "This is relational data \u2014 pandas handles it like SQL.",
    ],
    "Three separate tables (Orders, Customers, Products) with connecting lines on shared keys, merging into a single unified DataFrame.",
    "Real-world data rarely lives in a single table. CRM data has customers, orders, and products in separate tables. HR data has employees, departments, and salaries. Analytics data comes from multiple APIs. Merging these into a single DataFrame is the equivalent of SQL JOINs.",
    image_path=vis_path("joins.png")
)

# SLIDE 33: Topic 7 - Theory (Merge)
make_theory_slide(33, "THEORY  \u00b7  TOPIC 7",
    "Merge and Join: Combining DataFrames",
    [
        "pd.merge(df1, df2, on=\"key\") \u2014 inner join",
        "how=\"left\" / \"right\" / \"outer\" \u2014 join types",
        "left_on, right_on \u2014 different column names",
        "df1.join(df2) \u2014 join on index",
        "validate=\"one_to_many\" \u2014 catch errors",
    ],
    "Venn diagrams:\n\nINNER: overlap only\nLEFT: all left + matches\nRIGHT: all right + matches\nOUTER: everything",
    "merge() is pandas' SQL JOIN. Inner join keeps only matching rows, left join keeps all left rows (filling NaN for non-matches), outer join keeps everything. Always specify the join type explicitly \u2014 the default inner join silently drops non-matching rows. Use validate to catch data quality issues.",
    image_path=vis_path("joins.png")
)

# SLIDE 34: Topic 7 - Theory (Concat/Reshape)
make_theory_slide(34, "THEORY  \u00b7  TOPIC 7",
    "Concat, Pivot, and Reshape",
    [
        "pd.concat([df1, df2]) \u2014 stack vertically",
        "pd.concat([df1, df2], axis=1) \u2014 side by side",
        ".pivot_table(values, index, columns, aggfunc)",
        ".melt() \u2014 wide to long format",
        ".stack() / .unstack() \u2014 reshape multi-index",
    ],
    "Concat: stack DataFrames\n\n[Jan] + [Feb] + [Mar]\n= [Q1 combined]\n\nPivot: reshape\nLong \u2194 Wide format\n(like Excel pivot tables)",
    "concat is for combining datasets with the same structure \u2014 monthly reports, data from multiple sources. pivot_table reshapes data from long to wide format (like Excel pivot tables). melt does the reverse. These reshaping operations are critical for preparing data for visualization and ML.",
    image_path=vis_path("concat.png")
)

# SLIDE 35: Topic 7 - Example
make_example_slide(35, "REAL-WORLD EXAMPLE  \u00b7  TOPIC 7",
    "NYC Taxi & Limousine Commission (Uber/Lyft Data)",
    "The NYC TLC publishes 100GB+ of ride data from Uber, Lyft, and yellow taxis in separate Parquet files; researchers merge these to compare service patterns.",
    "Comparing tip rates, ride durations, and pricing between services requires merging trip records with zone lookups, weather data, and license-to-company mappings.",
    "NVIDIA and Coiled demonstrated the same pandas merge/join logic scales to 100GB+ using GPU-accelerated cuDF and distributed Dask \u2014 same API, 1000x faster.",
    "docs.coiled.io/examples/uber-lyft | NVIDIA RAPIDS docs",
    "The merge/join patterns you learn in pandas scale directly to massive datasets \u2014 the API stays the same, only the engine changes.",
    "The NYC taxi dataset is one of the best real-world examples of why merging matters. Trip data has pickup/dropoff zone IDs, but you need to merge with a zone lookup table to get neighborhood names. You merge with a license-to-company mapping to identify Uber vs. Lyft rides."
)

# SLIDE 36: Summary
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
tb = add_textbox(slide, emu(0.8), emu(0.5), emu(5), emu(0.35))
set_text(tb.text_frame, "SUMMARY", HEADING_FONT, Pt(11.5), True, PURPLE_DARK)
tb = add_textbox(slide, emu(0.8), emu(0.85), emu(10), emu(0.6))
set_text(tb.text_frame, "What We Covered Today", HEADING_FONT, Pt(29), True, DARK_TEXT)

summary_items = [
    ("Pandas", "Python\u2019s core data manipulation library", "AQR Capital", PURPLE_DARK),
    ("Series & DataFrame", "1D and 2D labeled data structures", "Two Sigma", PURPLE_DARK),
    ("Loading Data", "read_csv, read_excel, read_json, read_sql", "Netflix", PURPLE_DARK),
    ("Filtering", "loc, iloc, boolean indexing", "Instacart", PURPLE_DARK),
    ("Cleaning", "isna, dropna, fillna, interpolate", "Goldman Sachs", PURPLE_DARK),
    ("Transformation", "groupby, apply, agg, transform", "Spotify", PURPLE_DARK),
    ("Merging", "merge, concat, pivot_table, melt", "NYC TLC / Uber", PURPLE_DARK),
]
for i, (topic, desc, company, color) in enumerate(summary_items):
    y = 1.7 + i * 0.7
    add_shape_bg(slide, emu(0.6), emu(y), emu(11), emu(0.55), PURPLE_CARD_BG if i % 2 == 0 else WHITE, 0.02)
    # topic
    tb = add_textbox(slide, emu(0.8), emu(y + 0.05), emu(2.5), emu(0.4))
    set_text(tb.text_frame, topic, HEADING_FONT, Pt(13), True, DARK_TEXT)
    # desc
    tb = add_textbox(slide, emu(3.3), emu(y + 0.05), emu(5.5), emu(0.4))
    set_text(tb.text_frame, desc, BODY_FONT, Pt(12), False, BODY_GRAY)
    # company
    tb = add_textbox(slide, emu(9.2), emu(y + 0.05), emu(2.5), emu(0.4))
    set_text(tb.text_frame, company, HEADING_FONT, Pt(11), True, PURPLE_DARK, PP_ALIGN.RIGHT)

add_footer(slide, 36)
add_speaker_notes(slide, "Recap the journey: from 'what is pandas' to merging multi-table datasets. Each topic builds on the previous one. The real-world examples show these aren't academic exercises \u2014 every major data-driven company uses these exact operations daily.")

# SLIDE 37: Key Takeaways
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, PURPLE_BG)
add_rect(slide, 0, 0, SLIDE_WIDTH, Emu(80000), PURPLE_DARK)
tb = add_textbox(slide, emu(0.8), emu(0.8), emu(5), emu(0.35))
set_text(tb.text_frame, "KEY TAKEAWAYS", HEADING_FONT, Pt(11.5), True, AMBER)
tb = add_textbox(slide, emu(0.8), emu(1.2), emu(10), emu(0.6))
set_text(tb.text_frame, "Remember These Five Things", HEADING_FONT, Pt(29), True, WHITE)

takeaways = [
    "Pandas is the #1 data manipulation tool in Python",
    "77% of Python data professionals use it (JetBrains 2024)",
    "Master the pattern: Load \u2192 Inspect \u2192 Clean \u2192 Transform \u2192 Merge",
    "Always inspect data after loading (.info(), .describe())",
    "Choose the right missing-data strategy for your context",
]
for i, ta in enumerate(takeaways):
    y = 2.2 + i * 0.9
    add_shape_bg(slide, emu(0.8), emu(y), emu(0.5), emu(0.5), PURPLE_DARK, 0.5)
    tb = add_textbox(slide, emu(0.8), emu(y + 0.05), emu(0.5), emu(0.4))
    set_text(tb.text_frame, str(i + 1), HEADING_FONT, Pt(14), True, WHITE, PP_ALIGN.CENTER)
    tb = add_textbox(slide, emu(1.6), emu(y + 0.05), emu(9.5), emu(0.4))
    set_text(tb.text_frame, ta, BODY_FONT, Pt(16), False, WHITE)

add_footer(slide, 37)
add_speaker_notes(slide, "These five points are what learners should remember even if they forget everything else. The load-inspect-clean-transform-merge pattern applies to every data project.")

# SLIDE 38: Q&A
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
tb = add_textbox(slide, emu(3), emu(1.5), emu(6.5), emu(1.5))
set_text(tb.text_frame, "Questions?", HEADING_FONT, Pt(48), True, DARK_TEXT, PP_ALIGN.CENTER)

add_shape_bg(slide, emu(2.5), emu(3.5), emu(7.5), emu(3.0), PURPLE_CARD_BG, 0.03)
tb = add_textbox(slide, emu(2.8), emu(3.7), emu(7), emu(0.3))
set_text(tb.text_frame, "DISCUSSION PROMPTS", HEADING_FONT, Pt(10), True, PURPLE_DARK, PP_ALIGN.CENTER)

prompts = [
    "What kind of data do you work with daily?",
    "Have you hit Excel\u2019s row limit before?",
    "Which topic would you like to practice first?",
]
tb = add_textbox(slide, emu(3.0), emu(4.2), emu(6.5), emu(2.0))
tf = tb.text_frame
tf.word_wrap = True
for i, prompt in enumerate(prompts):
    if i == 0:
        set_text(tf, "\u25b8  " + prompt, BODY_FONT, Pt(15), False, DARK_TEXT, PP_ALIGN.CENTER)
    else:
        add_para(tf, "\u25b8  " + prompt, BODY_FONT, Pt(15), False, DARK_TEXT, PP_ALIGN.CENTER, Pt(16))
add_footer(slide, 38)
add_speaker_notes(slide, "Open the floor for questions. If no questions, use the prompts to spark discussion. Relate answers back to the topics covered.")

# SLIDE 39: References
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
tb = add_textbox(slide, emu(0.8), emu(0.5), emu(5), emu(0.35))
set_text(tb.text_frame, "REFERENCES", HEADING_FONT, Pt(11.5), True, PURPLE_DARK)
tb = add_textbox(slide, emu(0.8), emu(0.85), emu(10), emu(0.5))
set_text(tb.text_frame, "Sources and Attribution", HEADING_FONT, Pt(29), True, DARK_TEXT)

refs = [
    "Wikipedia \u2014 Pandas (software): en.wikipedia.org/wiki/Pandas_(software)",
    "Wes McKinney: wesmckinney.com/about.html",
    "Two Sigma \u2014 Pandas at a Crossroads: twosigma.com/articles/pandas-at-a-crossroads",
    "Two Sigma \u2014 The Future of Pandas: twosigma.com/articles/the-future-of-pandas",
    "TechRepublic \u2014 How Netflix Uses Python: techrepublic.com/article/how-netflix-uses-python",
    "Instacart Grocery Dataset: instacart.com/datasets/grocery-shopping-2017",
    "eFinancialCareers \u2014 Python Libraries for Finance: efinancialcareers.com/news/python-libraries-for-finance",
    "Spotify Engineering Blog: engineering.atspotify.com",
    "ByteByteGo \u2014 Spotify Data Platform: blog.bytebytego.com",
    "Coiled \u2014 Uber/Lyft ETL: docs.coiled.io/examples/uber-lyft",
    "NVIDIA RAPIDS \u2014 cudf.pandas: docs.nvidia.com/datascience/deployment",
    "JetBrains \u2014 State of Data Science 2024: blog.jetbrains.com/pycharm/2024/12/the-state-of-data-science",
]
tb = add_textbox(slide, emu(0.8), emu(1.5), emu(11), emu(5.0))
tf = tb.text_frame
tf.word_wrap = True
for i, ref in enumerate(refs):
    if i == 0:
        set_text(tf, str(i + 1) + ".  " + ref, BODY_FONT, Pt(10.5), False, BODY_GRAY)
    else:
        add_para(tf, str(i + 1) + ".  " + ref, BODY_FONT, Pt(10.5), False, BODY_GRAY, space_before=Pt(5))
add_footer(slide, 39)
add_speaker_notes(slide, "All sources used for real-world examples in this presentation. Every example was sourced from the internet with verifiable URLs.")

# SLIDE 40: Thank You
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, PURPLE_BG)
add_rect(slide, 0, 0, SLIDE_WIDTH, Emu(80000), PURPLE_DARK)
tb = add_textbox(slide, emu(1.5), emu(2.0), emu(9.5), emu(1.5))
set_text(tb.text_frame, "Thank You!", HEADING_FONT, Pt(54), True, WHITE, PP_ALIGN.CENTER)
tb = add_textbox(slide, emu(1.5), emu(3.8), emu(9.5), emu(0.5))
set_text(tb.text_frame, "Data Manipulation with Python Pandas", HEADING_FONT, Pt(20), True, PURPLE_PALE, PP_ALIGN.CENTER)

add_shape_bg(slide, emu(3.5), emu(4.8), emu(5.5), emu(0.7), RGBColor(0x2D, 0x1A, 0x56), 0.05)
tb = add_textbox(slide, emu(3.7), emu(4.85), emu(5.1), emu(0.6))
set_text(tb.text_frame, "Next Session: Data Visualization with Matplotlib & Seaborn", BODY_FONT, Pt(13), True, AMBER, PP_ALIGN.CENTER)

tb = add_textbox(slide, emu(1.5), emu(5.8), emu(9.5), emu(0.4))
set_text(tb.text_frame, "Part of a 5-Day Python Training Session", BODY_FONT, Pt(12), False, RGBColor(0xC9, 0xB8, 0xEE), PP_ALIGN.CENTER)
add_speaker_notes(slide, "Thank the audience. Remind them the next session covers data visualization with Matplotlib and Seaborn, building directly on the pandas skills learned today.")

# SAVE
output_dir = r"C:\Users\jayasurya.thirumaran\OneDrive - Accenture\Desktop\Learning session 9\Hands-on_1\output"
output_path = os.path.join(output_dir, "data-manipulation-with-python-pandas.pptx")
prs.save(output_path)
print("PPT saved to:", output_path)
print("Total slides:", len(prs.slides))
