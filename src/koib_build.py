import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
kivy.require('1.9.0')
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from pandasgui import show
#CONNECTING TO HOSTED POSTGRES DATABASE___ WE MADE THIS WAY HARDER THAN IT NEEDED TO BE AND IT ATE UP WAY TOO MUCH TIME. BUT HEY IT WORKS NOW
engine = create_engine("postgresql://doadmin:a8kz5iiddjdx1fdm@db-postgresql-nyc3-35484-do-user-8902057-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require")
connection = engine.connect()
#PSYCOP2 connection
conn = psycopg2.connect(host="db-postgresql-nyc3-35484-do-user-8902057-0.b.db.ondigitalocean.com", database="defaultdb", user="doadmin", password="a8kz5iiddjdx1fdm", port="25060")

#GLOBAL LISTS FOR DROPDOWNS
global all_seasons
all_seasons = []
global myroster
myroster = []
#DEFINE DIFFERENT SCREENS
class FirstWindow(Screen):
#all button functionality for screen 2 found in functions below
#button functions are in order as they appear in GUI
    pass

class SecondWindow(Screen):
#all button functionality for screen 2 found in functions below
#button functions are in order as they appear in GUI
    def clear_input(self):#CLEAR USER INPUT
        self.ids.user_input.text = ""
    def clear_roster(self):#CLEAR ROSTER
        self.ids.player1.text = "PLAYER 1"
        self.ids.player2.text = "PLAYER 2"
        self.ids.player3.text = "PLAYER 3"
        self.ids.player4.text = "PLAYER 4"
        self.ids.player5.text = "PLAYER 5"
        myroster.clear() #this removes players from roster
    def add_to_roster(self):#THIS FN UPDATES myroster AND RENAMES LABEL TEXT IN GUI TO REFLECT THIS CHANGE
        chosen_player = str(self.ids.user_input.text)
        query = pd.read_sql_query("SELECT * FROM t20_21_pergame", conn)
        #query = pd.read_sql_query('SELECT * FROM "t20_21_pergame" WHERE "Player" LIKE '%LeBron%'', conn)
        #query = pd.read_sql_query("select "Player", "Tm", "PTS", "FG%", "3P%" from t20_21_pergame WHERE lower("Player") LIKE lower('%lebron%');", conn)
        #test = self.ids.user_input.text
        show(query)
        #print(query)
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('my.kv')

#MAIN CLASS
#my.kv file used for MyApp
class MyApp(App):
    def build(self):
        Window.clearcolor = (40/255.0,44/255.0,52/255.0,1)
        Window.maximize()
        return kv #kv references our my.kv file as see above

if __name__ == '__main__':
    MyApp().run()
