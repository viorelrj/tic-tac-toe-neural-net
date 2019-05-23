from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty

import os
import numpy as np
from progress.bar import Bar
from intelligence import Intelligence


def load_weights(name):
    exists = os.path.isfile(name + '.npy')
    if (exists):
        weights = np.load(name +'.npy')
    else:
        weights = np.random.rand(10, 27)
    return weights

# 0 - unset
# 1 - ai
# 2 - player

DECODER = {
    0: "",
    1: "X",
    2: "O"
}

class Board(GridLayout, EventDispatcher):
    state = ObjectProperty([0, 0, 0, 0, 0, 0, 0, 0, 0])
    winner = None
    turn = True
    
    def __init__(self, firstAi=False):
        super(Board, self).__init__()

        # Define board speciffic settings       
        self.board = GridLayout()
        self.board.cols = 3
        self.board.boxes = []
        
        # Define main layout
        self.cols = 1
        self.message = Label(text="X", font_size=50)

        # Lower element of main layout (the board)
        for boxIndex in range(0, len(self.state)):
            self.board.boxes.append(Button(text="", font_size=30, id=str(boxIndex)))
        for box in self.board.boxes:
            box.bind(on_press=self.pressed)
            self.board.add_widget(box)

        # Add elements to main layout
        self.add_widget(self.message)
        self.add_widget(self.board)
    
    def pressed(self, instance):
        self.makeMove(instance.id)
    

    def on_state(self, instance, value):
        if not self.turn:
            self.makeMove(ai.step(self.state))

        boxes = instance.children[0].children
        for i in range(0, len(boxes)):
            boxes[i].text = DECODER[self.state[8 - i]]

        self.winner = self.checkWin()
        if (self.winner != None):
            if self.winner == 0:
                self.message.text = "It's a tie!"
            else:
                self.message.text = "The player " + DECODER[self.winner] + " won!"
        

    def makeMove(self, id):
        if self.winner != None:
            return
        
        if self.turn:
            self.message.text = "O"
        else:
            self.message.text = "X"

        # Notify state change
        state = self.state[:]
        
        if state[int(id)] == 0:
            if (self.turn):
                state[int(id)] = 1
            else:
                state[int(id)] = 2
        
        self.turn = not self.turn
        self.state = state
        

    def checkWin(self):
        board = self.state

        for i in range(0, 3):
            if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != 0:
                return board[i * 3]
            if board[i] == board[i + 3] == board[i + 6] and board[i] != 0:
                return board[i]

        if board[0] == board[4] == board[8] and board[0] != 0:
            return board[0]
        if board[2] == board[4] == board[6] and board[2] != 0:
            return board[2]
        
        if not 0 in board:
            return 0
        else:
            return None

class TicTacToeApp(App):
    def build(self):
        return Board()

weights = load_weights('weights_rules')
ai = Intelligence(weights, .0005)

TicTacToeApp().run()