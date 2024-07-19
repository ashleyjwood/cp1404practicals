from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

DISTANCE_CONVERSION = 1.60934  # Constant used to convert miles to kms


class ConvertMilesToKms(App):
    """Kivy App for converting miles to kilometers"""

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_distance(self):
        try:
            miles = float(self.root.ids.input_number.text)  # Should this be "mile" (as it's not a list)?
            kms = miles * DISTANCE_CONVERSION  # Likewise as above, "km"?
            self.root.ids.output_label.text = f"{kms:.5f}"
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

    def handle_increment(self, button_id):
        """Handle +ve or -ve increment button press, with error checking for invalid inputs."""
        try:
            miles = float(self.root.ids.input_number.text)
        except ValueError:
            miles = 0  # If the text entered is not a valid number, initialise to zero and then handle button press

        if button_id == "mile_up":
            miles += 1.0
        elif button_id == "mile_down":
            miles -= 1.0
        self.root.ids.input_number.text = str(miles)


ConvertMilesToKms().run()
