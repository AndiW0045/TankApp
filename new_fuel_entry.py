from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

from database_functions import get_vehicles, add_tankentry

class NewFuelEntry(Screen):
    def __init__(self, **kwargs):
        super(NewFuelEntry, self).__init__(**kwargs)
        # Use FloatLayout to place widgets on top of each other
        layout = FloatLayout()

        # Background Image
        background = Image(source='images/hose.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        title_layout = BoxLayout(orientation='vertical')
        title_layout.size_hint = (1, None)
        title_layout.height = dp(120)
        title_layout.pos_hint = {'center_x': 0.5, 'y': 0.8}

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
        
        title_layout.add_widget(title_label)


        # Create a BoxLayout for the form fields and back button
        box_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=[dp(10), dp(10), dp(10), dp(10)])
        box_layout.size_hint = (1, None)
        box_layout.height = dp(250)
        box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Create three text fields
        vehicle_button = Button(
                    text="Fahrzeug",
                    font_size='20sp',
                    size_hint_y=None,
                    height=dp(50),
                    bold=True,
                    background_color=(0,0,0,0.8),
                    color=(1, 1, 1, 1)  # White color
                )
        

        vehicles = get_vehicles()
        self.vehicle_list = []
        for v in vehicles:
            self.vehicle_list.append(v[1])

        self.vehicle_spinner = Spinner(
            text='Select Vehicle',
            font_size='20sp',
            values=self.vehicle_list, 
            size_hint_y=None,
            height=dp(50),
            bold=True,
            background_color=(1, 1, 1, 0.8),
            color=(0, 0, 0, 1)  
        )


        fuel_amount = Button(
                    text="Füllmenge",
                    font_size='20sp',
                    size_hint_y=None,
                    height=dp(50),
                    bold=True,
                    background_color=(0,0,0,0.8),
                    color=(1, 1, 1, 1)
                )
        self.fuel_input = TextInput(size_hint_y=None, height=dp(40))


        box_layout.add_widget(vehicle_button)
        box_layout.add_widget(self.vehicle_spinner)
        box_layout.add_widget(fuel_amount)
        box_layout.add_widget(self.fuel_input)


        # Add the BoxLayout to the FloatLayout
        layout.add_widget(title_layout)
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
            background_color=(0, 0, 0, 0.8),  
            color=(1, 1, 1, 1)  
        )
        submit_button.bind(on_press=self.on_submit)
        button_layout.add_widget(submit_button)

        # Add a Back button to return to the main page
        back_button = Button(
            text='Back',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  
            color=(1, 1, 1, 1)  
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

    def on_submit(self, instance):
        selected_vehicle = self.vehicle_spinner.text
        vehicle_id = self.vehicle_list.index(selected_vehicle) +1 # db starts with 1
        print(selected_vehicle, vehicle_id)
        status, msg = add_tankentry(vehicle_id, self.fuel_input) # adds new tankentry to db
        if status:
            popup_text = "Tankeintrag hinzugefügt"
        else:
            popup_text = f"{msg}"

        popup_content = BoxLayout(orientation='vertical')
        popup_content.add_widget(Label(text=popup_text))
        close_button = Button(text='OK', size_hint_y=None, height='40dp')
        popup_content.add_widget(close_button)

        popup = Popup(title='Submission Status',
                      content=popup_content,
                      size_hint=(None, None), size=('300dp', '200dp'),
                      auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()