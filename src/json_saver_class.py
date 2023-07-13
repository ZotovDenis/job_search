import json
import os
from abc import ABC, abstractmethod


class VacancyFileManager(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy_data):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass


class JSONSaver(VacancyFileManager):

    def add_vacancy(self, data: dict) -> None:
        """Добавляет вакансии в список и сохраняет его в JSON файл."""
        with open("my_vacancies.json", "a", encoding="utf-8") as file:
            if os.stat("my_vacancies.json").st_size == 0:
                json.dump([data], file, ensure_ascii=False)
            else:
                with open("my_vacancies.json", encoding="utf-8") as json_file:
                    data_list = json.load(json_file)
                data_list.append(data)
                with open("my_vacancies.json", "w", encoding="utf-8") as json_file:
                    json.dump(data_list, json_file, ensure_ascii=False)

    def get_vacancies(self, interval="0-0"):
        """Сохраняет в отдельный список вакансии, соответствующие заданному интервалу по зарплате."""
        filtered_vacs = []
        salary_filter = interval.split('-')
        with open("my_vacancies.json", "r", encoding="utf-8") as file:
            all_info = json.load(file)
            for vacancy in all_info:
                if int(salary_filter[0]) <= vacancy["salary_from"] or \
                        int(salary_filter[0]) <= vacancy["salary_to"] <= int(salary_filter[1]):
                    filtered_vacs.append(vacancy)

        return filtered_vacs

    def delete_vacancy(self, vacancy_id):
        """Удаляет вакансии из списка в JSON файле по 'vacancy_id', и перезаписывает список."""
        # Открытие JSON файла
        with open("my_vacancies.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Удаление словарей с ключом 'vacancy_id' равным переданному значению
        data = [dictionary for dictionary in data if dictionary["vacancy_id"] != vacancy_id]

        # Перезапись конечного списка в JSON файл
        with open("my_vacancies.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
