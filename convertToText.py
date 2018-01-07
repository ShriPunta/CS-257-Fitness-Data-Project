import os
import random
import time
import glob
import pandas as pd
import shutil

base_dir = r'C:\\Users\\shrip\\Pictures\\url_downloads\\Zips\\allcolumns\\convertedToCSVs\\convertedToCSVs\\'   # use your path

out_dir = base_dir+r"allInOne\\"

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

all_nfile_paths_list = []
def fill_list_of_filenames(curr_filepath):
    #for root, dirs, files in os.walk(curr_filepath, topdown=True):
     # for filename in files:
    for filename in glob.glob(curr_filepath + '/**/*.plt', recursive=True):
        all_nfile_paths_list.append(filename)
        #filepath = os.path.join(root,filename)
        #print(filepath)

        #print(filename.replace('\\','\\\\'))

        #print(ext)
        #print(b)
        #del_start_lines(filepath)



def enter_dir(curr_filepath):
    fill_list_of_filenames(curr_filepath)
    #print('-------',all_nfile_paths_map)
    for filename in all_nfile_paths_list:
       # print(filename)
       b, ext = os.path.splitext(filename)
       if ext == ".plt":
            rand_name = str(random.randrange(0, 99999))
            #print('^&^&^&',filename)
            new_file_path = out_dir+b[-14:]+".csv"
            #print('$$$$$$',new_file_path)
            #continue
            '''try:
                os.rename(filename,new_file_path)
            except:
                print('########')
                continue
            del_start_lines(new_file_path)
            print('-')'''
            try:
                df = pd.read_csv(skiprows=6,usecols=[0,1,5,6],header=None,filepath_or_buffer=filename)
                df.to_csv(new_file_path,encoding='utf-8',index=False,header=defin_header())
            except:
                print("ISOO!!")
                continue

    ''' elif ext == ".txt":
          os.rename(filepath, filepath[0:ind]+rand_name+ ".csv")
        print('-#####-')'''
    return

def defin_header():
    return (["lat","lon","Date","Time"])

#delete first 6 lines and a header
def del_start_lines(filename):
    f = open(filename,'r+')
    lines = f.readlines()
    f.seek(0,0)

    #f = open(filename, 'w')
    f.write(defin_header())
    f.write('\n')
    f.writelines(lines[6:])
    f.close()

def merge_all_csvs(base_path):


    # import csv files from folder

    allFilesSize = len(glob.glob(base_path + "/*.csv"))
    with open(out_dir+'oneFile.csv', 'wb') as outfile:
        for i, fname in enumerate(glob.glob(base_path + "/*.csv")):
            with open(fname, 'rb') as infile:
                if i != 0:
                    infile.readline()  # Throw away header on all but first file
                # Block copy rest of file from input to output without parsing
                shutil.copyfileobj(infile, outfile)
                #print(fname + " has been imported.")
                print(allFilesSize-i)

start_time = time.time()
merge_all_csvs(base_dir)
#enter_dir(base_dir)
print("--- %s seconds ---" % (time.time() - start_time))