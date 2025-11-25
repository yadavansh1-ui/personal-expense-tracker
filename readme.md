# 💰 Personal Expense Tracker — Python Project

This is a menu-driven Python application designed to help users manage their daily expenses easily and effectively. It allows for the secure tracking, storage, and summarization of expenses, providing a simple digital solution for personal finance management.

## 📋 Project Summary

Managing day-to-day spending becomes challenging when expenses are remembered manually. This project provides a reliable digital solution where users can record every expense along with:

* *Amount*
* *Category*
* *Note*
* *Date*

All data is saved *permanently* in a expenses.json file, enabling users to track spending anytime without data loss.

---

## ✨ Features

* *Add* a new expense (Amount, Category, Note, Date).
* *View* all saved expenses in a clean, user-friendly table format.
* *Delete* an expense using its unique ID.
* *View* a category-wise spending summary.
* *View* the total money spent.
* Supports multiple date formats.
* Data stored permanently in 'expenses.json'.

## ⚙️ Implementation Approach

The application is built with a focus on modularity and robustness:

* Developed using *modular functions* (addExp, show, removeExp, catSum, tot).
* *JSON file handling* used instead of a database for persistent storage.
* *Input validation* and automatic date formatting for smooth user experience.
* Menu-driven interface for smooth user interaction.
* Persistent storage ensures data remains saved even after restarting the program.

### 📁 Project Files

| File | Description |
| :--- | :--- |
| expense.py | Main program file containing the application logic. |
| expenses.json | Stores all expense records persistently. |
| README.md | Project documentation (this file). |
| statement.md | Project explanation (for academic submission). |

---

## 🚀 How to Run


1. Install Python 3

2. Download all project files

3. Open terminal inside the project folder

4. Run the program using:


```bash
python expense.py
```


---

## 🖥️ Sample Output (When Running)

``` === PERSONAL EXPENSE TRACKER ===
1.Add 2.View 3.Del 4.CatSum 5.Total 6.Exit

--- All Expenses ---
1 | 2025-11-22 | Grocery | 450.0 | Weekly shopping
2 | 2025-11-01 | Rent | 1200.0 | Done for November month
3 | 2025-11-23 | Food | 250.0 | Dinner with friends

--- Total Spent --- 1900.0

--- Sample Category Summary ---
Grocery : 450.0
Rent : 1200.0
Food : 250.0
```


---

## 🎯 Key Learnings

* This project helped me strengthen my understanding of:

* File handling using *JSON*

* Modular & menu-driven program design

* *Real-world problem* solving using Python

* Working with lists, dictionaries & user input


---

👤 Author

Ansh Yadav
Academic Year:2025 – 2026