from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty,BooleanProperty,StringProperty
from kivy.clock import Clock
from random import randint,choice
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget

class MainScreen(Screen):
    hi = NumericProperty(0)
    hi_game = NumericProperty(0)
    start = BooleanProperty(False)
    score = NumericProperty(0)
    fish_come = BooleanProperty(False)
    link = StringProperty('animation1.gif')
    fish_link= StringProperty()
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.minigame, 1.0/60.0)
        self.ispress = False
        self.minigame_up = False
        self.rand_fish = [n for n in range(1,101)]
        self.video = False
        self.fish_com=['fishpic/Sprite-0004.jpg','fishpic/Sprite-0005.jpg','fishpic/Sprite-0006.jpg','fishpic/Sprite-0007.jpg',
                       'fishpic/Sprite-0008.jpg','fishpic/Sprite-0009.jpg','fishpic/Sprite-0010.jpg','fishpic/Sprite-00011.jpg',
                       'fishpic/Sprite-0012.jpg','fishpic/Sprite-0013.jpg','fishpic/Sprite-0014.jpg','fishpic/Sprite-0015.jpg',
                       ]
        self.fish_rare=['fishpic/Sprite-0019.jpg','fishpic/Sprite-0020.jpg','fishpic/Sprite-0021.jpg','fishpic/Sprite-0022.jpg',
                        'fishpic/Sprite-0023.jpg','fishpic/Sprite-0024.jpg','fishpic/Sprite-0025.jpg']
        self.fish_epic=['fishpic/Sprite-0016.jpg','fishpic/Sprite-0017.jpg','fishpic/Sprite-0018.jpg','fishpic/Sprite-0026.jpg',
                        'fishpic/Sprite-0027.jpg','fishpic/Sprite-0028.jpg','fishpic/Sprite-0029.jpg','fishpic/Sprite-0030.jpg']
        self.fish_legendary=['fishpic/Sprite-0031.jpg','fishpic/Sprite-0032.jpg','fishpic/Sprite-0033.jpg']
    def minigame(self, dt):
        if self.start:
            self.rand=randint(1,10)
            self.rand_fight=randint(1,50)

            if self.hi > 0:
                self.hi -= 5
            if self.ispress and self.hi < 480:
                self.hi += 10
            if self.rand_fight==1:
                self.speed=randint(self.speed_fish//2,self.speed_fish)
            if self.hi_game<=0:
                self.minigame_up = True
                self.speed=randint(self.speed_fish//2,self.speed_fish)
            if self.hi_game>=480:
                self.minigame_up = False
                self.speed=randint(self.speed_fish//2,self.speed_fish)
            
            if self.hi>self.hi_game and self.hi< self.hi_game+50 and self.rand==1:
                self.minigame_up=not(self.minigame_up)
                self.speed=randint(self.speed_fish//2,self.speed_fish)
        
            if self.minigame_up:
                self.hi_game += self.speed
            if self.minigame_up==False:
                self.hi_game -= self.speed
            if self.hi>self.hi_game and self.hi< self.hi_game+50:
                self.score +=5
            if not(self.hi>self.hi_game and self.hi< self.hi_game+50) and self.score > 0:
                self.score -=1
            if self.score >= 500:
                self.start = False
                self.score = 0
                self.hi = 0
                self.hi_game = 0
                Clock.schedule_once(self.show_fish, 0)
                self.go_to_bag_screen()
                self.link = 'animation1.gif'
            if self.video:
                self.link = "animation2.gif"
                self.video = False
                
    def show_fish(self, dt):
        self.link = self.fish_link
    def on_button_down(self):
        self.ispress = True
    def on_button_up(self):
        self.ispress =False
    def on_click(self):
        self.fish = choice(self.rand_fish)
        if self.fish in [i for i in range(1,51)]:
            self.speed_fish = 2
            self.fish_link=choice(self.fish_com)
        elif self.fish in [i for i in range(51,71)]:
            self.speed_fish = 4
            self.fish_link=choice(self.fish_rare)
        elif self.fish in [i for i in range(71,96)]:
            self.speed_fish = 6
            self.fish_link=choice(self.fish_epic)
        elif self.fish in [i for i in range(96,101)]:
            self.speed_fish = 8
            self.fish_link=choice(self.fish_legendary)
        self.link = 'animation1.gif'
        
        self.start = True
        self.video=True
    def go_to_bag_screen(self):
        app = App.get_running_app()
        bag_screen = app.root.get_screen('bag_screen')
        bag_screen.update_fish_image(self.fish_link)
class BagScreen(Screen):
    fish_image_1 = StringProperty("fishpic/sonsai.jpg")
    fish_image_2 = StringProperty("fishpic/sonsai.jpg")
    fish_image_3 = StringProperty("fishpic/sonsai.jpg")
    fish_image_4 = StringProperty("fishpic/sonsai.jpg")
    fish_image_5 = StringProperty("fishpic/sonsai.jpg")
    fish_image_6 = StringProperty("fishpic/sonsai.jpg")
    fish_image_7 = StringProperty("fishpic/sonsai.jpg")
    fish_image_8 = StringProperty("fishpic/sonsai.jpg")
    fish_image_9 = StringProperty("fishpic/sonsai.jpg")
    fish_image_10 = StringProperty("fishpic/sonsai.jpg")
    fish_image_11 = StringProperty("fishpic/sonsai.jpg")
    fish_image_12 = StringProperty("fishpic/sonsai.jpg")
    fish_image_13 = StringProperty("fishpic/sonsai.jpg")
    fish_image_14 = StringProperty("fishpic/sonsai.jpg")
    fish_image_15 = StringProperty("fishpic/sonsai.jpg")
    fish_image_16 = StringProperty("fishpic/sonsai.jpg")
    fish_image_17 = StringProperty("fishpic/sonsai.jpg")
    fish_image_18 = StringProperty("fishpic/sonsai.jpg")
    fish_image_19 = StringProperty("fishpic/sonsai.jpg")
    fish_image_20 = StringProperty("fishpic/sonsai.jpg")
    fish_image_21 = StringProperty("fishpic/sonsai.jpg")
    fish_image_22 = StringProperty("fishpic/sonsai.jpg")
    fish_image_23 = StringProperty("fishpic/sonsai.jpg")
    fish_image_24 = StringProperty("fishpic/sonsai.jpg")
    fish_image_25 = StringProperty("fishpic/sonsai.jpg")
    fish_image_26 = StringProperty("fishpic/sonsai.jpg")
    fish_image_27 = StringProperty("fishpic/sonsai.jpg")
    fish_image_28 = StringProperty("fishpic/sonsai.jpg")
    fish_image_29 = StringProperty("fishpic/sonsai.jpg")
    fish_image_30 = StringProperty("fishpic/sonsai.jpg")
    def __init__(self, **kwargs):
        super(BagScreen, self).__init__(**kwargs)

    def update_fish_image(self, fish_links):
        self.fish_image = fish_links
        self.update_button_image()
        

class FishApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(BagScreen(name='bag_screen'))
        return sm

if __name__ == '__main__':
    FishApp().run()