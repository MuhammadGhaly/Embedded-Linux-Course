# test whether a passed letter is a vowel or not.

while True:

    letter = input("Enter a character: ")  
  

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
 
    if letter in vowels: 

        print(f"The character '{letter}' is a vowel")  

    else:  

        print(f"The character '{letter}' is not a vowel")  