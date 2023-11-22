from pygame_debug.debug import debug
from pygame_ui.ui_group import UiGroup
from pygame_ui.custom_components import *
from pygame_ui.buttons import *
from procedural_generation.map_generator import NoiseMap

import sys
import random


class VisualizeNoiseMap:
    def __init__(self):
        # Pygame stuff
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Gui Menu")
        self.clock = pygame.time.Clock()

        # Noise map
        self.noise_map = NoiseMap()
        self.noise_map.generate_map()
        self.noise_map.draw_map(4)
        # propertis
        self.view_scale = 4
        self.size = 256
        self.res = 8
        self.octaves = 5
        self.persistence = 0.5
        self.lacunarity = 2
        self.seed = 0

        # UI
        self.ui = UiGroup(self.screen)
        self.ui.button_hover_color = "#64918f"

        self.button_draw = ElevatedButton(
            self.ui,
            "Redraw Map",
            (1600, 850),
            width=315,
            height=30,
            function=self.redraw_map,
        )
        self.button_generate = ElevatedButton(
            self.ui,
            "Generate Map With Settings",
            (1600, 900),
            width=315,
            height=30,
            function=self.generate_map,
        )
        self.button_generate_random = ElevatedButton(
            self.ui,
            "Generate With Random Seed",
            (1600, 950),
            width=315,
            height=30,
            function=self.generate_with_random_seed,
        )
        self.button_export_map = ElevatedButton(
            self.ui,
            "Export Map As Image",
            (1600, 1000),
            width=315,
            height=30,
            function=self.export_map_as_image,
        )

        self.text_aa = Text(
            self.ui, "Next Settings", (1600, 20), font=self.ui.default_header_font
        )

        self.pf_size = PropertyField(
            self.ui,
            "Size",
            (1600, 100),
            numeric=True,
            input_field_function=self.check_property_field,
        )
        self.pf_res = PropertyField(
            self.ui,
            "Res",
            (1600, 150),
            numeric=True,
            input_field_function=self.check_property_field,
        )
        self.pf_octaves = PropertyField(
            self.ui,
            "Octaves",
            (1600, 200),
            numeric=True,
            input_field_function=self.check_property_field,
        )
        self.pf_persistence = PropertyField(
            self.ui,
            "Persistence",
            (1600, 250),
            numeric=True,
            input_field_function=self.check_property_field,
        )
        self.pf_lacunarity = PropertyField(
            self.ui,
            "Lacunarity",
            (1600, 300),
            numeric=True,
            input_field_function=self.check_property_field,
        )
        self.pf_seed = PropertyField(
            self.ui,
            "Seed",
            (1400, 20),
            numeric=True,
            input_field_function=self.check_property_field,
        )

        self.text_header = Text(
            self.ui, "Current Settings", (1600, 370), font=self.ui.default_header_font
        )

        self.pf_current_size = PropertyField(
            self.ui, "Size", (1600, 450), numeric=True, inactive_state=True
        )
        self.pf_current_res = PropertyField(
            self.ui, "Res", (1600, 500), numeric=True, inactive_state=True
        )
        self.pf_current_octaves = PropertyField(
            self.ui, "Octaves", (1600, 550), numeric=True, inactive_state=True
        )
        self.pf_current_persistence = PropertyField(
            self.ui, "Persistence", (1600, 600), numeric=True, inactive_state=True
        )
        self.pf_current_lacunarity = PropertyField(
            self.ui, "Lacunarity", (1600, 650), numeric=True, inactive_state=True
        )
        self.pf_current_seed = PropertyField(
            self.ui, "Seed", (1400, 370), numeric=True, inactive_state=True
        )

        self.pf_view_scale = PropertyField(
            self.ui,
            "View Scale",
            (1600, 750),
            numeric=True,
            input_field_function=self.check_property_field,
        )

    def run(self):
        self.set_current_property_field()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                self.ui.give_events(event)

            self.screen.fill("#51524f")

            self.screen.blit(self.noise_map.draw_surface, (0, 0))

            self.ui.update()
            self.ui.draw()

            debug(self.clock.get_fps())

            pygame.display.update()
            self.clock.tick(200)

    def redraw_map(self):
        self.view_scale = int(self.pf_view_scale.get_value())
        self.noise_map.draw_map(int(self.view_scale))

    def generate_map(self):
        self.check_property_field()
        self.noise_map.size = self.size
        self.noise_map.res = self.res
        self.noise_map.octaves = self.octaves
        self.noise_map.persistence = self.persistence
        self.noise_map.lacunarity = self.lacunarity
        self.noise_map.seed = self.seed

        self.noise_map.generate_map()
        self.redraw_map()

        self.set_current_property_field()

        self.redraw_map()

    def generate_with_random_seed(self):
        self.check_property_field()
        self.seed = random.randint(0, 9999)
        self.noise_map.size = self.size
        self.noise_map.res = self.res
        self.noise_map.octaves = self.octaves
        self.noise_map.persistence = self.persistence
        self.noise_map.lacunarity = self.lacunarity
        self.noise_map.seed = self.seed

        self.noise_map.generate_map()
        self.redraw_map()

        self.set_current_property_field()

    def check_property_field(self):
        self.view_scale = int(self.pf_view_scale.get_value())
        self.size = int(self.pf_size.get_value())
        self.res = int(self.pf_res.get_value())
        self.octaves = int(self.pf_octaves.get_value())
        self.persistence = self.pf_persistence.get_value()
        self.lacunarity = int(self.pf_lacunarity.get_value())
        self.seed = int(self.pf_seed.get_value())

    def set_current_property_field(self):
        # Current Property field
        self.pf_current_size.input_component.force_text_update(str(self.size))
        self.pf_current_res.input_component.force_text_update(str(self.res))
        self.pf_current_octaves.input_component.force_text_update(str(self.octaves))
        self.pf_current_persistence.input_component.force_text_update(
            str(self.persistence)
        )
        self.pf_current_lacunarity.input_component.force_text_update(
            str(self.lacunarity)
        )
        self.pf_current_seed.input_component.force_text_update(str(self.seed))

        # Modifiable field
        self.pf_size.input_component.force_text_update(str(self.size))
        self.pf_res.input_component.force_text_update(str(self.res))
        self.pf_octaves.input_component.force_text_update(str(self.octaves))
        self.pf_persistence.input_component.force_text_update(str(self.persistence))
        self.pf_lacunarity.input_component.force_text_update(str(self.lacunarity))
        self.pf_seed.input_component.force_text_update(str(self.seed))

        self.pf_view_scale.input_component.force_text_update(str(self.view_scale))

    def export_map_as_image(self):
        pygame.image.save(self.noise_map.draw_surface, "noise_map.png")


if __name__ == "__main__":
    VisualizeNoiseMap().run()
