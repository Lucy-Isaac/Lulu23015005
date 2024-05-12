def fibonacci_sequence(n):
    if n <= 1:
        return n
    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
user_input = int(input("Enter a non-negative integer (n): "))
result = fibonacci_sequence(user_input)
print(f"The {user_input}th Fibonacci number is: {result}")
