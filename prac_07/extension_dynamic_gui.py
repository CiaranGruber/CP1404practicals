"""
Show a list of names from a loaded file

Dynamic Name Viewer. Created by Ciaran Gruber - 22//09/18
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window


class DynamicNameViewer(App):
    """Show a kivy-based dynamic viewer"""
    save_file = 'dynamic_names.txt'

    def __init__(self, **kwargs):
        """Initialise the kivy-based App"""
        super().__init__(**kwargs)
        try:
            self.people = load_names(DynamicNameViewer.save_file)
        except FileNotFoundError:
            self.people = []

    def build(self):
        """Build the Kivy GUI"""
        Window.size = (400, 600)
        self.title = 'Dynamic Name Viewer'
        self.root = Builder.load_file('extension_dynamic_gui.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create all the people widgets"""
        for i, person in enumerate(self.people):
            name = Button(text=person[0], id=str(person[1]))
            name.bind(on_release=self.show_name)
            deletion_button = Button(text='Delete', id=str(i))
            deletion_button.bind(on_release=self.delete_entry)
            self.root.ids.names_box.add_widget(name)
            self.root.ids.deletions_box.add_widget(deletion_button)

    def delete_entry(self, button):
        """Delete a specific entry"""
        del self.people[int(button.id)]
        self.refresh_widgets()

    def refresh_widgets(self):
        """Clear all names and rebuild widget"""
        self.root.ids.names_box.clear_widgets()
        self.root.ids.deletions_box.clear_widgets()
        self.create_widgets()

    def show_name(self, name):
        """Show the name"""
        self.root.ids.output_label.text = 'Age: ' + str(name.id)

    def add_name(self):
        """Add a name to the people list"""
        if self.root.ids.name_input.text == '':
            self.root.ids.output_label.text = 'Must have a name'
        elif self.root.ids.age_input.text == '':
            self.root.ids.output_label.text = 'Must have an age'
        else:
            try:
                self.people.append([self.root.ids.name_input.text, int(self.root.ids.age_input.text)])
                self.refresh_widgets()
            except ValueError:
                self.root.ids.output_label.text = 'Invalid age'

    def on_stop(self):
        """Save file when stopped"""
        save_names(self.people, DynamicNameViewer.save_file)


def load_names(filename):
    """Load all the people from a specific filename"""
    people = []
    with open(filename) as names_file:
        file_lines = names_file.readlines()
    for line in file_lines:
        people.append(line.strip().split(','))
    return people


def save_names(people, filename):
    """Save all names to a specific file"""
    with open(filename, mode='w') as names_file:
        for person in people:
            names_file.write(person[0] + ',' + str(person[1]) + '\n')


DynamicNameViewer().run()
