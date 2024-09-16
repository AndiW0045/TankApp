from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout

from database_functions import get_tankentries, get_vehicles

class ViewTankEntries(Screen):
    def __init__(self, **kwargs):
        super(ViewTankEntries, self).__init__(**kwargs)
        # Fetch all entries from the database
        self.database_entries = get_tankentries()
        self.vehicles = get_vehicles()

        # Use FloatLayout to place widgets on top of each other
        self.layout = FloatLayout()

        # Background Image
        background = Image(source='images/tankeinträge.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)

        # Create a ScrollView for scrolling through the database entries
        self.scroll_view = ScrollView(size_hint=(1, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Create a GridLayout to contain the labels inside the ScrollView
        self.grid_layout = GridLayout(cols=1, padding=dp(10), spacing=dp(10), size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))

        self.scroll_view.add_widget(self.grid_layout)
        self.layout.add_widget(self.scroll_view)

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
        
        self.layout.add_widget(back_button)
        self.add_widget(self.layout)

    def on_pre_enter(self, *args):
        """Called just before entering the screen."""
        self.reload_entries()

    def reload_entries(self):
        """Clear old entries and load new ones from the database."""
        self.grid_layout.clear_widgets()

        self.database_entries = get_tankentries()
        self.vehicles = get_vehicles()

        # Add the title label
        title_label = Button(
            text="Registrierte Tankeinträge",
            font_size='28sp',
            size_hint_y=None,
            height=dp(50),
            bold=True,
            background_color=(0,0,0,0.8),
            color=(1, 1, 1, 1)  # White color
        )
        self.grid_layout.add_widget(title_label)
        
        vehicle_button = Button(
                    text="Id    -   Fahrzeug    -   Liter  -   Datum",
                    font_size='20sp',
                    size_hint_y=None,
                    height=dp(50),
                    bold=True,
                    background_color=(0,0,0,0.8),
                    color=(1, 1, 1, 1)  # White color
                )
        self.grid_layout.add_widget(vehicle_button)

        # Create labels for each database entry
        entries = []
        for i, entry in enumerate(self.database_entries):
            x = list(entry)
            x[1] = self.vehicles[x[1]-1][1]
            x = tuple(x)
            entries.append(x)
            
        for entry in entries:
            entry_label = Button(
                text=" - ".join([str(e) for e in entry]),
                font_size='20sp',
                size_hint_y=None,
                height=dp(40),
                background_color=(0,0,0,0.7),
                color=(1, 1, 1, 1)  # White color
            )
            self.grid_layout.add_widget(entry_label)

    def go_back(self, instance):
        self.manager.current = 'main'