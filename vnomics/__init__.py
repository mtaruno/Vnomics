# This is going to be where we put all our default scripts for the "vnomics" package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '../data_2021/'

def read_vehicles(path_to_file = path + 'vehicle_list.csv'):
    vehicles = pd.read_csv(path_to_file)
    return vehicles


def read_daily(path_to_file = path + 'individual_files//{}_daily_data.csv'):

    # Reading vehicles dataframe in
    vehicles = read_vehicles()

    # create empty dataframe
    all_data = pd.DataFrame()

    for i, e in vehicles.iterrows():
        try:
            tmp = pd.read_csv(path_to_file.format(e.platform_id))
            if len(all_data) == 0:  # first csv read replaces empty dataframe
                all_data = tmp
            else:  # all other csv reads append to dataframe
                all_data = all_data.append(tmp)
        except:
            None
        
    # delete index column 'Unnamed: 0'
    del all_data['Unnamed: 0']

    # set date column to datetime
    all_data['date'] = pd.to_datetime(all_data['date'], infer_datetime_format=True)

    # Saving raw data
    all_data.to_csv(path + 'raw_daily_data.csv')

    return all_data


def main():
    pass
    
if __name__ == '__main__':
    main()
                
