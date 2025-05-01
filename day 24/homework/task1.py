word = input("Enter a word: ")  
reversed_word = word[::-1]  

if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is a common word.")