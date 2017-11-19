import os
import random
import time
import glob


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
            new_file_path = filename[0:-4]+rand_name+".csv"
            #print('$$$$$$',new_file_path)
            #continue
            try:
                os.rename(filename,new_file_path)
            except:
                print('########')
                continue
            del_start_lines(new_file_path)
            print('-')

    ''' elif ext == ".txt":
          os.rename(filepath, filepath[0:ind]+rand_name+ ".csv")
        print('-#####-')'''
    return

def defin_header():
    return (r"lat,lon,name,Altitude,dele_colum,Date,Time")

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

start_time = time.time()
enter_dir(base_dir)
print("--- %s seconds ---" % (time.time() - start_time))