# Student Performance Analyzer

A beginner-friendly Python data analysis project that explores student academic performance using Pandas, NumPy, and Matplotlib.

The project works with student data such as study hours, attendance, subject scores, assignments, and sleep hours to find useful patterns and insights.

## What This Project Does

* Loads student data from a CSV file
* Inspects the dataset and checks for data-quality issues
* Finds duplicate records and missing values
* Calculates total and average scores
* Analyzes Math, Science, and English performance
* Finds the top and lowest-performing students
* Analyzes attendance and study hours
* Analyzes assignment completion
* Looks at sleep hours and their relationship with performance
* Compares performance between male and female students
* Groups students into different performance levels
* Identifies students who may need additional attention
* Creates visualizations using Matplotlib
* Generates a simple text report with important findings

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* CSV
* File Handling

## Project Structure

```text
Student_Performance_Analyzer/
│
├── data/
│   └── students.csv
│
├── analyzer.py
│
├── report.txt
│
└── README.md
```

## Analysis

Some of the questions explored in this project include:

* Who are the top-performing students?
* Which subject has the highest average score?
* Which subject has the lowest average score?
* Do students with higher attendance generally perform better?
* Is there a relationship between study hours and scores?
* Does assignment completion appear to be related to performance?
* Is there any visible relationship between sleep and performance?
* How is performance distributed among students?
* Which students may need additional attention?

## Visualizations

The project creates charts such as:

* Average score by subject
* Study hours vs total score
* Attendance vs total score
* Performance level distribution
* Top-performing students
* Sleep hours vs total score

## How to Run

Clone the repository and move into the project directory.

```bash
git clone <repository-url>
cd Student_Performance_Analyzer
```

Install the required libraries:

```bash
pip install pandas numpy matplotlib
```

Then run:

```bash
python analyzer.py
```

## Dataset

The dataset is sample student data created for this project. It is not collected from a real school or real students.

## Purpose

This project was built to practice working with a slightly larger and more detailed dataset and to move beyond basic calculations into finding relationships, patterns, and useful insights from data.

## Possible Improvements

Some things that could be added later:

* More detailed visualizations
* Correlation analysis
* Better report formatting
* More student records
* Interactive dashboards
* Exporting analysis results to Excel
* A simple user interface
* More advanced statistical analysis

## Author

Built by **nkxcodes** as part of my Python and data analysis learning.
