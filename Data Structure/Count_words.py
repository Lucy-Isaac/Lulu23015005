# A simple code that counts each letters of a word and gives the total.
# We used a len funtion for this

def count_word(word):
    word = input("Enter any word of your choice: ")
    return len(word)

print(count_word("hello"))
