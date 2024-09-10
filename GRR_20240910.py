"""
David Pih on 2022-07-05

Modified the example program from https://pypi.org/project/GaugeRnR/
for easier use and interpretation of the results

install GaugeRnR package
! pip install GaugeRnR
"""

# import GaugeRnR modules
from GaugeRnR import GaugeRnR, Result

# import numpy and pandas packages
import numpy as np
import pandas as pd

########################################
# Modify the data in the Google Sheet grrData to obtain GR&R analysis

########################################
# GR&R data as csv format; replace data if necessary
# url = 'https://drive.google.com/file/d/1zBmUbYpAHvQauV3qu6O3-4FjUL2IeMGx/view?usp=sharing'
# link = 'https://drive.google.com/uc?id=' + url.split('/')[-2]

#######################################
# GR&R data as Google Sheet format; replace data if necessary
# url = 'https://docs.google.com/spreadsheets/d/1X7abCjLLenbyptWCAL23Ti4PiRZG4UhCem1FZ8s1eB8/edit#gid=0'
# sheet_id = url.split('/')[-2]
# tab_name = 'testData'
# link = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={tab_name}"

link: str = "grrData.csv"
########################################
# Pandas_read_csv GR&R Data File
grrdata2d = pd.read_csv(link, usecols=["M1", "M2", "M3"])
rownum = int(grrdata2d.shape[0] / 3)

# reshape 2D array to Numpy 3D Array for three-operators of three repeated measurements for three DUTs
grrdata3d = np.reshape(grrdata2d.to_numpy(), (3, rownum, 3))

# print 3D GR&R Measurement Data
print('GR&R Measurement Data:')
print(grrdata3d)

########################################
# run GaugeRnR package / module to calculate GR&R outputs
g = GaugeRnR(grrdata3d)
result = g.calculate()

# print GR&R summary:
print('Summary:')
print(g.summary())

########################################
# print GR&R Variances:
print('GR&R Variances:')
for key, value in result[Result.Var].items():
    print(f"{key}: {value:2.2%}")

grr: str = "GaugeRnR"
grr_value = result[Result.Var].get(grr)
print(f"{grr}: {grr_value:2.2%}")
########################################
# acceptance criteria for pass or fail of the measurements
# value = GaugeRnR Variance
if grr_value < 0.10:
    print('Gage R&R variance < 10%: Acceptable and good test method')
elif grr_value > 0.10 and value < 0.3:
    print('Gage R&R variance between 10-30%: Acceptable dependent upon \
method of measurement, application')
elif grr_value > 0.3:
    print('Gage R&R variance >30%: Unacceptable and requires improvement')
