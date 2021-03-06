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

  def amount_spent(self) -> float:
    #displays the total value of all withdraws (entries with values < 0) 
    balance = 0.0
    for entry in self.ledger:
      if entry["amount"] < 0.0:
        balance += entry["amount"]
    return balance

  def amount_earned(self) -> float:
    #displays the total value of all deposits (entries with values > 0) 
    balance = 0.0
    for entry in self.ledger:
      if entry["amount"] > 0.0:
        balance += entry["amount"]
    return balance


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
    #print(printout)    
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
  percent_list = []
  print_string = "Percentage spent by category\n"
  total_spent = 0
  if len(categories) > 4:
    print("Can only process 4 categories")

  for category in categories:
    total_spent += abs(category.amount_spent())

  for category in categories:
    percent_list.append(({"Percent":(int((abs(category.amount_spent())/total_spent)*100)),"Category": category.category}))


  for row in range(100,-10,-10):
    print_string += str(row).rjust(3) + "| " #adding percentage to the row
    for category_index in percent_list:
        #print(category_index["Percent"])
        if category_index["Percent"] >= row:
          print_string += "o  "
        else:
          print_string += "   "
    print_string += "\n"    
  #print(percent_list)
  print_string += ("    " + "---" * len(percent_list)) + "-\n"
  longest_string = 0
  for category_name in percent_list:
    if len(category_name['Category']) > longest_string:
        longest_string = len(category_name['Category'])
  
  for string_index in range(0,longest_string):
    print_string += "    "
    for category_name_vert in percent_list:
      print_string += " "
      try:
        print_string += category_name_vert['Category'][string_index]
      except:
        print_string += " "
      print_string += " "
    if string_index < longest_string-1:
      print_string += " \n"
    else:
      print_string += " "
    
  #print(repr(print_string))

  


  
