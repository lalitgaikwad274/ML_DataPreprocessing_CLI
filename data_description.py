import pandas as pd

class DataDescription():
    tasks = [
        '\n1. Describe a specific Column',
        '2. Show Properties of Each Column',
        '3. Show the Dataset'
    ]

    def __init__(self, data):
        self.data = data

    def showDataset(self):
        while(1):
            try:
                rows = int(input("\nHow many rows do you want to print? (press -1 to go back"))
                if rows == -1:
                    break
                if rows <= 0:
                    print("Numbers of row should be greater than zero")
                    continue

                print(self.data.head(rows))
            except ValueError:
                print("NUmeric value is required. Try again....")
                continue
            break
        return

    #function to print all columns
    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end=" ")


    def describe(self):

        while(1):
            print("\ntasks (data description)")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input("\n\nWhat you want to do? (Press -1 to go back) : "))
                except ValueError:
                    print("Integer value required. Try again.....")
                    continue
                break

            if choice == -1:
                break

            elif choice == 1:
                self.showColumns()
                while(1):
                    describeColumn = input("\n\n which column? : ").lower()
                    try:
                        print(self.data[describeColumn].describe())
                    except KeyError:
                        print("Column is not present. Try again....")
                        continue
                    break

            elif choice == 2:
                print(self.data.describe())
                print("\n\n")
                print(self.data.info())

            elif choice == 3:
                self.showDataset()
            
            else:
                print("\nWrong Integer value!! Try again...")