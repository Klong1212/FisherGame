from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.clock import Clock
from random import randint
class FishGame(FloatLayout):
    hi = NumericProperty(0)
    hi_game = NumericProperty(0)
    def __init__(self, **kwargs):
        super(FishGame, self).__init__(**kwargs)
        Clock.schedule_interval(self.update,1/60)
        self.ispress = False
        self.minigame_up = False
        self.speed=1
    def update(self, dt):
        if self.hi > 0:
            self.hi -= 2
        if self.ispress and self.hi < 480:
            self.hi += 10
        if self.hi_game==0:
            self.minigame_up = True
            self.speed=randint(1,5)
        if self.hi_game==480:
            self.minigame_up = False
            self.speed=randint(1,5)
        if self.minigame_up:
            self.hi_game += self.speed
        else:
            self.hi_game -= self.speed
        print(self.hi)
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