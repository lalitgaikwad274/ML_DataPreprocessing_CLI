import pandas as pd

class download:

    def __init__(self, data):
        self.data = data

    
    def download(self):
        toBeDownload = {}
        for column in self.data.columns.values:
            toBeDownload[column] = self.data[column]

        newFileName = input("\nEnter the filename for the file that you want? (Press -1 to go back): ")
        if newFileName == "-1":
            return

        newFileName = newFileName + ".csv"

        pd.DataFrame(self.data).to_csv(newFileName, index=False)

        print("Done....")

        if input("DO you want to exit now? (y/n)").lower() == 'y':
            print("Exiting....")
            exit()
        else:
            return

        
