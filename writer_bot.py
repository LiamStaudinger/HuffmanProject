'''
File: writer_bot.py
Name: Liam Staudinger
Course: CSC 120, Spring 2024
Purpose: The program reads in a file containing words, a number n,
and a number of words to generate. The program then generates a text from the
file using a Markov chain and prints the text.
'''

import random
SEED = 8

def openfile():
    '''
    This function reads in a file containing words and returns a list of the
    words in the file.

    Parameters:
        None
    Returns:
        main_list (list): A list of words in the file.
    '''
    filename = input()
    file = open(filename, "r")
    main_list = []
    for line in file:
        # Skip empty lines
        if len(line) == 1:
            continue
        line = line.strip().split()
        for word in line:
            main_list.append(word)
    file.close()
    return main_list
         
def format_text(words, n):
    '''
    This function formats the text into a dictionary where the keys are tuples
    of n words and the values are lists of words that follow the n words.

    Parameters:
        words (list): A list of words in the file.
        n (int): The number of words to use in the prefix.
    Returns:
        formatted_text (dict): A dictionary where the keys are tuples of n 
        words and the values are lists of words that follow the n words.
    '''
    formatted_text = {}
    # Prepend 'NONWORD' to the list of words n times
    words = ['NONWORD'] * n + words
    for i in range(len(words) - n):
        # Create a prefix using a tuple of n words
        prefix = tuple(words[i:i+n])
        # Get the word that follows the prefix
        suffix = words[i+n]
        if prefix in formatted_text:
            formatted_text[prefix].append(suffix)
        else:
            formatted_text[prefix] = [suffix]
    return formatted_text   

def generate_text(formatted_text, num_of_words, n):
    '''
    This function generates a text using a Markov chain and returns the text.

    Parameters:
        formatted_text (dict): A dictionary where the keys are tuples of n 
        words and the values are lists of words that follow the n words.
        num_of_words (int): The number of words to generate.
        n (int): The number of words to use in the prefix.
    Returns:
        tlist (list): A list of words generated using the Markov chain.
    '''
    random.seed(SEED)
    tlist = []
    prefix = ()
    # Create the initial prefix with 'NONWORD' n times
    for i in range(n):
        prefix += ('NONWORD',)
    # Generate the specified number of words
    for i in range(num_of_words):
        if prefix not in formatted_text.keys():
            break
        # If there is more than one word that can follow the prefix, choose one
        # at random
        if len(formatted_text[prefix]) > 1:
            word = formatted_text[prefix][
                random.randint(0, len(formatted_text[prefix]) - 1)]
        else:
            # If there is only one word that can follow the prefix, choose that
            # word
            word = formatted_text[prefix][0]
        tlist.append(word)
        # Update the prefix for the next iteration
        prefix = prefix[1:] + (word,)
    return tlist

def print_text(tlist):
    '''
    This function formats the text into ten words per line.

    Parameters:
        tlist (list): A list of words generated using the Markov chain.
    Returns:
        line (str): A string containing the text with ten words per line.
    '''
    line = ''
    counter = 0
    for word in tlist:
        line += word + ' '
        counter += 1
        if counter % 10 == 0:
            line += '\n'
    return line

def main():
    '''
    Main function to drive the program.

    Parameters:
        None
    Returns:
        None
    '''
    words = openfile()
    n = int(input())
    formatted_text = format_text(words, n)
    num_of_words = int(input())
    tlist = generate_text(formatted_text, num_of_words, n)
    print(print_text(tlist))
main()