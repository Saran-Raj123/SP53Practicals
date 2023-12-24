"""
CP1404/CP5632 Practical - Saranraj Saravanan
Box layout demo
"""


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemo(BoxLayout):
    def handle_greet(self):
        print("greet")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        print("clear")
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


class BoxLayoutDemoApp(App):
    def build(self):
        return BoxLayoutDemo()


if __name__ == '__main__':
    BoxLayoutDemoApp().run()

