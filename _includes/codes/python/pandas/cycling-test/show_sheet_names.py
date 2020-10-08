import pandas as pd
import argparse


parse=argparse.ArgumentParser(description='Show the info of an excel file, such as sheet_names')
parse.add_argument("-f","--filename")
args=parse.parse_args()


def show_sheet_names(filename):
    summary=pd.ExcelFile(filename)
    print(summary.sheet_names)

show_sheet_names(args.filename)



