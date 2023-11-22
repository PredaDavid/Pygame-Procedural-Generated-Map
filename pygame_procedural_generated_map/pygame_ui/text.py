import pygame
from pygame_procedural_generated_map.pygame_ui.ui_group import UiGroup


class TextBox:
    def __init__(
        self,
        ui_group: UiGroup,
        text,
        pos,
        padding=5,
        font="",
        text_color="",
        box_color="",
        box_radius=0,
    ):
        # Core attributes
        self.ui_group = ui_group
        self.ui_group.container.append(self)

        # atributes
        self.text_color = (
            self.ui_group.button_text_color if text_color == "" else text_color
        )
        self.box_color = (
            self.ui_group.text_box_border_color if box_color == "" else box_color
        )
        self.box_radius = box_radius
        self.font = self.ui_group.default_font if font == "" else font

        self.text = text
        self.txt_surface = self.font.render(text, True, self.text_color)

        # size
        width = self.txt_surface.get_width() + padding
        height = self.font.get_height() + padding
        self.rect = pygame.Rect(pos, (width, height))

    def update(self):
        pass

    def draw(self, screen):
        # Blit the text.
        draw_rect = self.txt_surface.get_rect(center=self.rect.center)
        screen.blit(self.txt_surface, draw_rect)
        # Blit the rect.
        pygame.draw.rect(screen, self.box_color, self.rect, 2)


class Text:
    def __init__(self, ui_group: UiGroup, text, pos, font="", text_color="", padding=0):
        # Core attributes
        self.ui_group = ui_group
        self.ui_group.container.append(self)

        # atributes
        self.text_color = (
            self.ui_group.button_text_color if text_color == "" else text_color
        )
        self.font = self.ui_group.default_font if font == "" else font

        self.text = text
        self.txt_surface = self.font.render(text, True, self.text_color)

        # size
        width = self.txt_surface.get_width() + padding
        height = self.font.get_height() + padding
        self.rect = pygame.Rect(pos, (width, height))

    def update(self):
        pass

    def draw(self, screen):
        # Blit the text.
        draw_rect = self.txt_surface.get_rect(center=self.rect.center)
        screen.blit(self.txt_surface, draw_rect)

    def get_width(self):
        return self.rect.width
