import pandas as pd
import glob
import time


all_filenames = []
max_lat_from_file = []
min_lat_from_file = []
max_long_from_file = []
min_long_from_file = []

base_dir = r'C:\Users\shrip\Pictures\url_downloads\test\PLTs\\'   # use your path
#all_files = glob.glob(os.path.join(base_dir, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

Test_GIT = 'abcde'

def query_csv_filepaths(curr_dir):
   #print('enterd')
   for filename in glob.glob(curr_dir+'/**/*.csv', recursive=True):
       all_filenames.append(filename)
   print(len(all_filenames))

def readallcsv_getmaxmin(filename_list):
   i=1
   for each in filename_list:
      #print(each)
      try:
         df = pd.read_csv(each,usecols=[0,1],skipinitialspace=True)
         max_lat, max_long = df.values.max(axis=0)
         min_lat, min_long = df.values.min(axis=0)
         max_lat_from_file.append(max_lat)
         min_lat_from_file.append(min_lat)
         max_long_from_file.append(max_long)
         min_long_from_file.append(min_long)

      except:
         print('------')
         continue
      #print(df)
      #print(i)
      i=i+1

   print(max(max_lat_from_file))
   print(max(max_long_from_file))
   print(min(min_lat_from_file))
   print(min(min_long_from_file))


'''df_from_each_file = (pd.read_csv(f,usecols=[0,1],skiprows=6) for f in all_filenames)



for each_file in df_from_each_file:
   max_lat,max_long = each_file.values.max(axis=0)
   min_lat, min_long = each_file.values.min(axis=0)
   max_lat_from_file.append(max_lat)
   min_lat_from_file.append(min_lat)
   max_long_from_file.append(max_long)
   min_long_from_file.append(min_long)
   
'''

start_time = time.time()
query_csv_filepaths(base_dir)
if len(all_filenames) > 0:
   readallcsv_getmaxmin(all_filenames)
print("--- %s seconds ---" % (time.time() - start_time))
#concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
# doesn't create a list, nor does it append to one