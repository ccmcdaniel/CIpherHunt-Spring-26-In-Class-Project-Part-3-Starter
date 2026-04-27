import os
from shell import AppShell
import custom_widgets
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core.text import LabelBase
from screens.dashboard.dashboard import DashboardScreen
from screens.vault.vault import VaultScreen
from screens.lab.lab import LabScreen
from screens.settings.settings import SettingsScreen
from models.user_model import UserModel
from models.clue_model import ClueModel
from models.database import DatabaseModel

# Register the family under an alias (e.g., 'IBMPlex')

scale = 1
Window.size = (414 * scale, 917 * scale)
Window.clearcolor = (1, 1, 1, 1)

class MultiScreenApp(App):
    def build(self):
        LabelBase.register(
            name='AppFont', 
            fn_regular = os.path.join(self.resource_path, "fonts", "ibm_plex_sans", "IBMPlexSans-Regular.ttf"),
            fn_bold=os.path.join(self.resource_path, "fonts", "ibm_plex_sans", 'IBMPlexSans-Bold.ttf'),
            fn_italic=os.path.join(self.resource_path, "fonts", "ibm_plex_sans", "IBMPlexSans-Italic.ttf")
        )
        db_path = os.path.join(self.resource_path, "data", "database.db")
        db = DatabaseModel(db_path)

        self.user = UserModel(db)
        self.clues = ClueModel(db)

        Builder.load_file(os.path.join(self.resource_path, "stylesheets", "style.kv"))
        self.shell = AppShell()
        self.shell.set_dashboard()
        
        return self.shell
    
    @property
    def base_path(self):
        path = os.path.dirname(os.path.abspath(__file__))
        return path
    
    @property
    def resource_path(self):
        return os.path.join(self.base_path, "resources")

if __name__ == "__main__":
    MultiScreenApp().run()