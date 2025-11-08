from datetime import datetime


class Renderer:

    def __init__(self, tileSize, image):
        self.tileSize = tileSize
        self.image = image

    def time_to_rgb(self):
        # Get an RGB colour based on current time
        # Each channel ranges from 64-255 to avoid overly dark shades
        # 'Bounces' the value at the midpoint (e.g. mirrors around 30 seconds) to avoid colour jumps at boundaries
        # There's only so many values so would be easy to make a lookup table and cache the values, but
        # a Model 4 is powerful enough it's not really a necessary optimization.  YMMV as they say
        now = datetime.now()

        def mirrored_normalize(value, max_value):
            # Mirror the value around the midpoint
            if value > max_value / 2:
                value = max_value - value
            # Normalize to range 64–255
            return int(64 + (value / (max_value / 2)) * (255 - 64))

        r = mirrored_normalize(now.hour, 23)    # 0–23 hours
        g = mirrored_normalize(now.minute, 59)  # 0–59 minutes
        b = mirrored_normalize(now.second, 59)  # 0–59 seconds

        return r, g, b

    def clear(self, width, height):
        self.image.rectangle((0, 0, width, height), 'black')

    def output(self, game):
        col = self.time_to_rgb()
        for y in range(game.height):
            for x in range(game.width):
                if game.grid[y][x]:
                    x1 = x * self.tileSize
                    y1 = y * self.tileSize
                    x2 = x1 + self.tileSize
                    y2 = y1 + self.tileSize
                    self.image.rectangle([x1, y1, x2, y2], fill=col, outline=None)
