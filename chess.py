import pyautogui
import webbrowser
import time
import os

acceptableMoves = [
    'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
    'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
    'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
    'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
    'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
    'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
    ]

boardBottomLeft = [490, 1108]
boardTopRight = [1393, 202]
boardDimensions = [boardTopRight[0] - boardBottomLeft[0], boardTopRight[1] - boardBottomLeft[1]]

letterCoordinate = {
    'a': boardBottomLeft[0] + 1 * boardDimensions[0]/16,
    'b': boardBottomLeft[0] + 3 * boardDimensions[0]/16,
    'c': boardBottomLeft[0] + 5 * boardDimensions[0]/16,
    'd': boardBottomLeft[0] + 7 * boardDimensions[0]/16,
    'e': boardBottomLeft[0] + 9 * boardDimensions[0]/16,
    'f': boardBottomLeft[0] + 11 * boardDimensions[0]/16,
    'g': boardBottomLeft[0] + 13 * boardDimensions[0]/16,
    'h': boardBottomLeft[0] + 15 * boardDimensions[0]/16,
    }

rowCoordinate = {
    '1': boardBottomLeft[1] + 1 * boardDimensions[1]/16,
    '2': boardBottomLeft[1] + 3 * boardDimensions[1]/16,
    '3': boardBottomLeft[1] + 5 * boardDimensions[1]/16,
    '4': boardBottomLeft[1] + 7 * boardDimensions[1]/16,
    '5': boardBottomLeft[1] + 9 * boardDimensions[1]/16,
    '6': boardBottomLeft[1] + 11 * boardDimensions[1]/16,
    '7': boardBottomLeft[1] + 13 * boardDimensions[1]/16,
    '8': boardBottomLeft[1] + 15 * boardDimensions[1]/16,
}

