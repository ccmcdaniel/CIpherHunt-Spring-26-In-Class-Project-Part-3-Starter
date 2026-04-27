from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.utils import get_color_from_hex as hex
import os

class LabScreen(Screen):
    txtClueInput = ObjectProperty()
    txtKeyInput = ObjectProperty()
    lblFeedbackLabel = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        
        path = App.get_running_app().base_path
        Builder.load_file(os.path.join(path, "screens", "lab", "lab.kv"))

    def on_click_create(self):
        if(self.txtClueInput.text == '' or self.txtKeyInput.text == ''):
            self.set_feedback_message("Please enter clue and key before submitting.", "#CF7500")
            return
        
        app = App.get_running_app()
        user_id = app.user.id
        result = app.clues.AddClue(self.txtClueInput.text, self.txtKeyInput.text, user_id)

        if(result):
            self.txtClueInput.text = ""
            self.txtKeyInput.text = ""
            #app.screen_manager.change_screen('dashboard')
            self.set_feedback_message("Successfully created Clue!", "#108510")
            app.user.IncreasePoints(10)
            Clock.schedule_once(self.delay_close_screen, 3)
        else:
            self.set_feedback_message("Error: Could not add item.", "#FF0000")

    def set_feedback_message(self, message, color="#000000"):
         self.lblFeedbackLabel.text = message
         self.lblFeedbackLabel.color = color
         Clock.schedule_once(self.reset_feedback_message, 3)
         
    def reset_feedback_message(self, dt):
        self.lblFeedbackLabel.text = ''

    def delay_close_screen(self, dt):
         app = App.get_running_app()
         app.shell.change_screen('dashboard')

