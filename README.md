# 💰 BudgetBuddy

> Une application **CLI (console)** simple et efficace pour suivre vos **revenus**, **dépenses** et votre **Budget/Balance** directement depuis le terminal.

BudgetBuddy est pensé comme un **premier projet Python sérieux**, idéal pour les **débutants** souhaitant pratiquer la manipulation de fichiers et les bonnes pratiques de structuration de code.

---

## ✨ Fonctionnalités

* ➕ Ajouter des **revenus (Incomes)**
* ➖ Ajouter des **dépenses (Expenses)**
* 📝 Saisir les détails de chaque transaction :

  * Montant
  * Catégorie
  * Date
  * Nom / description
* 💾 **Sauvegarde automatique** des données dans un fichier CSV
* 📂 **Lecture automatique** des données existantes au démarrage
* 📊 Calcul du **solde total (Balance)** en temps réel
* 🖥️ Interface simple et claire en ligne de commande (CLI)

---

### 1️⃣ Prérequis

* Python **3.1+** installé sur votre machine

---

## 🗂️ Structure du fichier CSV

Les données sont stockées dans un fichier `income/expense.csv` avec la structure suivante :

| Colonne       | Description                           |
| ------------- | ------------------------------------  |
| `type`        | `income` ou `expense`                 |
| `amount`      | Montant de la transaction             | 
| `category`    | Catégorie (ex: Food, Rent, Salary)    |
| `date`        | Date au format `YYYY-MM-DD : HH-MM-SS`|
| `description` | Nom ou description de la transaction  |

---

## 🛠️ Technologies utilisées

* **Python 3**
* Bibliothèques standards :

  * `csv` → lecture et écriture des données
  * `datetime` → gestion des dates
  * `os` → gestion des fichiers

---

## 👥 Collaborateurs

* **[Ouaddi Salah eddine]** (@Salah-eddine-Ouaddi)
* **[Hamdane Salahdine]** (@salaheddine)
---

## 🧭 Prochaine étapes:

* 📈 Visualisation des dépenses avec **Matplotlib**
* 🖼️ Version **interface graphique (GUI)** avec Tkinter ou PyQt
* 🏷️ Filtres par catégorie et par date
* 📊 Statistiques mensuelles (dépenses moyennes, top catégories)
* 💾 Export vers Excel (`.xlsx`)

---

N’hésitez pas à laisser une ⭐ si ce projet vous aide !
