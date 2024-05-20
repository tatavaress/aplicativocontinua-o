from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window 

Window.size = (350, 600)

kv = '''
MDFloatLayout:
    Card:
        md_bg_color: 1, 1, 1, 1
        elevation: 5
        size_hint:.85,.9
        pos_hint: {"center_x":.5, "center_y":.5}
        radius: [10]

    Image: 
        source: "logoimcverde.png"
        size_hint: .5, 0.5
        pos_hint: {"center_x":.5, "center_y":.78}
'''

class Card(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class LoginPage(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
if __name__ == "__main__":
    LoginPage().run()