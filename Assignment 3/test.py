import pandas as pd
import numpy as np
from faker import Faker
from random import randint
import uuid
from reportlab.lib.pagesizes import letter
import reportlab.pdfgen.canvas as canvas

def main():
    fake = Faker()
    headers = [
        'patient_id',
        'patient_name',
        'phone_number',
        'email',
        'test_type',
        'result'
    ]
    dataset = pd.DataFrame(
        {
            'patient_id': [i for i in range(1, 11)],
            'patient_name': [fake.name() for _ in range(10)],
            'phone_number': [fake.phone_number() for _ in range(10)],
            'email': [fake.email() for _ in range(10)],
            'test_type': ['diabets' for i in range(0, 10)],
            'result': [randint(10, 100) for i in range(0, 10)]
        }
    )
    evaluation = []
    usernames = []
    reports = []
    shape = list(dataset.shape)
    # rows, columns = shape[0], shape[1]
    for index, row in dataset.iterrows():
        print("Patient ID:", row['patient_id'])
        print("Patient Name:", row['patient_name'])
        print("Phone Number:", row['phone_number'])
        print("Email:", row['email'])
        print("Test Type:", row['test_type'])
        print("Result:", row['result'])

        if row['result'] < 100:
            evaluation.append('Normal')
        elif 100 <= row['result'] <= 125:
            evaluation.append('Pre-diabetic')
        else:
            evaluation.append('Diabetic')
        username = uuid.uuid1()
        report_name = uuid.uuid4()
        usernames.append(username)
        reports.append(report_name)
        print("Evaluation:", evaluation[-1])
        print('Username: ', usernames[-1])
        print('report name: ', report_name)
        print()
        c = canvas.Canvas(f'{report_name}.pdf')
        x_start, y_start, y_offset = 50, 750, 15
        c.drawString(x_start, y_start, f"Patient ID: {row['patient_id']}")
        c.drawString(x_start, y_start - y_offset, f"Patient Name: {row['patient_name']}")
        c.drawString(x_start, y_start - 2*y_offset, f"Phone Number: {row['phone_number']}")
        c.drawString(x_start, y_start - 3*y_offset, f"Email: {row['email']}")
        c.drawString(x_start, y_start - 4*y_offset, f"Test Type: {row['test_type']}")
        c.drawString(x_start, y_start - 5*y_offset, f"Result: {row['result']}")
        c.drawString(x_start, y_start - 6*y_offset, f"Evaluation: {evaluation}")
        c.drawString(x_start, y_start - 7*y_offset, f"Username: {username}")
        c.drawString(x_start, y_start - 8*y_offset, f"Report Name: {report_name}")
        c.showPage()
        c.save()

    # for i in headers:
    #     for j in range(rows):
    #         print(i, end=': ')
    #         print(dataset[i][j])
    #         if (dataset['result'][i] < 100):
    #             evaluation.append('Normal')
    #         elif (dataset['result'][i] >= 100 or dataset['result'][i] <= 125):
    #             evaluation.append('pre diabetic')
    #         else:
    #             evaluation.append('diabetic')
    #     print()

if __name__ == '__main__':
    main()