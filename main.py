from file_storage import FileJunkStorage
from item import JunkItem
from repository import JunkRepository

# storage = FileJunkStorage()
config = {"storage": "file", "filename": "junk-storage.txt"}

junk_items = [
    JunkItem("Бляшанка", 5, 2.5),
    JunkItem("Стара плата", 3, 7.8),
    JunkItem("Купка дротів", 10, 1.2)
]

def choose_storage(config:dict) -> JunkRepository:
    if(config["storage"]=="file"):
        return FileJunkStorage(config["filename"])
    #else:
        # here we can return any other storage:
        # some CloudJunkStorage, for example

storage = choose_storage(config)
storage.save(junk_items)
storage.load()
print("Ось що міститься на нашому складі:")
for item in junk_items:
    print(item.name, item.quantity, item.value)
