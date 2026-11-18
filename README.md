# Data Science & AI

**A hands-on learning journey from Python fundamentals to machine learning, deep learning, and applied AI.**

This repository documents my structured approach to developing practical skills in **Python, Data Analytics, Mathematics, Decision Science, Machine Learning, and Deep Learning**.

The focus is on understanding the underlying concepts, implementing them independently, and applying them to real-world analytical and business problems.

---

## Learning Progress

**2 of 7 chapters completed** · Last updated: November 18, 2026

| Chapter | Focus | Status |
|:---|:---|:---|
| 01 | Python Fundamentals | ✅ Completed |
| 02 | Data Toolkit | ✅ Completed |
| 03 | Mathematics & Statistics | ⬜ Planned |
| 04 | Decision Science | ⬜ Planned |
| 05 | Machine Learning | ⬜ Planned |
| 06 | Deep Learning | ⬜ Planned |
| 07 | Applied Projects | ⬜ Planned |

**Current milestone:** Completed the Data Toolkit, including an end-to-end Logistics Performance Analytics project.

**Up next:** Mathematics & Statistics, followed by Decision Science.

[View detailed learning progress](PROGRESS.md)

---

## Featured Projects

### Logistics Performance Analytics

**Python · Pandas · NumPy · Matplotlib · Seaborn**

An end-to-end analytics project using a synthetic logistics shipment dataset to evaluate financial performance, delivery reliability, and customer profitability.

**Key components**

- Data ingestion, cleaning, and quality validation
- Exploratory data analysis
- Financial and operational KPI engineering
- Customer and regional performance analysis
- Data visualization and business storytelling
- Reusable Python analytics functions
- Automated validation and pipeline testing
- Executive KPI reporting

**Validated results**

| Metric | Result |
|:---|---:|
| Cleaned shipments | 11 |
| Financial shipments | 9 |
| Total revenue | €10,250 |
| Total profit | €3,050 |
| Profit margin | 29.76% |
| Delivery delay rate | 36.36% |

*The dataset is synthetic and intended for educational purposes.*

**[Explore the project notebook](02-data-toolkit/10-final-analytics-project/logistics_analytics.ipynb)**

### Bookstore Web Scraping

**Python · Requests · BeautifulSoup · Pandas · Regex**

Built a data collection workflow to extract and validate structured product information from a multi-page demonstration bookstore.

**Highlights**

- Scraped 50 catalogue pages
- Collected 1,000 book records
- Extracted titles, prices, ratings, and availability
- Converted extracted values into structured data
- Performed missing-value and duplicate analysis

**[Explore the web scraping module](02-data-toolkit/07-apis-web-scraping/)**

---

## Learning Roadmap

### 01 — Python Fundamentals

**Completed · 8/8 modules**

Developed a foundation in Python programming, software structure, and reusable code.

| Module | Topic |
|:---|:---|
| 01.01 | Python Basics |
| 01.02 | Control Flow |
| 01.03 | Functions |
| 01.04 | Data Structures |
| 01.05 | Modules |
| 01.06 | Object-Oriented Programming |
| 01.07 | Error Handling |
| 01.08 | Professional Python |

**Core skills:** Python syntax, functions, data structures, OOP, exceptions, debugging, type hints, testing, and Git workflows.

### 02 — Data Toolkit

**Completed · 10/10 modules**

Developed the ability to transform raw data into validated analytical results and actionable business insights.

| Module | Topic |
|:---|:---|
| 02.01 | NumPy |
| 02.02 | Pandas Fundamentals |
| 02.03 | Data Cleaning & Transformation |
| 02.04 | Data Aggregation & Business KPIs |
| 02.05 | Combining Multiple Datasets |
| 02.06 | Data Visualization & Storytelling |
| 02.07 | APIs, Web Scraping & Regex |
| 02.08 | Statistics & Probability |
| 02.09 | Professional Analytics Code |
| 02.10 | Final Analytics Project |

**Core skills:** Data manipulation, statistical analysis, data quality, APIs, visualization, KPI development, reproducible pipelines, and analytical storytelling.

### Upcoming Chapters

| Chapter | Key topics |
|:---|:---|
| **03 — Mathematics & Statistics** | Linear algebra, calculus, probability, statistical inference |
| **04 — Decision Science** | Optimization, linear programming, integer programming, operations research |
| **05 — Machine Learning** | Supervised and unsupervised learning, feature engineering, model evaluation |
| **06 — Deep Learning** | Neural networks, backpropagation, optimization, TensorFlow/Keras |
| **07 — Applied Projects** | End-to-end projects integrating multiple disciplines |

Future chapters will be developed and documented progressively.

---

## Repository Structure

```text
data-science-prep/
│
├── 01-python/
│   └── Python fundamentals and exercises
│
├── 02-data-toolkit/
│   ├── 01-numpy/
│   ├── 02-pandas/
│   ├── 03-data-cleaning/
│   ├── 04-data-aggregation/
│   ├── 05-data-merging/
│   ├── 06-data-visualization/
│   ├── 07-apis-web-scraping/
│   ├── 08-statistics-probability/
│   ├── 09-professional-analytics-code/
│   └── 10-final-analytics-project/
│       └── logistics_analytics.ipynb
│
├── README.md
├── PROGRESS.md
├── requirements.txt
└── .gitignore
```

*The repository grows incrementally. Future chapters are added as the learning path progresses.*

---

## Tech Stack

| Area | Technologies |
|:---|:---|
| Programming | Python |
| Data manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Statistics | SciPy, statistical methods |
| Data collection | Requests, BeautifulSoup, Regex |
| Development | VS Code, Jupyter Notebook |
| Version control | Git, GitHub |

Additional technologies will be introduced as the curriculum progresses.

---

## Getting Started

Clone the repository:

```bash
git clone <repository-url>
cd data-science-prep
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Open the repository in VS Code:

```bash
code .
```

Select the project's Python environment as the Jupyter kernel and open any notebook to explore the exercises.

---

## Learning Philosophy

My learning approach prioritizes **active implementation over passive consumption**.

Each topic follows a consistent cycle:

**Understand → Implement → Experiment → Debug → Explain → Refactor → Revisit**

The goal is not to memorize syntax or reproduce solutions, but to develop the ability to:

- Explain the underlying concepts
- Implement solutions independently
- Interpret analytical results
- Debug and improve existing code
- Apply methods to unfamiliar problems
- Build reliable, reusable workflows

Progress is measured through completed exercises, working implementations, and practical projects.

---

## Documentation

- **[Learning Progress](PROGRESS.md)** — Completed modules, milestones, and upcoming topics
- **[Python Fundamentals](01-python/)** — Programming foundations and exercises
- **[Data Toolkit](02-data-toolkit/)** — Analytics notebooks and practical applications
- **[Final Analytics Project](02-data-toolkit/10-final-analytics-project/logistics_analytics.ipynb)** — End-to-end logistics analysis

---

*Building practical Data Science & AI capabilities, one concept and one project at a time.*