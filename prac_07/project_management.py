"""
CP1404/CP5632 Practical - Saranraj Saravanan
Project Management

"""

import datetime


class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def update(self, percentage, new_priority):
        if percentage:
            self.completion = percentage
        if new_priority:
            self.priority = new_priority


def print_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def display_projects(incomplete, completed):
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects, filter_date):
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    return filtered_projects


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, estimate, completion)


def update_project(projects):
    display_projects(projects, [])
    choice = int(input("Project choice: "))
    project = projects[choice]

    print(project)
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))

    project.update(new_percentage, new_priority)


def main():
    projects = [
        Project("Organise Pantry", "20/07/2022", 1, 25.00, 55),
        Project("Build Car Park", "12/09/2021", 2, 600000.00, 95),
        Project("Mow Lawn", "31/10/2022", 3, 3.00, 0),
        Project("Record Music Video", "01/12/2022", 9, 250000.00, 0),
        Project("Read 7 Habits Book", "13/12/2021", 6, 99.00, 100)
    ]

    while True:
        print_menu()
        choice = input(">>> ").lower()

        if choice == 'd':
            incomplete_projects = [project for project in projects if project.completion < 100]
            completed_projects = [project for project in projects if project.completion == 100]
            display_projects(incomplete_projects, completed_projects)

        elif choice == 'u':
            update_project(projects)

        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)

        elif choice == 'f':
            filter_date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.datetime.strptime(filter_date_str, "%d/%m/%Y").date()
            filtered_projects = filter_projects_by_date(projects, filter_date)
            display_projects(filtered_projects, [])

        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break


if __name__ == "__main__":
    main()
