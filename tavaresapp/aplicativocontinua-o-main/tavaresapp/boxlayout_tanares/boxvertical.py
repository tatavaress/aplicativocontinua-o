from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 10])
        botao1 = Button(text='Oiee')
        botao2 = Button(text='Não')
        botao3 = Button(text='sim')
        layout.add_widget(botao1)
        layout.add_widget(botao2)
        layout.add_widget(botao3)
        return layout
    
MinhaApp().run()