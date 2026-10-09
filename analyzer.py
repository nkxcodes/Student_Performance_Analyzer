
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

if __name__ == "__main__":
    main()