#!/usr/local/Caskroom/miniconda/base/envs/adly_venv/bin/python
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(
            text = "Adly",
            size_hint = (.9, .9),
            pos_hint={'center_x': .5 , 'center_y': .5 }
            )

        return label

if __name__ == "__main__":
    app = MainApp()
    app.run()