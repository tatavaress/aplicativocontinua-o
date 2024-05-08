from kivy.app import App 
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        carousel = Carousel(direction='right', loop= True)

        imagens = ["mario.jpeg", "spider.jpeg", "gulk.jpeg"]
        for imagem in imagens:
            imagem_widget = AsyncImage(source=imagem)
            carousel.add_widget(imagem_widget)

        return carousel
    
if __name__ == '__main__':
    MinhaApp().run()
