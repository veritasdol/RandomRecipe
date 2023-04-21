from kivy.app import App
from kivy.app import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import *
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.config import Config
     
# 0 being off 1 being on as in true / false
# you can use 0 or 1 && True or False
Config.set('graphics', 'resizable', True)
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "600")

class Background(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.bg = Background()
        self.logo = Image(source='logo.png')
        self.logo.size_hint_x = 0.7
        self.logo.pos_hint = {'center_x': 0.5, 'y': 0.25}
        self.logo.opacity = 0
        self.ani=Animation(opacity=1, duration=2)
        self.add_widget(self.bg)
        self.add_widget(self.logo)
        Clock.schedule_once(self.main_animation, 1)
        

    def main_animation(self, dt):
        self.ani.start(self.logo)


class RandomRecipeApp(App):

    def build(self):
        self.icon = 'box.png'
        return MainScreen()


if __name__ == '__main__':
    RandomRecipeApp().run()

def p(dsd):
    print('sdfsdf')