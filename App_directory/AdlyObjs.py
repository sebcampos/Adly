#import kivy Objects/Classes to build our version of it
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation

#Main Title
class MainTitle(Label):
    def __init__(self, **kwargs):
        super(MainTitle, self).__init__(**kwargs)
        self.text = "[font=fonts/great-vibes/GreatVibes-Regular.otf]Adly[/font]"
        self.font_size = '100'
        self.pos_hint={'center_x': .2 , 'center_y': .9}
        self.markup = True

#Navigation bar
class AdlyNavBar(BoxLayout):
    def __init__(self, **kwargs):
        super(AdlyNavBar, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint=(.8, .1)
        self.pos_hint={'center_x': .5, 'center_y': .1 }
        self.buttons = ["Fourth", "Third", "Second", "First"]
        self.animation = Animation(
                size_hint=(1, 1),
                pos_hint={'center_x': .1, 'center_y': .5 },
                duration = .2
            )
        for i in reversed(self.buttons):
            self.add_widget(Button(text=i, on_press = lambda x: mainScreen.change_menu()))
    
    def reposition(self):
        if self.orientation != "vertical":
            self.orientation = "vertical"
            self.size_hint = (0,1)
            #self.size_hint=(1, 1)
            self.pos_hint={'center_x': 0, 'center_y': .5}
            for child, newval in list(zip(self.children, [f"Menu 2 {i.text}" for i in self.children])):
                child.text = newval
            anim = Animation(
                size_hint=(1, 1),
                pos_hint={'center_x': .1, 'center_y': .5 },
                duration = .2
            )
            anim.start(self)
            

        elif self.orientation == "vertical":
            self.orientation = "horizontal"
            self.size_hint=(.8, .1)
            self.pos_hint={'center_x': .5, 'center_y': .1 }
            for child, oldval in list(zip(self.children, self.buttons)):
                child.text = oldval


    

navBar = AdlyNavBar()


#Nav button
class AdlyNavButton(Button):
    def __init__(self, **kwargs):
        super(AdlyNavButton, self).__init__(**kwargs)
        self.size_hint=(.08, .1)
        self.pos_hint={'center_x': .9 , 'center_y': .9}
        self.background_normal = "./imgs/size_64px.png"
        self.on_press = lambda: navBar.reposition()
    
    
navButton = AdlyNavButton()


class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
    
    def change_menu(self):
        self.clear_widgets()
        self.add_widget(MainTitle())
        self.add_widget(navButton)


mainScreen = MainScreen()
