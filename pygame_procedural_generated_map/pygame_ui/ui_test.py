import pygame, sys

from pygame_procedural_generated_map.pygame_ui.buttons import ElevatedButton, FlatButton
from pygame_procedural_generated_map.pygame_ui.ui_group import UiGroup
from pygame_procedural_generated_map.pygame_ui.input_field import InputField
from pygame_procedural_generated_map.pygame_ui.text import TextBox, Text
from pygame_procedural_generated_map.pygame_ui.custom_components import PropertyField



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Gui Menu")
        self.clock = pygame.time.Clock()

        self.ui = UiGroup(self.screen)

        self.button1 = ElevatedButton(
            self.ui,
            "Button 1",
            (100, 100),
            paddingx=100,
            function=(lambda: self.print_something("1")),
        )
        self.button2 = ElevatedButton(
            self.ui,
            "Button 2",
            (400, 100),
            width=200,
            height=40,
            function=(lambda: self.print_something("2")),
        )

        self.flat_button = FlatButton(
            self.ui,
            "Flat",
            (100, 200),
            paddingx=100,
            paddingy=20,
            function=(lambda: self.print_something("Flat")),
        )

        self.input_field = InputField(
            self.ui,
            "something",
            (100, 300),
            on_enter_function=(lambda: self.print_something(self.input_field.text)),
        )

        self.text_box = TextBox(self.ui, "Something", (100, 400), padding=20)

        self.text = Text(self.ui, "Hello", (400, 400))

        self.property_field = PropertyField(
            self.ui, "Property", (100, 500), numeric=True
        )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.ui.give_events(event)

            self.screen.fill("#DCDDD8")

            self.ui.update()
            self.ui.draw()

            pygame.display.update()
            self.clock.tick(60)

    def print_something(self, text="DEFAULT"):
        print("UI print!: " + text)


if __name__ == "__main__":
    game = Game()
    game.run()
