from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty,BooleanProperty,StringProperty
from kivy.clock import Clock
from random import randint,choice

class in_bag(FloatLayout):
    def __init__(self, **kwargs):
        super(in_bag, self).__init__(**kwargs)
        self.back = False
    def display(self):
        if self.back:
            return FishGame()
    def on_click_back(self):
        self.back = True
class FishGame(FloatLayout):
    hi = NumericProperty(0)
    hi_game = NumericProperty(0)
    start = BooleanProperty(False)
    score = NumericProperty(0)
    fish_come = BooleanProperty(False)
    link = StringProperty('fishpic/animation11.gif')
    def __init__(self, **kwargs):
        super(FishGame, self).__init__(**kwargs)
        Clock.schedule_interval(self.minigame, 1.0/60.0)
        self.ispress = False
        self.minigame_up = False
        self.rand_fish = [1,2,3,4,5,6,7]
        self.video = False
        self.bag = False
    def minigame(self, dt):
        if self.start:
            self.rand=randint(1,10)
            self.fish = choice(self.rand_fish)
            if self.hi > 0:
                self.hi -= 5
            if self.ispress and self.hi < 480:
                self.hi += 10
                
            if self.hi_game<=0:
                self.minigame_up = True
                self.speed=randint(1,self.fish)
            if self.hi_game>=480:
                self.minigame_up = False
                self.speed=randint(1,self.fish)
                
            if self.hi>self.hi_game and self.hi< self.hi_game+50 and self.rand==1:
                self.minigame_up=~self.minigame_up
                self.speed=randint(1,self.fish)
        
            if self.minigame_up:
                self.hi_game += self.speed
            if self.minigame_up==False:
                self.hi_game -= self.speed
            if self.hi>self.hi_game and self.hi< self.hi_game+50:
                self.score +=5
            if ~(self.hi>self.hi_game and self.hi< self.hi_game+50) and self.score > 0:
                self.score -=1
            if self.score >= 500:
                self.start = False
                self.score = 0
                self.hi = 0
                self.hi_game = 0
                self.link = 'fishpic/animation11.gif'
            if self.video:
                self.link = 'fishpic/animation12.gif'
                
                self.video = False
        
    def on_button_down(self):
        self.ispress = True
    def on_button_up(self):
        self.ispress =False
    def on_click(self):
        self.start = True
        self.video=True
    def build(self):
        print("11")
        return in_bag()
class FishApp(App):
    def build(self):  
        return FishGame()

if __name__ == '__main__':
    FishApp().run()