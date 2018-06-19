from __future__ import print_function, division
from nilmtk import DataSet, HDFDataStore, TimeFrame
from os.path import join
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math
from nilmtk.metrics import f1_score # metrics is actually different; need to look at this
from nilmtk.metrics import rms_error_power
from nilmtk.metrics import mean_normalized_error_power
from nilmtk.disaggregate import fhmm_exact # OK, only different in what is printed to screen (and this is diagonal covariance matrix)

building_number = 1
ds = DataSet('/nilmtk/data/iawe.h5') #('/nilmtk/data/ukdale.h5') #("/data/REDD/redd.h5")
print(ds.buildings)

train = DataSet('/nilmtk/data/iawe.h5') #('/nilmtk/data/ukdale.h5') #("/data/REDD/redd.h5")
test = DataSet('/nilmtk/data/iawe.h5') #('/nilmtk/data/ukdale.h5') #("/data/REDD/redd.h5")

elec = train.buildings[building_number].elec

mains = elec.mains()
df_all = mains.power_series_all_data() #df_all has a bunch of NaNs
df_all_noNan = df_all.dropna()
a = df_all_noNan.keys()
middleTime = a[int(math.floor(a.size/2))]
middleTimeStr = "%d-%02d-%02d %02d:%02d:%02d" % (middleTime.year, middleTime.month, middleTime.day, middleTime.hour, middleTime.minute, middleTime.second)

print(middleTimeStr)

train.set_window(end=middleTimeStr)
test.set_window(start=middleTimeStr)

train_elec = train.buildings[building_number].elec
test_elec = test.buildings[building_number].elec

top_train_elec = train_elec.submeters().select_top_k(k=5)

fhmm = fhmm_exact.FHMM() #mk change this later  to default
fhmm.train(top_train_elec, sample_period=60, resample=True)

outputAddress = "/nilmtk/data/iawe_449_3.h5"
output = HDFDataStore(outputAddress, 'w')
fhmm.disaggregate(test_elec.mains(), output, sample_period=60, resample=True)
output.close()

disag = DataSet(outputAddress) #load FHMM prediction
disag_elec = disag.buildings[building_number].elec
#disag_elec.plot() # plot all disaggregated data
f1 = f1_score(disag_elec, test_elec)
f1.index = disag_elec.get_labels(f1.index)
f1.plot(kind='barh')

disag.store.window = TimeFrame(start='2013-07-10 18:00:00-05:00', end='2013-07-17 04:00:00-05:00')
disag.buildings[building_number].elec.plot() # plot all disaggregated data



