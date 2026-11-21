

products = {
    "Wireless Mouse": (350, 599, 120),
    "Bluetooth Speaker": (900, 1499, 75),
    "USB Cable": (60, 149, 300),
    "Phone Case": (80, 299, 250),
    "Power Bank": (700, 1199, 90),
    "Headphones": (1100, 1899, 60),
    "Laptop Bag": (650, 999, 55),
    "Smart Watch": (1800, 2999, 40),
    "Keyboard": (500, 849, 85),
    "Webcam": (800, 1399, 30),
}

def get_product_figures(name):
    """Return (total_cost, revenue, profit, profit_percent) for one product."""
    cost_price, selling_price, units = products[name]  
    total_cost = cost_price * units
    revenue = selling_price * units
    profit = revenue - total_cost
    profit_percent = (profit / total_cost) * 100

    return (total_cost, revenue, profit, profit_percent) 


def get_overall_figures():
    """Return (total_cost, total_revenue, net_profit, profit_percent) for all products."""
    all_cost = 0
    all_revenue = 0

    for name in products:
        total_cost, revenue, profit, percent = get_product_figures(name)
        all_cost = all_cost + total_cost
        all_revenue = all_revenue + revenue

    net_profit = all_revenue - all_cost
    profit_percent = (net_profit / all_cost) * 100

    return (all_cost, all_revenue, net_profit, profit_percent)

def show_all_products():
    print("\n--- PRODUCT LIST ---")
    print("Product | Cost Price | Selling Price | Units Sold")
    for name in products:
        cost_price, selling_price, units = products[name]
        print(name, "|", "Rs", cost_price, "|", "Rs", selling_price, "|", units)


def show_sales_report():
    print("\n--- PRODUCT-WISE SALES REPORT ---")
    for name in products:
        total_cost, revenue, profit, percent = get_product_figures(name)
        print("\nProduct       :", name)
        print("Total Cost    : Rs", total_cost)
        print("Revenue       : Rs", revenue)
        print("Net Profit    : Rs", profit)
        print("Profit Percent:", round(percent, 2), "%")


def show_overall_summary():
    total_cost, total_revenue, net_profit, percent = get_overall_figures()

    print("\n--- OVERALL BUSINESS SUMMARY ---")
    print("Total Products      :", len(products))
    print("Total Cost          : Rs", total_cost)
    print("Total Revenue       : Rs", total_revenue)
    print("Net Profit          : Rs", net_profit)
    print("Overall Profit %    :", round(percent, 2), "%")


def show_best_and_worst():
    best_name = ""
    best_profit = -999999999
    worst_name = ""
    worst_profit = 999999999

    for name in products:
        profit = get_product_figures(name)[2]  
        if profit > best_profit:
            best_profit = profit
            best_name = name
        if profit < worst_profit:
            worst_profit = profit
            worst_name = name

    print("\n--- MOST AND LEAST PROFITABLE ---")
    print("Most profitable product :", best_name, "- Rs", best_profit)
    print("Least profitable product:", worst_name, "- Rs", worst_profit)
    top_percent_name = ""
    top_percent = -999999999
    for name in products:
        percent = get_product_figures(name)[3]
        if percent > top_percent:
            top_percent = percent
            top_percent_name = name

    print("Highest profit % product:", top_percent_name, "-", round(top_percent, 2), "%")


def show_loss_making():
    print("\n--- LOSS-MAKING PRODUCTS ---")
    found = False
    for name in products:
        profit = get_product_figures(name)[2]
        if profit < 0:
            print(name, "- Loss of Rs", abs(profit))
            found = True
    if not found:
        print("No product is making a loss. Great!")


def search_product():
    name = input("Enter product name: ")

    if name in products:
        cost_price, selling_price, units = products[name]
        total_cost, revenue, profit, percent = get_product_figures(name)

        print("\nProduct       :", name)
        print("Cost Price    : Rs", cost_price)
        print("Selling Price : Rs", selling_price)
        print("Units Sold    :", units)
        print("Total Cost    : Rs", total_cost)
        print("Revenue       : Rs", revenue)
        print("Net Profit    : Rs", profit)
        print("Profit Percent:", round(percent, 2), "%")
    else:
        print("Product not found.")


def update_units_sold():
    name = input("Enter product name: ")

    if name in products:
        extra_units = int(input("Enter number of new units sold: "))
        cost_price, selling_price, units = products[name]
        products[name] = (cost_price, selling_price, units + extra_units)
        print("Updated! Total units sold:", units + extra_units)
    else:
        print("Product not found.")


def update_price():
    name = input("Enter product name: ")

    if name in products:
        new_cost = float(input("Enter new cost price: "))
        new_selling = float(input("Enter new selling price: "))
        units = products[name][2]

        products[name] = (new_cost, new_selling, units)   # new tuple
        print("Prices updated successfully!")
    else:
        print("Product not found.")


def add_product():
    name = input("Enter new product name: ")

    if name in products:
        print("Product already exists.")
    else:
        cost_price = float(input("Enter cost price: "))
        selling_price = float(input("Enter selling price: "))
        units = int(input("Enter units sold: "))

        products[name] = (cost_price, selling_price, units)
        print("Product added successfully!")


def remove_product():
    name = input("Enter product name to remove: ")

    if name in products:
        del products[name]
        print("Product removed.")
    else:
        print("Product not found.")
while True:
    print("\n====== E-COMMERCE SALES MANAGER ======")
    print("1. Show all products")
    print("2. Product-wise sales report (profit and profit %)")
    print("3. Overall summary (net profit and profit %)")
    print("4. Most and least profitable products")
    print("5. Show loss-making products")
    print("6. Search a product")
    print("7. Add units sold to a product")
    print("8. Update cost / selling price")
    print("9. Add a new product")
    print("10. Remove a product")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_all_products()
    elif choice == "2":
        show_sales_report()
    elif choice == "3":
        show_overall_summary()
    elif choice == "4":
        show_best_and_worst()
    elif choice == "5":
        show_loss_making()
    elif choice == "6":
        search_product()
    elif choice == "7":
        update_units_sold()
    elif choice == "8":
        update_price()
    elif choice == "9":
        add_product()
    elif choice == "10":
        remove_product()
    elif choice == "0":
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid choice. Try again.")
