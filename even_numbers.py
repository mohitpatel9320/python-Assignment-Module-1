def generate_even_numbers():
    """Generator function to yield the first 10 even numbers."""
    for i in range(1, 11):
        yield i * 2

# Example usage:
for num in generate_even_numbers():
    print(num)