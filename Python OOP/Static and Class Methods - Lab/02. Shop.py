class Shop:
    kind = "online"
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        cls.kind = "physical"
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity > 0:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            self.capacity -= 1
            return f"{item_name} added to the shop"
        return f"Not enough capacity in the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            self.capacity += amount
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} " \
               f"with capacity {self.capacity}"