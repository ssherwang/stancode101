"""
File: anagram.py
Name: Sher
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'              # Controls when to stop the loop
word_list = []           # A list to contain all of information in FILE


def main():
    print('Welcome to stanCode \"Anagram Generator" (or -1 to quit)')
    #  Read file, which contains a list of words
    read_dictionary()
    while True:
        s = input('Find anagram for: ')
    ####################
        start = time.time()
        #  Terminated condition
        if s == EXIT:
            break
        else:
            print("Searching ...")
            find_anagrams(s)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    # Read file
    global word_list
    with open(FILE, 'r') as f:
        for word in f:
            #  Remove space
            word_list.append(word.strip())


def find_anagrams(s):
    """
    :param s: user's input
    :return: a word which is present in dictionary
    """
    #  A empty list to contain answers
    ans_list = []
    find_anagrams_helper(s, '', ans_list)
    print(f'{len(ans_list)} anagrams: {ans_list}')


def find_anagrams_helper(s, current_s, ans_list):
    #  Base-case
    if len(s) == len(current_s):
        #  Check the final word in word list or not
        if current_s in word_list:
            #  Check if the word in our answer list or not
            if current_s not in ans_list:
                ans_list.append(current_s)
                print(f'Found: {current_s}')
                print('Searching...')
    #  Backtracking
    else:
        #  Choose
        for ele in s:
            #  Calculate the present times for alphabets of user's input
            if s.count(ele) > current_s.count(ele):
                current_s += ele
                #  Explore
                if has_prefix(current_s) is True:
                    find_anagrams_helper(s, current_s, ans_list)
                    #  Un-choose
                    current_s = current_s[:-1]
                else:
                    #  Un-choose
                    current_s = current_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: a string which is needed to be valued in word list
    :return: True or False
    """
    #  explore
    global word_list
    for word in word_list:
        if word.startswith(sub_s) is True:
            return True


if __name__ == '__main__':
    main()
