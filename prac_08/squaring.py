"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = f"{float(value) ** 2:.3f}"  # Round the result to 3 decimal places
            self.root.ids.output_label.text = result
        except ValueError:
            self.root.ids.output_label.text = "Value\nError"


SquareNumberApp().run()
