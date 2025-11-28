class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


rectangles = [
    Rectangle(5, 10),
    Rectangle(3, 7),
    Rectangle(8, 4)
]

for i, rect in enumerate(rectangles, 1):
    print(f"Прямоугольник {i}: {rect.width}x{rect.height}")
    print(f"  Площадь: {rect.get_area()}")
    print(f"  Периметр: {rect.get_perimeter()}")
    print()


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"{self.a} + {self.b} = {result}")

    def multiplication(self):
        result = self.a * self.b
        print(f"{self.a} * {self.b} = {result}")

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"{self.a} / {self.b} = {result}")
        else:
            print(f"{self.a} / {self.b} = Ошибка! Деление на ноль")

    def subtraction(self):
        result = self.a - self.b
        print(f"{self.a} - {self.b} = {result}")


numbers = [
    (15, 3),
    (20, 4),
    (9, 0)
]

for a, b in numbers:
    calc = Math(a, b)
    print(f"\nЧисла: {a} и {b}")
    calc.addition()
    calc.multiplication()
    calc.division()
    calc.subtraction()


class SidebarButton:
    def __init__(self, text):
        self.button_text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.button_text}"

    def __str__(self):
        return f"Кнопка: {self.button_text}"


# Создаем и используем кнопки
buttons = ["Text Box", "Check Box", "Radio Button", "Web Tables", "Buttons"]

print("Все кнопки сайдбара:")
for button_text in buttons:
    button = SidebarButton(button_text)
    print(f"- {button}")

print("\nКлики по кнопкам:")
for button_text in buttons:
    button = SidebarButton(button_text)
    print(button.click())
