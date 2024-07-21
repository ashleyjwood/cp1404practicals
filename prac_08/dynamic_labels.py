from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Simple Kivy app which creates labels from a list of names."""
    def __init__(self, **kwargs):
        """Initialise the app."""
        super().__init__(**kwargs)
        self.names = ["Henry", "Leo", "Olivia", "Charlotte"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the names list."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabels().run()
