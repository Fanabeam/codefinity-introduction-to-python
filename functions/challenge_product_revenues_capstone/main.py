def calculate_revenue(prices, quantities_sold):
    total_price = []
    for i in range(len(prices)):
        rev = prices[i] * quantities_sold[i]
        total_price.append(rev)
    return total_price

def formatted_output(rev):
    rev = sorted(rev)
    for i in range(len(rev)):
        print(f'{rev[i][0]} has total revenue of ${rev[i][1]}')


products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
revenue = []
revenue = calculate_revenue(prices, quantities_sold)

revenue_per_product = tuple(zip(products, revenue))
#print(revenue_per_product)

formatted_output(revenue_per_product)


# Example of expected output line (do not remove):
#print(f"{revenue_[0]} has total revenue of ${revenue[1]}")