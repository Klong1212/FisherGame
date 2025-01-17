from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

class FishGame(FloatLayout):
    score = StringProperty("0")

    def __init__(self, **kwargs):
        super(FishGame, self).__init__(**kwargs)

    def on_button_click(self, instance):
        print(f"Button clicked!")
        self.score = str(int(self.score) + 1)

class FishApp(App):
    def build(self):  
        return FishGame()

if __name__ == '__main__':
    FishApp().run()