from kivy.app import App
from kivy.uxi.label import Label

class DemoApp(App):
  def build(self):
    return Label(
          text="Hello World"
          )
Demo=DemoApp()
Demo.run()
