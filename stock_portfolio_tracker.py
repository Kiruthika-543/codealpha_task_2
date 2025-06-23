# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 125,
    "MSFT": 310
}

portfolio = {}
total_value = 0

print("Welcome to Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from the available list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock} shares: "))
        if quantity < 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = quantity
    total_value += stock_prices[stock] * quantity

# Display the portfolio and total value
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock}: {quantity} shares @ ${price} each = ${price * quantity}")

print(f"Total Investment Value: ${total_value}")

# Save to file
save = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            f.write(f"{stock}: {quantity} shares @ ${price} each = ${price * quantity}\n")
        f.write(f"Total Investment Value: ${total_value}\n")
    print("Summary saved to 'portfolio_summary.txt'")
