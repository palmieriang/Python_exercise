#!/usr/bin/env python
# encoding: utf-8
'''
word_game.py
created by Angelo Palmieri

'''
import operator

def sort_dict(d, reverse = True):
    return sorted(d.iteritems(), reverse = reverse, \
                  key = operator.itemgetter(1))

def rank_words_from_file(f):
    '''
        Takes in a file, then ranks all the words within the file
        Args: file
        Return: a dictionary of all the words as the key and the
                ranking as the value
    '''
    word_dict = {}
    words =[]
    for line in f:
        list_of_words = line.split()
        for w in list_of_words:
            words.append(w.lower())

    for word in words:
        if word_dict.has_key(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


def main ():
    # Title
    print 'The Word Game'
    print '='*30
    print ''

    # Game Setup
    print 'Loading words...'
    f = open('alice.txt', 'rU')
    orig_ranked_words_dict = rank_words_from_file(f)
    f.close()
    print 'Loading complete!'
    print 'Game starting...'
    print''

    # Game loops
    # loop for each game
    while True:
        # determine the round limit
        while True:
            try:
                round_limit = int(raw_input('Choose game lenght. How many rounds? [enter a number larger than 0]: '))
                if int(round_limit) <= 0:
                    print 'The answer must be bigger than 0. Please try again.'
                    print ''
                else:
                    break
            except:
                print 'An error occurred, make sure you enter an integer.'
                print ''

        # Setup initial variables
        points = [0,0]
        cur_player = 1 # start from player 1
        cur_word = '' # start from empty word 
        cur_round = 1 # start from round 1
        round_over = False

        # Create a copy of the dictionary (the game is gonna remove some
        # word; so at beginning I want the complete dictionary again)
        ranked_words_dict = orig_ranked_words_dict.copy()

        # loop for each round
        while True:
            print 'Round', cur_round
            print 'Player 1: %d     Player 2: %d' % (points[0],points[1])
            print ''

            # loop for each word
            while True:
                if len(cur_word) > 0:
                    print ''
                    print (' '*5)+'Current String =  "%s" ' % cur_word 
                    print ''

                # Get new letter
                new_letter = str(raw_input('Player %d, Please enter a letter: ' % cur_player))
                if len(new_letter) > 1:
                    new_letter = new_letter[0] # add only 1 letter! if I add a word it gets only the first letter

                # Add it to the current word
                cur_word = str(cur_word)+str(new_letter).lower()

                # Check if word in Ranked Word Dict
                potential_word = False
                for key, value in ranked_words_dict.items():   # key and value = 2 variables; items create a list in the dictionary
                    # found = re.match(str(cur_word), str(key))    (another way to do the same)
                    # if found:      # alice
                    if len(cur_word) <= len(key) and str(cur_word) == str(key[:len(cur_word)]):
                        potential_word = True
                    if str(cur_word) == str(key) and len(cur_word)>3:
                        round_over = True
                        round_points = value
                        del ranked_words_dict[key]

                # Check if the cur_word is not valid using the variable potential_word
                if potential_word == False:
                    round_over = True
                    round_points = int(5)

                    print ''
                    print '%s - will not make valid word, Player %d lost that round!' % \
                              (cur_word,cur_player)

                # Check if the round_over is True
                if round_over:
                    # Statement to determine list position of winning player
                    if cur_player == 2:
                        p = 0
                        winning_player = 1
                    else:
                        p = 1
                        winning_player = 2

                    # Assign points to winning player
                    points[p] += round_points

                    print ''
                    print '#YAH!'*10
                    print ''

                    print (" "*15)+'Winning Word = "%s"' % cur_word
                    print (' '*4)+'Player %d just won that round! (%d points)' % \
                              (winning_player, round_points)

                    print ''
                    print '#YAH!'*10
                    print ''

                    cur_word = ''
                    # Exit Round

                    break

                else:
                    # Change the player
                    if cur_player == 1:
                        cur_player = 2
                    else:
                        cur_player = 1

            # Back inside of the Rounds Loop
            if cur_round == round_limit:
                print ''
                print'Round Limit Reached'
                print ''
                print 'Player 1: %d    Player 2: %d' % (points[0],points[1])
                print ''
                if points[0] > points[1]:
                    print 'Player 1 WINS!'
                elif points[0] < points[1]:
                    print 'Player 2 WINS!'
                else:
                    print "It's a TIE!"
                print ''

                break

            else:
                round_over = False
                cur_round += 1

        # Back in the Game Loop
        user_input = str(raw_input('Type "q" to quit or "<any key>" to play again: '))
        if user_input.lower() == 'q':
            break

    # The Game has been exited
    print ''
    print 'Thank you for playing!'
                 



if __name__ == '__main__':
    main()
