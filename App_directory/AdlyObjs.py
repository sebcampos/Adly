#import kivy Object to build our version of it
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


#AdlyLayout will inherit from the FloatLayout object and will be our main Layout
class AdlyLayout(FloatLayout):
    pass


#Main Title
mainTitle = Label( 
    text = "[font=fonts/great-vibes/GreatVibes-Regular.otf]Adly[/font]",
    font_size = '100',
    pos_hint={'center_x': .2 , 'center_y': .90 },
    size_hint = (.1, .1),
    markup = True,
    )
        