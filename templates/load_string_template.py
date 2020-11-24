#demonstrates reading kivy from load_string method of Builder
from kivy.lang import Builder
from kivymd.app import MDApp


root_kv = """
BoxLayout:
    MDRaisedButton:
        text: "Button"
        on_release: print("Button Pressed")
"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "App title goes here"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)


if __name__ == "__main__":
    MainApp().run()