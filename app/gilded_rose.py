class Gilded_rose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        pass


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Normal_item(Item):
    def __init__(self, update_quality, set_sell_in):
        self.update_quality = update_quality
        self.set_sell_in = set_sell_in

    def set_sell_in(self):
        self.set_sell_in - 1

    def update_quality(self):
        if self.update_quality < 50 and self.update_quality > 0:
            self.update_quality - 1
