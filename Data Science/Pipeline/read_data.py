import pandas as pd
import numpy as np
import joblib

PATH = 'files/train.csv'
OUTPUT_PATH = 'files/output/'

def read_data(file_dir):
    '''
    Parameters
    ----------
    file_dir: path (string)
        path to your dataset
        
    Returns
    -------
    data: DataFrame
    '''
    
    data = pd.read_csv(PATH).set_index('id')
    
    joblib.dump(data,
                OUTPUT_PATH + 'data.pkl')

    print('---------------DONE READ DATA---------------')
    
if __name__ == '__main__':
    print('---------------START READ DATA---------------')
    read_data(PATH)