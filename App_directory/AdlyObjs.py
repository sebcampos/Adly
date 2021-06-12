#import kivy Objects/Classes to build our version of it
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Ellipse
from kivy.uix.image import Image


#Main Title
mainTitle = Label( 
    text = "[font=fonts/great-vibes/GreatVibes-Regular.otf]Adly[/font]",
    font_size = '100',
    pos_hint={'center_x': .2 , 'center_y': .9},
    #size_hint = (1, 1),
    markup = True
    )

#Navigation bar
navBar = BoxLayout(
    orientation = "horizontal",
    size_hint=(.8, .1),
    pos_hint={'center_x': .5, 'center_y': .1 }
    )

navBar.add_widget(
    Button(text="First")
    )

navBar.add_widget(
    Button(text="Second")
    )

navBar.add_widget(
    Button(text="Third")
    )

navBar.add_widget(
    Button(text="Fourth")
    )

#three dots
three_dots = Button(
    size_hint=(.05, .1),
    pos_hint={'center_x': .9 , 'center_y': .9},
    )
    
one_dot = Ellipse(
    angle_start = 0,
    angle_end = 360,
    size=(10,10)
)

three_dots.canvas.add(one_dot)
#img = Image(source="./imgs/test.png")