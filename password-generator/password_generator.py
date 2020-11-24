from kivy.lang import Builder
#from kivy.uix.textinput import Clipboard
from kivymd.app import MDApp
from random import choice
from kivy.core.window import Window


Window.size = (305, 480)

class MainApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "Password Generator"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_file("pass_gen_kivy.kv")

    def create_password(self, user_pass_length):
        self.grab_char(int(user_pass_length))
        # function chooses a char, appends it to a string a number of times specified by user. returns final password string

    def grab_char(self, n):
        ascii_for_pass = "".join(chr(c) for c in range(33, 127))
        pass_string = ""
        for i in range(0, n):
            char = choice(ascii_for_pass)
            pass_string += char
        self.place_text(pass_string)


    def place_text(self, text_from_input):
        self.root.ids.password_output.text = text_from_input

if __name__ == "__main__":
    MainApp().run()

