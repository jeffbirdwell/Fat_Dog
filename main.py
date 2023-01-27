import kivy

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import GraphicException
from kivy.uix.layout import Layout
from kivy.graphics import Canvas





class Trivia(App):
    def build(self):
        #with self.canvas:
           # Color(1.,1.,0)
        self.window = GridLayout(orientation = 'tb-lr')
        self.window.cols = 1

        #self.window.size_hint = (0.5,0.5)
        #self.window.pos_hint = {"center_x":0.5, "center_y":0.75}
        self.label = Label(
                            text='How FAT is your dog?',
                            size_hint = (1,0.23),
                            font_size = 20,
                            color = '#3399FF')

        self.window.add_widget(self.label)
        self.button = Button(
                            text='Want to find out?\n     Click Here',
                            size_hint = (1,0.25),
                            font_size = 20,
                            color = '#FF0000')
        self.button.background_color = '#9C27B0'
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        self.pic = Image(
                        source='Jackson.png',
                        size_hint = (1,1),
                        #keep_ratio = False,
                        allow_stretch = True)
        self.pic.pos_hint = {"center_x":1.0, "center_y":1.0}
        self.window.add_widget(self.pic)

        return self.window


    def callback(self, event):
        self.label.text = 'REALLY REALLY FAT!!!'
        self.window.remove_widget(self.button)
        self.pic.source = 'fat.png'
        return

if __name__ == '__main__':
    Trivia().run()
