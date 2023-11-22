import pygame

from pygame_procedural_generated_map.pygame_ui.ui_group import UiGroup


class InputField:
    def __init__(
        self,
        ui_group: UiGroup,
        text,
        pos,
        width=200,
        height=30,
        on_enter_function=None,
        inactive_state=False,
        delete_text_on_enter=False
    ):
        self.ui_group = ui_group
        self.ui_group.container.append(self)
        self.ui_group.event_acces.append(self)

        self.functions = []
        if on_enter_function != None:
            self.functions.append(on_enter_function)

        # colors and font
        self.active_color = self.ui_group.text_input_color_active
        self.inactive_color = self.ui_group.text_input_color_inactive
        self.font = self.ui_group.default_font

        self.box_color = self.inactive_color
        self.text_color = self.inactive_color
        self.default_width = width
        self.rect = pygame.Rect(pos, (width, height))
        self.text = text
        self.txt_surface = self.font.render(text, True, self.box_color)
        self._active = False
        
        self.delete_text_on_enter = delete_text_on_enter
        
        self.inactive_state = inactive_state
        if self.inactive_state:
            self.set_inactive_state(True)


    def handle_event(self, event):
        if self.inactive_state:
            return
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Activate
                self.activate()
            # If the user clicked outsite of the box rect
            else:
                if self._active:
                    self.deactivate()
        if event.type == pygame.KEYDOWN:
            # Redraw only if active == True
            if self._active:
                if event.key == pygame.K_RETURN:
                    self.deactivate()
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_DELETE:
                    self.text = ""
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.text_color)

    def activate(self):
        if self.delete_text_on_enter:
            self.text = ""
        
        self._active = True
        self.text_color = self.active_color
        self.box_color = self.active_color
        self.txt_surface = self.font.render(self.text, True, self.text_color)

    def deactivate(self):
        self._active = False
        self.text_color = self.inactive_color
        self.box_color = self.inactive_color
        self.txt_surface = self.font.render(self.text, True, self.text_color)

        self.on_press_enter()

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.default_width, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pygame.draw.rect(screen, self.box_color, self.rect, 2)

    def on_press_enter(self):
        for funct in self.functions:
            funct()

    def add_listener(self, function):
        self.functions.append(function)

    def set_inactive_state(self, state: bool):
        self.inactive_state = state
        if self.inactive_state:
            self.text_color = self.ui_group.text_input_inactive_state_true
            self.box_color = self.ui_group.text_input_inactive_state_true
            self.txt_surface = self.font.render(self.text, True, self.text_color)
            
    # Use when you want to update the text while the inactive_state is True
    def force_text_update(self, text):
        self.text = text
        self.txt_surface = self.font.render(self.text, True, self.text_color)