from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty
import os

class DashboardScreen(Screen):
    username = StringProperty("Guest")
    rank = StringProperty("Novice")
    rank_percent_complete = NumericProperty(0)
    rank_points = NumericProperty(45)
    next_rank_points = NumericProperty(250)

    def __init__(self, **kw):
        super().__init__(**kw)
        
        path = App.get_running_app().base_path
        Builder.load_file(os.path.join(path, "screens", "dashboard", "dashboard.kv"))
        
        self.rank_percent_complete = self.rank_points / self.next_rank_points

    def set_dashboard(self):
        app = App.get_running_app()
        self.username = app.user.username
        current_rank = app.user.rank.current_rank
        self.rank = current_rank[0]
        self.rank_points = app.user.rank.current_points
        self.next_rank_points = app.user.rank.next_rank_points
        self.rank_percent_complete = self.rank_points / self.next_rank_points



