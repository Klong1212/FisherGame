from kivy.uix.videoplayer import VideoPlayer
from kivy.app import App

class Vd(App):
    def build(self):
        vd = VideoPlayer(source='animation11.mp4', state='play',options={'eos': 'loop'})
        return vd
if __name__ == '__main__':
    Vd().run()