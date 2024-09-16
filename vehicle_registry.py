from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup

from database_functions import register_vehicle

class VehicleRegistry(Screen):
    def __init__(self, **kwargs):
        super(VehicleRegistry, self).__init__(**kwargs)
        # Use FloatLayout to place widgets on top of each other
        layout = FloatLayout()

        # Background Image
        background = Image(source='images/car2.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Create a BoxLayout for the form fields and back button
        box_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=[dp(10), dp(10), dp(10), dp(10)])
        box_layout.size_hint = (1, None)
        box_layout.height = dp(300)  # Adjusted height to accommodate checkboxes
        box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Add a title label at the top
        title_label = Label(
            text="Register New Vehicle",
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

        box_layout.add_widget(title_label)

        # Add checkboxes for vehicle type
        checkbox_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        checkbox_layout.size_hint = (None, None)  # Disable size hints to allow explicit sizing
        checkbox_layout.pos_hint = {'center_x': 0.4}  # Center horizontally

        self.car_checkbox = CheckBox(group='vehicle', size_hint=(None, None), size=(30, 30))
        self.car_checkbox.bind(active=self.update_km_label)
        car_label = Label(text='Auto', font_size='20sp', height=dp(25),bold=True, color=(1, 1, 1, 1), size_hint=(None, None), size=(80, 30), valign='middle')

        self.tractor_checkbox = CheckBox(group='vehicle', size_hint=(None, None), size=(30, 30))
        self.tractor_checkbox.bind(active=self.update_km_label)
        tractor_label = Label(text='Traktor', font_size='20sp', height=dp(25),bold=True, color=(1, 1, 1, 1), size_hint=(None, None), size=(80, 30), valign='middle')

        checkbox_layout.add_widget(self.car_checkbox)
        checkbox_layout.add_widget(car_label)
        checkbox_layout.add_widget(self.tractor_checkbox)
        checkbox_layout.add_widget(tractor_label)

        box_layout.add_widget(checkbox_layout)

        self.name_var = None
        # Create three text fields
        name = Label(
            text="Name",
            font_size='20sp',
            size_hint_y=None,
            height=dp(25),
            bold=True,
            color=(1, 1, 1, 1)  # White color
        )
        self.name_var = name
        self.name_input = TextInput(size_hint_y=None, height=dp(40))

        self.km_label = Label(
            text="Aktueller Kilometerstand",
            font_size='20sp',
            size_hint_y=None,
            height=dp(25),
            bold=True,
            color=(1, 1, 1, 1)  # White color
        )
        self.km_input = TextInput(size_hint_y=None, height=dp(40))

        box_layout.add_widget(name)
        box_layout.add_widget(self.name_input)
        box_layout.add_widget(self.km_label)
        box_layout.add_widget(self.km_input)

        # Add the BoxLayout to the FloatLayout
        layout.add_widget(box_layout)

        # Create a BoxLayout for the Submit and Back buttons
        button_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=[dp(10), dp(10), dp(10), dp(10)])
        button_layout.size_hint = (1, None)
        button_layout.height = dp(120)
        button_layout.pos_hint = {'center_x': 0.5, 'y': 0.05}

        # Add a Submit button
        submit_button = Button(
            text='Submit',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        submit_button.bind(on_press=self.on_submit)
        button_layout.add_widget(submit_button)

        # Add a Back button to return to the main page
        back_button = Button(
            text='Back',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        back_button.bind(on_press=self.go_back)
        button_layout.add_widget(back_button)

        # Add the button layout to the screen
        layout.add_widget(button_layout)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main'

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def update_km_label(self, instance, value):
        # Update km_label based on which checkbox is selected
        if self.car_checkbox.active:
            self.km_label.text = "Aktueller Kilometerstand"
        elif self.tractor_checkbox.active:
            self.km_label.text = "Aktuelle Betriebsstunden"

    def on_submit(self, instance):
        vtype = "Auto"
        if self.tractor_checkbox.active:
            vtype = "Traktor"

        status, msg = register_vehicle(vtype, self.name_input, self.km_input) # registers vehicle into db
        if status:
            popup_text = "Fahrzeug registriert"
        else:
            popup_text = f"{msg}"
    
        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=popup_text))
        close_button = Button(text='OK', size_hint_y=None, height='40dp')
        popup_content.add_widget(close_button)

        popup = Popup(title='Submission Status',
                      content=popup_content,
                      size_hint=(None, None), size=(300, 200),
                      auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)

        popup.open()
