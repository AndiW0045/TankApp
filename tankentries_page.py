from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle


class TankEntriesPage(Screen):
    def __init__(self, **kwargs):
        super(TankEntriesPage, self).__init__(**kwargs)
        # Use FloatLayout to place widgets on top of each other
        layout = FloatLayout()

        # Background Image
        background = Image(source='images/tractor.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        title_layout = BoxLayout(orientation='vertical')
        title_layout.size_hint = (1, None)
        title_layout.height = dp(120)
        title_layout.pos_hint = {'center_x': 0.5, 'y': 0.8}

        # Add a title label at the top
        title_label = Label(
            text="Tankeinträge",
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
        box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.6}

        tankentry = Button(
            text='Neuer Tankeintrag',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        tankentry.bind(on_press=self.go_to_new_fuel_entry)
        box_layout.add_widget(tankentry)

        registered_tankentries = Button(
            text='Alle Tankeinträge',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        registered_tankentries.bind(on_press=self.go_to_all_tankentries)
        box_layout.add_widget(registered_tankentries)

        # Add the BoxLayout to the FloatLayout
        layout.add_widget(title_layout)
        layout.add_widget(box_layout)

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

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_new_fuel_entry(self, instance):
        self.manager.current = 'new_fuel_entry'

    def go_to_all_tankentries(self, instance):
        self.manager.current = 'all_tankentries'

    def go_back(self, instance):
        self.manager.current = 'main'