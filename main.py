from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.clock import Clock
import time
class FishGame(FloatLayout):
    hi = NumericProperty(0)

    def __init__(self, **kwargs):
        super(FishGame, self).__init__(**kwargs)
        Clock.schedule_interval(self.update,0.1)

    def update(self, dt):
        if self.hi > 0:
            self.hi -= 1
    def on_button_click(self):
        print(f"Button clicked!")
        self.hi += 10

class FishApp(App):
    def build(self):  
        return FishGame()

if __name__ == '__main__':
    FishApp().run()