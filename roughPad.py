import geoplotlib
import pandas as pd
import glob
all_filenames = []
base_dir = r'C:\Users\shrip\Pictures\url_downloads\test\PLTs\\'   # use your path
for filename in glob.glob(base_dir+'/**/*.csv', recursive=True):
    all_filenames.append(filename)
print(len(all_filenames))
i = 1
for file_name in all_filenames:

    i=i+1
    if i<242:
        print(i,file_name)
        continue

    #if i==39:
    #    continue
    try:
        data = geoplotlib.utils.read_csv(file_name)
    except:
        continue
    geoplotlib.dot(data,color='red',point_size=2)


#all_files = glob.glob(os.path.join(base_dir, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent


geoplotlib.show()
#print(all_filenames)