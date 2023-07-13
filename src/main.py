from api_classes import HeadHunterAPI
from api_classes import SuperJobAPI
from json_saver_class import JSONSaver


def headhunter_vacancies_search():
    """Функция для поиска вакансий на Headhunter."""
    hh_api = HeadHunterAPI()
    search_query = input("Введите через пробел ключевые слова, в том числе город поиска: ")
    vacancy_quantity = input("Введите количество вакансий: ")
    if search_query != '' and vacancy_quantity != '' and vacancy_quantity.isdigit():
        search_vacancies = hh_api.search_vacancies(search_query, vacancy_quantity)
        hh_api.get_vacancy_info(search_vacancies)
    else:
        print("Введите требуемые значения.")
        headhunter_vacancies_search()


def superjob_vacancies_search():
    """Функция для поиска вакансий на SuperJob."""
    superjob_api = SuperJobAPI()
    search_query = input("Введите через пробел ключевые слова, в том числе город поиска: ")
    vacancy_quantity = input("Введите количество вакансий: ")
    if search_query != '' and vacancy_quantity != '' and vacancy_quantity.isdigit():
        search_vacancies = superjob_api.search_vacancies(search_query, vacancy_quantity)
        superjob_api.get_vacancy_info(search_vacancies)
    else:
        print("Введите требуемые значения.")
        superjob_vacancies_search()


def get_top_vacancies(sorted_vacancies_list, n=1_000_000_000):
    """Возвращает n самых популярных вакансий из отсортированного списка sorted_vacancies_list."""
    if n <= len(sorted_vacancies_list):
        top = sorted_vacancies_list[:n]
        return top
    elif n > len(sorted_vacancies_list):
        return sorted_vacancies_list


def return_sorted_vacancies(sorted_vacancies_list):
    """Выводит вакансии в удобочитаемом виде"""
    for vac in sorted_vacancies_list:
        for key, value in vac.items():
            print(f"{key}: {value}")
        print('--------------------------------------------')


def search():
    """Выбирает платформу для поиска вакансий и вызывает соответствующую функцию."""
    platforms = input("Выберите платформу для поиска вакансии: HeadHunter или SuperJob? ").lower()
    if platforms == "hh" or platforms == "headhunter" or platforms == "хх":
        headhunter_vacancies_search()
    elif platforms == "sj" or platforms == "superjob" or platforms == "сд":
        superjob_vacancies_search()


def main():
    my_object = JSONSaver()
    search()
    continue_search = input("Продолжить поиск на другой платформе? ")
    if continue_search == "да" or continue_search == "yes" or continue_search == "lf":
        search()

    salary_interval = input("Введите интервал зарплаты в формате 'XXXXX-YYYYY', где XXXXX-нижняя планка зарплаты, "
                            "YYYYY-верхняя планка зарплаты: ")
    my_list_by_salary = my_object.get_vacancies(salary_interval)

    sorted_list = sorted(my_list_by_salary, key=lambda x: x["salary_from"], reverse=True)

    if not sorted_list:
        print("Нет вакансий, соответствующих заданным критериям.")
    else:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        top_vacancies = get_top_vacancies(sorted_list, top_n)
        print("--------------------------------")
        return_sorted_vacancies(top_vacancies)

    while True:
        result = input("Продолжить работу или завершить? (ПРОДОЛЖИТЬ/ЗАВЕРШИТЬ) ").lower()
        if result == "завершить" or result == "стоп":
            print("Программа завершена.")
            break
        if result == "продолжить" or result == "да":
            print("Выберите действие:\n"
                  "1. Произвести повторный поиск вакансий\n"
                  "2. Вывести N вакансий из сохраненного отсортированного списка\n"
                  "3. Удалить вакансию")

            continue_actions = input()
            if continue_actions == "1":
                search()
            elif continue_actions == "2":
                my_vacancies_list = my_object.get_vacancies()
                sortd_list = sorted(my_vacancies_list, key=lambda x: x["salary_from"], reverse=True)
                top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                top_vacancies = get_top_vacancies(sortd_list, top_n)
                print("--------------------------------")
                return_sorted_vacancies(top_vacancies)
            elif continue_actions == "3":
                del_vac = input("Введите ID вакансии, которую вы хотите удалить: ")
                my_object.delete_vacancy(del_vac)
                print("Вакансия удалена.")
            elif continue_actions == "завершить" or result == "стоп":
                print("Программа завершена.")
                break


if __name__ == "__main__":
    main()
    input()
