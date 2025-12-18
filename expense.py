class Expense:
    def __init__(self, name, categorie, amount, date) -> None:
        self.name = name 
        self.categorie = categorie
        self.amount = amount
    
    def __repr__(self):
        return f"<Expense(Name : {self.name}, Categorie: {self.categorie}, Amount: {self.amount},>"