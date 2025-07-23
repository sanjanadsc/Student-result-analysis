# Student Result Analysis Using Data Visualization

This project explores the academic performance of school students using data visualization and statistical analysis. The focus is to understand how different demographic and social factors influence students' scores in math, reading, and writing. It leverages Python libraries like pandas, seaborn, and matplotlib to draw meaningful insights from real-world student data.

## Project Overview

Every student’s academic performance is influenced by a combination of factors—some personal, some environmental. This project aims to uncover such insights using data from a group of students. By analyzing attributes such as gender, ethnic group, parental education level, and marital status, we aim to reveal trends that could inform educational interventions and policy planning.

Through grouping and visualization techniques, we examine:
- How parental education impacts academic scores
- The effect (or lack thereof) of parents' marital status
- Score distributions across gender and ethnic groups
- Outlier behavior in test results
- The demographic makeup of the student population

## Dataset Description

The dataset used (`students_data.csv`) consists of 200 student records with the following features:

- Gender: Male or Female
- EthnicGroup: Group A to Group E
- ParentEduc: Parent's highest level of education
- LunchType: Standard or free/reduced lunch
- TestPrep: Completion status of a test preparation course
- ParentMaritalStatus: Marital status of the student's parents
- MathScore: Score in math out of 100
- ReadingScore: Score in reading out of 100
- WritingScore: Score in writing out of 100

An index column (`Unnamed: 0`) was also present but removed during preprocessing.

## Objective

The main goals of this analysis are:

- To understand if and how parental education impacts student performance.
- To determine whether gender or ethnicity affects scores.
- To visualize the distribution of students across demographic factors.
- To identify any outliers in the scoring data.
- To present a clear, data-backed summary that can be used by educators and administrators.

## Tools and Technologies Used

- Python 3
- pandas – data manipulation and analysis
- numpy – numerical operations
- matplotlib – static plotting
- seaborn – statistical data visualization

## Methodology

1. Load and inspect the dataset
2. Clean unnecessary columns
3. Visualize gender distribution using a countplot
4. Group data by parental education and plot a heatmap to see its effect on student performance
5. Analyze whether marital status of parents affects academic scores
6. Use a boxplot to detect outliers in math scores
7. Visualize ethnic group distribution with a pie chart

Each visualization was paired with analysis and a conclusion.

## Key Findings

- Students whose parents have higher education levels tend to perform better across all subjects.
- Parents’ marital status does not significantly influence student performance.
- Female students slightly outnumber male students in the dataset.
- Group C contains the largest number of students based on ethnic distribution.
- Some outliers exist in math scores, suggesting very high or very low performance among certain students.

## Real-World Applications

- Educational institutions can use this analysis to better understand the influence of background variables on student success.
- Educators can provide additional academic support where patterns of low performance are identified.
- Policymakers can use such insights to guide investment in student preparation programs, parental involvement, and awareness initiatives.
- Helps design inclusive curricula and support systems that address diverse student needs.

## Conclusion

This project highlights how data visualization and analysis can provide actionable insights into educational performance. It demonstrates the importance of examining not just what students score—but why. By understanding the broader context of a student’s life, educators and institutions can design more effective interventions and support systems.

## Project Files

- Student result analysis.py – Python script containing the full analysis
- students_data.csv – The dataset used for analysis
- README.md – Project documentation

## Author

Sanjana Singh  
MCA Student | Data Science Enthusiast  
