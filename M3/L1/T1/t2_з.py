'''
Ця програма - приклад використання власної функції! Прочитай код, запусти і подивися, як вона працює!
У цьому завданні немає автоматичної перевірки! Коли закінчиш вивчати програму, просто переходь на наступний рівень.

'''


def dialog(question, right_answer, comment1, comment2):
    s = input(question)
    if s == right_answer:
        print(comment1)
    else:
        print(comment2)


dialog("Ти любиш програмувати?", "так", "Ми подружимося", "А ти спробуй!")
dialog("Скільки буде двічі два?", "4", "Звичайно", "Давай перерахуємо?")
dialog("А у тебе є домашні тварини?", "так", "Здорово!", "І у мене немає ...")
dialog("А я вже питав, чи любиш ти програмувати?",
       "так", "О, я й забув.", "Питав, ти забув!")
dialog("Знаєш, як записати 4 в двійковій системі? Напиши!",
       "100", "Точно, 100!", "Ні, 100")
