"""
ICFES Saber 11 Test in Colombia
Console-based interface for user interaction.

@author: Juan David Alfonso
"""

import saber11 as s11
import pandas as pd

def execute_load_data() -> pd.DataFrame:
    """Asks the user to enter the name of a CSV file containing the Saber 11 test data in Colombia.
    Returns: dict
        The dictionary of clubs with the information of the players in the file
    """
    data = None
    file = input("Please enter the name of the CSV file with the information of the Saber 11 tests: ")
    data = s11.load_data(file)
    if len(data) == 0:
        print("The selected file is not valid. The information could not be loaded.")
    else:
        print("The following data was loaded from the CSV file: ")
        print(data)
    return data

def execute_piechart_gender(dataframe: pd.DataFrame) -> None:
    """Executes the option to create a pie chart showing the gender distribution of schools."""
    s11.piechart_gender(dataframe)
    print("The gender distribution of schools was successfully charted!!!")

def execute_top10_departments(dataframe: pd.DataFrame) -> None:
    """Executes the option to create a bar chart of the top 10 departments that achieved the best results
    in a category specified by the user in the Saber 11 tests.
    """
    category = input("Enter the exam category for which you want to know the top 10: ")
    s11.top10_departments(dataframe, category)
    print("The top 10 departments with the best results in the Saber 11 tests in the category", category, "were successfully charted!!!")

def execute_evaluation_categories(dataframe: pd.DataFrame) -> None:
    """Executes the option to create a box plot diagram showing the distribution of scores by category
    in the Saber 11 tests.
    """
    s11.evaluation_categories(dataframe)
    print("The box plot diagram of the score distribution for the Saber 11 tests was successfully charted!!!")

def execute_create_matrix(dataframe: pd.DataFrame) -> tuple:
    """Executes the option to build the matrix of Department vs. Number of households that have a given
    appliance/service/device.
    """
    matrix = s11.create_matrix(dataframe)
    print("The assembled matrix of Department vs. Number of households with a service/appliance/device is:")
    print(matrix)
    return matrix

def execute_department_most_appliances(matrix: tuple) -> None:
    """Executes the option to find the department with the highest number of appliances (washing machines
    and microwaves). The message displayed to the user follows the format:
        'The department with the highest number of appliances is (department)'.
    """
    highest = s11.department_most_appliances(matrix)
    print("The department with the highest number of appliances is", highest)

def execute_count_appliances(matrix: tuple) -> None:
    """Executes the option to count the number of students in the country who have a given
    appliance/service/device. The message displayed to the user follows the format:
        'There are (quantity) people with the appliance/service/device (device) in the country.'
    """
    device = input("Enter the appliance/service/device for which you want to obtain the total count: ")
    quantity = s11.count_appliances(matrix, device)
    print("There are", quantity, "people with the appliance/service/device", device, "in the country.")

def execute_ICV_department(matrix: tuple) -> None:
    """Executes the option to calculate the Quality of Life Index (ICV) for a given department.
    The message displayed to the user follows the format:
        'The Quality of Life Index (ICV) for the department (department) is (index)'
    """
    department = input("Enter the department for which you want to know the Quality of Life Index: ")
    ICV = s11.ICV_department(matrix, department)
    print("The Quality of Life Index (ICV) for the department", department, "is", ICV)

def show_menu():
    """Prints the available execution options for the user."""
    print("\nOptions")
    print("1. Load data from the Saber 11 tests calendar A 2020 in Colombia.")
    print("2. Check the distribution of students in different genders of schools.")
    print("3. Check the top 10 departments in the Saber 11 tests in a given category.")
    print("4. Check the distribution of scores by category in the Saber 11 tests.")
    print("5. Construct the matrix of Departments vs. Number of households that have a given appliance/service/device.")
    print("6. Check the department with the highest number of appliances.")
    print("7. Check the number of students in the country who have a given appliance/service/device.")
    print("8. Check the Quality of Life Index of a given department.")
    print("9. Exit.")

def start_application():
    """Runs the program for the user."""
    continue_running = True
    data = None
    matrix = None
    while continue_running:
        show_menu()
        selected_option = int(input("Please select an option: "))
        if selected_option == 1:
            data = execute_load_data()
        elif selected_option == 2:
            execute_piechart_gender(data)
        elif selected_option == 3:
            execute_top10_departments(data)
        elif selected_option == 4:
            execute_evaluation_categories(data)
        elif selected_option == 5:
            matrix = execute_create_matrix(data)
        elif selected_option == 6:
            execute_department_most_appliances(matrix)
        elif selected_option == 7:
            execute_count_appliances(matrix)
        elif selected_option == 8:
            execute_ICV_department(matrix)
        elif selected_option == 9:
            continue_running = False
        else:
            print("Please select a valid option.")

# MAIN PROGRAM
start_application()
