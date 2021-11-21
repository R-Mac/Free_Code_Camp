class Category:
  def __init__(self,category=""):
    #create a list variable called ledger
    self.category = category
    self.ledger = []

  def deposit(self,amount:float,description:str=""):
    self.ledger.append({"amount": amount, "description": description})
    #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}

  def get_balance(self) -> float:
    #returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    balance = 0.0
    for entry in self.ledger:
      balance += entry["amount"]
    return balance

  def check_funds(self,amount:float) -> bool:
    #method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    
    if amount > self.get_balance():
      return False
    else:
      return True


  def withdraw(self,amount:float,description:str="") -> bool:
    if self.get_balance() > amount:
      self.deposit(amount*-1.0, description)
      return True
    else:
      return False
    #but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.


  
  def transfer(self,amount:float, receiving_budget) -> bool:
    #check if funds are available 
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + receiving_budget.category)
      receiving_budget.deposit(amount,"Transfer from " + self.category)
      return True
    else:
      return False
    #accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise



  def __str__(self) -> str:
    printout = self.category.center(30,'*') + "\n"
    for item in self.ledger:
      printout += item['description'][:23].ljust(23)
      printout +=  ("{:7.2f}".format(item['amount'])).rjust(7) + '\n'

    printout += "Total:" + "{:7.2f}".format(self.get_balance())
    print(printout)    
    return printout
    #When the budget object is printed it should display:

    #A title line of 30 characters where the name of the category is centered in a line of * characters.
    #A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    #A line displaying the category total.
    #Here is an example of the output:

    #*************Food*************
    #initial deposit        1000.00
    #groceries               -10.15
    #restaurant and more foo -15.89
    #Transfer to Clothing    -50.00
    #Total: 923.96

def create_spend_chart(categories:list):
  return True
