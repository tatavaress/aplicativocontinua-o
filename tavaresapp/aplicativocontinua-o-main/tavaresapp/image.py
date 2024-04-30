from kivy.app import App 
from kivy.uix.image import Image 

class MinhaApp(App):
    def build(self):
        return Image(source='C:/Users/aluno.sesipaulista/Downloads/pablodyego.jpeg')
    
if __name__ == '__main__':
    MinhaApp().run()    