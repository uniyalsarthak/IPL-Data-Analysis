# IPL Data Analysis

This repository contains an analysis of **IPL 2024** cricket data, focusing on various aspects of match performance. The analysis includes visualizations for the following:

- **Points Table** (Based on Wins, Losses, and Points)
- **Successful Run Chases** (Targets 170–200 and 200+)
- **All-Out Occurrences** in First and Second Innings
- **Distribution of First Innings Scores**
- **Toss Comparison** (Field vs Batting Decision)

## Project Overview

The goal of this project is to provide insights into IPL 2024 match statistics through visual analysis. This includes understanding trends in team performance, run chases, and analyzing match conditions such as the first innings score and toss decisions.

## Visualizations

The project generates the following visualizations:

1. **Points Table**:
   - A bar plot representing the points, wins, and losses for each team based on match results.

2. **Successful Run Chases**:
   - A histogram showing the successful run chases across different target ranges: 170–200 and 200+.

3. **All-Out Occurrences**:
   - A bar plot comparing the number of **all-out** occurrences in both first and second innings.

4. **First Innings Score Distribution**:
   - A histogram displaying the distribution of first innings scores across all matches.

5. **Toss Decision Comparison**:
   - A bar plot comparing how often teams chose to bat or field first and the corresponding win rates.

## Files in the Repository

- `ipl_data_analysis.py`: The Python script containing the code for data cleaning, analysis, and generation of visualizations.
- `ipl2024.csv`: The dataset containing the IPL 2024 match data.
- `graphs/`: Folder containing the generated graphs (histograms, bar plots, etc.).
- `README.md`: This file with an overview of the project.

## Requirements

The following Python libraries are required to run the analysis:

- **Pandas**: For data manipulation.
- **Matplotlib** and **Seaborn**: For plotting graphs.
- **NumPy**: For numerical operations.
