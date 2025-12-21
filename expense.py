import datetime
class Expense:
    def __init__(self, name, categorie, amount, date) -> None:
        self.name = name
        self.categorie = categorie
        self.amount = amount
        self.date = date
    
    def __repr__(self):
        return f"<Expense: {self.name}, {self.categorie}, ${self.amount:.2f}, {self.date}>"
