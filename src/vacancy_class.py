from src.json_saver_class import JSONSaver


class Vacancy:
    """Класс для работы с каждой отдельной вакансией из полученного списка с HeadHunter или SuperJob"""

    def __init__(self, title: str, vacancy_url: str, company_name: str, work_place: str,
                 salary_from: int, salary_to: int, salary_currency: str, experience: str):
        self.title = title
        self.vacancy_url = vacancy_url
        self.company_name = company_name
        self.work_place = work_place
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.experience = experience

        self.info = dict(title=self.title, vacancy_url=self.vacancy_url,
                         company_name=self.company_name, work_place=self.work_place,
                         salary_from=self.salary_from, salary_to=self.salary_to,
                         salary_currency=self.salary_currency, experience=self.experience)

    def __str__(self):
        return f"Вакансия: {self.title}\n" \
               f"Ссылка на вакансию: {self.vacancy_url}\n" \
               f"Компания: {self.company_name}\n" \
               f"Место работы: {self.work_place}\n" \
               f"Зарплата: {self.salary_from} - {self.salary_to} {self.salary_currency}\n" \
               f"Опыт: {self.experience}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.title}', {self.vacancy_url}, " \
               f"{self.company_name}, {self.work_place}, {self.experience}, " \
               f"{self.salary_from}, {self.salary_to}, {self.salary_currency})"

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from


if __name__ == "__main__":
    vacancy1 = Vacancy("Python Developer", "https://ya.ru", "Yandex", "Москва",
                       100_000, 200_000, "RUB", "от 3 лет")
    print(vacancy1.__repr__())
    print('----------------------------------------------------------------')
    print(vacancy1)
    my_object = JSONSaver()
    new_vacancy_list = my_object.add_vacancies(vacancy1.info)
    print(my_object.vacancies)

    vacancy2 = Vacancy("DevOps", "https://hh.ru", "HH", "Москва",
                       120_000, 200_000, "RUB", "от 6 лет")

    my_object = JSONSaver()
    new_vacancy_list1 = my_object.add_vacancies(vacancy2.info)
    print(my_object.vacancies)
    my_object.save_vacancies(my_object.vacancies)
