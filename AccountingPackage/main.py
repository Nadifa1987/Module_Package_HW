from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date
import emoji



if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print('Потерпите, сегодня уже', date.today())
    print(emoji.emojize("Всем добра :red_heart:"))



