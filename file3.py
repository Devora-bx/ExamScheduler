def get_exam_dates(exam_dates_data, course_names):
    """
    Filters and retrieves the exam dates for the selected courses.

    Args:
    exam_dates_data (DataFrame): DataFrame containing the exam dates for each course.
    course_names (list): List of courses for which to get the exam dates.

    Returns:
    exam_dates (dict): Dictionary with course names as keys and a list of their exam dates as values.
    """
    exam_dates = {course: exam_dates_data[course].dropna().tolist() for course in course_names if course in exam_dates_data.columns}
    return exam_dates
