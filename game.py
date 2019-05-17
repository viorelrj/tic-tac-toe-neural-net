from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CustomGrid(GridLayout):
    move = True
    boardState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, **kwargs):
        super(CustomGrid, self).__init__(**kwargs)
        
        self.board = GridLayout()
        self.board.cols = 3
        self.board.boxesCount = 9
        self.board.boxes = []
        for boxIndex in range(0, self.board.boxesCount):
            self.board.boxes.append(Button(text="", font_size=30, id=str(boxIndex)))
        for box in self.board.boxes:
            box.bind(on_press=self.pressed)
            self.board.add_widget(box)

        self.cols = 1
        self.add_widget(Label(text="The score"))
        self.add_widget(self.board)

    def pressed(self, instance):
        if instance.text == "":
            if self.move == True:
                self.board.boxes[int(instance.id)].text = "X"
                self.boardState[int(instance.id)] = 1
            else:
                self.board.boxes[int(instance.id)].text = "O"
                self.boardState[int(instance.id)] = 2
            self.move = not self.move
            print(self.boardState)

class TicTacToeApp(App):
    def build(self):
        return CustomGrid()

TicTacToeApp().run()