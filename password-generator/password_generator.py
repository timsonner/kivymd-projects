
from kivy.lang import Builder
#from kivy.uix.textinput import Clipboard
from kivymd.app import MDApp
from random import choice
from kivy.core.window import Window


Window.size = (305, 480)

class MainApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "Password Generator"
        #self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_file("pass_gen_kivy.kv")    #load this kivy file


    def generate_password(self, n):
        self.root.ids.password_output.text = ""
        ascii_for_pass = "".join(chr(c) for c in range(33, 127))    #range of ascii for the choice function
        pass_string = ""    #empty string
        while len(n.strip()) == 0:  #if MDtextfield is blank, return control
            self.root.ids.text_field_input.error = True
            return

        self.root.ids.text_field_input.error = False
        n = int(n)  #must convert string to int
        for i in range(0, n):
            character = choice(ascii_for_pass)  #choose a character in range of ascii chars
            pass_string += character    #add char to string
            self.root.ids.password_output.text = pass_string    #place text in MDlabel


if __name__ == "__main__":
    MainApp().run()

