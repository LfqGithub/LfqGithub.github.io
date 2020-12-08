"""
turn excel data of battery test result to hdf file.

input: excel data imported from neware battery equipment, from origin NDA data to excel.
output: 
  hdf file, contain cycle number--charge/discharge relation, detail of charge/discharge process
  to keys of the output hdf file
    1. cycle number--charge/discharge capacities and the decay rate.
    2. charge/discharge detail, time-action-voltage-current

>> because generally the excel file > 15Mb, so hdf format is used instead of csv file.

"""
import argparse 
import pandas as pd
import argparse
import matplotlib.pyplot as plt


parser=argparse.ArgumentParser(description="convert the excel file of battery test result from Neware equipment to HDF5 file")
parser.add_argument("-fn","--filename",help="Excel file to be converted")
args=parser.parse_args()

cycle_number_data=pd.read_excel(args.filename, sheet_name=1, skiprows=0, names=['channel_num','cycle_num', 'charge_capacity', 'discharge_capacity', 'decay_rate'])

detail_column_names=['record_num', 'status', 'jump_num', 'cycle_num','step_num', 'current_mA','voltage_V', 'capacity_mAh', 'energy_mWh', 'time_h_min_s_ms', 'absolute_time']

test_detail=pd.DataFrame(columns=detail_column_names)

isheet=3

while True:
    try: 
        tmp_data=pd.read_excel(args.filename, sheet_name=isheet, skiprows=0, names=detail_column_names)
    except IndexError as ie:
        break
    test_detail=pd.concat([test_detail, tmp_data], axis=0, join='inner',sort=False, ignore_index=True) 
    isheet+=1

#print(test_detail.tail(10))

cycle_number_data.to_hdf('1-5.h5', key='cycle_num--capacity', mode='w')
test_detail.to_hdf('1-5.h5', key='detail', mode='w')














