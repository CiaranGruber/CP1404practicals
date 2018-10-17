"""
Convert Temperatures in a Kivy-based GUI

Temperature Converter. Created by Ciaran Gruber - 22/09/18
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class TemperatureConverter(App):
    """Kivy-based GUI for a Temperature converter program"""

    def build(self):
        """Build the Kivy-GUI"""
        Window.size = (800, 300)
        self.title = 'Temperature Converter'
        self.root = Builder.load_file('extension_temperature_converter.kv')
        return self.root

    def change_celsius(self, amount=0):
        """Change celsius amount"""
        try:
            self.root.ids.celsius_input.text = str(float(self.root.ids.celsius_input.text) + amount)
        except ValueError:
            self.root.ids.celsius_input.text = str(amount)

    def change_fahrenheit(self, amount=0):
        """Change fahrenheit amount"""
        try:
            self.root.ids.fahrenheit_input.text = str(float(self.root.ids.fahrenheit_input.text) + amount)
        except ValueError:
            self.root.ids.fahrenheit_input.text = str(amount)

    def convert_to_fahrenheit(self):
        """Convert celsius to fahrenheit"""
        try:
            self.root.ids.fahrenheit_input.text = '{:.2f}'.format(float(self.root.ids.celsius_input.text)
                                                                  * 9.0 / 5 + 32)
        except ValueError:
            self.root.ids.celsius_input.text = 'Invalid number'

    def convert_to_celsius(self):
        """Convert fahrenheit to celsius"""
        try:
            self.root.ids.celsius_input.text = '{:.2f}'.format((float(self.root.ids.fahrenheit_input.text) - 32)
                                                                 * 5 / 9)
        except ValueError:
            self.root.ids.fahrenheit_input.text = 'Invalid number'

    def clear_all(self):
        self.root.ids.celsius_input.text = ''
        self.root.ids.fahrenheit_input.text = ''


TemperatureConverter().run()
