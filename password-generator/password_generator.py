from kivy.lang import Builder
from kivy.uix.textinput import Clipboard
from kivymd.app import MDApp
#from random import choice
from kivy.core.window import Window


Window.size = (305, 480)

class MainApp(MDApp):
    how_many_numbers = 4
    def __init__(self, **kwargs):
        self.title = "Password Generator"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_file("pass_gen_kivy.kv")

    def place_text(self, text_from_input):
        self.root.ids.password_output.text = text_from_input

if __name__ == "__main__":
    MainApp().run()

