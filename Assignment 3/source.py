import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def tasks(headers, filename):
    # task 1 implementation
    df = pd.read_csv(filename)
    df.columns = headers
    print(df)
    # task 2 implementation
    print('Columns that having null values and there count is given below')
    print(df.isnull().sum())
    # task 3
    print(f'Before applying median values on Hours_Studied\n{df['Hours_Studied']}')
    median_value = df['Hours_Studied'].median()
    df_hours = df['Hours_Studied'].fillna(median_value)
    print(f'After applying median values on Hours_Studied\n{df_hours}')
    # task 4
    frequent_gpa = df['GPA'].mode()[0]
    print(f'Before Setting null values to most frequent CGPA\n{df['GPA']}')
    df_frequent_gpa = df['GPA'].fillna(frequent_gpa)
    print(f'After setting null values to most frequent CGPA\n{df_frequent_gpa}')
    # task 5
    print(f'Before applying normalization on attendance column\n{df['Attendance']}')
    normalized_attendance = df['Attendance'] * (6 / 5)
    print(f'After applying normalization on attendance column\n{normalized_attendance}')
    # task 6
    plt.figure(figsize=(12, 8))
    plt.bar(
        df['student_id'], df['Hours_Studied'],
        color='blue', label='Hours Studied',
        width=0.4
    )
    plt.bar(
        df['student_id'], df['GPA'], 
        color='#ad0000', label='GPA',
        width=0.4
    )
    plt.xlabel('Student ID')
    plt.ylabel('Values')
    plt.title('Hours Studied and GPA by Student ID')
    plt.legend()
    plt.grid()
    plt.savefig('student_id_hours_and_gpa.png', dpi = 1000)
    plt.show()
    # task 7
    df.sort_values(by='Hours_Studied', inplace=True)
    plt.figure(figsize=(10, 6))
    plt.stackplot(
        df['Hours_Studied'], df['GPA'],
        color=['b', '#ad0000']
    )
    plt.xlabel('Hours Studied')
    plt.ylabel('GPA')
    plt.title('Student GPA Progress with respect to Hours Studied')
    plt.grid()
    plt.savefig('Hours_Studied_GPA_Graph.png')
    plt.show()
    

def main():
    headers = [
        'student_id', 'Test_Score',
        'Hours_Studied', 'GPA',
        'Attendance', 'Scholarship %',
        'Extracurricular_Activities'
    ]
    filename = 'students_dataset_csv_file.csv'
    tasks(
        headers,
        filename
    )


if __name__ == '__main__':
    main()
    