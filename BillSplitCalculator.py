print("====Bill Split Calculator====")
print("Enter bill amount: ")
bill_amount = float(input())
print("Will the bill be split? Yay or Nay")
is_split = input()
if(is_split=="Yay" or "yay"):
  print("Enter splitting amount: ")
  split_number = int(input())
print("Enter tipping amount(in dollars): ")
tip_percentage = float(input())  
tip_amount = (tip_percentage / 100) * bill_amount
bill_amount += tip_amount
print(f"Total (including tip): ${bill_amount}")
if (is_split!="nay" or "Nay"):
  split_amount = bill_amount / split_number
  print(f"Each person pays: ${split_amount}")



