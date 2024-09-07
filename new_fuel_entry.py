from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle


class NewFuelEntry(Screen):
    def __init__(self, **kwargs):
        super(NewFuelEntry, self).__init__(**kwargs)
        # Use FloatLayout to place widgets on top of each other
        layout = FloatLayout()

        # Background Image
        background = Image(source='images/hose.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        self.text_inputs = []


        # Create a BoxLayout for the form fields and back button
        box_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=[dp(10), dp(10), dp(10), dp(10)])
        box_layout.size_hint = (1, None)
        box_layout.height = dp(250)
        box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Add a title label at the top
        title_label = Label(
            text="Neuer Tankeintrag",
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


        # Create three text fields
        vehicle = Button(
                    text="Fahrzeug",
                    font_size='20sp',
                    size_hint_y=None,
                    height=dp(50),
                    bold=True,
                    background_color=(0,0,0,0.5),
                    color=(1, 1, 1, 1)  # White color
                )
        vehicle_input = TextInput(size_hint_y=None, height=dp(40))

        fuel_amount = Button(
                    text="Füllmenge",
                    font_size='20sp',
                    size_hint_y=None,
                    height=dp(50),
                    bold=True,
                    background_color=(0,0,0,0.5),
                    color=(1, 1, 1, 1) # White color
                )
        fuel_input = TextInput(size_hint_y=None, height=dp(40))

        self.text_inputs.append(vehicle_input)
        self.text_inputs.append(fuel_input)

        box_layout.add_widget(vehicle)
        box_layout.add_widget(vehicle_input)
        box_layout.add_widget(fuel_amount)
        box_layout.add_widget(fuel_input)


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
        submit_button.bind(on_press=self.submit_form)
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

    def submit_form(self, instance):
        # Collect the text from the text fields
        form_data = [text_input.text for text_input in self.text_inputs]
        print("Form Submitted with Data:", form_data)
        # Add form submission logic here (e.g., save data, send to a server, etc.)
        # TODO

    def go_back(self, instance):
        self.manager.current = 'main'

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
