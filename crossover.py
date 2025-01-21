# Словарь для хранения вопросов и ответов
questions = {
    "1": {"question": "Столица Франции", "answer": "Париж"},
    "2": {"question": "Самый большой океан", "answer": "Тихий"},
    "3": {"question": "Основное топливо для автомобилей", "answer": "Бензин"},
    "4": {"question": "Главный герой романа 'Война и мир'", "answer": "Пьер"},
    "5": {"question": "Единица измерения скорости звука", "answer": "Мах"},
    "6": {"question": "Самая длинная река в мире", "answer": "Нил"},
    "7": {"question": "Самое большое число в ряду от 0 до 9",
           "answer": "Девять"},
    "8": {"question": "Первый космонавт Земли", "answer": "Гагарин"}
}


def main():
    print("Добро пожаловать в кроссворд!")

    for key in questions:
        question = questions[key]["question"]
        answer = input(f"{key}. {question}: ").strip().title()

        if answer == questions[key]["answer"]:
            print("Правильно! Продолжаем.")
        else:
            print(f"Неправильно. Правильный ответ: {questions[key]['answer']}")


if name == "main":
    main()
