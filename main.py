from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home import HomePage
from new_fuel_entry import NewFuelEntry


class MyApp(App):
    def build(self):
        # Create a ScreenManager to manage the screens
        sm = ScreenManager()
        sm.add_widget(HomePage(name='main'))
        sm.add_widget(NewFuelEntry(name='form'))
        return sm

if __name__ == '__main__':
    MyApp().run()