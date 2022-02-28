from tkinter import E
import pandas as pd
from sqlalchemy import column
from data_description import DataDescription

class Imputation:

    tasks = [
        "\n1. Show number of Null Values",
        "2. Remove Columns",
        "3. Fill Null Values (with mean)",
        "4. Fill Null Values (with median)",
        "5. Fill Null Values (with mode)",
        "6. Show the Dataset"
    ]

    def __init__(self, data):
        self.data = data

    def showColumns(self):
        print("Columns\n")
        for column in self.data.columns.values:
            print(column, end=" ")
        return

    def printNullvalues(self):
        print("\nNULL values of each column :")
        for column in self.data.columns.values:
            print('{0: <20}'.format(column) + '{0: <5}'.format(sum(pd.isnull(self.data[column]))))
        print("")
        return

    def removecolumn(self):
        self.showColumns()
        while(1):
            columns = input("\nEnter the column that you want to delete (Press -1 to go back) : ").lower()

            if columns == -1:
                break

            choice = input("Are you sure?(y/n) ")
            if choice == "y" or choice == "Y":
                try:
                    self.data.drop(columns.split(" "), axis=1, inplace=True)
                except KeyError:
                    print("Column is not present. Try again....")
                    continue
                print("Task Done.....")
                break
            else:
                print("Not Deleting.......")
        return

    def fillNullWithMean(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name (Press -1 to go back) : ").lower()
            if column == "-1":
                break
            choice = input("Are you sure?(y/n) : ")
            if choice == "y" or choice == "Y":
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mean())
                except KeyError:
                    print("Column is not present. Try again....")
                    continue
                except TypeError:
                    print("The Imputation is not possibale here. Try again....")
                    continue
                print("Done.....")
                break
            else:
                print("Not changing")
        return

    def fillNullWithMedian(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name (Press -1 to go back) : ").lower()
            if column == "-1":
                break
            choice = input("Are you sure?(y/n) : ")
            if choice == "y" or choice == "Y":
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].median())
                except KeyError:
                    print("Column is not present. Try again....")
                    continue
                except TypeError:
                    print("The Imputation is not possibale here. Try again....")
                    continue
                print("Done.....")
                break
            else:
                print("Not changing")
        return

    def fillNullWithMode(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name (Press -1 to go back) : ").lower()
            if column == "-1":
                break
            choice = input("Are you sure?(y/n) : ")
            if choice == "y" or choice == "Y":
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mode())
                except KeyError:
                    print("Column is not present. Try again....")
                    continue
                except TypeError:
                    print("The Imputation is not possibale here. Try again....")
                    continue
                print("Done.....")
                break
            else:
                print("Not changing")
        return

    def imputer(self):
        while(1):
            print("\nImputation tasks")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input("\nWhat you want to do? (Press -1 to go back) "))
                except ValueError:
                    print("Integer value required. Try again.....")
                    continue
                break

            if choice == -1:
                break

            elif choice==1:
                self.printNullvalues()

            elif choice==2:
                self.removecolumn()

            elif choice==3:
                self.fillNullWithMean()

            elif choice==4:
                self.fillNullWithMedian()

            elif choice==5:
                self.fillNullWithMode()

            elif choice==6:
                DataDescription.showDataset(self)

            else:
                print("\nWrong Integer value!! Try again....")
        
        return self.data