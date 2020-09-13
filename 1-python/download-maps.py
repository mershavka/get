import requests
import os
import shutil
import pathlib

# names = [
# 'python',
# 'c-plus-plus-logo',
# 'c-sharp-logo'
# ]

path = str(pathlib.Path().absolute()) + '/maps'
print(path)

try:
	shutil.rmtree(path)
except OSError:
    print ("Deletion of the directory %s failed" % path)
else:
    print ("Successfully deleted the directory %s" % path)

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


# https://img.icons8.com/theme/color/size/name

# https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/2020/0912/AQUA_MODIS.20200912.L3m.DAY.SST.sst.4km.NRT.nc.png

first = 'https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/2020/09'
second = '/AQUA_MODIS.202009'
last = '.L3m.DAY.SST.sst.4km.NRT.nc.png'

# iconSize = 50
# iconTheme = 'ios'
# colors = {'blue': '005EB8', 'orange': 'FF9919'}

for i in range(1, 13):
    num = str(i).zfill(2)

    name = first + num + second + num + last
    print(name)

    r = requests.get(name, allow_redirects=True)
    open(path + '/' + num + '.png', 'wb').write(r.content)