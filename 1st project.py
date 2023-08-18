class GroceryList:
  def __init__(self):
    self.items = []
    self.size = 0

  def add(self, item):
    self.items.append(item)
    self.size += 1

  def total_cost(self):
    total_cost = 0
    for item in self.items:
      total_cost += item.cost(item.quantity)
    return total_cost

class GroceryItemOrder:
  def __init__(self, name, quantity, price_per_unit):
    self.name = name
    self.quantity = quantity
    self.price_per_unit = price_per_unit

  def cost(self, item):
    return item * self.price_per_unit

  def quantity(self):
    return self.quantity

item1 = GroceryItemOrder("boxes of cookies", 4, 2.5)
item2 = GroceryItemOrder("watermelons", 100, 1.5)

grocery_list = GroceryList()
grocery_list.add(item1)
grocery_list.add(item2)

print("Grocery List:")
for i, item in enumerate(grocery_list.items, start = 1):
  print(f"Item {i}: {item.quantity} {item.name} at ${item.price_per_unit:.2f} each")

print(f"Total cost: ${grocery_list.total_cost():.2f}")