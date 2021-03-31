# This is going to be where we put all our default scripts for the "vnomics" package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objs as go
from sklearn.impute import SimpleImputer


class etl:
    def __init__(self):
        # Path to the data folder
        self.path = '../data_2021/'

    def read_vehicles(self, path_to_file = None):
        if path_to_file == None:
            path_to_file = self.path + 'vehicle_list.csv'
        vehicles = pd.read_csv(path_to_file)
        return vehicles


    def read_daily(self, path_to_file = None):
        
        if path_to_file == None:
            path_to_file = self.path + 'individual_files//{}_daily_data.csv'

        # Reading vehicles dataframe in
        vehicles = self.read_vehicles()

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
#         all_data.to_csv(path + 'raw_daily_data.csv')

        return all_data

    def read_fullwindow_data(self, path):
        # Taking the windowed data
        fullwindow = pd.read_csv(path + 'fullwindow_data.csv')
        fullwindow.drop("Unnamed: 0", inplace = True, axis = 1)
        fullwindow['date'] = pd.to_datetime(fullwindow['date'])
        return fullwindow
        
    def read_dan(self, path = None):
        ''' 
        Paramaters
        ----------
        path: Path to data folder
        
        Outputs:
        --------
        data: dataframe containing Daniel's data after imputation and a bit of cleaning
        '''
        if path == None:
            path = self.path
        
        # Getting Daniel's Data - plus some modifying
        data = pd.read_csv(path + "Features.csv")
        data.drop('Unnamed: 0',axis=1,inplace=True)
        data['date'] = pd.to_datetime(data['date'])
        data['Days of Rest'].fillna(0, inplace = True)

        # I can't have any nulls, so I used a simple 
        # imputer to fill the percentage columns he made
        cols_to_impute =['percent_idle','percent_fuel_lost',
                        'percent_regen_inhibited',
                        'percent_regen_needed',
                        'percent_regen_inhibit_switch_not_active']
        col_names = data.columns.to_list()
        residual_cols = list(set(col_names) - set(cols_to_impute))
        imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
        imputed_cols = imp_mean.fit_transform(np.array(data[cols_to_impute]))
        data = pd.concat([data[residual_cols], pd.DataFrame(imputed_cols, columns = cols_to_impute)],axis=1)
        
        return data


def main():
    pass
    
if __name__ == '__main__':
    main()
                
