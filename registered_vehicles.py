from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout

from database_functions import get_vehicles

class ViewRegisteredVehicles(Screen):
    def __init__(self, **kwargs):
        super(ViewRegisteredVehicles, self).__init__(**kwargs)
        # Fetch all entries from the database
        self.database_entries = get_vehicles()

        # Use FloatLayout to place widgets on top of each other
        layout = FloatLayout()

        # Background Image
        background = Image(source='images/all_cars.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Create a ScrollView for scrolling through the database entries
        scroll_view = ScrollView(size_hint=(1, 0.7), pos_hint={'center_x': 0.5, 'center_y': 0.55})

        # Create a GridLayout to contain the labels inside the ScrollView
        self.grid_layout = GridLayout(cols=1, padding=dp(10), spacing=dp(10), size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))


        # Add the GridLayout to the ScrollView
        scroll_view.add_widget(self.grid_layout)

        # Add the ScrollView to the FloatLayout
        layout.add_widget(scroll_view)

        # Add a Back button to return to the main page
        back_button = Button(
            text='Back',
            font_size='20sp',
            size_hint=(None, None),
            size=(dp(100), dp(50)),
            pos_hint={'center_x': 0.5, 'y': 0.05},
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def on_pre_enter(self, *args):
        self.reload_entries()

    def reload_entries(self):
        self.grid_layout.clear_widgets()
        self.database_entries = get_vehicles()
        
        # Add the title label
        title_label = Button(
            text="Registrierte Fahrzeuge",
            font_size='28sp',
            size_hint_y=None,
            height=dp(50),
            bold=True,
            background_color=(0,0,0,0.8),
            color=(1, 1, 1, 1)  # White color
        )
        self.grid_layout.add_widget(title_label)

        # Create column description
        vehicle_button = Button(
                    text="Name    -   Km/Bh",
                    font_size='20sp',
                    size_hint_y=None,
                    height=dp(50),
                    bold=True,
                    background_color=(0,0,0,0.8),
                    color=(1, 1, 1, 1)  # White color
                )
        self.grid_layout.add_widget(vehicle_button)

        # Create labels for each database entry
        for entry in self.database_entries:
            if entry[5] == 'Traktor':
                text = " - ".join([str(entry[1]), str(entry[3])]) + "h"
            else:
                text = " - ".join([str(entry[1]), str(entry[2])]) + "km"

            entry_label = Button(
                text=text,
                font_size='20sp',
                size_hint_y=None,
                height=dp(40),
                background_color=(0,0,0,0.7),
                color=(1, 1, 1, 1)  # White color
            )
            self.grid_layout.add_widget(entry_label)

    def go_back(self, instance):
        self.manager.current = 'vehicles_page'