squareCoordinates = {
    'a1': [letterCoordinate['a'], rowCoordinate['1']],
    'a2': [letterCoordinate['a'], rowCoordinate['2']],
    'a3': [letterCoordinate['a'], rowCoordinate['3']],
    'a4': [letterCoordinate['a'], rowCoordinate['4']],
    'a5': [letterCoordinate['a'], rowCoordinate['5']],
    'a6': [letterCoordinate['a'], rowCoordinate['6']],
    'a7': [letterCoordinate['a'], rowCoordinate['7']],
    'a8': [letterCoordinate['a'], rowCoordinate['8']],

    'b1': [letterCoordinate['b'], rowCoordinate['1']],
    'b2': [letterCoordinate['b'], rowCoordinate['2']],
    'b3': [letterCoordinate['b'], rowCoordinate['3']],
    'b4': [letterCoordinate['b'], rowCoordinate['4']],
    'b5': [letterCoordinate['b'], rowCoordinate['5']],
    'b6': [letterCoordinate['b'], rowCoordinate['6']],
    'b7': [letterCoordinate['b'], rowCoordinate['7']],
    'b8': [letterCoordinate['b'], rowCoordinate['8']],

    'c1': [letterCoordinate['c'], rowCoordinate['1']],
    'c2': [letterCoordinate['c'], rowCoordinate['2']],
    'c3': [letterCoordinate['c'], rowCoordinate['3']],
    'c4': [letterCoordinate['c'], rowCoordinate['4']],
    'c5': [letterCoordinate['c'], rowCoordinate['5']],
    'c6': [letterCoordinate['c'], rowCoordinate['6']],
    'c7': [letterCoordinate['c'], rowCoordinate['7']],
    'c8': [letterCoordinate['c'], rowCoordinate['8']],

    'd1': [letterCoordinate['d'], rowCoordinate['1']],
    'd2': [letterCoordinate['d'], rowCoordinate['2']],
    'd3': [letterCoordinate['d'], rowCoordinate['3']],
    'd4': [letterCoordinate['d'], rowCoordinate['4']],
    'd5': [letterCoordinate['d'], rowCoordinate['5']],
    'd6': [letterCoordinate['d'], rowCoordinate['6']],
    'd7': [letterCoordinate['d'], rowCoordinate['7']],
    'd8': [letterCoordinate['d'], rowCoordinate['8']],

    'e1': [letterCoordinate['e'], rowCoordinate['1']],
    'e2': [letterCoordinate['e'], rowCoordinate['2']],
    'e3': [letterCoordinate['e'], rowCoordinate['3']],
    'e4': [letterCoordinate['e'], rowCoordinate['4']],
    'e5': [letterCoordinate['e'], rowCoordinate['5']],
    'e6': [letterCoordinate['e'], rowCoordinate['6']],
    'e7': [letterCoordinate['e'], rowCoordinate['7']],
    'e8': [letterCoordinate['e'], rowCoordinate['8']],

    'f1': [letterCoordinate['f'], rowCoordinate['1']],
    'f2': [letterCoordinate['f'], rowCoordinate['2']],
    'f3': [letterCoordinate['f'], rowCoordinate['3']],
    'f4': [letterCoordinate['f'], rowCoordinate['4']],
    'f5': [letterCoordinate['f'], rowCoordinate['5']],
    'f6': [letterCoordinate['f'], rowCoordinate['6']],
    'f7': [letterCoordinate['f'], rowCoordinate['7']],
    'f8': [letterCoordinate['f'], rowCoordinate['8']],

    'g1': [letterCoordinate['g'], rowCoordinate['1']],
    'g2': [letterCoordinate['g'], rowCoordinate['2']],
    'g3': [letterCoordinate['g'], rowCoordinate['3']],
    'g4': [letterCoordinate['g'], rowCoordinate['4']],
    'g5': [letterCoordinate['g'], rowCoordinate['5']],
    'g6': [letterCoordinate['g'], rowCoordinate['6']],
    'g7': [letterCoordinate['g'], rowCoordinate['7']],
    'g8': [letterCoordinate['g'], rowCoordinate['8']],

    'h1': [letterCoordinate['h'], rowCoordinate['1']],
    'h2': [letterCoordinate['h'], rowCoordinate['2']],
    'h3': [letterCoordinate['h'], rowCoordinate['3']],
    'h4': [letterCoordinate['h'], rowCoordinate['4']],
    'h5': [letterCoordinate['h'], rowCoordinate['5']],
    'h6': [letterCoordinate['h'], rowCoordinate['6']],
    'h7': [letterCoordinate['h'], rowCoordinate['7']],
    'h8': [letterCoordinate['h'], rowCoordinate['8']],
}

# Opens chess.com homepage.
url = 'https://www.chess.com/home'
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
webbrowser.get(chrome_path).open(url)

# Lets page load before clicking on contents.
time.sleep(2)

# Clicks on "New Game" button.
# Only works on 2240 x 1260 resolution, will eventually rewrite
# with OpenCV to visually locate button on any screen.

pyautogui.click(755, 222)
time.sleep(2)

# Clicks on second "New Game" button.
pyautogui.click(1612, 169)
time.sleep(2)

# Clicks on "Play" button to start game.
pyautogui.click(1675, 322)

continueFlag = True
while continueFlag:

    # Re-opens Terminal to enter move.
    pyautogui.hotkey("command", "space")
    pyautogui.typewrite("t")
    pyautogui.press("enter")

    # Move entry
    move1 = input("Enter the position of the piece you would look to move: ")
    move2 = input("Enter the position where you would like to move the piece: ")
    if move1 == "stop":
        continueFlag = False
    elif move1 in acceptableMoves and move2 in acceptableMoves:
        # First click moves you from Terminal to Chrome, second click selects the piece.
        pyautogui.click(squareCoordinates[move1])       
        pyautogui.click(squareCoordinates[move1])
        time.sleep(1)
        pyautogui.click(squareCoordinates[move2])
    else:
        print("Invalid input. Try again.")
        
