import plotly.express as px
import csv
import numpy as np

def plotGraph(data_csv):
    with open(data_csv) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    student_marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : student_marks, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks Of Students vs Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "D:/DATA DESKTOP/Notes Of Code/Python/Homework/Pro-C106Correlation/Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotGraph(data_path)

setup()

