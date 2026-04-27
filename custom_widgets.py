from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ColorProperty
from kivy.app import App
from kivy.utils import get_color_from_hex

class TabButton(Button):
    route = StringProperty("dashboard")
    image_filename = StringProperty("house-solid.png")
    is_active = BooleanProperty(False)

    def on_release(self):
        app = App.get_running_app()
        app.shell.change_screen(self.route)

class TextBox(BoxLayout):
    text = StringProperty("")
    hint_text = StringProperty("")
    is_multiline = BooleanProperty(False)
    back_color = ColorProperty(get_color_from_hex("#D9D9D9"))

class ArrowButton(Button):
    is_left = BooleanProperty(True)

class ContentBox(BoxLayout):
    title_text = StringProperty()

class CheckmarkBox(CheckBox):
    background_color = ColorProperty(get_color_from_hex("#000000"))
    checkmark_name = StringProperty("check-solid-dark.png")

class AppButton(Button):
    color_normal = ColorProperty(get_color_from_hex("#87E5FF"))
    color_pressed = ColorProperty(get_color_from_hex("#126f89"))

Builder.load_file('custom_widgets.kv')