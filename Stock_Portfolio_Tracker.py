stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 350
}

name = input("Enter Your Name: ")

total = 0

print("\nAvailable Stocks:")
for stock in stocks:
    print(stock, "-", stocks[stock])

file = open("portfolio.txt", "w")

while True:

    stock_name = input("\nEnter Stock Name (or done to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:

        qty = int(input("Enter Quantity: "))

        amount = stocks[stock_name] * qty

        total = total + amount

        print("Investment in", stock_name, "= ₹", amount)

        file.write(stock_name + " : ₹" + str(amount) + "\n")

    else:
        print("Stock Not Available")

file.write("\nTotal Investment = ₹" + str(total))
file.close()

print("\n===== Portfolio Summary =====")
print("Investor:", name)
print("Total Investment: ₹", total)

print("\nData saved in portfolio.txt")
