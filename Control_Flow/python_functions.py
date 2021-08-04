def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  total_bill = food_bill + electricity_bill + internet_bill + rent
  if budget < total_bill:
    return True
  else:
    return False
