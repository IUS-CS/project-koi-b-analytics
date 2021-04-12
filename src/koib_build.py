import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image
#from kivy.uix.dropdown import DropDown
#from kivy.base import runTouchApp
kivy.require('1.9.0')
from kivy.config import Config
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
from kivy.core.window import Window
#import psycopg2
from sqlalchemy import create_engine
engine = create_engine("postgresql://doadmin:show-password@db-postgresql-nyc3-35484-do-user-8902057-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require")




Builder.load_file('my.kv')

class MyLayout(Widget):
    def press(self):
        self.ids.buildR.outline_color = utils.get_color_from_hex('#86c232')

#MAIN CLASS
#my.kv file used for MyApp
class MyApp(App):
    def build(self):
        Window.clearcolor = (40/255.0,44/255.0,52/255.0,1)
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
