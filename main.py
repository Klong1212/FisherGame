from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class FishGame(BoxLayout):
    image = "puppy.jpg"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class FishApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        button = Button(text='My first button')
        button1 = Button(text='My first button')
        layout.add_widget(button1)
        
        layout.add_widget(button)
        
        return FishGame()

if __name__ == '__main__':
    FishApp().run()
