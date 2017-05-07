from ps3a import *
import time
from perm import *
from random import *


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
    listOfWords = get_perms(hand, randint(0,len(hand)))
    # print(listOfWords)
    word = ""
    score = 0
    for i in range(len(listOfWords)):
        if listOfWords[i] in word_list:
            tempScore = get_word_score(listOfWords[i], len(listOfWords[i]))
            if score < tempScore:
                score = tempScore
                word = listOfWords[i]

    return word



#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(word_list, hand):
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
        # print(compWord)
        if compWord == None:
            print("Total score: ", score)
            break

        if is_valid_word(compWord, hand, word_list) == False:
            print("Invalid word, please try again")

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
    firstPrompt = ""
    hand = {}
    previousHand = {}

    while firstPrompt != "e":
        firstPrompt = input("Welcome to word game, if you want to play a random hand type \"n\", if you want to play the last hand again type \"r\". If you want to exit just type \"e\": ")
        if firstPrompt is "n":
            hand = deal_hand(HAND_SIZE)
            previousHand = hand.copy()
            secondPrompt = input("If you want to play, type \"u\", if you want the computer to play type \"c\" ")

            if secondPrompt == "u":
                play_hand(word_list, hand)
            elif secondPrompt == "c":
                comp_play_hand(word_list, hand)

        elif firstPrompt is "r":
            if bool(hand) is False:
                hand = deal_hand(HAND_SIZE)
                previousHand = hand.copy()

            secondPrompt = input("If you want to play, type \"u\", if you want the computer to play type \"c\" ")

            tempHand = previousHand.copy()
            if secondPrompt == "u":
                play_hand(word_list, tempHand)
            elif secondPrompt == "c":
                comp_play_hand(word_list, tempHand)


# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
