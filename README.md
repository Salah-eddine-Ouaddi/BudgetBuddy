# 💰 BudgetBuddy

> A simple and efficient **CLI (console)** application to track your **incomes**, **expenses**, and **Budget/Balance** directly from the terminal.

BudgetBuddy is designed as a **serious first Python project**, ideal for **beginners** wishing to practice file manipulation and code structuring best practices.

---

## ✨ Features

* ➕ Add **incomes**
* ➖ Add **expenses**
* 📝 Enter details for each transaction :

  * Amount
  * Category
  * Date
  * Name / description
* 💾 **Auto-save** data to a CSV file
* 📂 **Auto-load** existing data at startup
* 📊 Real-time calculation of Total Balance
* 🖥️ Simple and clear Command Line Interface (CLI)

---

### 1️⃣ Requirement

* Python **3.1** (or above) installed on your machine

---

## 🗂️ CSV File Structure

Data is stored in an file `income/expense.csv` with the following structure:

| Column        | Description                           |
| ------------- | ------------------------------------  |
| `type`        | `income` or `expense`                 |
| `amount`      | Transaction amount                    | 
| `category`    | Category  (ex: Food, Rent, Salary)    |
| `date`        | Date format `YYYY-MM-DD : HH-MM-SS`   |
| `description` | Name or description of transaction    |

---

## 🛠️ Technologies Used

* **Python 3**
* Standard libraries:

  * `csv` → lecture et écriture des données
  * `datetime` → gestion des dates
  * `os` → gestion des fichiers

---

## 👥 Collaborators

* **[Ouaddi Salah eddine]** (@Salah-eddine-Ouaddi)
* **[Hamdane Salahdine]** (@salaheddine0407)
---

## 🧭 Next Steps:

* ⛔ Add Budget limitations
* 📃 Add Monthly Report functionality
* 📈 Expense visualization with **Matplotlib**
* 🖼️ Graphical **User Interface (GUI)** version with Tkinter 
* 🏷️ Filters by category and by date
* 📊 Monthly statistics (average expenses, top categories)
* 💾 Export to Excel (`.xlsx`)

---

