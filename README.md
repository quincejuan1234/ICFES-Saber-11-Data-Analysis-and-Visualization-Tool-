# ICFES Saber 11 Data Analysis and Visualization Tool

This project provides a small console application for exploring the 2020 Calendar A results of the Colombian **Saber 11** exam. It loads the provided dataset, offers quick visualizations with Matplotlib, and computes a few summary indicators to help understand performance and household characteristics across departments.

## Project Structure
- `saber_11.py`: Core analysis functions (data loading, charting, aggregations, and indicators).
- `saber_11_user_interface.py`: Console-based menu that orchestrates data loading and runs the analysis helpers.
- `saber_11.csv`: Sample dataset containing the Saber 11 records used by the scripts.

## Requirements
- Python 3.8+
- [pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

You can install the dependencies with:
```bash
pip install -r requirements.txt
```
> If `requirements.txt` is not present, install at least `pandas` and `matplotlib` manually.

## Getting Started
1. Ensure `saber_11.csv` is present in the repository root (or provide the path when prompted).
2. Run the interactive console menu:
   ```bash
   python3 saber_11_user_interface.py
   ```
3. Follow the prompts to select actions. Most options display Matplotlib charts; keep the plot window open until you are ready to return to the menu.

## Menu Options
1. **Load data** – Read the Saber 11 CSV into a pandas DataFrame.
2. **Pie chart of school gender distribution** – Visualizes the proportion of coeducational, male, and female schools.
3. **Top 10 departments by exam category** – Horizontal bar chart of average scores for a user-provided category (e.g., `ciencias`, `matematicas`).
4. **Score distribution by category** – Box plot comparing score distributions across `ciencias`, `matematicas`, `lectura_critica`, `sociales`, and `ingles`.
5. **Department vs. services/appliances matrix** – Builds a matrix that tallies household services and devices per department.
6. **Department with most appliances** – Finds the department with the highest combined number of washing machines and microwaves.
7. **Total count of a service/device** – Sums how many households have a specified service or device nationwide.
8. **Quality of Life Index (ICV)** – Computes a weighted index for a given department using household assets.
9. **Exit** – Quit the program.

## Notes and Tips
- Ensure the CSV headers match the column names expected by the scripts (see the column references inside `saber_11.py`).
- Charts open in separate windows; close them to return control to the console.
- If you extend the project, consider renaming the import in `saber_11_user_interface.py` (currently `import saber11 as s11`) to match the module filename.
