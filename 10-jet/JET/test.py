import matplotlib.mlab as mlab
import numpy as np
import pandas as pd


# [mean, variance] pairs are stored in a dictionary
conds = {}
conds[1] = [0, 100] # x and y
conds[2] = [200, 400]
conds[3] = [-200, 800]



# generate a common x values and set it as an index of the empty dataframe
# it needs to be equally spaced so that shifted graphs are not deformed
x = np.linspace(-400, 400, 801) # массив 1 ось x
df = pd.DataFrame(index=x) # массив 2 индексы X





# add 3 columns (normal distributions) to the dataframe
for key, value in conds.items(): #
    y = mlab.normpdf(x, value[0], np.sqrt(value[1]))
    df['col{}'.format(key)] = y #

# we want to shift all the graphs around index of 0 in this example
center_index = 0


# search for index locations of maximum values in each column
peak_locs = [df[x].argmax() for x in df.columns.tolist()]
offsets = [center_index - x for x in peak_locs]



# shift columns according to the offset from the desired center (which in this case is 0)
for offset, col in zip(offsets, df.columns):
    df[col] = df[col].shift(int(offset))



df.plot()

df.plot()