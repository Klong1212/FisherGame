from kivy.app import App

from kivy.properties import NumericProperty,BooleanProperty,StringProperty
from kivy.clock import Clock
from random import randint,choice
from kivy.uix.screenmanager import Screen,ScreenManager

from kivy.core.audio import SoundLoader
class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
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
        self.sound_before=SoundLoader.load("pixel-song-21-72593.mp3")
        self.sound_fight=SoundLoader.load('pixel-song-3-72687.mp3')

    def play_sound_before(self):
        if self.sound_before :
            self.sound_before.loop = True
            if self.sound_before.state != 'play':
                self.sound_before.play()

    def stop_sound_before(self):
        if self.sound_before:
            self.sound_before.stop()

    def play_sound_fight(self):
        if self.sound_fight:
            self.sound_fight.play()

    def stop_sound_fight(self):
        if self.sound_fight:
            self.sound_fight.stop()
        
                
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
        elif self.fish in [j for j in range(51,71)]:
            self.speed_fish = 4
            self.fish_link=choice(self.fish_rare)
        elif self.fish in [k for k in range(71,96)]:
            self.speed_fish = 6
            self.fish_link=choice(self.fish_epic)
        elif self.fish in [f for f in range(96,101)]:
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
    text_input = StringProperty("None")
    def __init__(self, **kwargs):
        super(BagScreen, self).__init__(**kwargs)

    def update_fish_image(self, fish_links):
        if fish_links == "fishpic/Sprite-0004.jpg":
            self.fish_image_1 = "fishpic/Sprite-0004.jpg"
        elif fish_links == "fishpic/Sprite-0005.jpg":
            self.fish_image_2 = "fishpic/Sprite-0005.jpg"
        elif fish_links == "fishpic/Sprite-0006.jpg":
            self.fish_image_3 = "fishpic/Sprite-0006.jpg"
        elif fish_links == "fishpic/Sprite-0007.jpg":
            self.fish_image_4 = "fishpic/Sprite-0007.jpg"
        elif fish_links == "fishpic/Sprite-0008.jpg":
            self.fish_image_5 = "fishpic/Sprite-0008.jpg"
        elif fish_links == "fishpic/Sprite-0009.jpg":
            self.fish_image_6 = "fishpic/Sprite-0009.jpg"
        elif fish_links == "fishpic/Sprite-0010.jpg":
            self.fish_image_7 = "fishpic/Sprite-0010.jpg"
        elif fish_links == "fishpic/Sprite-00011.jpg":
            self.fish_image_8 = "fishpic/Sprite-00011.jpg"
        elif fish_links == "fishpic/Sprite-0012.jpg":
            self.fish_image_9 = "fishpic/Sprite-0012.jpg"
        elif fish_links == "fishpic/Sprite-0013.jpg":
            self.fish_image_10 = "fishpic/Sprite-0013.jpg"
        elif fish_links == "fishpic/Sprite-0014.jpg":
            self.fish_image_11 = "fishpic/Sprite-0014.jpg"
        elif fish_links == "fishpic/Sprite-0015.jpg":
            self.fish_image_12 = "fishpic/Sprite-0015.jpg"
        elif fish_links == "fishpic/Sprite-0016.jpg":
            self.fish_image_13 = "fishpic/Sprite-0016.jpg"
        elif fish_links == "fishpic/Sprite-0017.jpg":
            self.fish_image_14 = "fishpic/Sprite-0017.jpg"
        elif fish_links == "fishpic/Sprite-0018.jpg":
            self.fish_image_15 = "fishpic/Sprite-0018.jpg"
        elif fish_links == "fishpic/Sprite-0019.jpg":
            self.fish_image_16 = "fishpic/Sprite-0019.jpg"
        elif fish_links == "fishpic/Sprite-0020.jpg":
            self.fish_image_17 = "fishpic/Sprite-0020.jpg"
        elif fish_links == "fishpic/Sprite-0021.jpg":
            self.fish_image_18 = "fishpic/Sprite-0021.jpg"
        elif fish_links == "fishpic/Sprite-0022.jpg":
            self.fish_image_19 = "fishpic/Sprite-0022.jpg"
        elif fish_links == "fishpic/Sprite-0023.jpg":
            self.fish_image_20 = "fishpic/Sprite-0023.jpg"
        elif fish_links == "fishpic/Sprite-0024.jpg":
            self.fish_image_21 = "fishpic/Sprite-0024.jpg"
        elif fish_links == "fishpic/Sprite-0025.jpg":
            self.fish_image_22 = "fishpic/Sprite-0025.jpg"
        elif fish_links == "fishpic/Sprite-0026.jpg":
            self.fish_image_23 = "fishpic/Sprite-0026.jpg"
        elif fish_links == "fishpic/Sprite-0027.jpg":
            self.fish_image_24 = "fishpic/Sprite-0027.jpg"
        elif fish_links == "fishpic/Sprite-0028.jpg":
            self.fish_image_25 = "fishpic/Sprite-0028.jpg"
        elif fish_links == "fishpic/Sprite-0029.jpg":
            self.fish_image_26 = "fishpic/Sprite-0029.jpg"
        elif fish_links == "fishpic/Sprite-0030.jpg":
            self.fish_image_27 = "fishpic/Sprite-0030.jpg"
        elif self.fish_image_11 == "fishpic/Sprite-0014.jpg" and self.fish_image_13 == "fishpic/Sprite-0016.jpg" and self.fish_image_12 == "fishpic/Sprite-0015.jpg" and self.fish_image_14 == "fishpic/Sprite-0017.jpg" and self.fish_image_10 == "fishpic/Sprite-0013.jpg" and self.fish_image_9 == "fishpic/Sprite-0012.jpg" and self.fish_image_17 == "fishpic/Sprite-0020.jpg" and self.fish_image_18 == "fishpic/Sprite-0021.jpg":
            self.fish_image_28 = "fishpic/Sprite-0031.jpg"
        elif fish_links == "fishpic/Sprite-0032.jpg":
            self.fish_image_29 = "fishpic/Sprite-0032.jpg"
        elif fish_links == "fishpic/Sprite-0033.jpg":
            self.fish_image_30 = "fishpic/Sprite-0033.jpg"

    def text_inputs(self, number_id):
        if number_id == "pic1" and self.fish_image_1 == "fishpic/Sprite-0004.jpg":
            self.text_input = "Ice cream or mushroom, guess"
        elif number_id == "pic2" and self.fish_image_2 == "fishpic/Sprite-0005.jpg":
            self.text_input = "Santa's delivery car"
        elif number_id == "pic3" and self.fish_image_3 == "fishpic/Sprite-0006.jpg":
            self.text_input = "Smiling spider"
        elif number_id == "pic4" and self.fish_image_4 == "fishpic/Sprite-0007.jpg":
            self.text_input = "Nong Pun"
        elif number_id == "pic5" and self.fish_image_5 == "fishpic/Sprite-0008.jpg":
            self.text_input = "Poop"
        elif number_id == "pic6" and self.fish_image_6 == "fishpic/Sprite-0009.jpg":
            self.text_input = "Pacman"
        elif number_id == "pic7" and self.fish_image_7 == "fishpic/Sprite-0010.jpg":
            self.text_input = "Haunted tree"
        elif number_id == "pic8" and self.fish_image_8 == "fishpic/Sprite-00011.jpg":
            self.text_input = "Fishbone"
        elif number_id == "pic9" and self.fish_image_9 == "fishpic/Sprite-0012.jpg":
            self.text_input = "Six stars"
        elif number_id == "pic10" and self.fish_image_10 == "fishpic/Sprite-0013.jpg":
            self.text_input = "Five stars"
        elif number_id == "pic11" and self.fish_image_11 == "fishpic/Sprite-0014.jpg":
            self.text_input = "One star"
        elif number_id == "pic12" and self.fish_image_12 == "fishpic/Sprite-0015.jpg":
            self.text_input = "Three stars"
        elif number_id == "pic13" and self.fish_image_13 == "fishpic/Sprite-0016.jpg":
            self.text_input = "Two stars"
        elif number_id == "pic14" and self.fish_image_14 == "fishpic/Sprite-0017.jpg":
            self.text_input = "Four stars"
        elif number_id == "pic15" and self.fish_image_15 == "fishpic/Sprite-0018.jpg":
            self.text_input = "Dog boat"
        elif number_id == "pic16" and self.fish_image_16 == "fishpic/Sprite-0019.jpg":
            self.text_input = "Luffy's hat"
        elif number_id == "pic17" and self.fish_image_17 == "fishpic/Sprite-0020.jpg":
            self.text_input = "Seven stars"
        elif number_id == "pic18" and self.fish_image_18 == "fishpic/Sprite-0021.jpg":
            self.text_input = "Eight stars"
        elif number_id == "pic19" and self.fish_image_19 == "fishpic/Sprite-0022.jpg":
            self.text_input = "Real fish"
        elif number_id == "pic20" and self.fish_image_20 == "fishpic/Sprite-0023.jpg":
            self.text_input = "SCB easy"
        elif number_id == "pic21" and self.fish_image_21 == "fishpic/Sprite-0024.jpg":
            self.text_input = "Legendary tank"
        elif number_id == "pic22" and self.fish_image_22 == "fishpic/Sprite-0025.jpg":
            self.text_input = "Thai flag"
        elif number_id == "pic23" and self.fish_image_23 == "fishpic/Sprite-0026.jpg":
            self.text_input = "Heart star man"
        elif number_id == "pic24" and self.fish_image_24 == "fishpic/Sprite-0027.jpg":
            self.text_input = "Ordinary world"
        elif number_id == "pic25" and self.fish_image_25 == "fishpic/Sprite-0028.jpg":
            self.text_input = "Used paper"
        elif number_id == "pic26" and self.fish_image_26 == "fishpic/Sprite-0029.jpg":
            self.text_input = "Snake crawling to the waist"
        elif number_id == "pic27" and self.fish_image_27 == "fishpic/Sprite-0030.jpg":
            self.text_input = "Hi"
        elif number_id == "pic28" and self.fish_image_28 == "fishpic/Sprite-0031.jpg":
            self.text_input = "Evil from the dark web"
        elif number_id == "pic29" and self.fish_image_29 == "fishpic/Sprite-0032.jpg":
            self.text_input = "Badly designed bird"
        elif number_id == "pic30" and self.fish_image_30 == "fishpic/Sprite-0033.jpg":
            self.text_input = "Smiling ball"
         
    

class FishApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start_screen'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(BagScreen(name='bag_screen'))
        return sm

if __name__ == '__main__':
    FishApp().run()