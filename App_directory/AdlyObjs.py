#import kivy Objects/Classes to build our version of it
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


#Main Title
mainTitle = Label( 
    text = "[font=fonts/great-vibes/GreatVibes-Regular.otf]Adly[/font]",
    font_size = '200',
    pos_hint={'center_x': .2 , 'center_y': .90 },
    size_hint = (.1, .1),
    markup = True
    )
        