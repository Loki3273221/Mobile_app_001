from kivymd.app import MDApp
from kivymd.uix.label import *


class MainApp(MDApp):
     def build(self):
        return MDLabel(text="Hello, Calculator", halign="center")


MainApp().run()