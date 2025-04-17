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

- `all_out.py`: Python script that analyzes the occurrences of all-out teams in both first and second innings.
- `pointstable.py`: Python script that generates the points table for IPL teams based on match results.
- `runs_band.py`: Python script that visualizes the distribution of runs scored by teams in various ranges (e.g., 170–200, 200+).
- `successful_chases.py`: Python script that analyzes successful run chases across different target ranges (170–200 and 200+).
- `toss.py`: Python script that analyzes toss decisions and their impact on match outcomes (Field vs Batting).
- `imagespy/`: Folder containing the generated images (graphs, plots, etc.).


## Requirements

The following Python libraries are required to run the analysis:

- **Pandas**: For data manipulation.
- **Matplotlib** and **Seaborn**: For plotting graphs.
- **NumPy**: For numerical operations.
