from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source='https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2024/04/homem-aranha-tobey-tom-andrew.jpg?w=1220&h=674&crop=1')
   
    
if __name__ == '__main__':
    MinhaApp().run()    