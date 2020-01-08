from item import Item
from normal_item import Normal_item
from aged_brie import Aged_brie
from backstage_passes import Backstage_passes
from sulfuras import Sulfuras
from conjured import Conjured


class Gilded_rose(object, Normal_item):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.inventario:
            self.update_quality()

    def items(self):
        lista_items = Gilded_rose([
            Normal_item("+ 5 Dexterity Vest", 10, 20),
            Aged_brie("Aged Brie", 2, 0),
            Normal_item("Elixir of the Mongoose", 5, 7),
            Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
            Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
            Backstage_passes(
                "Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Backstage_passes(
                "Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Backstage_passes(
                "Backstage passes to a TAFKAL80ETC concert", 5, 49),
            Conjured("Conjured Mana Cake", 3, 6)])
        for day in range(1, 31):
            lista_items.update_quality()
        return lista_items.updated_item()

    def get_item(self):
        return self.items


if __name__ == "__main__":
    lista_items = Gilded_rose([
        Normal_item("+ 5 Dexterity Vest", 10, 20),
        Aged_brie("Aged Brie", 2, 0),
        Normal_item("Elixir of the Mongoose", 5, 7),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        Backstage_passes("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Conjured("Conjured Mana Cake", 3, 6)])
