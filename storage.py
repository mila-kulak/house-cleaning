class JunkItem:
    def __init__(self, name:str, quantity:int, value:float):
        self.name = name
        self.quantity = quantity
        self.value = value


class JunkStorage:

    #Записує список предметів у файл у власному форматі CSV
    def serialize(self, items: list[JunkItem], filename: str):
        item_info_lines = []
        item_line=""

        # Валідація
        for item in items:
            try:
                quantity = int(item.quantity)
                value = float(item.value)
            except:
                print(f"У предметі '{item.name}' ціна та кількість повинні бути вказані числами\nЗмініть це, щоб даний предмет міг бути записаним у файл")
                item_line=""
            else:
                quantity = str(item.quantity)
                value = str(item.value).replace(".", ",")
                item_line = f"{item.name} > {quantity} шт. > {value} грн\n"

            if(item_line!=""):
                item_info_lines.append(item_line)

        # Запис у файл
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for line in item_info_lines:
                    file.write(line)
            print("Дані у файлик записані успішно ✅")

        except OSError as e:
            print(f"Помилка роботи з файлом... {e}")

    #Читає та відновлює об'єкти JunkItem із файлу
    def parse(self, filename: str) -> list[JunkItem]:
        junk_items=[]
        lines_in_file=[]
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    lines_in_file.append(line)

        except FileNotFoundError:
            print("Файл з таким іменем не знайдено...")

        # Прибираємо зайве, декомпозуємо
        try:
            for line in lines_in_file:
                line=line.strip().replace(" шт.", "").replace("грн", "")
                name, quantity, value = line.split(" > ")
                quantity=int(quantity)
                value=value.replace(",", '.')
                value=float(value)
                junk_items.append(JunkItem(name, quantity, value))
            return junk_items
        except Exception as e:
            print(f"Помилка... {e}")
