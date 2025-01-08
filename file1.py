import pandas as pd

def load_data():
    """
    Load the study data and exam dates from CSV files.

    Returns:
    study_data (DataFrame): DataFrame containing the study times for each course.
    exam_dates_data (DataFrame): DataFrame containing the exam dates for each course.
    """
    # Input file paths
    study_data_path = "courses.csv"  
    exam_dates_path = "exams_dates.csv"  

    # Reading the data from CSV files
    study_data = pd.read_csv(study_data_path)
    exam_dates_data = pd.read_csv(exam_dates_path)

    return study_data, exam_dates_data

def get_courses(study_data):
    """
    Extracts the course names from the study data.

    Args:
    study_data (DataFrame): DataFrame containing the study times for each course.

    Returns:
    courses (list): List of course names extracted from the study data.
    """
    courses = study_data.columns[1:-2]  # Assuming courses are between first and last columns
    return courses

def get_user_input():
    """
    Gets course names from the user input.

    Returns:
    course_names (list): List of course names entered by the user.
    """
    user_input = input("Enter the names of courses (separated by commas): ").strip()
    if user_input:
        course_names = [course.strip() for course in user_input.split(",")]
    else:
        print("No courses were entered. The scheduling will be canceled.")
        course_names = []
    
    return course_names
