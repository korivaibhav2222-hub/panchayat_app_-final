from kivy.app import App
from kivy.uix.label import Label

class PanchayatApp(App):
    def build(self):
        return Label(text="Panchayat App - Ban Gaya!")

PanchayatApp().run()
