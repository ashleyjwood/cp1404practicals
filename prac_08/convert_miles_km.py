from kivy.app import App
from kivy.lang import Builder

DISTANCE_CONVERSION = 1.60934  # Constant used to convert miles to kms


class ConvertMilesToKms(App):
    """Kivy App for converting miles to kilometers."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_conversion(self):
        """Calculate distance in kilometres."""
        miles = self.get_valid_input()
        kms = miles * DISTANCE_CONVERSION
        self.root.ids.output_label.text = f"{kms:.5f}"  # Handle odd cases such as 0.1mi->0.16093400000000002km

    def handle_increment(self, speed_delta):
        """Handle +ve or -ve increment button press."""
        miles = self.get_valid_input() + speed_delta
        self.root.ids.input_number.text = str(miles)
        self.calculate_conversion()

    def get_valid_input(self):
        """Get a valid number input from the user."""
        try:
            miles = float(self.root.ids.input_number.text)
            return miles
        except ValueError:
            return 0


ConvertMilesToKms().run()
