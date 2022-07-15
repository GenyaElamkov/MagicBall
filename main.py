from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MagicBallApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Magic Ball", halign="center")


MagicBallApp().run()


def main():
    pass


if __name__ == '__main__':
    main()
