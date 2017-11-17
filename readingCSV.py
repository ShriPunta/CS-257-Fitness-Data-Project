import pandas as pd
import glob
import time
start_time = time.time()


base_dir = r'C:\Users\shrip\Downloads\Geolife Trajectories 1.3\Data\\'   # use your path
#all_files = glob.glob(os.path.join(base_dir, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

all_filenames = []
for filename in glob.glob(base_dir+'/**/*.plt', recursive=True):
    all_filenames.append(filename)
print(len(all_filenames))
#print(all_filenames)

df_from_each_file = (pd.read_csv(f,usecols=[0,1],skiprows=6) for f in all_filenames)

max_lat_from_file = []
min_lat_from_file = []
max_long_from_file = []
min_long_from_file = []


for each_file in df_from_each_file:
   max_lat,max_long = each_file.values.max(axis=0)
   min_lat, min_long = each_file.values.min(axis=0)
   max_lat_from_file.append(max_lat)
   min_lat_from_file.append(min_lat)
   max_long_from_file.append(max_long)
   min_long_from_file.append(min_long)
   ''' max_lat_from_file.append(each_file['Latitude'].max())
    max_long_from_file.append(each_file['Longitude'].max())
    min_lat_from_file.append(each_file['Latitude'].min())
    min_long_from_file.append(each_file['Longitude'].min())'''

print(max(max_lat_from_file))
print(max(max_long_from_file))
print(min(min_lat_from_file))
print(min(min_long_from_file))

print("--- %s seconds ---" % (time.time() - start_time))
#concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
# doesn't create a list, nor does it append to one