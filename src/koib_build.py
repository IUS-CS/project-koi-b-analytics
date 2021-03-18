import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image
kivy.require('1.9.0')
from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
from kivy.core.window import Window





Builder.load_file('my.kv')

class MyLayout(Widget):
    pass
    #name = ObjectProperty(None)
    #email = ObjectProperty(None)
    #phone = ObjectProperty(None)
    #press fn
    #def press(self):
    #    name = self.name.text
    #    phone = self.phone.text
    #    email = self.email.text
        #self.add_widget(Label(text=f'Hello {name}, is {phone} your number and {email} your email?'))
    #    print(f'Hello {name}, is {phone} your number and {email} your email?')
    #    #clear input feilds
    #    self.name.text = ''
    #    self.phone.text = ''
    #    self.email.text = ''

#MAIN CLASS
#my.kv file used for MyApp
class MyApp(App):
    def build(self):
        Window.clearcolor = (71/255.0,75/255.0,79/255.0,1)
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
