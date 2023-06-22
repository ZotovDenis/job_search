import os
from abc import ABC, abstractmethod

import requests


class API(ABC):

    @abstractmethod
    def search_vacancies(self, keyword, quantity=15):
        """Подключение к API и получение вакансий"""
        pass

    @abstractmethod
    def get_vacancy_info(self, response):
        """Получение информации по вакансии"""
        pass


class HeadHunterAPI(API):
    """Класс для поиска вакансий на HeadHunter"""

    hh_base_url = 'https://api.hh.ru/vacancies'

    def search_vacancies(self, keyword, quantity=15, page=1):
        """Подключаемся к API HeadHunter"""

        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,  # Ключевое слово
            "per_page": quantity,  # Количество вакансий для вывода
            "only_with_salary": 'true'
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            vacancies = response.json().get("items")
            return vacancies
        else:
            print(f"Не удалось выполнить запрос к API HeadHunter")

    def get_vacancy_info(self, vacancies):
        """Получение информации, необходимой для создания экземпляра вакансии класса Vacancy"""

        for vacancy in vacancies:
            title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer").get("name")
            work_place = vacancy.get("area").get("name")
            salary_from = vacancy.get("salary").get("from") if not None else 0
            salary_to = vacancy.get("salary").get("to") if not None else 0
            salary_currency = vacancy.get("salary").get("currency")
            experience = vacancy.get("experience").get("name")

            # return title, vacancy_url, company_name, work_place, salary_from, salary_to, salary_currency, experience

            print(f"Компания: {company_name}")
            print(f"Вакансия: {title}")
            print(f"Зарплата: от {salary_from} до {salary_to} {salary_currency}")
            print(f"Опыт: {experience}")
            print(f"Город: {work_place}")
            print(f"Ссылка на вакансию: {vacancy_url}")
            # print(vacancy)
            print("----------------------------------------------------------------------------")


class SuperJobAPI(API):
    """Класс для поиска вакансий на SuperJob"""

    base_url = "https://api.superjob.ru/2.0/vacancies"
    api_key: str = os.getenv('SJ_API_KEY')

    def search_vacancies(self, keyword, quantity=15):
        """Подключаемся к API SuperJob"""

        params = {
            "keyword": keyword,  # Ключевое слово
            "count": quantity,  # Количество вакансий для вывода
            "town": "Москва"
        }

        headers = {"X-Api-App-Id": self.api_key}

        response = requests.get(self.base_url, params=params, headers=headers)
        if response.status_code == 200:
            vacancies = response.json().get("objects")
            return vacancies
        else:
            print("Не удалось выполнить запрос к API SuperJob")

    def get_vacancy_info(self, vacancies):
        """Получение информации, необходимой для создания экземпляра вакансии класса Vacancy"""

        for vacancy in vacancies:
            title = vacancy.get("profession")
            vacancy_url = vacancy.get("link")
            company_name = vacancy.get("client").get("title")
            work_place = vacancy.get("town").get("title")
            salary_from = vacancy.get("payment_from") if not None else 0
            salary_to = vacancy.get("payment_to") if not None else 0
            salary_currency = vacancy.get("currency")
            experience = vacancy.get("experience").get("title")

            # return title, vacancy_url, company_name, work_place, salary_from, salary_to, salary_currency, experience

            print(f"Компания: {company_name}")
            print(f"Вакансия: {title}")
            print(f"Зарплата: от {salary_from} до {salary_to} {salary_currency}")
            print(f"Опыт: {experience}")
            print(f"Город: {work_place}")
            print(f"Ссылка на вакансию: {vacancy_url}")
            print("----------------------------------------------------------------------------------------------")


if __name__ == '__main__':

    print("---------------------------HeadHunter----------------------------------")
    hh_example = HeadHunterAPI()

    hh_example.get_vacancy_info(hh_example.search_vacancies("Python Developer Москва", 10))

    print()
    print("---------------------------SuperJob----------------------------------")
    print()

    sj_example = SuperJobAPI()

    sj_example.get_vacancy_info(sj_example.search_vacancies("postgresql Москва", 10))
