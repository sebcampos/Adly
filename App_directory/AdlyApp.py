#!/usr/local/Caskroom/miniconda/base/envs/adly_venv/bin/python

#imported dependancies
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config


#Our Class object for Adly
from AdlyObjs import *

#Set out App to resizeable for Mobile functionality
Config.set("graphics", "resizable", True)




#Main App Object
class MainApp(App):
    def build(self):
        self.title = "Adly Beta Version"
        self.window = FloatLayout
        self.window.add_widget(mainTitle)
        return self.window

if __name__ == "__main__":
    MainApp().run()