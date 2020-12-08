import pandas as pd
import argparse
import matplotlib.pyplot as plt



def get_sheet_names(filename):
    summary=pd.ExcelFile(filename)
    return summary.sheet_names

def read_cycle(excel_name, nrow):
    excel_data=pd.read_excel(excel_name, sheet_name=1, nrows=nrow, skiprows=0, names=['channel_num','cycle_num', 'charge_capacity', 'discharge_capacity', 'decay_rate'])
    return excel_data

def show_charge_discharge_cycle_num(df):
    df.plot(x='cycle_num', y='discharge_capacity')
    plt.show()

nrow=None
filename='1C-4F-channel1-5.xls'
sheet_name=get_sheet_names(filename)

df=read_cycle(filename, nrow)
show_charge_discharge_cycle_num(df)





