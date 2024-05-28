import pandas as pd
from faker import Faker

def main():
    lst = ['h', 'e', 'l', 'l', 'o']
    pd_series = pd.Series(
        lst, 
        index=['a', 'b', 'c', 'd', 'e']
    )
    print(pd_series)
    print(pd_series.iloc[3:4]) # returns the value with respect to specified index that is given at dataframe creation
    print(pd_series.loc['a']) # returns the value with respect to user specified index that is given at dataframe creation
    
    dct = {
        'a': 10,
        'b': 20,
        'c': 30,
    }
    pd_dct = pd.Series(dct)
    print(pd_dct)
    
    fake = Faker()
    nameList = [fake.name() for _ in range(10)]
    emailList = [fake.email() for _ in range(10)]
    phoneNumberList = [fake.phone_number() for _ in range(10)]
    pd_dataframe = pd.DataFrame(
        {
            'Name': nameList,
            'Email': emailList,
            'phone_number': phoneNumberList
        },
        index = [i+1 for i in range(len(nameList))]
    )
    print(pd_dataframe)

    csv_df = pd.read_csv('data.csv')
    print(csv_df)
    pd_dataframe.insert(
        3,
        'address',
        [fake.address() for _ in range(10)]
    )
    print(pd_dataframe)
    
if __name__ == '__main__':
    main()