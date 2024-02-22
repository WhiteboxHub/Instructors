from itertools import product

def calculate_earnings(shoe_sizes, customer_preferences):
    total_earnings = 0

    # Generate all possible combinations of sizes and prices
    all_combinations = product(shoe_sizes, repeat=2)

    # Create a dictionary to store the availability and price of each size
    size_prices = {size: price for size, price in all_combinations}

    # Iterate through customer preferences
    for preference in customer_preferences:
        size, price = preference
        size = int(size)
        price = int(price)

        # Check if the requested size is available
        if size in size_prices and size_prices[size] == price:
            total_earnings += price
            # Mark the size as unavailable
            del size_prices[size]

    return total_earnings

if __name__ == "__main__":
    # Sample input
    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    num_customers = int(input())

    customer_preferences = [list(map(int, input().split())) for _ in range(num_customers)]

    result = calculate_earnings(shoe_sizes, customer_preferences)
    print(result)
