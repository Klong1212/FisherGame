from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.clock import Clock
class FishGame(FloatLayout):
    hi = NumericProperty(0)

    def __init__(self, **kwargs):
        super(FishGame, self).__init__(**kwargs)
        Clock.schedule_interval(self.update,0.1)
        self.ispress = False

    def update(self, dt):
        if self.hi > 0:
            self.hi -= 2
        if self.ispress:
            self.hi += 10
    def on_button_down(self):
        print(f"Button down!")
        self.ispress = True
    def on_button_up(self):
        print(f"Button up!")
        self.ispress =False
class FishApp(App):
    def build(self):  
        return FishGame()

if __name__ == '__main__':
    FishApp().run()