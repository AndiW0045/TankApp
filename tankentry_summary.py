from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

from database_functions import get_tankentries, get_vehicles

class TankEntrySummary(Screen):
    def __init__(self, **kwargs):
        super(TankEntrySummary, self).__init__(**kwargs)
        self.layout = FloatLayout()
        background = Image(source='images/tankeintraege.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.add_widget(background)

        self.title_layout = BoxLayout(orientation='vertical')
        self.title_layout.size_hint = (1, None)
        self.title_layout.height = dp(50)
        self.title_layout.pos_hint = {'center_x': 0.5, 'y': 0.8}

        title_label = Label(
            text="Zusammenfassung",
            font_size='28sp',
            size_hint_y=0.8,
            height=dp(50),
            bold=True,
            color=(1, 1, 1, 1)  # White color
        )
        with title_label.canvas.before:
            Color(0, 0, 0, 0.8)  # Black with 50% transparency
            self.rect = Rectangle(size=title_label.size, pos=title_label.pos)
        title_label.bind(size=self.update_rect, pos=self.update_rect)
        self.title_layout.add_widget(title_label)

        # Create a BoxLayout for the form fields and back button
        self.box_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=[dp(10), dp(10), dp(10), dp(10)])
        self.box_layout.size_hint = (1, None)
        self.box_layout.height = dp(300)  # Adjusted height to accommodate checkboxes
        self.box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}


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
        
        self.layout.add_widget(self.title_layout)
        self.layout.add_widget(self.box_layout)
        self.layout.add_widget(back_button)
        self.add_widget(self.layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_pre_enter(self, *args):
        """Called just before entering the screen."""
        self.reload_entries()

    def reload_entries(self):
        """Clear old entries and load new ones from the database."""
        self.box_layout.clear_widgets()
        self.vehicles = get_vehicles()
        self.tankentries = get_tankentries()

        liter_sum = 0
        for entry in self.tankentries:
            liter_sum += entry[2]
            

        liter_number = Button(
                    text=f"Gesamtverbrauch    -    {liter_sum}",
                    font_size='20sp',
                    size_hint_y=None,
                    height=dp(50),
                    bold=True,
                    background_color=(0,0,0,0.8),
                    color=(1, 1, 1, 1)  # White color
                )
        self.box_layout.add_widget(liter_number)

    def go_back(self, instance):
        self.manager.current = 'main'