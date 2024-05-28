from faker import Faker
import pandas as pd

def main():
    fake = Faker()
    nameList = [fake.name() for _ in range(10)]
    emailList = [fake.email() for _ in range(10)]
    phoneNumberList = [fake.phone_number() for _ in range(10)]
    # print(nameList)
    df = pd.DataFrame(
        {
            'names': nameList,
            'email': emailList,
            'phone_number': phoneNumberList
        }
    )
    df.to_excel(
        'task2File.xlsx'
    )

if __name__ == '__main__':
    main()