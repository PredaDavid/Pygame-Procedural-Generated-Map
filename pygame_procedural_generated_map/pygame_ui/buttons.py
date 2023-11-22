import pygame

from pygame_procedural_generated_map.pygame_ui.ui_group import UiGroup


class ElevatedButton:
    def __init__(
        self,
        ui_group: UiGroup,
        text,
        pos,
        width=0,
        height=0,
        function = None,
        paddingx=30,
        paddingy=15,
        elevation=5,
        text_color="",
        main_color="",
        shadow_color="",
        hover_color="",
    ):
        # Core attributes
        self.ui_group = ui_group
        self.ui_group.container.append(self)
        self.ui_group.event_acces.append(self)
        self.elevation = elevation

        self.beggin_press = False

        self.functions = []
        if function != None: 
            self.functions.append(function)

        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # colors
        self.text_color = (
            self.ui_group.button_text_color if text_color == "" else text_color
        )
        self.main_color = self.ui_group.button_color if main_color == "" else main_color
        self.shadow_color = (
            self.ui_group.button_shadow_color if shadow_color == "" else shadow_color
        )
        self.hover_color = (
            self.ui_group.button_hover_color if hover_color == "" else hover_color
        )

        # text
        self.text_surf = self.ui_group.default_font.render(text, True, self.text_color)

        # size
        width = max(width, self.text_surf.get_width() + paddingx)
        height = max(height, self.text_surf.get_height() + paddingy)

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = self.main_color

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = self.shadow_color

        # text rect
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def update(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

    def draw(self, screen):
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.hover_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.dynamic_elecation = 0
                self.beggin_press = True
            elif event.type == pygame.MOUSEBUTTONUP and self.beggin_press:
                self.beggin_press = False
                self.dynamic_elecation = self.elevation
                self.on_press_button()
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = self.main_color

    def on_press_button(self):
        if len(self.functions) == 0:
            return
        
        for funct in self.functions:
            funct()

    def add_listener(self, function):
        self.functions.append(function)


class FlatButton:
    def __init__(
        self,
        ui_group: UiGroup,
        text,
        pos,
        paddingx = 30,
        paddingy = 15,
        width = 0,
        height = 0,
        function=None,
        text_color="",
        main_color="",
        hover_color="",
    ):
        # Core attributes
        self.ui_group = ui_group
        self.ui_group.container.append(self)
        self.ui_group.event_acces.append(self)

        self.functions = []
        if function != None:
            self.functions.append(function)

        self.beggin_press = False

        # colors
        self.text_color = (
            self.ui_group.button_text_color if text_color == "" else text_color
        )
        self.main_color = self.ui_group.button_color if main_color == "" else main_color
        self.hover_color = (
            self.ui_group.button_hover_color if hover_color == "" else hover_color
        )

        # test surface
        self.text_surf = self.ui_group.default_font.render(text, True, self.text_color)

        # size
        width = max(width, self.text_surf.get_width() + paddingx)
        height = max(height, self.text_surf.get_height() + paddingy)

        # top rectangle
        self.rect = pygame.Rect(pos, (width, height))
        self.rect_color = self.main_color

        # text rect
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def update(self):
        # elevation logic
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.rect_color, self.rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.rect_color = self.hover_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.beggin_press = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.beggin_press:
                    self.beggin_press = False
                    self.on_press_button()
        else:
            self.rect_color = self.main_color

    def on_press_button(self):
        if len(self.functions) == 0:
            return
        
        for funct in self.functions:
            funct()

    def add_listener(self, function):
        self.functions.append(function)
