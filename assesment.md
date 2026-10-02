# Assessment 3 — Mini Project: Expense Tracker

## Objective

Build a simple **command-line Expense Tracker** using Python.

The application must store expenses permanently in:

```text
expenses.json
```

## Features

Your program should provide a menu:

```text
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Monthly Total
6. Category-wise Total
7. Exit
```

### 1. Add Expense

Store:

* Name
* Category
* Date
* Amount

### 2. View Expenses

Display all saved expenses.

### 3. Update Expense

Update an expense using its ID.

The user should be able to update:

* Category
* Date
* Amount

### 4. Delete Expense

Delete an expense using its ID.

### 5. Monthly Total

Ask for a month such as:

```text
2026-10
```

and display the total expenses for that month.

### 6. Category-wise Total

Display the total amount spent for each category.

Example:

```text
Food: ₹1200
Travel: ₹500
Shopping: ₹800
```

## Requirements

Students **must use**:

* Functions
* Modules
* Lists / Dictionaries
* Loops and conditions
* Exception handling
* File handling
* JSON

## Persistence

The program should:

* Load expenses from `expenses.json` when it starts.
* Save expenses to `expenses.json` after adding, updating, or deleting.
* Continue working even if `expenses.json` does not exist.

## Exception Handling

Handle common invalid inputs such as:

* Invalid amount
* Invalid ID
* Expense not found
* Invalid JSON/file errors

The program should **not crash because of normal user mistakes**.

## Suggested Structure

```text
expense_tracker/
│
├── main.py
├── expense.py
├── file_manager.py
└── expenses.json
```

## Submission

Create a GitHub repository:

```text
expense-tracker
```

Push the project to the `main` branch.

**Focus:** Write clean, simple, well-structured Python code rather than putting everything inside `main.py`.
