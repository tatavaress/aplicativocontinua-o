from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        layout_stack = StackLayout ()
        botao1 = Button(text='seila')
        botao2 = Button(text='não sabo')
        layout_stack.add_widget(botao1)
        layout_stack.add_widget(botao2)

        return layout_stack
    
if __name__ == '__main__':
    MinhaApp().run()
        