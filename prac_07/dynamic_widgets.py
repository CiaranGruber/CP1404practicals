"""
Show the use of dynamic widgets

Dynamic Widgets. Created by Ciaran Gruber - 16/09/18
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgets(App):
    """Create the class for dynamic widgets"""

    def __init__(self, **kwargs):
        """Initialise original names list"""
        super().__init__(**kwargs)
        self.names = []

    def build(self):
        """Build the Kivy GUI"""
        self.title = 'Dynamic Widgets'
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Label(text=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.names_box.add_widget(temp_button)

    def press_entry(self):
        pass

    def add_widget(self):
        """Clear the current widgets and add the new ones"""
        self.root.ids.names_box.clear_widgets()
        self.names.append(self.root.ids.text_input.text)
        self.create_widgets()


DynamicWidgets().run()
