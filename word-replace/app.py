#!/usr/bin/env python3

def replace_word():
    print('This is a simple program that helps you replace words')
    str = input("Enter your sentence: ")
    print('You wrote the following: ' + str)
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()
