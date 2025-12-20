import datetime
class Expense:
    def __init__(self, name, categorie, amount) -> None:
        self.name = name 
        self.categorie = categorie
        self.amount = amount
    
    def __repr__(self):
        return f"<Expense(Name : {self.name}, Categorie: {self.categorie}, Amount: {self.amount}, Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}>"