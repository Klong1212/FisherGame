# https://github.com/Ghosteon/kivy-calculator
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class FishGame(BoxLayout):
    pass

class FishApp(App):
    def build(self):
        return FishGame()

if __name__ == '__main__':
    FishApp().run()
