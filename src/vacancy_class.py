class Vacancy:
    """Класс для работы с каждой отдельной вакансией из полученного списка с HeadHunter и SuperJob"""

    def __init__(self, title: str, vacancy_url: str, vacancy_id: int, company_name: str, work_place: str,
                 salary_from: int, salary_to: int, salary_currency: str, experience: str) -> None:
        self.title = title
        self.vacancy_url = vacancy_url
        self.vacancy_id = vacancy_id
        self.company_name = company_name
        self.work_place = work_place
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.experience = experience

        self.info = dict(title=self.title, vacancy_url=self.vacancy_url, vacancy_id=self.vacancy_id,
                         company_name=self.company_name, work_place=self.work_place,
                         salary_from=self.salary_from, salary_to=self.salary_to,
                         salary_currency=self.salary_currency, experience=self.experience)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Вакансия: {self.title}\n" \
               f"Ссылка на вакансию: {self.vacancy_url}\n" \
               f"ID: {self.vacancy_id}\n" \
               f"Компания: {self.company_name}\n" \
               f"Место работы: {self.work_place}\n" \
               f"Зарплата: {self.salary_from} - {self.salary_to} {self.salary_currency}\n" \
               f"Опыт: {self.experience}"

    def __repr__(self):
        """ Возвращает читаемое строковое представление объекта класса."""
        return f"{self.__class__.__name__}('{self.title}', {self.vacancy_url}, {self.vacancy_id}, " \
               f"{self.company_name}, {self.work_place}, {self.experience}, " \
               f"{self.salary_from}, {self.salary_to}, {self.salary_currency})"

    def __eq__(self, other):
        """Проверяет, равны ли объект self и объект other по значению атрибута 'salary_from'."""
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        """Сравнивает объект self с объектом other на основе значения атрибута 'salary_from'."""
        return self.salary_from < other.salary_from

    def validate_salary(self):
        """Проверяет, является ли значение переменной salary_from целым числом и больше или равным нулю."""
        if isinstance(self.salary_from, int) and self.salary_from >= 0:
            return True
        return False
