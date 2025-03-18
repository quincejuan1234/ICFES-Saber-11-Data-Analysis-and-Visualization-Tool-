#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICFES Saber 11 Test in Colombia
Function module.

@author: Juan David Alfonso
"""
import pandas as pd
import matplotlib.pyplot as plt 

def create_matrix(dataframe: pd.DataFrame) -> list:
    # Dictionary skeletons
    services_devices = sorted(["internet", "tv", "computer", "microwave", "car", "washing machine", "motorcycle", "video games"])
    services_devices_dict = dict(list(enumerate(services_devices)))
    departments = sorted(dataframe["dpto"].unique())
    dept_dict = dict(list(enumerate(departments)))
    
    grouped_data = {}
    for service in services_devices:
        group = dataframe.groupby("dpto")[service].sum()
        grouped_data[service] = group
    
    matrix = []
    for i in dept_dict:
        department = dept_dict[i]
        row = []
        for j in services_devices_dict:
            service_device = grouped_data[services_devices_dict[j]][department]
            row.append(service_device)
        matrix.append(row)
    return matrix, services_devices_dict, dept_dict

def load_data(file: str) -> pd.DataFrame:
    """Function to create a DataFrame from a .csv file."""
    dataframe = pd.read_csv(file)  # Creates the DataFrame
    return dataframe  # Returns the DataFrame from the .csv file

def piechart_gender(dataframe: pd.DataFrame) -> None:
    data = dataframe.loc[:, ["genero_col"]].value_counts()  # Creates a DataFrame with the school gender data
    values = data.unique().tolist()  # Extracts the number of students per school gender
    total = sum(values)  # Calculates the total number of students
    
    labels = ["COEDUCATIONAL", "MALE", "FEMALE"]  # Chart labels
    percentages = [values[0]/total, values[1]/total, values[2]/total]  # Student percentages
    colors = ['green', 'blue', 'yellow']  # Chart colors
    plt.pie(x=percentages, labels=labels, colors=colors, autopct='%1.2f%%')  # Chart parameters
    plt.title('Percentage distribution by school gender')  # Chart title
    plt.show()  # Displays the chart

def top10_departments(dataframe: pd.DataFrame, category: str) -> None:
    """Creates a horizontal bar chart for the top 10 departments based on a given test category."""
    data = dataframe[["dpto", category]]  # Filters the DataFrame by the given category
    data = data.groupby("dpto").mean().sort_values(ascending=False, by=category).head(10)  # Sorts and selects top 10 departments
    data.plot(kind="bar")  # Specifies chart type
    plt.ylabel('Average percentage score')  # Y-axis label
    plt.xlabel("Department")  # X-axis label
    plt.title('Top 10 departments with the highest score in ' + category + ' in Saber 11 tests')  # Chart title
    plt.show()

def evaluation_categories(dataframe: pd.DataFrame) -> None:
    """Creates a box plot for the score distribution across evaluation categories."""
    categories = dataframe[["ciencias", "matematicas", "lectura_critica", "sociales", "ingles"]]  # Filters DataFrame
    categories.plot(kind="box")  # Specifies chart type
    plt.ylabel('Score')  # Y-axis label
    plt.xlabel("Category")  # X-axis label
    plt.title('Score distribution by evaluation category')  # Chart title
    plt.show()

def department_most_appliances(matrix: tuple) -> None:
    """Finds the department with the highest number of appliances (washing machines and microwaves)."""
    data_matrix = matrix[0]  # First row with appliance data
    dict_services = matrix[1]  # Second row with service names
    dict_departments = matrix[2]  # Third row with department names
    
    values = list(dict_services.values())  # Extracts appliance names
    washer_index = values.index('washing machine')
    microwave_index = values.index('microwave')
    
    best_department = ["", 0]  # Stores department name and count of appliances
    for i in range(len(data_matrix)):
        total_appliances = data_matrix[i][washer_index] + data_matrix[i][microwave_index]
        if total_appliances > best_department[1]:
            best_department[1] = total_appliances
            best_department[0] = dict_departments[i]
    return best_department[0]  # Returns department with the most appliances

def count_appliances(matrix: tuple, device: str) -> None:
    """Counts the total number of a given appliance/service/device in the country."""
    data_matrix = matrix[0]
    dict_services = matrix[1]
    
    values = list(dict_services.values())  # Extract appliance names
    device_index = values.index(device)  # Find index of the given device
    
    total_count = sum(row[device_index] for row in data_matrix)  # Sum up occurrences
    return total_count  # Returns total count of the device

def ICV_department(matrix: tuple, department: str) -> None:
    """Calculates the Quality of Life Index (ICV) for a given department."""
    data_matrix = matrix[0]  # First row with appliance data
    dict_departments = matrix[2]  # Third row with department names
    
    values = list(dict_departments.values())  # Extract department names
    dept_index = values.index(department)  # Find index of the department
    
    icv_score = 0
    weights = [0.2, 0.09, 0.09, 0.07, 0.08, 0.16, 0.13, 0.18]
    
    for i in range(len(weights)):
        icv_score += data_matrix[dept_index][i] * weights[i]  # Calculate weighted score
    
    return round(icv_score, 2)  # Returns rounded ICV score