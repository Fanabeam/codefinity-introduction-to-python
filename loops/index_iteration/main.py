prices = [29.99, 45.50, 12.75, 38.20]
discount = [.1, .2, .15, .05]

for i in range(len(prices)):
    original_price = prices[i]
    new_price = original_price * (1 - discount[i])
    prices[i] = new_price
    print(f'Updated price for item {i + 1}: {new_price:.2f}')