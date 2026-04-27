from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class WindowManager(ScreenManager):
    """Manages the switching between different content screens."""
    pass


class AppShell(BoxLayout):
    screen_manager = ObjectProperty()
    tabs = ObjectProperty()

    def change_screen(self, screen):
        self.screen_manager.current = screen

        if(self.screen_manager.current == 'dashboard'):
            self.set_dashboard()
        elif(self.screen_manager.current == 'vault'):
            self.screen_manager.get_screen('vault').load_clue()
        elif(self.screen_manager.current == 'settings'):
            self.screen_manager.get_screen('settings').load_settings()

        for tab_button in self.tabs.children:
            if tab_button.route == screen:
                tab_button.is_active = True
            else:
                tab_button.is_active = False

    def set_dashboard(self):
       self.screen_manager.get_screen('dashboard').set_dashboard() 
    


        

Builder.load_file('shell.kv')

