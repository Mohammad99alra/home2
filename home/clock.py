import time
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button

class DigitalClock(Label):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.update_time()
        self.font_size = 50
        self.halign = 'center'
        self.valign = 'middle'

    def start(self):
        Clock.schedule_interval(self.update_time, 1)

    def stop(self):
        Clock.unschedule(self.update_time)

    def update_time(self, *args):
        self.text = f"It's {time.strftime('%H:%M:%S')} on a beautiful {time.strftime('%A, %B %d')} "
    

class ClockApp(App):
    def build(self):
        Window.size = (500, 500)  # Adjust height to accommodate additional text
        layout = BoxLayout(orientation='vertical')
        
        self.clock_label = DigitalClock()
        layout.add_widget(self.clock_label)

        info_label = Label(text=" Created by Mohammad Alragheb ", font_size=35)
        layout.add_widget(info_label)

        self.change_button = Button(text="Change Color", size_hint=(1, 0.2))
        self.change_button.bind(on_press=self.change_color)
        layout.add_widget(self.change_button)
        
        self.clock_label.start()
        return layout

    def on_stop(self):
        self.clock_label.stop()

    def change_color(self, instance):
        if self.clock_label.color == [1, 1, 1, 1]:
            self.clock_label.color = [1, 0, 0, 1]  # Change to red
        else:
            self.clock_label.color = [1, 1, 1, 1]  # Change back to white


if __name__ == '__main__':
    ClockApp().run()
