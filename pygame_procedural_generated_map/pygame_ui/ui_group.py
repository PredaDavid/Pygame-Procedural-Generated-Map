import pygame


class UiGroup:
    def __init__(self, screen):
        self.screen = screen

        self.container = []
        self.event_acces = []

        # For text
        self.default_font = pygame.font.Font(None, 30)
        self.default_header_font = pygame.font.Font(None, 50)
        self.text_default_color = "#FFFFFF"

        # For buttons
        self.button_color = "#475F77"
        self.button_shadow_color = "#354B5E"
        self.button_hover_color = "#D74B4B"
        self.button_text_color = "#FFFFFF"

        # For text input
        self.text_input_color_active = "dodgerblue2"
        self.text_input_color_inactive = "lightskyblue3"
        self.text_input_inactive_state_true = "#c9c9c9"

        # For text
        self.text_text_color = "black"
        self.text_box_border_color = "lightskyblue3"

    def update(self):
        for item in self.container:
            item.update()

    def draw(self):
        for item in self.container:
            item.draw(self.screen)

    def give_events(self, events):
        for item in self.event_acces:
            item.handle_event(events)
