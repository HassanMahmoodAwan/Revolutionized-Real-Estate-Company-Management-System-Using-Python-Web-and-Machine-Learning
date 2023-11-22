import pandas as pd
import time

from Functionalities.Create_DataBase import create_database

class Real_estate_Bussiness:
    def __init__(self):
        self.CompanyName = 'HM Real Estate'
        self.Location = '86-G, Sabzazar Scheme, Lahore'
        self.area = 'Lahore'
        self.owner = 'Muhammad Mahmood'
        self.services = ['Property Sale_Purchase', 'Property_Renting', 'Property Management', 'Societies Files', 'Construction', 'Commercial']


if __name__ == '__main__':
    company = Real_estate_Bussiness()

    # =========== MENU / DASHBOARD =============

    print(f'=========== {company.CompanyName}===========')
    print('     ======= Main Menu =======    ')

    runserver = ''
    while runserver != 'n':
        
        print('Show Company \'Info\': ')
        print('Do you Want to Create a new \'Storage\': ')
        print('To Add Data in Your Storage \'Add\': ')
        print('Start APP: ')
        choice = input('Enter Your Choice: ')
        print('\n')

        match choice:

            case 'Info':
                print(f'{company.CompanyName} is a real Estate Company, Providing Services in {company.area}. Providing Seamless Experience in Real Estate Services')

                print(f'Company Name : {company.CompanyName}')
                print(f'CEO :          {company.owner}')
                print(f'Location :     {company.Location}')
                services = ', '.join(company.services)
                print(f'Area:          {company.area}')
                print(f'Services :     {services}')

                print('\n')

            case 'Storage':
                no_features: int = int(input('Enter the Num of Features: '))
                feature_list = list()
                for i in range(no_features):
                    feature_list.append(input(f'Enter the {i+1} Feature: '))

                name = input('Enter the Name of DataBase: ')
                create_database(feature_list, name)

                # Wait
                time.sleep(1.5)

                # Reading DataBase
                db = pd.read_csv(f'./{name}.csv')
                db_dict = db.to_dict('list')
                del db_dict['Unnamed: 0']

        
        runserver = input('Do you want to Stop(n): ')