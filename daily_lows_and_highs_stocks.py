stock_prices = [34.68, 
                36.09, 
                34.94, 
                33.97, 
                34.68, 
                35.82, 
                43.41, 
                44.29, 
                44.65, 
                53.56, 
                49.85, 
                48.71, 
                48.71, 
                49.94, 
                48.53, 
                47.03, 
                46.59, 
                48.62, 
                44.21, 
                47.21]

# Helper function to find price of stock at every iteration
def price_at(i):
    return stock_prices[i - 1]

# Finds maximum price within a given amount of days
def max_price(a, b):
    maximum = 0
    for i in range(a, b - 1):
        maximum = max(maximum, price_at(i))
    return maximum

# Finds minimum price within a given amount of days
def min_price(a, b):
    minimum = price_at(a)
    for i in range(a, b - 1):
        minimum = min(minimum, price_at(i))
    return minimum


# Test cases
print(max_price(1, 15))
print(min_price(5, 10))
print(price_at(3))