print("===================================")
print("      STOCK PORTFOLIO TRACKER      ")
print("===================================")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 300,
    "MSFT": 220,
    "AMZN": 270
}

total_investment = 0

print("\nAvailable Stocks:")
print("AAPL - Rs.180")
print("TSLA - Rs.250")
print("GOOG - Rs.300")
print("MSFT - Rs.220")
print("AMZN - Rs.270")

number_of_stocks = int(input("\nHow many different stocks do you want to enter? "))

for i in range(number_of_stocks):

    print("\nStock", i + 1)

    stock_name = input("Enter Stock Name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter Quantity: "))

        investment = stock_prices[stock_name] * quantity

        total_investment += investment

        print("Price Per Share :", stock_prices[stock_name])
        print("Investment Value :", investment)

    else:
        print("Stock Not Available!")

print("\n===================================")
print("        PORTFOLIO SUMMARY")
print("===================================")

print("Total Investment Value = Rs.", total_investment)

file = open("portfolio_report.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("=========================\n")
file.write("Total Investment Value = Rs." + str(total_investment))

file.close()

print("\nReport Saved Successfully!")
print("File Name : portfolio_report.txt")