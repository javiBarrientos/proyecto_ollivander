from gilded_rose import Normal_item


class Aged_brie(Normal_item):
    def __init__(self, name, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self):
        if self.sell_in > 0:
            self.quality + 1
            return self.quality
        else:
            self.quality + 2
            return self.quality

    def set_sell_in(self):
        self.sell_in - 1
        return self.sell_in
