def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count
user_input = input("Enter a string: ")
result = count_vowels(user_input)
print(f"Number of vowels in the string: {result}")
