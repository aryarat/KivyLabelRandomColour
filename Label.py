import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window

Builder.load_file("Label.kv")

class MyWidget(BoxLayout):
    background_color = ListProperty()

    def stop(self):
        self.event.cancel()

    def start(self):
        # self.rand_color()
        self.event = Clock.schedule_interval(self.Callback, 1)

    def Callback(self, dt):
        self.rand_color()

    # background_color = ListProperty([22/255, 160/255, 133/255, 1])
    def rand_color(self):
        r = NumericProperty(0)
        g = NumericProperty(0)
        b = NumericProperty(0)
        z = NumericProperty(0)
        self.background_color = self.gen_rbg(r, g, b, z)
        # self.background_color = Clock.schedule_interval(partial(self.gen_rbg(r, g, b, z)), 0.5)

    def gen_rbg(self, r, g, b, a):
        new_r = random.randint(1, 255)
        new_g = random.randint(1, 255)
        new_b = random.randint(1, 255)
        r = new_r / 255
        g = new_g / 255
        b = new_b / 255
        z = 1
        return r, g, b, z

class SampleApp(App):
    def build(self):
        a = MyWidget()
        Window.borderless = True
        return a

if __name__ == "__main__":
    SampleApp().run()