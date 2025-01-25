from kivy.app import App

from kivy.properties import NumericProperty,BooleanProperty,StringProperty 
from kivy.clock import Clock
from random import randint,choice
from kivy.uix.screenmanager import Screen,ScreenManager
import pygame
class StartScreen(Screen): #หน้าจอเริ่มต้น
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class MainScreen(Screen): # หน้าจอเล่น
    
    hi = NumericProperty(0) # ตัวเก็บค่าความสูงของผู้เล่น
    hi_game = NumericProperty(0) # ตัวเก็บค่าความสูงบล็อกปลา
    start = BooleanProperty(False) # เก็บค่าความจริง ของเกมว่าเริ่มหรือยัง
    score = NumericProperty(0) # เก็บค่าคะแนน
    link = StringProperty('animation1.gif') # เก็บค่าลิ้ง อนิเมชั่น
    fish_link= StringProperty() #เก็บลิ้งปลาที่สุ่มมได้
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.minigame, 1.0/60.0) #เรียกใช้ minigame ทุกๆ 1/60 วินาที
        self.ispress = False #เก็บค่าว่ากดปุ่มสู้อยู่ไหม ถ้ากดให้เป็น fail
        self.minigame_up = False #ให้ค่า บล็อกปลา ถ้า false ปลาจะลง ถ้า True จะขึ้น
        self.rand_fish = [n for n in range(1,101)] # สุ่มปลาจาก100ตัว
        self.video = False #เก็บค่าเปลี่ยนวิดีโอ
        self.fish_com=['fishpic/Sprite-0004.jpg','fishpic/Sprite-0005.jpg','fishpic/Sprite-0006.jpg','fishpic/Sprite-0007.jpg', # link common fish
                       'fishpic/Sprite-0008.jpg','fishpic/Sprite-0009.jpg','fishpic/Sprite-0010.jpg','fishpic/Sprite-00011.jpg',
                       'fishpic/Sprite-0012.jpg','fishpic/Sprite-0013.jpg','fishpic/Sprite-0014.jpg','fishpic/Sprite-0015.jpg',
                       ]
        self.fish_rare=['fishpic/Sprite-0019.jpg','fishpic/Sprite-0020.jpg','fishpic/Sprite-0021.jpg','fishpic/Sprite-0022.jpg',# link rare fish
                        'fishpic/Sprite-0023.jpg','fishpic/Sprite-0024.jpg','fishpic/Sprite-0025.jpg']
        self.fish_epic=['fishpic/Sprite-0016.jpg','fishpic/Sprite-0017.jpg','fishpic/Sprite-0018.jpg','fishpic/Sprite-0026.jpg',# link epic fish
                        'fishpic/Sprite-0027.jpg','fishpic/Sprite-0028.jpg','fishpic/Sprite-0029.jpg','fishpic/Sprite-0030.jpg']
        self.fish_legendary=['fishpic/Sprite-0032.jpg','fishpic/Sprite-0033.jpg']# link legendary fish
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)#ตัวเล่นเพลง
        self.sound_before = pygame.mixer.Sound("pixel-song-21-72593.mp3")# เลือกเพลง
        self.play_sound_before()#ใช้ฟังชั่นเล่นเพลง

    def play_sound_before(self):#ฟังชั่นเล่นเพลง
        if not pygame.mixer.get_busy():
            self.sound_before.set_volume(0.5)#ปรับเสียงเพลงดังครึ่งเดียว
            self.sound_before.play(loops=-1)#ลูป
    def minigame(self, dt):#ฟังชั่นเกม
        if self.start: #จะเริ่มเกมถ้ากดปุ่มสตาท
            self.rand=randint(1,20) #สุ่มเลข1-10
            self.rand_fight=randint(1,50)# สุ่มเลข1-50

            if self.hi > 0: #ถ้าไม่ขยับและมากกว่า0ให้ตำแหน่งผู้เล่นลดลง
                self.hi -= 5
            if self.ispress and self.hi < self.height*0.82: #ถ้ากดสู้อยู่แล้วตำแหน่งผู้เล่นน้อยกว่าจุดสูงสุดให้ตำแหน่งผู้เล่นขึ้น
                self.hi += 10
            if self.rand_fight==1: #ถ้าเป็น1หมายถึง มีโอกาศ1ใน550 ที่ปลาจะเปลี่ยนแปลงความเร็ว
                self.speed=randint(self.speed_fish//2,self.speed_fish)
            if self.hi_game<=0:#ถ้าตำแหน่งปลาอยู่จุดตำ่สุดให้เด้งขึ้น
                self.minigame_up = True
                self.speed=randint(self.speed_fish//2,self.speed_fish)
            if self.hi_game>=self.height*0.82-90:#ถ้าตำแหน่งปลาอยู่จุดสูงสุดให้เด้งลง
                self.minigame_up = False
                self.speed=randint(self.speed_fish//2,self.speed_fish)
            
            if self.hi>self.hi_game and self.hi< self.hi_game+100 and self.rand==1:# ถ้าอยู่ในช่องปลามีโอกาศ1ใน10 ที่ปลาจะเด้งกลับและเปลี่ยนความเร็ว
                self.minigame_up=not(self.minigame_up)
                self.speed=randint(self.speed_fish//2,self.speed_fish)
        
            if self.minigame_up:#ถ้าเป็นจริงปลาจะขึ้นด้วยความเร็วเท่ากับที่สุ่ม
                self.hi_game += self.speed
            if self.minigame_up==False:#ถ้าเป็นเท็จปลาจะลงด้วยความเร็วเท่ากับที่สุ่ม
                self.hi_game -= self.speed
            if self.hi>self.hi_game and self.hi< self.hi_game+100: #ถ้าอยู่ในตัวปลาจะได้คะแนน
                self.score +=5
            if not(self.hi>self.hi_game and self.hi< self.hi_game+100) and self.score > 0: # ถ้าไม่ได้อยู่ในตัวปลาคะแนนจะลดลง
                self.score -=1
            if self.score >= self.height*0.82: #ถ้าคะแนนถึง630จะหยุดเล่นรีเซ็ตทุกอย่างและเอาภาพปลาที่สุ่มได้ขึ้นมา
                self.start = False
                self.score = 0
                self.hi = 0
                self.hi_game = 0
                Clock.schedule_once(self.show_fish, 0)
                self.go_to_bag_screen() #เรียกใช้ฟังชั่นเก็บปลาใส่กระเป๋า
                self.link = 'animation1.gif'
            if self.video: #ถ้าตัวแปรวิดีโอเป็นจริงจะเปลี่ยนอนิเมชั่น ซึ่งจะเป็นจริงก็ต่อเมื่อกดปุ่ม start
                self.link = "animation2.gif"
                self.video = False
                
    def show_fish(self, dt):#ฟังชั่นโชว์ปลา
        self.link = self.fish_link
    def on_button_down(self):#ฟังชั่นกด
        self.ispress = True
    def on_button_up(self):#ฟังชั่นปล่อย
        self.ispress =False
    def on_click(self):#ฟังชั่นปุ่ม start เริ่มด้วยสุ่มปลาจากนั้นดูว่าปลาอยู่ในช่วงไหนจากนั้นสุ่มลิ้งปลาจากช่วงนั้น
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
        
    def go_to_bag_screen(self):#ฟังชันเก็บใส่กระเปล๋าโดยจะส่งself.link เข้าไปใน ฟังชั่น ของง class bagscreen
        app = App.get_running_app()
        bag_screen = app.root.get_screen('bag_screen')
        bag_screen.update_fish_image(self.fish_link)
class BagScreen(Screen): #ฟังชั่นกระเป่า
    fish_image_1 = StringProperty("fishpic/sonsai.jpg")#เก็บภาพทั้งหมดเอาไว้ 30ภาพ
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
    text_input = StringProperty("None")#เก็บภาพข้อความเอาไว้ (การอธิบายภาพ)
    def __init__(self, **kwargs):
        super(BagScreen, self).__init__(**kwargs)

    def update_fish_image(self, fish_links):#ฟังชั่นเปลี่ยนช่องนั้นๆให้เป็นภาพนั้นๆถ้าภาพของปลาที่สุ่มได้ตรงกัน
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
        elif (self.fish_image_11 == "fishpic/Sprite-0014.jpg" and self.fish_image_13 == "fishpic/Sprite-0016.jpg" 
              and self.fish_image_12 == "fishpic/Sprite-0015.jpg" and self.fish_image_14 == "fishpic/Sprite-0017.jpg" 
              and self.fish_image_10 == "fishpic/Sprite-0013.jpg" and self.fish_image_9 == "fishpic/Sprite-0012.jpg" 
              and self.fish_image_17 == "fishpic/Sprite-0020.jpg" and self.fish_image_18 == "fishpic/Sprite-0021.jpg"): #ถ้าภาพทั้งหมดเป็นจริงแล้วปลาตัวนี้จะโผล่
            self.fish_image_28 = "fishpic/Sprite-0031.jpg"
        elif fish_links == "fishpic/Sprite-0032.jpg":
            self.fish_image_29 = "fishpic/Sprite-0032.jpg"
        elif fish_links == "fishpic/Sprite-0033.jpg":
            self.fish_image_30 = "fishpic/Sprite-0033.jpg"

    def text_inputs(self, number_id):#ตัวเปลี่ยนคำอธิบายปลา
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
         
    

class FishApp(App):#class ของแอปใช่ screenmanager เพื่อเปลี่ยนหน้า
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start_screen'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(BagScreen(name='bag_screen'))
        return sm

if __name__ == '__main__':
    FishApp().run()