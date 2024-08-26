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

        # Create a BoxLayout for the title and buttons
        box_layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=[dp(10), dp(10), dp(10), dp(10)])
        box_layout.size_hint = (1, None)
        box_layout.height = dp(250)
        box_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        # Add a title label at the top
        title_label = Label(
            text="Andi's Supercoole TankApp",
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

        # Create the first button that navigates to the second screen
        button1 = Button(
            text='Neuer Tankeintrag',
            font_size='20sp',
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
            color=(1, 1, 1, 1)  # White text color
        )
        button1.bind(on_press=self.go_to_form)
        box_layout.add_widget(button1)

        # Add two more buttons for demonstration
        for i in range(2, 4):
            button = Button(
                text=f'Button {i}',
                size_hint_y=None,
                font_size='20sp',
                height=dp(50),
                background_color=(0, 0, 0, 0.8),  # Semi-transparent black background
                color=(1, 1, 1, 1)  # White text color
            )
            box_layout.add_widget(button)

        # Add the BoxLayout to the FloatLayout
        layout.add_widget(box_layout)

        self.add_widget(layout)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_form(self, instance):
        self.manager.current = 'form'
