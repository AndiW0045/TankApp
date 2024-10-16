from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle


class HomePage(Screen):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        # Use FloatLayout to place widgets on top of each other
        layout = FloatLayout()

        # Background Image
        background = Image(source='images/fuel_station.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        title_layout = BoxLayout(orientation='vertical')
        title_layout.size_hint = (1, None)
        title_layout.height = dp(120)
        title_layout.pos_hint = {'center_x': 0.5, 'y': 0.8}

        # Add a title label at the top
        title_label = Label(
            text="My TankApp",
            font_size='28sp',
            size_hint_y=None,
            height=dp(50),
            bold=True,
            color=(1, 1, 1, 1)  # White color
        )

        # Adding a semi-transparent background behind the title
        with title_label.canvas.before:
            Color(0, 0, 0, 0.8)  # Black with 50% transparency
            self.rect = Rectangle(size=title_label.size, pos=title_label.pos)
        title_label.bind(size=self.update_rect, pos=self.update_rect)

        title_layout.add_widget(title_label)

        # Create a BoxLayout for the title and buttons
        box_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=[dp(10), dp(10), dp(10), dp(10)])
        box_layout.size_hint = (1, None)
        box_layout.pos_hint = ()
        box_layout.height = dp(350)
        box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        """# Create the first button that navigates to the second screen
        fuel_entry_button = Button(
            text='Neuer Tankeintrag',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        fuel_entry_button.bind(on_press=self.go_to_form)
        box_layout.add_widget(fuel_entry_button)

        vehicle_button = Button(
            text='Fahrzeug Registrieren',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        vehicle_button.bind(on_press=self.go_to_vehicle_registry)
        box_layout.add_widget(vehicle_button)

        registered_v_button = Button(
            text='Alle Fahrzeuge',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        registered_v_button.bind(on_press=self.go_to_all_vehicles)
        box_layout.add_widget(registered_v_button)

        registered_te_button = Button(
            text='Alle Tankeinträge',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        registered_te_button.bind(on_press=self.go_to_all_tankentries)
        box_layout.add_widget(registered_te_button)"""

        vehicles = Button(
            text='Fahrzeuge',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        vehicles.bind(on_press=self.go_to_vehicles_page)
        box_layout.add_widget(vehicles)

        tank_entries = Button(
            text='Tankeinträge',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        tank_entries.bind(on_press=self.go_to_tankentries_page)
        box_layout.add_widget(tank_entries)

        summary_button = Button(
            text='Zusammenfassung',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        summary_button.bind(on_press=self.go_to_summary)
        box_layout.add_widget(summary_button)

        # Add the BoxLayout to the FloatLayout
        layout.add_widget(title_layout)
        layout.add_widget(box_layout)

        self.add_widget(layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_vehicles_page(self, instance):
        self.manager.current = 'vehicles_page'

    def go_to_tankentries_page(self, instance):
        self.manager.current = 'tankentries_page'

    def go_to_summary(self, instance):
        self.manager.current = 'tankentry_summary'
        
    """#def go_to_form(self, instance):
    #    self.manager.current = 'new_fuel_entry'

    #def go_to_vehicle_registry(self, instance):
    #    self.manager.current = 'vehicle_registry'

    def go_to_all_vehicles(self, instance):
        self.manager.current = 'all_vehicles'

    def go_to_all_tankentries(self, instance):
        self.manager.current = 'all_tankentries'"""
