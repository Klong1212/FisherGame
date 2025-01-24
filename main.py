from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty,BooleanProperty,StringProperty
from kivy.clock import Clock
from random import randint,choice
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget

class BagScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.back = False

class MainScreen(Screen):
    hi = NumericProperty(0)
    hi_game = NumericProperty(0)
    start = BooleanProperty(False)
    score = NumericProperty(0)
    fish_come = BooleanProperty(False)
    link = StringProperty('animation1.gif')
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.minigame, 1.0/60.0)
        self.ispress = False
        self.minigame_up = False
        self.rand_fish = [1,2,3,4,5,6,7,8,9,10]
        self.video = False
        self.bag = False
    def minigame(self, dt):
        if self.start:
            self.rand=randint(1,10)
            self.rand_fight=randint(1,50)
            self.fish = choice(self.rand_fish)
            if self.fish in [1,2,3,4,5]:
                self.fish = 5
            if self.hi > 0:
                self.hi -= 5
            if self.ispress and self.hi < 480:
                self.hi += 10
            if self.rand_fight==1:
                self.speed=randint(1,self.fish)
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
                self.link = 'fishpic/animation1.gif'
            if self.video:
                self.link = "animation2.gif"
                self.video = False
                
        
    def on_button_down(self):
        self.ispress = True
    def on_button_up(self):
        self.ispress =False
    def on_click(self):
        self.start = True
        self.video=True

class FishApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(BagScreen(name='bag_screen'))
        return sm

if __name__ == '__main__':
    FishApp().run()