import numpy as np
import pygame


from .noise import generate_fractal_noise_2d
from .falloff_generator import generate_falloff_map


class NoiseMap:
    def __init__(
        self,
        size=256,
        res=8,
        octaves=5,
        persistence=0.5,
        lacunarity=2,
        seed=0,
        use_falloff=True,
    ):
        self.size = size
        self.res = res
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.seed = seed

        self.use_falloff = use_falloff

    def generate_map(self):
        '''Generate the noise map and returns it; the map is also stored in self.map'''
        np.random.seed(self.seed)

        self.falloff_map = generate_falloff_map(self.size)

        self.map = generate_fractal_noise_2d(
            (self.size, self.size),
            (self.res, self.res),
            self.octaves,
            self.persistence,
            self.lacunarity,
            (False, False),
        )

        def clamp(n):
            if n < -1:
                return -1
            elif n > 1:
                return 1
            else:
                return n

        if self.use_falloff:
            for y in range(self.size):
                for x in range(self.size):
                    self.map[x][y] = clamp(self.map[x][y] - self.falloff_map[x][y])

    def draw_map(self, view_scale=1):
        '''Generate the surface where the map is drawn and then returns it; the surface is also stored in self.draw_surface'''
        blue = [65, 105, 225]
        green = [34, 139, 34]
        beach = [238, 214, 175]
        snow = [255, 250, 250]
        mountain = [139, 137, 137]

        self.draw_surface = pygame.Surface(
            (view_scale * self.size, view_scale * self.size)
        )

        for i in range(self.size):
            for j in range(self.size):
                surf = pygame.Surface((1 * view_scale, 1 * view_scale))
                if self.map[i][j] < -0.05:
                    surf.fill(blue)
                elif self.map[i][j] < 0.05:
                    surf.fill(beach)
                elif self.map[i][j] < 0.35:
                    surf.fill(green)
                elif self.map[i][j] < 0.6:
                    surf.fill(mountain)
                else:
                    surf.fill(snow)


                self.draw_surface.blit(surf, (i * view_scale, j * view_scale))
