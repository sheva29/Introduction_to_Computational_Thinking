from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    # 1. Use get_perms to get a list [] of possible words
    # 2. From that list, calculate which hand gives the highest score and store in a dictionary with the highest value
    # 3. As we get scores, we track of the highest and the word itself
    # 4. At the end, return score
    listOfWords = get_perms(hand, len(hand))
    word = ""
    score = 0
    for i in range(listOfWords):
        tempScore = get_word_score(listOfWords[i], len(listOfWords[i]))
        if score < tempScore):
            score = tempScore
            word = listOfWords[i]

    return word



#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed,
       the remaining letters in the hand are displayed, and the computer
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...

    compWord = ""
    score = 0

    while compWord != None:

        print("Current hand: ", display_hand(hand))
        input("Enter word, or a \".\" to indicate that you are finished: ")
        comWord = comp_choose_word(hand, word_list)

        if compWord == None:
            print("Total score: ", score)
            break

        if is_valid_word(comp, hand, word_list) == False:
            print("INvalid word, please try again")

        else:
            tempScore = get_word_score(compWord, len(compWord))
            score = score + tempScore
            update_hand(hand, compWord)
            print("\"" + compWord + "\"" + " earnd " + str(tempScore) + " points. Total: " + str(score) + " points")


#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    comptWord = ""
    hand = {}
    previoushand = {}

    while compWord != "e"
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
