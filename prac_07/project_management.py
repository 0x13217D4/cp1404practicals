import datetime
from operator import attrgetter
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"
HEADER = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load from: ")
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print(f"{filename} not found")
        elif choice == "S":
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").lower()
    if save_choice.startswith("y"):
        save_projects(DEFAULT_FILENAME, projects)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILENAME}")
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.datetime.strptime(parts[1], DATE_FORMAT).date()
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, "w", encoding="utf-8") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime(DATE_FORMAT)}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    incomplete_projects = sorted([project for project in projects if not project.is_complete()])
    completed_projects = sorted([project for project in projects if project.is_complete()])
    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    filter_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    for project in sorted(filtered_projects, key=attrgetter("start_date")):
        print(project)


def add_project(projects):
    print("Let's add a new project")
    name = get_valid_name("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ", int)
    cost_estimate = get_valid_number("Cost estimate: $", float)
    completion_percentage = get_valid_number("Percent complete: ", int)
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    for i, project in enumerate(projects):
        print(i, project)
    project_index = get_valid_index("Project choice: ", len(projects))
    project = projects[project_index]
    print(project)
    new_percentage = get_optional_number("New Percentage: ")
    if new_percentage is not None:
        project.completion_percentage = new_percentage
    new_priority = get_optional_number("New Priority: ")
    if new_priority is not None:
        project.priority = new_priority


def get_valid_name(prompt):
    name = input(prompt).strip()
    while name == "":
        print("Name cannot be blank")
        name = input(prompt).strip()
    return name


def get_valid_date(prompt):
    while True:
        date_string = input(prompt)
        try:
            return datetime.datetime.strptime(date_string, DATE_FORMAT).date()
        except ValueError:
            print("Invalid date, please use d/m/yyyy")


def get_valid_number(prompt, number_type):
    while True:
        try:
            number = number_type(input(prompt))
            if number >= 0:
                return number
            print("Number must be >= 0")
        except ValueError:
            print("Invalid input; enter a valid number")


def get_optional_number(prompt):
    while True:
        value = input(prompt)
        if value == "":
            return None
        try:
            number = int(value)
            if number >= 0:
                return number
            print("Number must be >= 0")
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_index(prompt, number_of_items):
    while True:
        try:
            index = int(input(prompt))
            if 0 <= index < number_of_items:
                return index
            print("Invalid project choice")
        except ValueError:
            print("Invalid input; enter a valid number")


main()
