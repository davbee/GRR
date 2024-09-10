"""
First: 2022-07-05
Last: 2024-09-10

Modified the example program from https://pypi.org/project/GaugeRnR/
for easier use and interpretation of the results

This program calcualtes Gauge R&R parameters from test data.

# acceptance criteria for pass or fail of the measurements
# value = GaugeRnR Variance
if grr_value < 0.10:
    print('Gage R&R variance < 10%: Acceptable and good test method')
elif grr_value > 0.10 and value < 0.3:
    print('Gage R&R variance between 10-30%: Acceptable dependent upon \
method of measurement, application')
elif grr_value > 0.3:
    print('Gage R&R variance >30%: Unacceptable and requires improvement')

"""

# import GaugeRnR modules
from GaugeRnR import GaugeRnR, Result

# import numpy and pandas packages
import numpy as np
import pandas as pd


def array2d_to_3d(data: pd.DataFrame) -> np.ndarray:
    '''
    convert 2D array to 3D array
    '''
    # devide row number by 3
    rownum: int = int(data.shape[0] / 3)

    # reshape 2D array to Numpy 3D Array for three-operators of
    # three repeated measurements for three DUTs
    data3d: np.ndarray = np.reshape(data.to_numpy(), (3, rownum, 3))

    # print 3D GR&R Measurement Data
    print("GR&R Measurement Data:")
    print(data3d)

    return data3d


def main(link: str) -> np.float64:
    '''
    function to calculate Gauge R&R
    '''
    # Pandas_read_csv GR&R Data File
    grrdata2d: pd.DataFrame = pd.read_csv(link, usecols=["M1", "M2", "M3"])

    grrdata3d: np.ndarray = array2d_to_3d(grrdata2d)

    ########################################
    # run GaugeRnR package / module to calculate GR&R outputs
    g: GaugeRnR = GaugeRnR(grrdata3d)
    # print(type(g))
    result: dict = g.calculate()

    # print GR&R summary:
    print('\nSummary:')
    print(g.summary())

    ########################################
    # print GR&R Variances:
    print('\nGR&R Variances:')
    for key, value in result[Result.Var].items():
        print(f"{key}: {value:2.2%}")

    print('\n')
    ########################################
    # obtain GaugeGnR value and determine acceptance criteria
    grr: str = "GaugeRnR"
    grr_value: np.float64 = result[Result.Var].get(grr)
    # print(f"{grr}: {grr_value:2.2%}\n")

    # acceptance criteria for pass or fail of the measurements
    # value = GaugeRnR Variance
    if grr_value < 0.10:
        print('Gage RnR variance < 10%: Acceptable and good test method')
    elif grr_value > 0.10 and grr_value < 0.3:
        print('Gage RnR variance between 10-30%: '
              'Acceptable dependent upon method of measurement, application')
    elif grr_value > 0.3:
        print('Gage RnR variance >30%: Unacceptable and requires improvement')

    return grr_value


if __name__ == '__main__':
    # test data file
    testdata: str = "grrData.csv"
    gvalue = main(testdata)
