from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создаем соединение к базе данных
engine = create_engine('sqlite:///:memory:', echo=True)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Задание: Напишите запросы для следующих операций
# 1. Добавление студента в базу данных
# 2. Добавление курса в базу данных
# 3. Привязка студента к курсу
# 4. Получение списка всех студентов
# 5. Получение списка всех курсов для конкретного студента