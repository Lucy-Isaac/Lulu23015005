# The code is used to find the maximum and minimum of numbers given

def find_max_min(number):
    return (max(number), min(number))


number = input("Enter numbers(seperate the numbers by space please): ")
number = tuple(int(x) for x in number.split())

result = find_max_min(number)
print ("The maximum and minimum number is: ", result)
