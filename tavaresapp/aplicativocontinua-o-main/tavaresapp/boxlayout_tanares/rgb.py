from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class MinhaApp(App):
    def build(self):
        Window.clearcolor = (255, 255, 0, 1)

        label = Label(text="Esta é uma tela em fundo amarelo", color=(0, 0, 1, 1))

        return label 
    
if __name__ == '__main__':
    MinhaApp().run()