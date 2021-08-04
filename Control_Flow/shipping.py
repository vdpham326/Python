
weight = 8.4
cost = 0
cost_premium = 125.0
cost_drone = 0
# Ground Shipping

if weight <= 2:
  cost = weight * 1.5 + 20
elif weight <= 6:
  cost = weight * 3.0 + 20
elif weight <= 10:
  cost = weight * 4.00 + 20
else:
  cost = weight * 4.75 + 20

print(cost)

weight = 1.5
# Drone Shipping
if weight <=2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print(cost_drone)
