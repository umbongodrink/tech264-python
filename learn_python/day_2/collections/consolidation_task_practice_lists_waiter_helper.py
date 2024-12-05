
# Level 1
customer = input("Please tell me your name, Sir: ")
print(f"Greetings {customer}")

list_of_starters = ["hummous and bread", "tomato soup", "onion soup"]
print(f"The list of starters is {list_of_starters}")

customer_starter = input(f"What starter would you like, {customer}? ")
if customer_starter not in list_of_starters:
    print(f"Sorry, {customer}, we do not have {customer_starter} on the menu.")
    customer_starter = input(f"What starter would you like instead, {customer}? ")

list_of_mains = ["steak", "weiner schnitzel", "hamburger", "vegeburger"]
print(f"The list of main dishes is: {list_of_mains}")

customer_main = input(f"What would you like your main dish to be, {customer}? ")
if customer_main not in list_of_mains:
    print(f"Sorry, {customer}, we do not have {customer_main} on the menu.")
    customer_main = input(f"What main dish would you like instead, {customer}? ")

list_of_deserts = ["ice cream", "sorbet", "chocolate cake"]
print(f"The list of deserts is: {list_of_deserts}")

customer_desert = input(f"What would you like for desert, {customer}? ")
if customer_desert not in list_of_deserts:
    print(f"Sorry, {customer}, we do not have {customer_desert} on the menu.")
    customer_desert = input(f"What desert would you like instead, {customer}? ")

print(f"Your choice of dishes is: {customer_starter} followed by {customer_main}, and finally {customer_desert}.")


## level 2
customer_order_list = [customer_starter, customer_main, customer_desert]

dish_prices = {"hummous and bread": 5.95, "tomato soup": 6.99, "onion soup": 5.99,
               "steak": 11.99, "weiner schnitzel": 15.99, "hamburger": 10.99, "vegeburger": 8.99,
               "ice cream": 5.99, "sorbet": 4.99, "chocolate cake": 7.99}

total_price = 0
for dish in customer_order_list:
    total_price += dish_prices[dish]

print(f"The total price of your order {customer} is: {total_price}")