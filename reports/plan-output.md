# PPT Plan: Data Manipulation with Python Pandas

**Audience:** Python developers and aspiring data analysts (part of a 5-day Python training)
**Level:** Intermediate
**Total Slides:** 40
**Topics:** 7

---

## Slide 1: Title
- **Layout:** Title slide
- **Content:** "Data Manipulation with Python Pandas" | Subtitle: "Intermediate Level — 5-Day Python Training" | Author/Organization placeholder
- **Visual:** Clean title with Pandas logo icon and a subtle data-grid background

---

## Slide 2: Agenda
- **Layout:** Agenda / Table of Contents
- **Content:**
  1. Introduction to Pandas — What and Why
  2. Pandas Data Structures — Series and DataFrame
  3. Loading and Inspecting Data
  4. Data Selection and Filtering
  5. Data Cleaning and Handling Missing Values
  6. Data Transformation
  7. Merging, Joining, and Reshaping Data
- **Visual:** Numbered list with small icons per topic (magnifying glass, table, filter, broom, gears, link)

---

## Slide 3: Topic 1 — Use Case
- **Layout:** Visual + text
- **Content:**
  - "You have 10,000 rows of sales data in a CSV"
  - "Your manager wants a summary by region — by tomorrow"
  - "Excel crashes. SQL feels overkill. What do you use?"
- **Visual:** Illustration of an overloaded Excel spreadsheet with a "Not Responding" dialog
- **Speaker Notes:** Frame the problem: raw data is everywhere — CSVs, databases, APIs. Analysts need a tool that sits between Excel (too limited) and SQL (too rigid for exploration). Pandas fills that gap. It was literally created for this — Wes McKinney built it at a hedge fund because existing tools couldn't keep up with financial data analysis.

## Slide 4: Topic 1 — Theory
- **Layout:** Bullet + diagram
- **Content:**
  - Pandas: Python library for data manipulation
  - Built on top of NumPy arrays
  - Handles tabular data (rows and columns)
  - Read, clean, transform, analyze — all in one
  - `import pandas as pd` — the universal convention
- **Visual:** Simple diagram: Raw Data → Pandas → Clean Insights
- **Speaker Notes:** Pandas provides two core data structures (Series and DataFrame — covered next). It integrates with the entire Python data ecosystem: NumPy for computation, Matplotlib/Seaborn for visualization, scikit-learn for ML. Created by Wes McKinney in 2008, open-sourced in 2009. The name comes from "panel data," an econometrics term.

## Slide 5: Topic 1 — Real-World Example
- **Layout:** Case study card
- **Content:**
  - **Organization:** AQR Capital Management
  - **What:** Wes McKinney, a quantitative analyst at AQR, built pandas in 2008 because existing tools couldn't handle the firm's financial data analysis needs efficiently
  - **Why:** The quant research team needed a high-performance, flexible tool for analyzing trading strategies across global macro and credit markets
  - **Outcome:** Pandas was open-sourced in 2009 and is now used by 77% of Python data professionals (JetBrains/PSF Developer Survey 2024)
