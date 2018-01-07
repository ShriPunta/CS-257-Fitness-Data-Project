import os
import random
import time
import glob
import pandas as pd

base_dir = r'C:\Users\shrip\Pictures\url_downloads\test\Data\\'   # use your path

out_dir = base_dir+r"onlyCSVs\\"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)



all_nfile_paths_list = []
def fill_list_of_filenames(curr_filepath):
    for filename in glob.glob(curr_filepath + '/**/*.plt', recursive=True):
        all_nfile_paths_list.append(filename)

def defin_header():
    return (r"lat,lon,name,Altitude,dele_colum,Date,Time")

def enter_dir(curr_filepath):
    fill_list_of_filenames(curr_filepath)
    #print('-------',all_nfile_paths_map)
    for filename in all_nfile_paths_list:
       # print(filename)
       b, ext = os.path.splitext(filename)
       if ext == ".plt":
            rand_name = str(random.randrange(0, 99999))
            #print('^&^&^&',filename)
            new_file_path = out_dir+b[-14:]+".csv" #+rand_name+".csv"
            #print('$$$$$$',new_file_path)
            #continue
            try:
                df = pd.read_csv(skiprows=6,usecols=[0,1],header=None,filepath_or_buffer=filename)
                df.to_csv(new_file_path,encoding='utf-8',index=False,header=["lat","lon"])
            except:
                print("ISOO!!")
                continue
            '''try:
                os.rename(filename,new_file_path)
            except:
                print('########')
                continue
            del_start_lines(new_file_path)
            print('-')'''

    ''' elif ext == ".txt":
          os.rename(filepath, filepath[0:ind]+rand_name+ ".csv")
        print('-#####-')'''
    return


start_time = time.time()
enter_dir(base_dir)
print("--- %s seconds ---" % (time.time() - start_time))