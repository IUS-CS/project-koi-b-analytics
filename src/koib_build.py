import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    #initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        #set columns
        self.cols = 1
        #creating a second GridLayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        # add widgets here
        self.top_grid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        #
        self.top_grid.add_widget(Label(text="Number: "))
        self.number = TextInput(multiline=False)
        self.top_grid.add_widget(self.number)
        #
        self.top_grid.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.top_grid.add_widget(self.email)
        # add the new topgrid to application
        self.add_widget(self.top_grid)


        #Button
        self.submit = Button(text="SUBMIT", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    #press fn
    def press(self, instance):
        name = self.name.text
        number = self.number.text
        email = self.email.text
        self.add_widget(Label(text=f'Hello {name}, is {number} your number and {email} your email?'))
        #clear input feilds
        self.name.text = ''
        self.number.text = ''
        self.email.text = ''
class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()
