from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

decoder = {
    1: "X",
    2: "O"
}

class CustomGrid(GridLayout):
    move = True
    boardState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    winner = None

    def __init__(self, **kwargs):
        super(CustomGrid, self).__init__(**kwargs)

        # Define board speciffic settings       
        self.board = GridLayout()
        self.board.cols = 3
        self.board.boxesCount = 9
        self.board.boxes = []
        
        # Define main layout
        self.cols = 1

        # Upper element of main layout
        self.message = Label(text="Fuck c*nsor", font_size=50)

        # Lower element of main layout (the board)
        for boxIndex in range(0, self.board.boxesCount):
            self.board.boxes.append(Button(text="", font_size=30, id=str(boxIndex)))
        for box in self.board.boxes:
            box.bind(on_press=self.pressed)
            self.board.add_widget(box)

        # Add elements to main layout
        self.add_widget(self.message)
        self.add_widget(self.board)

    # yet to be optimized
    # This function checks the winner by creating sublists and counting 
    # occurences of items.
    def checkWin(self, rows):
        board = self.boardState
        # Check horizontal lines
        for i in range(0, rows):
            line = board[i*rows:i*rows + rows]
            if (line.count(1) == rows):
                return 1
            if (line.count(2) == rows):
                return 2

        # Check vertical lines
        for i in range(0, rows):
            line = board[i: rows**2: rows]
            if (line.count(1) == rows):
                return 1
            if (line.count(2) == rows):
                return 2
                
        # Check diagonals
        diagonal = board[0:rows**2:rows + 1]
        if (diagonal.count(1) == rows):
            return 1
        if (diagonal.count(2) == rows):
            return 2
        
        diagonal = board[rows - 1: rows**2: rows - 1]
        if (diagonal.count(1) == rows):
            return 1
        if (diagonal.count(2) == rows):
            return 2

    # This method is called when a button is clicked
    def pressed(self, instance):
        # Prohibit player from making a move if there is a winner
        if self.winner != None:
            return
        
        # If the box is still available (I know, will have to make this check from a single list)
        # Buttons with dynamic text - sounds like a good solution. Yet to be implemented in the
        # process of learning kivi templating.
        if instance.text == "":
            if self.move == True:
                self.board.boxes[int(instance.id)].text = "X"
                self.boardState[int(instance.id)] = 1
            else:
                self.board.boxes[int(instance.id)].text = "O"
                self.boardState[int(instance.id)] = 2
            
            self.move = not self.move
            
            self.winner = self.checkWin(3)
            if (self.winner != None):
                self.message.text = "The player " + decoder[self.winner] + " won!"

class TicTacToeApp(App):
    def build(self):
        return CustomGrid()

TicTacToeApp().run()