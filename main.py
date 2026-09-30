from storage import JunkStorage
from storage import JunkItem

storage = JunkStorage()
junk_items = [
    JunkItem("Бляшанка", 5, 2.5),
    JunkItem("Стара плата", 3, 7.8),
    JunkItem("Купка дротів", 10, 1.2)
]

storage.serialize(junk_items, "junk-storage.txt")
junk_items = storage.parse("junk-storage.txt")
for item in junk_items:
    print(item.name, item.quantity, item.value)
