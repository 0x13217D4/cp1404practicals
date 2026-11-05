from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    output_km = StringProperty("0.0")

    def build(self):
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        miles = self.get_valid_miles(text)
        self.output_km = str(miles * MILES_TO_KM)

    def handle_increment(self, text, change):
        miles = self.get_valid_miles(text) + change
        self.root.ids.input_miles.text = str(miles)

    @staticmethod
    def get_valid_miles(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()