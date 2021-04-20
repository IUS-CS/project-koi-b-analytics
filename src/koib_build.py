"""Koib Build"""
"""This document initiates the connection with our digitalocean database and manages the kivy configuartion for the application window """

"""#Imports"""
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.animation import Animation, AnimationTransition
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
kivy.require('1.9.0')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
#Config.write()
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from pandasgui import show
import numpy as np
"""#CONNECTING TO HOSTED POSTGRES DATABASE___ WE MADE THIS WAY HARDER THAN IT NEEDED TO BE AND IT ATE UP WAY TOO MUCH TIME. BUT HEY IT WORKS NOW"""
engine = create_engine("postgresql://doadmin:a8kz5iiddjdx1fdm@db-postgresql-nyc3-35484-do-user-8902057-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require")
connection = engine.connect()
"""#PSYCOP2 connection"""
conn = psycopg2.connect(host="db-postgresql-nyc3-35484-do-user-8902057-0.b.db.ondigitalocean.com", database="defaultdb", user="doadmin", password="a8kz5iiddjdx1fdm", port="25060")

"""#GLOBAL LISTS FOR DROPDOWNS"""
global all_seasons
all_seasons = []
global myroster
myroster = []
"""#DEFINE DIFFERENT SCREENS"""
class FirstWindow(Screen):
"""#all button functionality for screen 2 found in functions below
#button functions are in order as they appear in GUI"""
    pass

class SecondWindow(Screen):
"""#all button functionality for screen 2 found in functions below
#button functions are in order as they appear in GUI"""
    def clear_input(self):"""#CLEAR USER INPUT"""
        self.ids.user_input.text = ""
    def srch_btn(self):"""#UPDATES PRELIMINARY STATS SO USER CAN DECIDE IF THEY WANT TO ADD THIS PLAYER"""
        chosen_player = str(self.ids.user_input.text)
        """#line below grabs stats for updating label"""
        query = pd.read_sql_query("select \"Player\", \"Tm\", \"Pos\", \"PTS\", \"FG%\" from t20_21_pergame WHERE lower(\"Player\") LIKE lower('%"+chosen_player+"%');", conn)
        """#This keeps the program from crashing if the query returns an empty dataframe (2 lines below)"""
        if query.empty == True:
            return
        """#creating variables that reference certain fields within the stats table"""
        global player_name
        player_name = query.loc[0].at["Player"]
        team_name = query.loc[0].at["Tm"]
        pos_name = query.loc[0].at["Pos"]
        pts_name = query.loc[0].at["PTS"]
        fg_name = query.loc[0].at["FG%"]
        print(query)
        """#updating preliminary stat labels based on user input and clicking of search button"""
        self.ids.stat_name.text = "NAME:\n" + player_name
        self.ids.stat_team.text = "TEAM:\n" + team_name
        self.ids.stat_pos.text = "POSITION:\n" + pos_name
        self.ids.stat_pts.text = "PPG:\n" + pts_name
        self.ids.stat_fg.text = "FG %:\n" + fg_name
    def clear_roster(self):#CLEAR ROSTER
        self.ids.player1.text = "PLAYER 1"
        self.ids.player2.text = "PLAYER 2"
        self.ids.player3.text = "PLAYER 3"
        self.ids.player4.text = "PLAYER 4"
        self.ids.player5.text = "PLAYER 5"
        myroster.clear() #this removes players from roster
    def add_to_roster(self):"""#THIS FN UPDATES myroster AND RENAMES LABEL TEXT IN GUI TO REFLECT THIS CHANGE"""
        self.ids.user_input.text = ""
        roster_length = len(myroster)
        if roster_length == 5:"""#this keeps the roster list at a max of 5 & adds the final 5 spot if it is the last player to be added"""
            self.ids.player5.text  = player_name
            myroster.append(player_name)
            return
        myroster.append(player_name)# adding players to myroster list
        roster_length = len(myroster)
        print(myroster)#testing purposes
        """#iterating through list to update labels"""
        for i in myroster:
            if roster_length == 1:
                self.ids.player1.text = player_name
            if roster_length == 2:
                self.ids.player2.text  = player_name
            if roster_length == 3:
                self.ids.player3.text  = player_name
            if roster_length == 4:
                self.ids.player4.text  = player_name
    def anal_roster(self):
        if len(myroster) < 5:#will only allow roster analysis with a full roster (5)
            return
        p1 = myroster[0]#these lines reference the players stored in myroster list
        p2 = myroster[1]#    |
        p3 = myroster[2]#   |
        p4 = myroster[3]#  |
        p5 = myroster[4]# V
        query = pd.read_sql_query("select * from t20_21_pergame WHERE \"Player\" = '"+p1+"' OR \"Player\" = '"+p2+"' OR \"Player\" = '"+p3+"' OR \"Player\" ='"+p4+"' OR \"Player\" ='"+p5+"';", conn)
        show(query)
    """#THIS HANDLES ALL BUTTON ANIMATION"""
    def animate_it(self, widget, *args):
        #this defines our button animation
        animate = Animation(duration=.1, opacity=.5)
        animate += Animation(duration=.1, opacity=1)
        #starting animation
        animate.start(widget)


class WindowManager(ScreenManager):
    pass# no necessary fns for first screen

kv = Builder.load_file('my.kv')# had to reduce this to a variable to return in myAPP

"""#MAIN CLASS"""
"""#my.kv file used for MyApp"""
class MyApp(App):

    def build(self):
        #sets title bar
        self.title = 'KOI-B ANALYTICS'
        #sets application background color
        Window.clearcolor = (40/255.0,44/255.0,52/255.0,1)
        return kv #kv references our my.kv file as see above-> line 118

if __name__ == '__main__':
    MyApp().run()
