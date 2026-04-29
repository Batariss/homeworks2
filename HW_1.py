vacancies = [
    {"id": 1, "title": "Python Developer", "company": "TechCorp", "city": "Kyiv", "salary": 1800, "remote": True},
    {"id": 2, "title": "Frontend Engineer", "company": "WebWorks", "city": "Lviv", "salary": 1500, "remote": False},
    {"id": 3, "title": "Data Analyst", "company": "DataLine", "city": "Kyiv", "salary": 1400, "remote": True},
    {"id": 4, "title": "DevOps Specialist", "company": "CloudSolutions", "city": "Kharkiv", "salary": 2200, "remote": False},
    {"id": 5, "title": "QA Engineer", "company": "TestMasters", "city": "Odesa", "salary": 1300, "remote": True},
    {"id": 6, "title": "Project Manager", "company": "PlanIt", "city": "Dnipropetrovsk", "salary": 1700, "remote": False},
    {"id": 7, "title": "Backend Developer", "company": "BuildIt", "city": "Lviv", "salary": 1900, "remote": True},
    {"id": 8, "title": "UI/UX Designer", "company": "DesignHub", "city": "Kyiv", "salary": 1600, "remote": False},
    {"id": 9, "title": "Mobile Developer", "company": "AppWorks", "city": "Odesa", "salary": 2100, "remote": True},
    {"id": 10, "title": "Support Engineer", "company": "HelpDesk", "city": "Kharkiv", "salary": 1200, "remote": False},
]


def print_vacancy(vacancy):
    remote_text = "Remote" if vacancy["remote"] else "On-site"
    print(
        f"{vacancy['id']}. {vacancy['title']} at {vacancy['company']} - {vacancy['city']}, "
        f"salary: ${vacancy['salary']}, {remote_text}"
    )


def show_all(vacancies_list=None):
    if vacancies_list is None:
        vacancies_list = vacancies
    if not vacancies_list:
        print("No vacancies found.")
        return
    for vacancy in vacancies_list:
        print_vacancy(vacancy)


def filter_only_remote():
    return [job for job in vacancies if job["remote"]]


def filter_by_salary(min_salary):
    return [job for job in vacancies if job["salary"] > min_salary]


def filter_by_city_and_salary(city, min_salary):
    return [job for job in vacancies if job["city"].lower() == city.lower() and job["salary"] > min_salary]


def average_salary():
    total = sum(job["salary"] for job in vacancies)
    return total / len(vacancies) if vacancies else 0


def most_expensive_vacancy():
    return max(vacancies, key=lambda job: job["salary"])


def input_integer(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")


def main():
    print("Welcome to Vacancy Finder")
    print(f"Average salary: ${average_salary():.2f}")
    top_job = most_expensive_vacancy()
    print("Most expensive vacancy:")
    print_vacancy(top_job)
    print()

    while True:
        print("Menu:")
        print("1 - Show all vacancies")
        print("2 - Filter by city")
        print("3 - Filter by salary")
        print("4 - Only remote")
        print("5 - Exit")

        choice = input("Choose an option (1-5): ").strip()
        print()

        if choice == "1":
            show_all()
        elif choice == "2":
            city = input("Enter city name: ").strip()
            results = [job for job in vacancies if job["city"].lower() == city.lower()]
            show_all(results)
        elif choice == "3":
            salary_limit = input_integer("Enter minimum salary (X): ")
            show_all(filter_by_salary(salary_limit))
        elif choice == "4":
            show_all(filter_only_remote())
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select 1-5.")

        print()


if __name__ == "__main__":
    main()
