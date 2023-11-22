import pygame

from pygame_procedural_generated_map.pygame_ui.ui_group import UiGroup
from pygame_procedural_generated_map.pygame_ui.text import TextBox, Text
from pygame_procedural_generated_map.pygame_ui.input_field import InputField


class PropertyField:
    def __init__(
        self,
        ui_group: UiGroup,
        text,
        pos,
        default_input_text="",
        numeric=False,
        inactive_state=False,
        input_field_function=None,
        input_delete_text_on_enter=False
    ):
        self.text_component = Text(
            ui_group, text, pos, padding=5
        )  # we add padding so the text will be level with the input field
        text_width = self.text_component.get_width()
        self.numeric = numeric

        posx = pos[0] + text_width + 10
        posy = pos[1] - 4
        
        input_text = default_input_text if default_input_text != "" else "0.00"
        input_width = 30 if numeric else 100
        input_delete_text_on_enter = input_delete_text_on_enter if not numeric else True
        
        self.input_component = InputField(
            ui_group,
            input_text,
            (posx, posy),
            width=input_width,
            inactive_state=inactive_state,
            on_enter_function=input_field_function,
            delete_text_on_enter=input_delete_text_on_enter
        )

    def get_value(self):
        if self.numeric:
            try:
                value = float(self.input_component.text)
            except ValueError:
                value = 0.0
        else:
            value = self.input_component.text

        return value
