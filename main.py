from kivy.app import App
from kivy.app import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import *
from kivy.animation import Animation
from kivy.graphics.texture import Texture


class Background(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.bg = Background()
        self.logo = Image(source='logo.png')
        self.logo.size_hint_x = 0.4
        # self.logo.pos_hint = {'center_x': 0.5, 'y': 0}
        self.add_widget(self.bg)
        self.add_widget(self.logo)

    
class RandomRecipeApp(App):

    def build(self):
        # self.icon = 'box.png'
        return MainScreen()


if __name__ == '__main__':
    RandomRecipeApp().run()