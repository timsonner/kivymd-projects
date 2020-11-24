#demonstrates reading kivy from external .kv file
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "App title goes here"
        super().__init__(**kwargs)

    def build(self):
        return Builder.load_file("kv_file.kv")


if __name__ == "__main__":
    MainApp().run()
