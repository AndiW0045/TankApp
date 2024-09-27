from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from home import HomePage
from new_fuel_entry import NewFuelEntry
from vehicle_registry import VehicleRegistry
from registered_vehicles import ViewRegisteredVehicles
from registered_tankentries import ViewTankEntries
from tankentry_summary import TankEntrySummary

class MyApp(App):
    def build(self):
        # Create a ScreenManager to manage the screens
        sm = ScreenManager()
        sm.add_widget(HomePage(name='main'))
        sm.add_widget(NewFuelEntry(name='new_fuel_entry'))
        sm.add_widget(VehicleRegistry(name='vehicle_registry'))
        sm.add_widget(ViewRegisteredVehicles(name="all_vehicles"))
        sm.add_widget(ViewTankEntries(name="all_tankentries"))
        sm.add_widget(TankEntrySummary(name="tankentry_summary"))
        return sm

if __name__ == '__main__':
    MyApp().run()