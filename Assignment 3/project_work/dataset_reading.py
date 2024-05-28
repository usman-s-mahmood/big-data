import pandas as pd
import numpy as np
from faker import Faker
from random import randint
import uuid
from reportlab.lib.pagesizes import letter
import reportlab.pdfgen.canvas as canvas

def main():
    dataset = pd.DataFrame(
        pd.read_excel('diabetes-695630da-12a2-11ef-9463-e8b1fc60720e.xlsx')
    )
    # dataset.to_excel('dataset.xlsx')
    evaluation = []
    usernames = []
    reports = []
    for index, row in dataset.iterrows():
        print("Patient ID:", row['patient_id'])
        print("Patient Name:", row['patient_name'])
        print("Phone Number:", row['phone_number'])
        print("Email:", row['email'])
        print("Test Type:", row['test_type'])
        print("Result:", row['result'])
        evaluate = ''
        if row['result'] < 100:
            evaluate = 'Normal'
        elif 100 <= row['result'] <= 125:
            evaluate = 'Pre-Diabetic'
        else:
            evaluate = 'Diabetic'
        evaluation.append(evaluate)
        username = uuid.uuid1()
        report_name = uuid.uuid4()
        usernames.append(username)
        reports.append(report_name)
        print("Evaluation:", evaluation[-1])
        print('Username: ', usernames[-1])
        print('report name: ', report_name)
        print()
        c = canvas.Canvas(f'{report_name}.pdf')
        c.setFont("Helvetica", 18)
        x_start, y_start, y_offset = 50, 750, 55
        x_center = letter[0] / 2
        company_name = "Big Data Project - Medical Lab System, Diabetes Report"
        c.drawCentredString(x_center, y_start, company_name)

        # Draw a line break
        c.line(50, y_start - y_offset, 550, y_start - y_offset)
        # c.drawString(x_start, y_start, f"Patient ID: {row['patient_id']}")
        c.drawString(x_start, y_start - 2*y_offset, f"Patient ID: {row['patient_id']}")
        c.drawString(x_start, y_start - 3*y_offset, f"Patient Name: {row['patient_name']}")
        c.drawString(x_start, y_start - 4*y_offset, f"Phone Number: {row['phone_number']}")
        c.drawString(x_start, y_start - 5*y_offset, f"Email: {row['email']}")
        c.drawString(x_start, y_start - 6*y_offset, f"Test Type: {row['test_type']}")
        c.drawString(x_start, y_start - 7*y_offset, f"Result: {row['result']}")
        c.drawString(x_start, y_start - 8*y_offset, f"Evaluation: {evaluate}")
        c.drawString(x_start, y_start - 9*y_offset, f"Username: {username}")
        c.drawString(x_start, y_start - 10*y_offset, f"Report Name: {report_name}")
        c.line(x_start, y_start - 11*y_offset, 550, y_start - 11*y_offset)
        c.showPage()
        c.save()

if __name__ == '__main__':
    main()