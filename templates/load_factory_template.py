#demonstrates reading kivy from factory method
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory


Builder.load_string("""
<Root@BoxLayout>:
    MDRaisedButton:
        text: "Button"
        on_release: print("Button Pressed")
""")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "App title goes here"
        super().__init__(**kwargs)

    def build(self):
        return Factory.Root()


if __name__ == "__main__":
    MainApp().run()