- **Source:** [Wikipedia — Pandas](https://en.wikipedia.org/wiki/Pandas_(software)) | [Wes McKinney — About](https://wesmckinney.com/about.html)
- **Key Takeaway:** Pandas was born from a real business need in finance — it wasn't an academic project, it was built to solve daily data problems.
- **Speaker Notes:** McKinney worked at AQR from 2007-2010 on the front office quant research team. He convinced management to open-source the library before leaving. Chang She, another AQR employee, became the second major contributor in 2012. This origin story shows that pandas was designed for real-world, messy, time-series financial data — not just clean textbook datasets.

---

## Slide 6: Transition
- **Layout:** Section divider
- **Content:** "Now that you know WHY pandas exists, let's learn its building blocks"
- **Visual:** Arrow icon pointing forward

---

## Slide 7: Topic 2 — Use Case
- **Layout:** Visual + text
- **Content:**
  - "You receive a list of 500 product prices — that's a Series"
  - "You receive a full product catalog with names, prices, stock — that's a DataFrame"
  - "Knowing which to use is the first step"
- **Visual:** Side-by-side: a single column (Series) vs. a multi-column table (DataFrame)
- **Speaker Notes:** Before you can manipulate data, you need to understand how pandas stores it. Think of Series as a single column in a spreadsheet and DataFrame as the entire spreadsheet. Every pandas operation returns one of these two structures.

## Slide 8: Topic 2 — Theory (Series)
- **Layout:** Bullet + code snippet
- **Content:**
  - Series: 1D labeled array
  - Holds any data type (int, float, string)
  - Has an index (labels for each value)
  - Created from lists, dicts, or NumPy arrays
  - `pd.Series([10, 20, 30], name="prices")`
- **Visual:** Diagram showing index-value pairs in a vertical strip
- **Speaker Notes:** A Series is like a Python dictionary with superpowers — it has an index (like keys) and values, but supports vectorized operations. You can do math on an entire Series at once without loops. The index doesn't have to be integers — it can be dates, names, or any hashable type.

## Slide 9: Topic 2 — Theory (DataFrame)
- **Layout:** Bullet + code snippet
- **Content:**
  - DataFrame: 2D labeled table
  - Collection of Series sharing an index
  - Rows = observations, Columns = variables
  - Most common pandas object you'll use
  - `pd.DataFrame({"name": [...], "price": [...]})`
- **Visual:** Table diagram with labeled rows (index) and columns (Series)
- **Speaker Notes:** A DataFrame is essentially a dictionary of Series objects that share the same index. Each column is a Series. You can select a single column and get a Series back. DataFrames support SQL-like operations (select, filter, group, join) but with Python's flexibility. Most data you load from files becomes a DataFrame automatically.

## Slide 10: Topic 2 — Real-World Example
- **Layout:** Case study card
- **Content:**
  - **Organization:** Two Sigma Investments
  - **What:** Two Sigma built an internal data stack called "Bamboo" with pandas DataFrames at its core for quantitative research
  - **Why:** Their research teams need to manipulate financial time-series data rapidly; DataFrames provide the natural tabular structure for this
  - **Outcome:** Jeff Reback, a Two Sigma Managing Director, became one of pandas' most prolific open-source contributors, and Two Sigma actively sponsors pandas development
- **Source:** [Two Sigma — Pandas at a Crossroads](https://www.twosigma.com/articles/pandas-at-a-crossroads-the-past-present-and-future-with-jeff-reback) | [Two Sigma — The Future of Pandas](https://www.twosigma.com/articles/the-future-of-pandas)
- **Key Takeaway:** The DataFrame is so central to data work that one of the world's largest hedge funds built its entire research infrastructure around it.
- **Speaker Notes:** Two Sigma manages over $60 billion and runs thousands of quantitative models. Their "Bamboo" stack uses pandas for datasets that fit in memory and translates to Apache Spark via Ibis for larger datasets. The fact that a Two Sigma MD contributes to pandas core shows how critical the DataFrame abstraction is to real finance workflows.

---

## Slide 11: Transition
- **Layout:** Section divider
- **Content:** "You know the structures — now let's load real data into them"
- **Visual:** File icons (CSV, Excel, JSON) with an arrow into a DataFrame

---

## Slide 12: Topic 3 — Use Case
- **Layout:** Visual + text
- **Content:**
  - "Your data lives in CSVs, Excel sheets, databases, APIs"
  - "Step one of every analysis: get it into pandas"
  - "Pandas reads 20+ file formats out of the box"
- **Visual:** Icons for CSV, Excel, JSON, SQL converging into a single DataFrame
- **Speaker Notes:** No analysis starts without loading data. In practice, you'll encounter messy CSVs with encoding issues, Excel files with multiple sheets, JSON from APIs, and SQL databases. Pandas has a `read_*` function for each. The most common is `read_csv()`, which handles 90% of use cases.

## Slide 13: Topic 3 — Theory (Loading)
- **Layout:** Bullet + code snippets
- **Content:**
  - `pd.read_csv("sales.csv")` — most common
  - `pd.read_excel("report.xlsx", sheet_name="Q1")`
  - `pd.read_json("api_response.json")`
  - `pd.read_sql("SELECT * FROM users", conn)`
  - Key params: `sep`, `encoding`, `na_values`, `parse_dates`
- **Visual:** Code snippets with arrow to resulting DataFrame preview
- **Speaker Notes:** `read_csv` is the workhorse — it handles delimiters, headers, data types, missing value markers, date parsing, and more. Common gotchas: wrong encoding (use `encoding='utf-8'` or `'latin1'`), dates read as strings (use `parse_dates=['date_col']`), and custom missing values (use `na_values=['N/A', 'missing']`). For large files, use `chunksize` to read in batches.

## Slide 14: Topic 3 — Theory (Inspecting)
- **Layout:** Bullet + code snippets
- **Content:**
  - `.head()` / `.tail()` — first/last 5 rows
  - `.shape` — (rows, columns) count
  - `.dtypes` — data type of each column
  - `.describe()` — summary statistics
  - `.info()` — memory usage and non-null counts
- **Visual:** Screenshot-style output of `.info()` on a sample DataFrame
- **Speaker Notes:** Always inspect after loading. `.info()` is your best friend — it shows column names, non-null counts (reveals missing data), data types, and memory usage in one call. `.describe()` gives mean, std, min, max, quartiles for numeric columns. If dtypes look wrong (e.g., numbers read as strings), you caught it early.

## Slide 15: Topic 3 — Real-World Example
- **Layout:** Case study card
- **Content:**
  - **Organization:** Netflix
  - **What:** Netflix's engineering teams use pandas alongside NumPy, SciPy, and other scientific Python libraries for data analysis across their content and streaming operations
  - **Why:** Their CORE team analyzes large volumes of signals after operational alerts, requiring fast data loading and inspection from multiple sources
  - **Outcome:** Python and pandas are embedded across Netflix's full content lifecycle — from content analytics to A/B testing to real-time monitoring
- **Source:** [TechRepublic — How Netflix Uses Python](https://www.techrepublic.com/article/how-netflix-uses-python-streaming-giant-reveals-its-programming-language-libraries-and-frameworks/)
- **Key Takeaway:** Even companies processing billions of events daily rely on pandas for exploratory analysis and signal inspection.
- **Speaker Notes:** Netflix has publicly documented their Python stack. Their teams use Jupyter notebooks with pandas for interactive data exploration before building production pipelines. The key insight: pandas isn't just for small datasets — it's the starting point for understanding data before scaling up. Netflix engineers load samples, inspect patterns, then build production systems based on what they find.

---

## Slide 16: Transition
- **Layout:** Section divider
- **Content:** "Data is loaded — now let's slice and dice it"
- **Visual:** Scissors icon cutting through a data table

---

## Slide 17: Topic 4 — Use Case
- **Layout:** Visual + text
- **Content:**
  - "You have 1 million transactions but only need Q4 sales"
  - "Or only orders above $500 from California"
  - "Filtering is how you ask questions of your data"
- **Visual:** Large table with a highlighted subset (filtered rows glowing)
- **Speaker Notes:** Filtering and selection are the most frequent operations in data analysis. You rarely analyze an entire dataset — you zoom into subsets. "Show me all customers who churned last month," "Find transactions over $10K," "Get revenue by product for the West region." All of these are filtering operations.

## Slide 18: Topic 4 — Theory (loc/iloc)
- **Layout:** Bullet + code snippets
- **Content:**
  - `.loc[]` — select by label (row/column names)
  - `.iloc[]` — select by integer position
  - `df.loc[0:5, "name":"price"]` — label range
  - `df.iloc[0:5, 0:3]` — position range
  - Both support single values, slices, and lists
- **Visual:** Grid diagram showing loc (label-based) vs iloc (position-based) access
- **Speaker Notes:** The #1 confusion in pandas: loc vs iloc. Simple rule — loc uses labels (what you see), iloc uses positions (0-based integers). loc includes the endpoint in slices, iloc doesn't (like Python lists). When the index is integers, this gets confusing — that's why being explicit with loc/iloc is better than using `df[0:5]`.

## Slide 19: Topic 4 — Theory (Boolean Indexing)
- **Layout:** Bullet + code snippets
- **Content:**
  - `df[df["price"] > 100]` — filter by condition
  - `df[df["city"] == "Mumbai"]` — exact match
  - Combine: `&` (and), `|` (or), `~` (not)
  - `.isin(["A", "B"])` — match multiple values
  - `.query("price > 100 and city == 'Mumbai'")`
- **Visual:** Flowchart: Condition → Boolean mask (True/False) → Filtered rows
- **Speaker Notes:** Boolean indexing is the pandas equivalent of SQL's WHERE clause. The expression `df["price"] > 100` returns a Series of True/False values — a "mask." Passing that mask into `df[...]` returns only the True rows. Always wrap multiple conditions in parentheses: `df[(df["a"] > 5) & (df["b"] < 10)]`. The `.query()` method is more readable for complex filters.

## Slide 20: Topic 4 — Real-World Example
- **Layout:** Case study card
- **Content:**
  - **Organization:** Instacart
  - **What:** Instacart released a dataset of 3.4 million grocery orders from 200,000 users; analysts worldwide use pandas boolean indexing and filtering to uncover shopping patterns
  - **Why:** Understanding which products are reordered, at what time, and in what combinations drives Instacart's recommendation engine and inventory planning
  - **Outcome:** Analysis revealed that bananas are the #1 reordered item (557,763 reorders), and filtering by time-of-day and department exposed distinct shopping behaviors
- **Source:** [Instacart Market Basket Analysis](https://www.instacart.com/datasets/grocery-shopping-2017) | [Kaggle Competition](https://www.kaggle.com/c/instacart-market-basket-analysis)
- **Key Takeaway:** Filtering 3.4M rows to answer "which products get reordered on weekends?" is exactly what boolean indexing was built for.
- **Speaker Notes:** The Instacart dataset is one of the most popular real-world datasets for learning pandas filtering. Analysts filter by department, hour of day, days since prior order, and reorder status. A common exercise: filter to only organic products reordered on weekends — this requires chaining multiple boolean conditions. The dataset is freely available on Kaggle and Instacart's website.

---

## Slide 21: Transition
- **Layout:** Section divider
- **Content:** "Real data is messy — let's learn to clean it"
- **Visual:** Broom icon sweeping away "NaN" and "null" labels

---

## Slide 22: Topic 5 — Use Case
- **Layout:** Visual + text
- **Content:**
  - "Your dataset has 15% missing values"
  - "Some rows have 'N/A', others have blank cells"
  - "Drop them? Fill them? It depends on the context"
- **Visual:** Table with scattered empty cells highlighted in red
- **Speaker Notes:** Missing data is the most common real-world data problem. Surveys have unanswered questions, sensors fail, APIs return partial records, users skip optional fields. How you handle missing values can change your analysis results dramatically. Dropping too aggressively loses information; filling incorrectly introduces bias.

## Slide 23: Topic 5 — Theory (Detection)
- **Layout:** Bullet + code snippets
- **Content:**
  - `df.isna()` — detect missing values (True/False)
  - `df.isna().sum()` — count missing per column
  - `df.isna().mean()` — percentage missing per column
  - Non-standard markers: `na_values` param in `read_csv`
  - Visualize: `df.isna().sum().plot(kind="bar")`
- **Visual:** Bar chart showing missing value counts per column
- **Speaker Notes:** Always start by measuring the problem. `isna().sum()` gives you the count, `isna().mean()` gives the percentage. Rule of thumb: if a column is >50% missing, consider dropping it entirely. If a row is mostly missing, drop the row. For scattered missing values in important columns, filling is usually better. Non-standard markers like "N/A", "missing", "-" won't be detected automatically — specify them when loading.

## Slide 24: Topic 5 — Theory (Handling)
- **Layout:** Bullet + code snippets
- **Content:**
  - `df.dropna()` — remove rows with any missing
  - `df.dropna(thresh=3)` — keep rows with 3+ valid values
  - `df.fillna(0)` — fill with a constant
  - `df.fillna(df.mean())` — fill with column mean
  - `df.interpolate()` — estimate from neighbors
- **Visual:** Before/after table showing NaN cells filled with values
- **Speaker Notes:** `dropna()` is the simplest but most aggressive approach — it removes entire rows. Use `thresh` to be more selective. `fillna()` with mean/median is common for numeric data, mode for categorical. For time-series data, `interpolate()` or `fillna(method='ffill')` (forward fill) preserves trends. The choice depends on context: dropping is fine for analysis, but filling is usually necessary before feeding data into ML models.

## Slide 25: Topic 5 — Real-World Example
- **Layout:** Case study card
- **Content:**
  - **Organization:** Goldman Sachs (GS Quant)
  - **What:** Goldman Sachs built and open-sourced GS Quant, a Python toolkit for quantitative finance that uses pandas for data manipulation including handling missing market data
  - **Why:** Financial time-series data frequently has gaps — markets close on holidays, instruments halt trading, data feeds drop — and these gaps must be handled correctly for accurate risk modeling
  - **Outcome:** GS Quant provides built-in functions for filling missing financial data, built on top of pandas' fillna and interpolation capabilities
- **Source:** [eFinancialCareers — Python Libraries for Finance](https://www.efinancialcareers.com/news/python-libraries-for-finance)
- **Key Takeaway:** Even the world's largest investment bank relies on pandas' missing data tools — the stakes of getting fill strategies wrong are measured in millions.
- **Speaker Notes:** In finance, missing data isn't just an inconvenience — it can break risk models. A missing price for a stock on a holiday needs forward-filling (use last known price), not zero-filling (which would imply the stock is worthless). Goldman Sachs built GS Quant to standardize these decisions. The library wraps pandas operations with finance-specific logic for data cleaning.

---

## Slide 26: Transition
- **Layout:** Section divider
- **Content:** "Clean data in hand — time to transform and aggregate"
- **Visual:** Gears icon turning raw data into summarized insights

---

## Slide 27: Topic 6 — Use Case
- **Layout:** Visual + text
- **Content:**
  - "You have 100K rows of individual transactions"
  - "Boss asks: 'What's total revenue per region per month?'"
  - "That's a groupby-aggregate operation"
- **Visual:** Raw transaction rows funneling into a summary table grouped by region
- **Speaker Notes:** Transformation is where analysis actually happens. Loading and cleaning are prep work — groupby and aggregation are where you extract meaning. "Total sales by store," "average salary by department," "count of orders by customer" — these are all split-apply-combine operations that pandas handles with groupby.

## Slide 28: Topic 6 — Theory (groupby)
- **Layout:** Bullet + code snippets
- **Content:**
  - `df.groupby("region")["sales"].sum()` — basic groupby
  - Split → Apply → Combine pattern
  - Multiple columns: `groupby(["region", "month"])`
  - Multiple aggregations: `.agg(["sum", "mean", "count"])`
  - Named aggs: `.agg(total=("sales", "sum"))`
- **Visual:** Three-step diagram: Split (groups) → Apply (function) → Combine (result)
- **Speaker Notes:** The split-apply-combine pattern is the foundation of data aggregation. `groupby` splits the DataFrame into groups based on column values, applies a function (sum, mean, count, custom), and combines results into a new DataFrame. You can group by multiple columns for nested summaries. The `.agg()` method lets you apply different functions to different columns in one call.

## Slide 29: Topic 6 — Theory (apply/map/transform)
- **Layout:** Bullet + code snippets
- **Content:**
  - `.apply(func)` — apply any function row/column-wise
  - `.map(dict)` — map values using a dictionary
  - `.transform()` — return same-size output
  - Method chaining: `df.assign(...).query(...).groupby(...)`
  - Lambda functions: `.apply(lambda x: x.upper())`
- **Visual:** Flow diagram showing apply on each row vs. transform on each group
- **Speaker Notes:** `apply` is the Swiss army knife — it can apply any function to rows or columns. It's flexible but slower than built-in methods. Prefer vectorized operations when possible (e.g., `df["col"] * 2` instead of `df["col"].apply(lambda x: x*2)`). `transform` is special — it returns a result with the same index as the input, making it perfect for "group-level calculations assigned back to each row" (e.g., each row's percentage of its group total).

## Slide 30: Topic 6 — Real-World Example
- **Layout:** Case study card
- **Content:**
  - **Organization:** Spotify (Data Platform)
  - **What:** Spotify operates 20,000+ batch data pipelines across 300+ teams; data scientists use pandas groupby and aggregation in Jupyter notebooks for exploratory analysis of listening patterns, playlist performance, and user behavior
  - **Why:** Before building production pipelines, Spotify's analysts prototype aggregations in pandas — grouping streams by artist, region, and time period to identify trends
  - **Outcome:** Insights from pandas-based exploration inform Spotify's recommendation algorithms and business decisions for 600M+ users
- **Source:** [Spotify Engineering — Data Platform](https://engineering.atspotify.com/category/infrastructure) | [ByteByteGo — How Spotify Built Its Data Platform](https://blog.bytebytego.com/p/how-spotify-built-its-data-platform)
- **Key Takeaway:** Groupby-aggregate is the first analysis step even at massive scale — Spotify analysts prototype in pandas before building production pipelines.
- **Speaker Notes:** Spotify's data platform processes petabytes of data, but the analysis journey often starts in a Jupyter notebook with pandas. An analyst might group stream data by country and genre to spot emerging trends, then hand that logic off to a Spark pipeline for production. This prototype-then-scale pattern is common across tech companies. The groupby in a notebook becomes the GROUP BY in a production SQL query.

---

## Slide 31: Transition
- **Layout:** Section divider
- **Content:** "Single datasets are useful — combining them is powerful"
- **Visual:** Two table icons merging into one with a link/chain icon

---

## Slide 32: Topic 7 — Use Case
- **Layout:** Visual + text
- **Content:**
  - "Orders in one table, customers in another, products in a third"
  - "You need a unified view joining all three"
  - "This is relational data — pandas handles it like SQL"
- **Visual:** Three separate tables with connecting lines (foreign keys) merging into one
- **Speaker Notes:** Real-world data rarely lives in a single table. CRM data has customers, orders, and products in separate tables. HR data has employees, departments, and salaries. Analytics data comes from multiple APIs. Merging these into a single DataFrame for analysis is one of the most important pandas skills — it's the equivalent of SQL JOINs.

## Slide 33: Topic 7 — Theory (Merge/Join)
- **Layout:** Bullet + code snippets
- **Content:**
  - `pd.merge(df1, df2, on="key")` — inner join (default)
  - `how="left"` / `"right"` / `"outer"` — join types
  - `left_on`, `right_on` — different column names
  - `df1.join(df2)` — join on index
  - Validate: `validate="one_to_many"` catches errors
- **Visual:** Venn diagrams for inner, left, right, outer joins
- **Speaker Notes:** `merge()` is pandas' SQL JOIN. Inner join keeps only matching rows, left join keeps all left rows (filling NaN for non-matches), outer join keeps everything. Always specify the join type explicitly — the default inner join silently drops non-matching rows, which can lose data unexpectedly. Use `validate` to catch data quality issues (e.g., duplicate keys creating a Cartesian product).

## Slide 34: Topic 7 — Theory (Concat/Reshape)
- **Layout:** Bullet + code snippets
- **Content:**
  - `pd.concat([df1, df2])` — stack vertically
  - `pd.concat([df1, df2], axis=1)` — stack horizontally
  - `.pivot_table(values, index, columns, aggfunc)`
  - `.melt()` — wide to long format
  - `.stack()` / `.unstack()` — reshape multi-index
- **Visual:** Diagrams showing concat (stacking) and pivot (reshaping wide↔long)
- **Speaker Notes:** `concat` is for combining datasets with the same structure — monthly reports, data from multiple sources, etc. `pivot_table` reshapes data from long to wide format (like Excel pivot tables). `melt` does the reverse — wide to long. These reshaping operations are critical for preparing data for visualization (most plotting libraries expect long format) and for ML (most models expect wide format).

## Slide 35: Topic 7 — Real-World Example
- **Layout:** Case study card
- **Content:**
  - **Organization:** NYC Taxi & Limousine Commission (Uber/Lyft analysis)
  - **What:** The NYC TLC publishes 100GB+ of ride data from Uber, Lyft, and yellow taxis in separate Parquet files; researchers merge these datasets using pandas-compatible tools to compare service patterns
  - **Why:** Comparing tip rates, ride durations, and pricing between Uber, Lyft, and traditional taxis requires merging trip records with zone lookups, weather data, and license-to-company mappings
  - **Outcome:** NVIDIA and Coiled demonstrated that the same pandas merge/join logic scales to 100GB+ datasets using GPU-accelerated cuDF and distributed Dask — same API, 1000x faster
- **Source:** [Coiled — Cloud Parquet ETL with Dask](https://docs.coiled.io/examples/uber-lyft.html) | [NVIDIA RAPIDS — cudf.pandas](https://docs.nvidia.com/datascience/deployment/stable/examples/rapids-coiled-cudf/notebook/)
- **Key Takeaway:** The merge/join patterns you learn in pandas scale directly to massive datasets — the API stays the same, only the engine changes.
- **Speaker Notes:** The NYC taxi dataset is one of the best real-world examples of why merging matters. Trip data has pickup/dropoff zone IDs, but you need to merge with a zone lookup table to get neighborhood names. You merge with a license-to-company mapping to identify Uber vs. Lyft rides. And you can merge with weather data to analyze how rain affects ride demand. This multi-table join pattern is exactly what production analytics looks like.

---

## Slide 36: Summary / Recap
- **Layout:** Summary slide
- **Content:**
  - **Pandas** — Python's core library for data manipulation (born at AQR Capital)
  - **Series & DataFrame** — 1D and 2D data structures (used at Two Sigma's core)
  - **Loading** — `read_csv`, `read_excel`, `read_json`, `read_sql` (Netflix's starting point)
  - **Filtering** — `loc`, `iloc`, boolean indexing (Instacart's 3.4M orders analyzed)
  - **Cleaning** — `isna`, `dropna`, `fillna` (Goldman Sachs' GS Quant foundation)
  - **Transformation** — `groupby`, `apply`, `agg` (Spotify's analyst workflow)
  - **Merging** — `merge`, `concat`, `pivot_table` (NYC 100GB+ taxi data joins)
- **Visual:** One-line-per-topic recap with company logos or icons
- **Speaker Notes:** Recap the journey: we went from "what is pandas" to merging multi-table datasets. Each topic builds on the previous one. The real-world examples show that these aren't academic exercises — every major data-driven company uses these exact operations daily. In the next sessions of this training, these pandas skills become the foundation for visualization and machine learning.

## Slide 37: Key Takeaways
- **Layout:** Highlight slide
- **Content:**
  - Pandas is the #1 data manipulation tool in Python
  - 77% of Python data professionals use it (JetBrains 2024)
  - Master the pattern: Load → Inspect → Clean → Transform → Merge
  - Always inspect data after loading (`.info()`, `.describe()`)
  - Choose the right missing-data strategy for your context
- **Visual:** Five key points with checkmark icons
- **Speaker Notes:** These five points are what learners should remember even if they forget everything else. The load-inspect-clean-transform-merge pattern applies to every data project. And always, always inspect your data after loading — most bugs in analysis come from assumptions about data that turned out to be wrong.

## Slide 38: Q&A
- **Layout:** Q&A slide
- **Content:** "Questions?"
- **Discussion prompts:**
  - What kind of data do you work with daily?
  - Have you hit Excel's row limit before?
  - Which topic would you like to practice first?
- **Visual:** Question mark icon with chat bubble design
- **Speaker Notes:** Open the floor. If no questions, use the prompts to spark discussion. Relate answers back to the topics covered. If someone mentions a specific use case, show how pandas would handle it.

## Slide 39: References
- **Layout:** References list
- **Content:**
  - [Wikipedia — Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))
  - [Wes McKinney — About](https://wesmckinney.com/about.html)
  - [Two Sigma — Pandas at a Crossroads](https://www.twosigma.com/articles/pandas-at-a-crossroads-the-past-present-and-future-with-jeff-reback)
  - [Two Sigma — The Future of Pandas](https://www.twosigma.com/articles/the-future-of-pandas)
  - [TechRepublic — How Netflix Uses Python](https://www.techrepublic.com/article/how-netflix-uses-python-streaming-giant-reveals-its-programming-language-libraries-and-frameworks/)
  - [Instacart Grocery Dataset 2017](https://www.instacart.com/datasets/grocery-shopping-2017)
  - [eFinancialCareers — Python Libraries for Finance](https://www.efinancialcareers.com/news/python-libraries-for-finance)
  - [Spotify Engineering Blog](https://engineering.atspotify.com/category/infrastructure)
  - [ByteByteGo — Spotify Data Platform](https://blog.bytebytego.com/p/how-spotify-built-its-data-platform)
  - [Coiled — Uber/Lyft Cloud ETL](https://docs.coiled.io/examples/uber-lyft.html)
  - [NVIDIA RAPIDS — cudf.pandas](https://docs.nvidia.com/datascience/deployment/stable/examples/rapids-coiled-cudf/notebook/)
  - [JetBrains — State of Data Science 2024](https://blog.jetbrains.com/pycharm/2024/12/the-state-of-data-science/)
- **Visual:** Clean numbered list

## Slide 40: Thank You
- **Layout:** Closing slide
- **Content:** "Thank You" | Contact info placeholder | "Next session: Data Visualization with Matplotlib & Seaborn"
- **Visual:** Clean closing design matching title slide style
