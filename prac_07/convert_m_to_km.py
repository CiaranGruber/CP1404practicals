"""
Convert any amount of miles to kilometres.

Convert Distance. Created by Ciaran Gruber - 16/09/18
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertDistance(App):

    def build(self):
        """
        Build the Kivy GUI
        :return:
        """
        Window.size = (400, 200)
        self.title = 'Convert Miles To Kilometres'
        self.root = Builder.load_file('convert_m_to_km.kv')
        return self.root

    def handle_increment(self, value):
        """
        Add an amount to the text_input box
        :param value:
        :return:
        """
        try:
            self.root.ids.text_input.text = str(int(self.root.ids.text_input.text) + value)
        except ValueError:
            self.root.ids.text_input.text = str(value)

    def convert_distance(self):
        """
        Convert distance from miles to kilometres
        :return:
        """
        try:
            self.root.ids.output_label.text = '{:.3f}'.format(int(self.root.ids.text_input.text) * 1.60934)
        except ValueError:
            self.root.ids.output_label.text = '0.0'


ConvertDistance().run()
