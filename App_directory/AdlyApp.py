#!/usr/local/Caskroom/miniconda/base/envs/adly_venv/bin/python

#imported dependancies
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config


#Our objects for Adly
from AdlyObjs import *

#Set out App to resizeable for Mobile functionality
Config.set("graphics", "resizable", True)



#Main App Object
class MainApp(App):
    #build function is conventional way to build the app
    def build(self):
        #setting the title for the window
        self.title = "Adly Beta Version"
        
        #setting the app window attribute to a float layout using the FloatLayout() class
        self.window = FloatLayout()
        
        #adding mainTitle object to the app window 
        self.window.add_widget(mainTitle)
        
        #adding navBar object to the app window 
        self.window.add_widget(navBar)
        
        self.window.add_widget(three_dots)
        
        #returning the window will return the app
        return self.window


if __name__ == "__main__":
    MainApp().run()