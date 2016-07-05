'''
Created by Angelo Palmieri
'''

import re

def find_words(pat,f):

    # 'a'   ' a'
    words = []
    for line in f:
        found = re.findall( r'\s%s\w' % str(pat), str(line))

        if len(found) > 0:
            for w in found:
                if w not in words:
                    words.append(w)
    return words

def main():

    while True:
        f = open('alice.txt', 'rU')

        pat = str(raw_input('Please enter a letter combo: (or type "QUIT" to quit) '))

        if pat == 'QUIT':
            break
        if pat:
            words = find_words(pat,f)
        else:
            words = None
            print 'Please enter a letter combo.'
            
        if words:
            print ''
            print ' There are %s words beginning with "%s" in the file' % \
                  (int(len(words)), str(pat))
            print ''
            for word in words:
                print word
            print ''
            
        else:
            print 'No words found'
            
        f.close()


if __name__ == '__main__':
    main()
