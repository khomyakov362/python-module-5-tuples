def choose_dictionary() -> dict:
    
    words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
    }

    words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
    }

    words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
    }

    user_input = input('Введите уровень сложности: "простой", "средний" или "сложный": ').lower().strip()
    match user_input:
        case "простой":
            return words_easy
        case "средний":
            return words_medium
        case "сложный":
            return words_hard
        case _:
            print('Некорректный ввод!') 
            return choose_dictionary()

def check_word(key : str, value : str) -> bool:

    user_input = input(f'Слово :{key}, {len(value)} букв, первая буква: {value[0]}... Ваш ответ: ').lower().strip()

    if user_input == value:
        print(f'Верно: {key} - это {value}.\n')
        return True
    else:
        print(f'Неверно: {key} - это {value}.\n')
        return False

def check_dictionary(dictionary : dict) -> dict:
    answers = {}

    for key, value in dictionary.items():
        answers[key] = check_word(key, value)
    
    return answers

def print_results(answers : dict) -> None:
    
    levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
    }

    correct = [key for key in answers if answers[key]]
    incorrect = [key for key in answers if not answers[key]]
    
    if len(correct) > 0:
        print('Ваши правильные ответы: ')
        for answer in correct:
            print(answer)
        print()
    if len(incorrect) > 0:
        print('Ваши неправиьные ответы: ')
        for answer in incorrect:
            print(answer)
        print()
    
    level = levels[len(correct)]
    print(f'Ваш уровень:\n{level}')

dictionary = choose_dictionary()
print(dictionary)
answers = check_dictionary(dictionary)
print_results(answers)
