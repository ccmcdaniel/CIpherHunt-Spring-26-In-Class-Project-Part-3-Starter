from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.utils import get_color_from_hex as hex
import os

class SettingsScreen(Screen):
    txtUsername = ObjectProperty()
    txtEmail = ObjectProperty()
    tglNotificationsToggle = ObjectProperty()
    lblFeedbackLabel = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.__update_delay = 1 # seconds
        self.__clock_username_update = None
        self.__clock_email_update = None
        path = App.get_running_app().base_path
        Builder.load_file(os.path.join(path, "screens", "settings", "settings.kv"))

    def load_settings(self):
        app = App.get_running_app()
        self.txtUsername.text = app.user.username
        self.__clock_username_update.cancel()
        self.txtEmail.text = app.user.email
        self.__clock_email_update.cancel()

    def schedule_username_update(self):
        if self.txtUsername.text == '':
            self.set_feedback_message("Username cannot be blank.", "#CA864B")
            if(self.__clock_username_update != None):
                self.__clock_username_update.cancel()
            return
        
        if(self.__clock_username_update != None):
            self.__clock_username_update.cancel()

        self.__clock_username_update = Clock.schedule_once(self.update_username, self.__update_delay)

    def schedule_email_update(self):
        if self.txtEmail.text == '':
            self.set_feedback_message("Email cannot be blank.", "#CA864B")
            if(self.__clock_email_update != None):
                self.__clock_email_update.cancel()
            return
        
        if(self.__clock_email_update != None):
            self.__clock_email_update.cancel()

        self.__clock_email_update = Clock.schedule_once(self.update_email, self.__update_delay)

    def schedule_notifications_update(self):
        pass

    def schedule_deletedata_update(self):
        pass

    def update_username(self, dt):
        app = App.get_running_app()
        result = app.user.UpdateUsername(self.txtUsername.text)

        if(result):
            self.set_feedback_message("Username Successfully Updated!", "#498F3F")
        else:
            self.set_feedback_message("Error: Username could not be updated.", "#C74F4F")

    def update_email(self, dt):
        app = App.get_running_app()
        result = app.user.UpdateEmail(self.txtEmail.text)

        if(result):
            self.set_feedback_message("Email Successfully Updated!", "#498F3F")
        else:
            self.set_feedback_message("Error: Email could not be updated.", "#C74F4F")

    def set_feedback_message(self, message, color="#000000"):
         self.lblFeedbackLabel.text = message
         self.lblFeedbackLabel.color = color
         Clock.schedule_once(self.reset_feedback_message, 3)
         
    def reset_feedback_message(self, dt):
        self.lblFeedbackLabel.text = ''
        
