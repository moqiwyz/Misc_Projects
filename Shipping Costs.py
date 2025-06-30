weight = float(input("How much does it weigh? "))
if weight <= 0:
  print("Please enter a positive weight.")
  exit()


# Ground Shipping
if weight <= 2:
  ground_price = weight * 1.50 + 20.00
elif 2 < weight <= 6:
  ground_price = weight * 3.00 + 20.00
elif 6 < weight <= 10:
  ground_price = weight * 4.00 + 20.00
else:
  ground_price = weight * 4.75 + 20.00
print(f"Ground Shipping ${ground_price:.2f}")


# Ground Shipping Premium
premium = 125.00
print(f"Ground Shipping Premium ${premium:.2f}")


# Drone Shipping
if weight <= 2:
  drone_price = weight * 4.50 
elif 2 < weight <= 6:
  drone_price = weight * 9.00
elif 6 < weight <= 10:
  drone_price = weight * 12.00
else:
  drone_price = weight * 14.25
print(f"Drone Shipping ${drone_price:.2f}")