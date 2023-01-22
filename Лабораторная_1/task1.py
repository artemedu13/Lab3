import doctest

class Bowling:

    def __init__(self, opponents_score: int, number_of_pins_dropped: int):
        self.opponents_score = opponents_score
        if number_of_pins_dropped < 0:
            raise ValueError ("Ошибка считывателя, игра не засчитана")
        self.number_of_pins_dropped = number_of_pins_dropped

    def hit_rate(self) -> str:
        if self.number_of_pins_dropped == 0:
            return 'Аут'
        elif self.number_of_pins_dropped == 10:
            return 'Страйк'
        else:
            return 'Кегли сбиты'

    def game_result(self) -> str:
        if self.opponents_score < self.number_of_pins_dropped:
            return 'Победа'
        if self.opponents_score > self.number_of_pins_dropped:
            return 'Проигрыш'
        else:
            return 'Ничья'

game_1 = Bowling(6, 1)
game_2 = Bowling(8, 1)

print("Боулинг")
print(game_1.hit_rate(), ", засчитан(а)", game_1.game_result())
print(game_2.hit_rate(), ", засчитан(а)", game_2.game_result())

if __name__ == "__main__":
    doctest.testmod()

class Printer:

    def __init__(self, paper_in_tray: int, one_picture_paint: int, pages_to_print: int, color_pictures: int):
        self.paper_in_tray = paper_in_tray
        if paper_in_tray < 0:
            raise ValueError ("Число не может быть отрицательным, печать невозможна!")
        self.one_picture_paint = one_picture_paint
        if one_picture_paint < 0:
            raise ValueError ("Число не может быть отрицательным, печать невозможна!")
        self.pages_to_print = pages_to_print
        if pages_to_print < 0:
            raise ValueError("Число не может быть отрицательным, печать невозможна!")
        self.color_pictures = color_pictures
        if color_pictures < 0:
            raise ValueError("Число не может быть отрицательным, печать невозможна!")

    def check_printability(self) -> str:
        if self.pages_to_print >= self.paper_in_tray:
            return "Документ будет напечатан не полностью"
        else:
            return "ОК"

    def check_printability_for_color(self) -> str:
        if self.one_picture_paint < self.color_pictures:
            return "Краски не хватит на все изображения"
        else:
            return "ОК"

doc_1 = Printer(1, 2, 1, 2)
doc_2 = Printer(4, 3, 2, 6)

print("Принтер")
print("Проверка кол-во бумаги для печати:", doc_1.check_printability(), ", Проверка кол-во краски для печати:", doc_1.check_printability_for_color())
print("Проверка кол-во бумаги для печати:", doc_2.check_printability(), ", Проверка кол-во краски для печати:", doc_2.check_printability_for_color())

class Juice:

    def __init__(self, number_of_package: int, finished_products: int, right_amount: int):
        self.number_of_package = number_of_package
        if number_of_package < 0:
            raise ValueError("Ошибка конвейера, производство невозможно!")
        self.finished_products = finished_products
        if finished_products < 0:
            raise ValueError("Ошибка конвейера, производство невозможно!")
        self.right_amount = right_amount
        if right_amount < 0:
            raise ValueError("Число не может быть отрицательным!")

    def pipeline_error_checking (self) -> str:
        if self.number_of_package == self.finished_products:
            return "Ошибок нет"
        else:
            return "Проверьте ленту конвейера"

    def profitability(self) -> str:
        if self.finished_products > self.right_amount:
            return "+"
        else:
            return "-"

variant_1 = Juice(25, 25, 30)
variant_2 = Juice(12, 13, 40)

print("Производство сока")
print("Проверка потери пакетов на ленте:", variant_1.pipeline_error_checking(), ", Рентабильность:", variant_1.profitability())
print("Проверка потери пакетов на ленте:", variant_2.pipeline_error_checking(), ", Рентабильность:", variant_2.profitability())
#Конец