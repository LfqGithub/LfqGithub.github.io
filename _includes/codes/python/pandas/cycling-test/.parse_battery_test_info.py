import pandas as pd
import matplotlib.pyplot as plt
import argparse

parse=argparse.ArgumentParser(description='Parse the battery test result, such as the relation between cycle No and capacity.')
parse.add_argument("-f","--filename")
parse.add_argument("-cn","--channel number")
args=parse.parse_args()

summary=pd.ExcelFile(args.filename)

cycle_no_capacity=pd.read_excel(summary,'Cycle_98_9_1',names=['channel_no','cycle_no', 'charge_cap', 'discharge_cap','degradation_ratio'],index_col=1)

statis=pd.read_excel(summary,'Statis_98_9_1',names=['channel_no','cycle_no', 'step_no','original_step_no','state','start_v','end_v','start_i','end_i','capacity', 'duration_t','relative_t','absolute_t','net_discharge_cap','charge_cap','discharge_cap','net_discharge_cap','charge_energy','discharge_energy'],index_col=2)

#statis['absolute_t']=pd.to_datetime(statis['absolute_t'])

#cycle_no_capacity.plot(y=['charge_cap','discharge_cap'])

#print(statis.info())


# plot absolute time--charge capacity
#statis_charge_cap=statis.loc[lambda df:df['charge_cap']>0]
#statis_charge_cap.plot(x='absolute_t',y=['charge_cap'])

plt.show()


#print(cycle_no_capacity)
#print(statis['absolute_t'].head())
