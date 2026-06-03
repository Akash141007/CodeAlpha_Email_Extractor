# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")

# Number of stocks user wants to enter
n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input(f"\nEnter stock {i+1} name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not found in price list!")

# Calculate total investment
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

print("\n===== Portfolio Summary =====")
for stock, quantity in portfolio.items():
    print(
        f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${stock_prices[stock] * quantity}"
    )

print(f"\nTotal Investment Value = ${total_investment}")

# Save result to file
choice = input("\nDo you want to save the result? (yes/no): ").lower()

if choice == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("=======================\n")

        for stock, quantity in portfolio.items():
            file.write(
                f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${stock_prices[stock] * quantity}\n"
            )

        file.write(f"\nTotal Investment Value = ${total_investment}")

    print("Portfolio saved successfully in portfolio.txt")

print("\nThank you for using Stock Portfolio Tracker!")