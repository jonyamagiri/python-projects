#!/usr/bin/env python3

# entry point to the program
def main():
    '''
    This function takes user input for a sentence and performs word replacement
    based on user-defined criteria.
    '''
    print("This is a simple program that helps you replace words")
    
    sentence = input("Enter your sentence: ")
    print("You wrote the following:", sentence)
    
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    
    result = sentence.replace(word_to_replace, word_replacement)
    print(result)

# if the program is run (instead of imported), run word-replace:
if __name__ == "__main__":
    main()


# alternative code that achieves the same results
# #!/usr/bin/env python3

# def replace_word():
#     print('This is a simple program that helps you replace words')
#     str = input("Enter your sentence: ")
#     print('You wrote the following: ' + str)
#     word_to_replace = input("Enter the word to replace: ")
#     word_replacement = input("Enter the word replacement: ")
#     print(str.replace(word_to_replace, word_replacement))

# replace_word()