import matplotlib.pyplot as plt
from datetime import datetime

def is_date_too_close(new_date, assigned_dates, min_gap_days):
    """
    Checks if a new exam date is too close to any previously assigned exam dates.

    Args:
    new_date (str): The new exam date in "dd.mm.yy" format.
    assigned_dates (list): List of previously assigned dates and their required gaps.
    min_gap_days (int): Minimum gap in days between the new date and assigned dates.

    Returns:
    bool: True if the new date is too close to any assigned dates, False otherwise.
    """
    try:
        new_date = datetime.strptime(new_date, "%d.%m.%y")
        for assigned_date, required_gap in assigned_dates:
            existing_date = datetime.strptime(assigned_date, "%d.%m.%y")
            if abs((new_date - existing_date).days) < required_gap:
                return True
        return False
    except ValueError as e:
        print(f"Error parsing date: {new_date}. Exception: {e}")
        return True

def schedule_exams_backtracking(courses, exam_dates, average_study_times, assigned_dates=None, course_schedule=None):
    """
    Schedules exams for the courses using backtracking.

    Args:
    courses (list): List of course names to schedule exams for.
    exam_dates (dict): Dictionary with available exam dates for each course.
    average_study_times (dict): Dictionary with average study times for each course.
    assigned_dates (list): List of already assigned exam dates and required gaps.
    course_schedule (dict): Dictionary with the current course schedule.

    Returns:
    dict: A dictionary containing the exam schedule with course names as keys and their exam dates as values.
    """
    if assigned_dates is None:
        assigned_dates = []
    if course_schedule is None:
        course_schedule = {}

    # If all courses have been scheduled, return the schedule
    if len(course_schedule) == len(courses):
        return course_schedule

    # Try to schedule each course
    for course in courses:
        if course in course_schedule:
            continue

        # Calculate average study time in days
        study_time_days = int(average_study_times[course] * 7)

        for date in exam_dates[course]:
            if not is_date_too_close(date, assigned_dates, study_time_days):
                assigned_dates.append((date, study_time_days))
                course_schedule[course] = date

                # Recursively schedule the remaining courses
                result = schedule_exams_backtracking(courses, exam_dates, average_study_times, assigned_dates, course_schedule)
                if result is not None:
                    return result  # Found a valid schedule

                # Backtrack if no solution is found
                assigned_dates.pop()
                del course_schedule[course]

    return None  # No valid schedule found

def plot_average_study_time(average_study_times, exam_schedule):
    """
    Plots the average study time per course and displays the exam schedule.

    Args:
    average_study_times (dict): Dictionary containing the average study times for each course.
    exam_schedule (dict): Dictionary containing the assigned exam dates for each course.
    """
    # Plot the average study time per course
    plt.figure(figsize=(10, 6))
    plt.bar(average_study_times.keys(), average_study_times.values(), color='skyblue')

    # Set the course names to be horizontal for better readability
    plt.xticks(rotation=0, ha='center', fontsize=10)  # 0 degrees to keep it horizontal
    plt.ylabel("Average Study Time (weeks)")
    plt.title("Average Study Time per Course")
    plt.tight_layout()

    # Add the exam schedule text above the graph
    assignment_text = "\n".join([f"{course}: {date}" for course, date in exam_schedule.items()])
    plt.gcf().text(0.5, 0.95, f"\nExam Schedule:\n{assignment_text}", fontsize=10, ha='center', va='top')

    # Show the plot
    plt.show()
