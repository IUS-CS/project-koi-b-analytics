import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="Look a GUI", font_size=65)

if __name__ == '__main__':
    MyApp().run()
