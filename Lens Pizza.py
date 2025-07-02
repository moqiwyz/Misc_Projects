# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Counting
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Number of toppings
num_pizzas = len(toppings)

# Advertising
print(f"We sell {num_pizzas} different kinds of pizza!")

# Pizza prices and toppings
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Sort pizza_and_prices in ascending price order
pizza_and_prices.sort(reverse=False)

# Get the cheapest and priciest pizzas
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
print(f"The cheapest pizza is {cheapest_pizza}")
print(f"The priciest pizza is {priciest_pizza}")
# Remove the most expensive pizza
pizza_and_prices.pop()
# Add new topping
pizza_and_prices.insert(3, [2.5, "peppers"])

# 3 cheapest pizzas sold
three_cheapest = pizza_and_prices[:3]
print(f"These are sold: {three_cheapest}")