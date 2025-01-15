from autoviz.AutoViz_Class import AutoViz_Class


AV = AutoViz_Class()


import matplotlib.pyplot as plt
# %matplotlib inline
filename = "california_housing_train.csv"
dft = AV.AutoViz(
    filename
)