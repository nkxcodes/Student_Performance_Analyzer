
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/students.csv')

    print()
    print('========== DATASET ==========')

    number_of_rows = df.shape[0]
    number_of_columns = df.shape[1]
    column_names = df.columns
    data_types = df.dtypes
    missing_values = df.isnull().sum()
    duplicate_rows = df.duplicated().sum()
    basic_statistics = df.describe()

    print()
    print(f'Number of rows: {number_of_rows}')

    print()
    print(f'Number of columns: {number_of_columns}')

    print()
    print(f'Column names: {column_names}')

    print()
    print(f'Data types: {data_types}')

    print()
    print(f'Missing values: {missing_values}')

    print()
    print(f'Duplicate rows: {duplicate_rows}')

    print()
    print('Basic statistics: ')
    print()
    print(basic_statistics)

    rows_with_missing_values = df[df.isnull().any(axis=1)]
    duplicate_ids = df[df['Student_ID'].duplicated(keep=False)]

    print()
    print(rows_with_missing_values)

    print()
    print(duplicate_ids)

    df = df.drop_duplicates()

    df['Total_Score'] = df['Math_Score'] + df['Science_Score'] + df['English_Score']

    print()
    print('========== BASIC ANALYSIS ==========')

    total_number_of_students = df['Student_ID'].count()
    average_age = df['Age'].mean()
    minimum_age = df['Age'].min()
    maximum_age = df['Age'].max()
    number_of_male_students = df[df['Gender'] == 'Male'].shape[0]
    number_of_female_students = df[df['Gender'] == 'Female'].shape[0]

    print()
    print(f'Total number of students: {total_number_of_students}')

    print()
    print(f'Average age: {average_age}')

    print()
    print(f'Minimum age: {minimum_age}')

    print()
    print(f'Maximum age: {maximum_age}')

    print()
    print(f'Number of male students: {number_of_male_students}')

    print()
    print(f'Number of female students: {number_of_female_students}')

    print()
    print('========== ACADEMIC PERFORMANCE ==========')

    average_math_score = df['Math_Score'].mean()
    average_science_score = df['Science_Score'].mean()
    average_english_score = df['English_Score'].mean()
    average_total_score = df['Total_Score'].mean()
    highest_total_score = df['Total_Score'].max()
    lowest_total_score = df['Total_Score'].min()
    top_performing_student = df.loc[df['Total_Score'].idxmax(), 'Name']
    lowest_performing_student = df.loc[df['Total_Score'].idxmin(), 'Name']

    print()
    print(f'Average math score: {average_math_score}')

    print()
    print(f'Average science score: {average_science_score}')

    print()
    print(f'Average english score: {average_english_score}')

    print()
    print(f'Average total score: {average_total_score}')

    print()
    print(f'Highest total score: {highest_total_score}')

    print()
    print(f'Lowest total score: {lowest_total_score}')

    print()
    print(f'Top performing student: {top_performing_student}')

    print()
    print(f'Lowest performing student: {lowest_performing_student}')

    average_scores = pd.Series({
        'Math': df['Math_Score'].mean(),
        'Science': df['Science_Score'].mean(),
        'English': df['English_Score'].mean()
    })

    highest_average_subject = average_scores.idxmax()
    lowest_average_subject = average_scores.idxmin()

    print()
    print(f'Subject with highest average: {highest_average_subject}')

    print()
    print(f'Subject with lowest average: {lowest_average_subject}')

    print()
    print('========== TOP STUDENTS ==========')

    top_5_students = df.head().sort_values('Total_Score', ascending=False)

    print()
    print('Top 5 Students: ')
    print()
    print(top_5_students)

    print()
    print('========== ATTENDANCE ANALYSIS ==========')

    average_attendance = df['Attendance'].mean()
    highest_attendance = df['Attendance'].max()
    lowest_attendance = df['Attendance'].min()
    student_with_highest_attendance = df.loc[df['Attendance'].idxmax(), 'Name']
    student_with_lowest_attendance = df.loc[df['Attendance'].idxmin(), 'Name']

    print()
    print(f'Average attendance: {average_attendance}')

    print()
    print(f'Highest attendance: {highest_attendance}')

    print()
    print(f'Lowest attendance: {lowest_attendance}')

    print()
    print(f'Student with highest attendance: {student_with_highest_attendance}')

    print()
    print(f'Student with lowest attendance: {student_with_lowest_attendance}')

    print()
    print('========== STUDY-HOURS ANALYSIS ==========')

    average_study_hours = df['Study_Hours'].mean()
    highest_study_hours = df['Study_Hours'].max()
    lowest_study_hours = df['Study_Hours'].min()
    student_studying_the_most = df.loc[df['Study_Hours'].idxmax(), 'Name']
    student_studying_the_least = df.loc[df['Study_Hours'].idxmin(), 'Name']

    print()
    print(f'Average study hours: {average_study_hours}')

    print()
    print(f'Highest study hours: {highest_study_hours}')

    print()
    print(f'Lowest study hours: {lowest_study_hours}')

    print()
    print(f'Student studying the most: {student_studying_the_most}')

    print()
    print(f'Student studying the least: {student_studying_the_least}')

    print()
    print('========== ASSIGNMENT ANALYSIS ==========')

    average_assignments_completed = df['Assignments_Completed'].mean()
    maximum_assignments_completed = df['Assignments_Completed'].max()
    minimum_assignments_completed = df['Assignments_Completed'].min()
    student_completing_the_most_assignments = df.loc[df['Assignments_Completed'].idxmax(), 'Name']
    students_who_completed_fewer_than_6_assignments = df[df['Assignments_Completed'] < 6]

    print()
    print(f'Average assigments completed: {average_assignments_completed}')

    print()
    print(f'Maximum assignments completed: {maximum_assignments_completed}')

    print()
    print(f'Minimum assignments completed: {minimum_assignments_completed}')

    print()
    print(f'Student completing the most assignments: {student_completing_the_most_assignments}')

    print()
    print(f'Student who completed fewer than 6 assignments: ')
    print()
    print(students_who_completed_fewer_than_6_assignments)
if __name__ == "__main__":
    main()