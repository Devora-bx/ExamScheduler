from file1 import load_data, get_courses, get_user_input
from file2 import calculate_average_study_times
from file3 import get_exam_dates
from file4 import schedule_exams_backtracking, plot_average_study_time

def main():
    """
    Main function to load data, calculate average study times, get user input,
    schedule exams using backtracking, and plot the results.
    """
    # Load data
    study_data, exam_dates_data = load_data()

    # Get the courses
    courses = get_courses(study_data)

    # Get user input for course selection
    course_names = get_user_input()

    if not course_names:
        return  # If no courses are selected, exit

    # Calculate average study times for the selected courses
    average_study_times = calculate_average_study_times(study_data, course_names)

    # Get the exam dates for the selected courses
    exam_dates = get_exam_dates(exam_dates_data, course_names)

    # Schedule exams using backtracking
    exam_schedule = schedule_exams_backtracking(course_names, exam_dates, average_study_times)

    if exam_schedule is None:
        print("No valid schedule found.")
    else:
        print("Exam Schedule:")
        for course, date in exam_schedule.items():
            print(f"{course}: {date}")

        # Plot the average study time and exam schedule
        plot_average_study_time(average_study_times, exam_schedule)

if __name__ == "__main__":
    main()
