stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 350
}

name = input("Enter your name: ")

total_investment = 0
stock_count = 0

file = open("portfolio.txt", "w")
file.write("Stock Portfolio Report\n")
file.write("Investor Name: " + name + "\n\n")

while True:
    stock_name = input("Enter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        try:
            quantity = int(input("Enter quantity: "))

            investment = stocks[stock_name] * quantity
            total_investment += investment
            stock_count += 1

            print(stock_name, ": ₹", investment)

            file.write(
                f"{stock_name} - Quantity: {quantity} - Investment: ₹{investment}\n"
            )

        except ValueError:
            print("Please enter a valid quantity.")

    else:
        print("Stock not found!")

file.write(f"\nTotal Investment Value: ₹{total_investment}")
file.close()

print("\nPortfolio Summary")
print("Investor Name:", name)
print("Stocks Entered:", stock_count)
print("Total Investment Value: ₹", total_investment)

print("Result saved to portfolio.txt")
