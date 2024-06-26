def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num*0.5) + 1):
        if num % i == 0:
            return False
    return True 
user_input = int(input("Enter a positive integer: "))
result = check_prime(user_input)
if result:
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.") 
