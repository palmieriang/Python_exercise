#!/usr/bin/env python
# encoding: utf-8
'''
alice_file.py

Created by Angelo Palmieri.
'''
import operator

## Get each word - Turn to Lower case (.lower())
## Count Duplicates of words
## Dictionary {word:count,word2:count2}
## Sort this based on most used word
## Print the Top 20 Words

def rank_words(f):
    '''
        Takes in a file, then ranks all the words within the file
        Args: a text file
        Return: a sorted list of tuples
    '''
    word_dict = {} # start with empty dictionary
    words = [] # word list empty
    for line in f:
        list_of_words = line.split()
        for w in list_of_words:
            words.append(w.lower()) # add word to list

    for word in words:
        if word_dict.has_key(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return sorted(word_dict.iteritems(), reverse = True, \
                      key = operator.itemgetter(1))
        # sort function can be used with a list
        # .iteritems = iterate over the items (not
        #               necessarily copy them to a list)
        #               (iteration key|value)
        # reverse = biggest -> smallest (reverse order) 
        # key = what we want to sort on
                

def main():
    # file
    f = open('alice.txt', 'rU') # by changing the name we can use different files

    ranked_words_list = rank_words(f)

    f.close()

    # Print result
    for w in list(ranked_words_list[:20]):
        print w[0], '---', w[1]

if __name__ == '__main__':
    main()
