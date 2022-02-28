from categorical import Categorical
from data_input import InputData
from download import download
from data_description import DataDescription
from feature_scaling import FeatureScaling
from imputation import Imputation


class Preprocesser:
    
    tasks = [
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]

    data = 0

    def __init__(self):
        self.data = InputData().InputFunction()
        print("WELCOME TO MACHINE LEARNING PREPROCESSING CLI\n")

    #Function to remove target column from the dataframe.
    def removeTargetColumn(self):
        print("Columns\n")
        for column in self.data.columns.values:
            print(column, end=" ")
        
        while(1):
            column = input("\nWhich is the target variable? (Press -1 to exit) : ").lower()
            if(column == "-1"):
                exit()

            choice = input("\nAre you sure?(y/n) ")
            if(choice=="y" or choice=="Y"):
                try:
                    self.data.drop([column], axis=1, inplace=True)
                except KeyError:
                    print("column is not present with this name. try again.....\n")
                    continue
                print("Done.....\n")
                break
            else:
                print("Try again with different column name")
        return
    #finction to print the dataframe
    def printData(self):
        print(self.data)

    #main function for preprocessing
    def preprocessingMain(self):
        self.removeTargetColumn()
        while(1):
            print("\nTasks in preprocessing\n")
            for task in self.tasks:
                print(task)
            
            while(1):
                try:
                    choice = int(input("\n What do you want to do? (Press -1 to exit) : "))
                except ValueError:
                    print("Interger value requried. Try again....")
                    continue
                break
                
            if choice == -1:
                exit()

            elif choice == 1:
                DataDescription(self.data).describe()
            
            elif choice == 2:
                self.data = Imputation(self.data).imputer()

            elif choice == 3:
                self.data = Categorical(self.data).categoricalMain()

            elif choice == 4:
                self.data = FeatureScaling(self.data).scaling()

            elif choice == 5:
                download(self.data).download()

            else:
                print("\nWrong Integer value!! try again...")

obj = Preprocesser()

obj.preprocessingMain()    