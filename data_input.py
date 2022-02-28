import pandas as pd
from os import path
import sys

class InputData:

    supported_file_extensions = ['.csv', '.xlsx']

    # function to convert all column name of dataset to lower case
    def change_to_lower_case(self, data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace=True)
        return data

    
    def InputFunction(self):

        try:
            filename, extension = path.splitext(sys.argv[1])
            if extension == "":
                raise SystemExit("Provide the Dataset with file extension\n")

            if extension not in self.supported_file_extensions:
                raise SystemExit("This file extension is not supported\n")
            
        except IndexError:
            raise SystemExit("Provide the Dataset with file extension\n")
        
        try:
            if extension == ".csv":
                data = pd.read_csv(filename+extension)
            
            if extension == ".xlsx":
                data = pd.read_excel(filename+extension)
            
        except pd.errors.EmptyDataError:
            raise SystemExit("The file is Empty\n")
        
        data = self.change_to_lower_case(data)

        return data

