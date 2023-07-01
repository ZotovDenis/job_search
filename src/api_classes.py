import os
from abc import ABC, abstractmethod

import requests

from json_saver_class import JSONSaver
from vacancy_class import Vacancy


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
        """Подключение к API HeadHunter"""

        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,  # Ключевое слово
            "per_page": quantity,  # Количество вакансий для вывода
            "only_with_salary": 'true'  # Только с информацией по зарплате
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
            vacancy_id = vacancy.get("id")
            company_name = vacancy.get("employer").get("name")
            work_place = vacancy.get("area").get("name")
            salary_from = vacancy.get("salary").get("from")

            if salary_from is None:
                salary_from = 0

            salary_to = vacancy.get("salary").get("to")

            if salary_to is None:
                salary_to = 0

            salary_currency = vacancy.get("salary").get("currency")
            experience = vacancy.get("experience").get("name")

            vac = Vacancy(title, vacancy_url, vacancy_id, company_name, work_place,
                          salary_from, salary_to, salary_currency, experience)
            print("----------------------------------------------------------------------------------------------")
            print(vac)
            user_answer = input("Добавить вакансию? (ДА/НЕТ) ").lower()
            if user_answer == "да" or user_answer == "yes" or user_answer == "lf":
                my_object = JSONSaver()
                my_object.add_vacancy(vac.info)
            elif user_answer == "стоп" or user_answer == "stop":
                break
            else:
                continue


class SuperJobAPI(API):
    """Класс для поиска вакансий на SuperJob"""

    base_url = "https://api.superjob.ru/2.0/vacancies"
    api_key: str = os.getenv('SJ_API_KEY')

    def search_vacancies(self, keyword, quantity=15):
        """Подключение к API SuperJob"""

        params = {
            "keyword": keyword,  # Ключевое слово
            "count": quantity  # Количество вакансий для вывода
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
            vacancy_id = vacancy.get("id")
            company_name = vacancy.get("client").get("title")
            work_place = vacancy.get("town").get("title")
            salary_from = vacancy.get("payment_from") if not None else 0
            salary_to = vacancy.get("payment_to") if not None else 0
            salary_currency = vacancy.get("currency")
            experience = vacancy.get("experience").get("title")

            vac = Vacancy(title, vacancy_url, vacancy_id, company_name, work_place,
                          salary_from, salary_to, salary_currency, experience)
            print("----------------------------------------------------------------------------------------------")
            print(vac)
            user_answer = input("Добавить вакансию? (ДА/НЕТ) ").lower()
            if user_answer == "да" or user_answer == "yes" or user_answer == "lf":
                my_object = JSONSaver()
                my_object.add_vacancy(vac.info)
            elif user_answer == "стоп" or user_answer == "stop":
                break
            else:
                continue
