# Expense Tracker

A simple command-line expense tracker written in Python. It's my final project for the [Codédex](https://www.codedex.io) Python course.

## Features

- Add an expense with an amount, a category and a description
- View all expenses
- Filter expenses by category
- Delete an expense by its ID

## Requirements

- Python 3 (no external libraries needed)

## How to run

```bash
git clone https://github.com/artemkhtml/Final-Project-Expense-tracker-.git
cd Final-Project-Expense-tracker-
python tracker.py
```

## Example

```
=== Expense Tracker ===
1. Add expense
2. Show all expenses
3. Show expenses by category
4. Delete expense
5. Exit
Choose an action (1-5): 2
ID: 1, Amount: 450.0, Category: food, Description: lunch
ID: 2, Amount: 60.0, Category: transport, Description: subway
```

## Notes

Expenses are stored in memory only, so they are cleared when the program exits. Saving to a JSON file is planned as the next step.
