
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

if __name__ == "__main__":
    main()