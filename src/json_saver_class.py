import json


class JSONSaver:
    """
    Класс для добавления вакансий в файл, получения данных из файла
    по указанным критериям и удаления информации о вакансиях
    """
    vacancies = []

    def save_vacancies(self, data):
        """Метод, сохраняющий в файл информацию по вакансиям"""
        with open("my_vacancies.json", "a", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

    def load_vacancies(self):
        """Метод для чтения JSON данных из файла и преобразования их в словарь Python"""
        try:
            with open("my_vacancies.json", "r", encoding="utf-8") as file:
                self.vacancies = json.load(file)
                return self.vacancies
        except FileNotFoundError:
            self.vacancies = []

    def add_vacancies(self, data):
        """Метод для добавления вакансии в список вакансий"""
        self.vacancies.append(data)
