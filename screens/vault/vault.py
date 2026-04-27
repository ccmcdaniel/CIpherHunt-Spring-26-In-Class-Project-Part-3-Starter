from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.utils import get_color_from_hex as hex
from kivy.clock import Clock
import os

class VaultScreen(Screen):
    clue_text = StringProperty("What was the name of that awful teacher in school that makes us do work?")
    txtAnswerInput = ObjectProperty()
    lblFeedbackLabel = ObjectProperty()
    username = StringProperty("cmcdaniel2008")
    date = StringProperty("4/15/2026")

    def __init__(self, **kw):
        super().__init__(**kw)
        
        path = App.get_running_app().base_path
        Builder.load_file(os.path.join(path, "screens", "vault", "vault.kv"))

    def load_clue(self):
        app = App.get_running_app()
        self.clue_data = app.clues.GetCurrentClue()
        self.clue_text = self.clue_data.clue_text
        self.date = self.clue_data.date_created.strftime("%d-%m-%Y %H:%M:%S")
        self.username = app.clues.GetClueUsername()

    def on_click_fetch_clue(self):
        app = App.get_running_app()
        self.clue_data = app.clues.FetchNewClue()

        if(self.clue_data != None):
            self.clue_text = self.clue_data.clue_text
            self.date = self.clue_data.date_created.strftime("%d-%m-%Y %H:%M:%S")
            self.username = app.clues.GetClueUsername()

        else:
            self.clue_text = "Error: Could not fetch clue..."
            self.date = "??"
            self.user = "??"


    def on_click_submit(self):
        if self.clue_data == None:
            return
        
        app = App.get_running_app()
        if(self.txtAnswerInput.text == ''):
            self.show_feedback("Please enter a key","#CF7500")

        else:       
            result = app.clues.AttemptCurrentClueSolve(self.txtAnswerInput.text)

            if(result):
                self.show_feedback("Successfully solved!", "#4F8C00")
                app.user.IncreasePoints(5)
                self.on_click_fetch_clue()
            else:
                self.show_feedback("That is not corrrect.", "#A80000")

        
        self.txtAnswerInput.text = ''

    def reset_feedback_label(self, dt):
        self.lblFeedbackLabel.text = ""

    def show_feedback(self, message, color):
        self.lblFeedbackLabel.text = message
        self.lblFeedbackLabel.color = hex(color)
        Clock.schedule_once(self.reset_feedback_label, 3)

        

