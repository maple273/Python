#!C:\Python27\python.exe

'''
Programmer: Mary Qiu


Hit && Match game 

Assumptions: The house will choose three different random digits for the left,
middle, and right positions. The user will input a single digit when he or she is ask to
enter a digit for each of the three positions. 

'''

from __future__ import print_function
import random

ERROR_VALUE = -777777 #This is known information that functions can use,
                      #therefore there should be a global constant

    
def welcomePlayer():
    ''' Welcomes the player to the Hit && Match Game \
        and tells the player to hit a key to start playing'''
    raw_input('Welcome to the Hit && Match Game \nhit any key to start playing... \n')
def farewellPlayer():
    ''' Tells the player to come back and play again after his or her try '''
    print('Come back and play again sometime \n')
def getRandomHouseDigits(): 
    ''' This function randomly generates three digits for the house for the left,
        middle, and right position'''
    leftPosition = random.randint(0, 9)
    middlePosition = random.randint(0, 9)
    rightPosition = random.randint(0, 9)
    return leftPosition, middlePosition, rightPosition
def getDigits():
    ''' Gets the digits for the left, middle, and right position from the player'''
    leftPosition = int(raw_input('Enter digit for left position: '))
    middlePosition = int(raw_input('Enter digit for middle position: '))
    rightPosition = int(raw_input('Enter digit for right position: '))
    return leftPosition, middlePosition, rightPosition
def determineScoreHit(left, middle, right, houseLeft, houseMiddle, houseRight):
    ''' Gets the score for Hits when the player's left, middle, and right position
        matches with the house's left, middle, and right position respectively. Then,
        it calculates the total number of hits'''
    if left == houseLeft:
        leftHit = 1
    else:
        leftHit = 0

    if middle == houseMiddle:
        middleHit = 1
    else:
        middleHit = 0

    if right == houseRight:
        rightHit = 1
    else:
        rightHit = 0
    totalHits = leftHit + middleHit + rightHit
    return totalHits
def determineScoreMatch(left, middle, right, houseLeft, houseMiddle, houseRight):
    ''' Gets the number of matches when the player's digits matches
        with the house's digits excluding the digit that matches in the same position. Then,
        it calculates the total number of matches'''
    if left == houseMiddle:
        matchOne = 1
    elif left == houseRight:
        matchOne = 1
    else:
        matchOne = 0

    if middle == houseLeft:
        matchTwo = 1
    elif middle == houseRight:
        matchTwo = 1
    else:
        matchTwo = 0

    if right == houseLeft:
        matchThree = 1
    elif right == houseMiddle:
        matchThree = 1
    else:
        matchThree = 0
    totalMatch = matchOne + matchTwo + matchThree
    return totalMatch
def displayHitsAndMatches(hits, matches):
    ''' Displays the number of hits and matches that occured '''
    if hits == 0:
        print('%i hits' % (hits))
    elif hits >= 2:
        print('%i hits' % (hits))
    else:
        print('%i hit' % (hits))

    if matches == 0:
        print('%i matches' % (matches))
    elif matches >= 2:
        print('%i matches' % (matches))
    else:
        print('%i match' % (matches))
def testAllDigits(houseLeft, houseMiddle, houseRight):
    ''' Checks if all three digits are the same. Kills program when all three digits are the same '''
    if houseLeft == houseMiddle == houseRight:
        print('We are sorry but the game has malfunctioned. \nEnding...')
        print('\nTraceback...\n...\nSystemExit: ', ERROR_VALUE)
        exit()
def testPairDigits(houseLeft, houseMiddle, houseRight):
    ''' Checks if any pair of digits are the same. Kills program when any pair of digits are the same.'''
    if houseLeft == houseMiddle or houseLeft == houseRight or houseRight == houseMiddle:
        print('We are sorry but the game has malfunctioned. \nEnding...')
        print('\nTraceback...\n...\nSystemExit: ', ERROR_VALUE)
        exit()   
def testPlayerGuesses(left, middle, right, houseLeft, houseMiddle, houseRight):
    ''' Checks if any two guesses are the same. If is the same, the game will end for that player. If not, hits and matches will display '''
    if (left == middle) or (left == right) or (middle == right):
        print('Sorry, that is an invalid try.')
    else:
        hits = determineScoreHit(left, middle, right, houseLeft, houseMiddle, houseRight)
        matches = determineScoreMatch(left, middle, right, houseLeft, houseMiddle, houseRight)
        displayHitsAndMatches(hits,matches)     
def playOneHitAndMatchGame():
    ''' Lets the user play the Hit && Match game for one try '''
    welcomePlayer()
    houseLeft, houseMiddle, houseRight = getRandomHouseDigits()
    testAllDigits(houseLeft, houseMiddle, houseRight)
    testPairDigits(houseLeft, houseMiddle, houseRight)
    left, middle, right = getDigits()
    testPlayerGuesses(left, middle, right, houseLeft, houseMiddle, houseRight)
    farewellPlayer()
def main():
    while True:
        playOneHitAndMatchGame()

if __name__ == '__main__':
    main()
    



