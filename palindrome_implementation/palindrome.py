#!/usr/bin/env python3

def is_palindrome(string):
    '''Function that gets a string as input argument
    , and outputs if the string is palindrome or not'''
    # remove space and tabs from the string
    string = string.replace(" ","")
    # convert string to lowercase
    string = string.lower()

    return string == string[::-1]

if __name__ == '__main__':
    # Write some phrases in a list
    phrases = ["Anna  ", "B  o  b", "leve     l", "ten      et", "Rac   e Car", "Top spot", "Never odd or even", "One tWo three", "testing"," one more testing phrase "]

    for phrase in phrases:
        res = is_palindrome(phrase)
        if res:
            print("'" + phrase + "'" + " is a palindrome")
        else:
            print("'" + phrase + "'" + " is not a palindrome")
        