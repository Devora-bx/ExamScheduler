def calculate_average_study_times(study_data, course_names):
    """
    Calculates the average study times for the selected courses.

    Args:
    study_data (DataFrame): DataFrame containing the study times for each course.
    course_names (list): List of courses to calculate the average study time for.

    Returns:
    average_study_times (dict): Dictionary with course names as keys and their average study times as values.
    """
    average_study_times = {course: study_data[course].mean() for course in course_names if course in study_data.columns}
    return average_study_times
