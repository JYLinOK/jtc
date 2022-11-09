"""
@Author: Jinwei Lin
@ORCID: 0003 0558 6699
@Time: 2022/07/25
@Description: Processsing libarary for json txt and csv.
"""


import json
import csv
import os
import ctypes
import time
import subprocess
from subprocess import Popen, PIPE



txt_encoding = 'utf-8'
# _____________________________________
json_encoding = 'utf-8'
json_indent = 3
json_ensure_ascii = False
# _____________________________________
csv_newline = ''
csv_delimiter = ','
csv_quotechar = '|'
csv_quoting = csv.QUOTE_MINIMAL
v = ''
# _____________________________________
VNAME_V = ''
VNAME_N = ''

# =========================================================================================================
# =========================================================================================================


# =========================================================================================================
# Varibles
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
# Execute the the variables name code
'''
# Menu:
VNAME_V = varible
exec(v_name_code())
print(f'{v_name(VNAME_N) = }')
'''
# T*
def v_name_code():
    lambda_coda = '''
v_name_lambda = lambda v: [key for key, variable in globals().items() if variable == VNAME_V]
VNAME_N = v_name_lambda(VNAME_V)
'''
    return lambda_coda

# ________________________________________________________________________________________________________
def v_name(VNAME_N:object):
    """
    Get the name of value
    """
    return VNAME_N[len(VNAME_N)-1]


# ________________________________________________________________________________________________________
def fname_code():
    """
    Get the code of: get the name of the function 
    """
    return 'sys._getframe().f_code.co_name' 


# ________________________________________________________________________________________________________
def flocals_dic_code():
    """
    Get the code of: get the f_locals dict of the function 
    """
    return 'sys._getframe().f_locals' 


# ________________________________________________________________________________________________________
def value_by_id(obj_id):
    """
    Get the value by its id
    """
    return ctypes.cast(obj_id, ctypes.py_object).value



# =========================================================================================================
# String
# ________________________________________________________________________________________________________
def reverse_str(str:str):
    """
    Reverse the string
    """
    return str[::-1]


# ________________________________________________________________________________________________________
def two_ends_of_str(str, front_ind:int, end_ind:int):
    """
    Get two ends of the string with range
    """
    return [str[:front_ind], str[-end_ind:]]


# ________________________________________________________________________________________________________
def two_end_chars_of_str(str:str):
    """
    Get two chars of the ends of the string with range
    """
    return two_ends_of_str(str, 1, 1)


# ________________________________________________________________________________________________________
def if_quots_str(str:str):
    """
    Check if the two ends of a str is quotations 
    """
    if two_end_chars_of_str(str) == ['\'', '\''] or \
        two_end_chars_of_str(str) == ['\"', '\"']:
        return True
    else:
        return False


# ________________________________________________________________________________________________________
def delect_quots_of_str(quot_str:str):
    """
    Delete the two ends quotation marks of the str
    """
    return quot_str[1:-1]


# ________________________________________________________________________________________________________
def b_from_abcStr(str_abc:str, substr_a:str, substr_c:str):
    """
    Get the middle string by two end substrings
    """
    if substr_a != '':
        return str_abc.strip(substr_a).strip(substr_c)
    else:
        ind = str_abc.index(substr_c)
        return str_abc[:ind]


# ________________________________________________________________________________________________________
def add_ac_to_b_abcStr(startstr_a:str, midstr_b:str, endstr_c:str):
    """
    Add startstr_a endstr_c to midstr_b to make str abc
    """
    return startstr_a + midstr_b + endstr_c


# ________________________________________________________________________________________________________
def abcStr_change_mid_num(str_abc:str, prestr_a:str, prestr_c:str, new_a:str, new_c:str):
    """
    Change the middle num value of a abcStr
    """
    b = b_from_abcStr(str_abc, prestr_a, prestr_c)
    new_numStr = add_ac_to_b_abcStr(new_a, numStr_2_num(b), new_c)
    return new_numStr


# ________________________________________________________________________________________________________
def intStr_2_int(int_str:str):
    """
    Change the int str to int variable
    """
    if int_str.isdigit():
        int_str = int_str[::-1]
        result = 0
        for i in range(len(int_str)):
            result += (10 ** i) * int(int_str[i]) 
        return result
    else:
        return False


# ________________________________________________________________________________________________________
def if_floatStr(floatStr:str):
    """
    Make a judgement that whether a string is a float numeric string
    """
    str_split = floatStr.split('.')
    # print(f'{str_split = }')
    if len(str_split) != 2:
        return False
    else:
        if str_split[0].isdigit() and str_split[1].isdigit():
            return [str_split[0], str_split[1]]
        elif str_split[0].isdigit() and str_split[1] == '':
            return [str_split[0], '0']


# ________________________________________________________________________________________________________
def floatStr_2_float(floatStr:str):
    """
    Change the float str to float variable
    """
    float_s = if_floatStr(floatStr)
    if float_s:
        head_str = float_s[0]
        end_str = float_s[1]
        int_num = intStr_2_int(head_str)
        decimals_num = intStr_2_int(end_str) / (10 ** len(end_str)) 
        return int_num + decimals_num
    else:
        return False


# ________________________________________________________________________________________________________
def numStr_2_num(numStr:str):
    """
    Change numeric string to numeric variable
    """
    try:
        if numStr.isdigit():
           return intStr_2_int(numStr)
        elif if_floatStr(numStr):
            return floatStr_2_float(numStr)
        else:
            return False
    except:
        return numStr



# =========================================================================================================
# Print 
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
def printf(input):
    """
    Print x with f'{x = }'
    """
    print(f'{input = }')


# ________________________________________________________________________________________________________
def printt(input):
    """
    Print input with f'{input = }' and its type
    """
    print(f'type({input}) = {type(input)}')


# ________________________________________________________________________________________________________
def printft(input):
    """"
    Print input with f'{input = }' and its type
    """
    print(f'input = {input}, type({input}) = {type(input)}')



# =========================================================================================================
# Path
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
def now_path():
    """
    Get now working path 
    """
    return os.getcwd()


# ________________________________________________________________________________________________________
def if_path_or_file_exist(path:str):
    """
    Judge is a path or file is existed or null 
    """
    return True if os.path.exists(path) else False


# ________________________________________________________________________________________________________
def if_path_not_exist_create(path:str):
    """
    Judge is a path is null, if null then create
    """
    if not if_path_or_file_exist(path):
        os.makedirs(path)


# ________________________________________________________________________________________________________
def if_path_not_exist_create_judge(path:str):
    """
    Judge is a path is null, if null then create, and return the judge result
    """
    if not if_path_or_file_exist(path):
        os.makedirs(path)
        return True
    else:
        return False


# ________________________________________________________________________________________________________
def if_file_not_exist_create(file_path:str, default_write:str=''):
    """"
    Judge is a file is null, if null then create
    """
    if not if_path_or_file_exist(file_path):
        write_file(file_path, default_write)


# ________________________________________________________________________________________________________
def if_file_not_exist_create_judge(file_path:str, default_write:str=''):
    """
    Judge if a file is null, if null then create, and return the judge result
    """
    if not if_path_or_file_exist(file_path):
        write_file(file_path, default_write)
        return True
    else:
        return False


# ________________________________________________________________________________________________________
def file_extension(file_path:str):
    """
    Get the extension of a file
    """
    rev_file_path = reverse_str(file_path)
    return reverse_str(rev_file_path.split('.')[0])


# ________________________________________________________________________________________________________
def path_fileName(file_path:str):
    """
    Get the path and file name of a file
    """
    rev_file_path = reverse_str(file_path)
    return reverse_str(rev_file_path.split('.')[1])


# ________________________________________________________________________________________________________
def only_fileName(file_path:str):
    """
    Get the only and diret pure file name of a file
    """
    a_path_fileName = path_fileName(file_path)
    return a_path_fileName.split('/')[-1]


# ________________________________________________________________________________________________________
def fileName_fileExtension(file_path:str):
    """
    Get the extension and name of a file
    """
    rev_file_path = reverse_str(file_path)
    return [reverse_str(rev_file_path.split('.')[1]), reverse_str(rev_file_path.split('.')[0])]


# ________________________________________________________________________________________________________
def file_path(file_path_name:str):
    """
    Get the exist dir of a file
    """
    return file_path_name[:-(reverse_str(file_path_name).index("/"))]


# ________________________________________________________________________________________________________
def file_path_noSprit(file_path_name:str):
    """
    Get the path of the file with no sprit symbol
    """
    return file_path_name[:-(reverse_str(file_path_name).index("/"))-1]


# =========================================================================================================
# Dir and Path
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
def create_path_if_pathNul_from_filePath(path:str):
    """
    If path not exist then create
    """
    if_path_not_exist_create(file_path(path))


# ________________________________________________________________________________________________________
def list_dir(path:str):
    """
    List all files and folders on the dir
    """
    dir_list = os.listdir(path)
    return dir_list


# ________________________________________________________________________________________________________
def connect_path_fileName(path:str, file_name:str):
    """
    Connect path and file name
    """
    if path[-1] == '/':
        return path + file_name
    else:
        return path + '/' + file_name


# ________________________________________________________________________________________________________
pre_path = ''
set_pre_path = False
def clear_dir(path:str):
    """
    Clear the dir
    """
    global pre_path
    global set_pre_path
    if not set_pre_path:
        pre_path = path
        set_pre_path = True
    dir_list = list_dir(path)
    history_dir_list = []
    if len(dir_list) > 0: 
        for f in dir_list:
            f_path = connect_path_fileName(path, f)
            if os.path.isfile(f_path):
                os.remove(f_path)
            elif os.path.isdir(f_path):
                if len(list_dir(f_path)) == 0:
                    os.rmdir(f_path)
                else:
                    history_dir_list.append(f_path)
                    clear_dir(f_path)
    else:
        os.rmdir(path)
    if path != pre_path:
        os.rmdir(path)



# ________________________________________________________________________________________________________
def delete_dir(path:str):
    """
    Delete the dir
    """
    clear_dir(path)
    os.rmdir(path)
        


# =========================================================================================================
# Read and Write
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
def read_txt(f_path:str):
    """
    Open a txt file with its path
    """
    with open(file=f_path, mode="r", encoding=txt_encoding) as f:
        txt_str = f.read()
        return txt_str


# ________________________________________________________________________________________________________
def readLines_txt(f_path:str):
    """
    Read a txt file with its path, in multiple lines
    """
    with open(file=f_path, mode="r", encoding=txt_encoding) as f:
        txt_str_list = f.readlines()
        return txt_str_list
    

# ________________________________________________________________________________________________________
def write_txt(f_path:str, txt_str:str):
    """
    Write a txt file with its path
    """
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="w", encoding=txt_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
def write_txt_add(f_path:str, txt_str:str):
    """
    Write to add a txt file with its path behind the end of the file
    """
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="a", encoding=txt_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
def dict_2_jsonStr(dict:dict):
    """
    Change dict to json str
    """
    return json.dumps(dict)


# ________________________________________________________________________________________________________
def jsonStr_2_dict(json_str:str):
    """
    Change json dict to dict
    """
    return json.loads(json_str)


# ________________________________________________________________________________________________________
def dict_2_jsonDict(dict:dict):
    """
    Change dict to json dict obj
    json dict: all indexes are string type
    """
    return json.loads(dict_2_jsonStr(dict)) 


# ________________________________________________________________________________________________________
def strList_2_numList(str_list:list):
    """
    Change string list to numeric list  
    """
    num_list = []
    for item in str_list:
        num_list.append(numStr_2_num(item))
    return num_list


# ________________________________________________________________________________________________________
def str2dlist_2_num2dlist(str_list:list):
    """
    Change 2D string list to 2D numeric list 
    """
    d2_num_list = []
    for item_d2 in str_list:
        d2_num_list.append(strList_2_numList(item_d2))
    return d2_num_list


# ________________________________________________________________________________________________________
def read_json_str(f_path:str):
    """
    Read json str from a json file
    """
    with open(file=f_path, mode="r", encoding=json_encoding) as f:
        txt_str = f.read()
        return txt_str


# ________________________________________________________________________________________________________
def read_json_as_dict_or_list(f_path:str):
    """
    Load json content as a dict or a list from a json file
    """
    with open(file=f_path, mode="r", encoding=json_encoding) as f:
        return json.load(f)


# ________________________________________________________________________________________________________
def dictTxt_2_dict(dict_txt:str):
    """
    Generate dict from dict txt
    """
    return_dict = {}
    b_dict_txt = b_from_abcStr(dict_txt, '{', '}')
    b_dict_txt_list = b_dict_txt.split(',')
    for kv in  b_dict_txt_list:
        k_v = kv.split(':')
        key = k_v[0].split()[0]
        value = k_v[1].split()[0]
        if key.isdigit():
            key = numStr_2_num(key)
        return_dict[key] = value
    return return_dict


# ________________________________________________________________________________________________________
def read_txt_2_dict(f_path:str):
    """
    Read str from txt file and change it to dict
    """
    return jsonStr_2_dict(read_txt(f_path)) 


# ________________________________________________________________________________________________________
def read_txt_2_json_dict(f_path:str):
    """
    Read str from txt file and change it to json dict
    """
    return dict_2_jsonDict(jsonStr_2_dict(read_txt(f_path))) 


# ________________________________________________________________________________________________________
def write_str_in_json(f_path:str, json_str:str):
    """
    Write json str into a json file
    """
    write_txt(f_path, json_str)


# ________________________________________________________________________________________________________
def write_dict_in_json(f_path:str, dict:dict):
    """
    Write dict or json dict into a json file
    """
    write_txt(f_path, dict_2_jsonStr(dict))


# ________________________________________________________________________________________________________
def write_dict_in_txt(f_path:str, dict:dict):
    """
    Write dict or json dict into a txt file
    """
    write_txt(f_path, str(dict))



# =====================================================================================================================
# =====================================================================================================================
# CSV
# ________________________________________________________________________________________________________
# Read a csv content from a csv file
# T*
def read_csv(csv_path):
    with open(file=csv_path, newline=csv_newline) as f:
        reader = csv.reader(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
        # print(f'{reader = }')
        csv_list = []
        for row_i in reader:
            csv_rwo_list = []
            for item in row_i:
                csv_rwo_list.append(item)
            csv_list.append(csv_rwo_list)
        return csv_list



# ________________________________________________________________________________________________________
# Read a csv content from a csv file, and do process for each line, not return
# T*
def read_csv_process_eachLine_func(csv_path, process_func, **params):
    with open(file=csv_path, newline=csv_newline) as f:
        reader = csv.reader(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
        # print(f'{reader = }')
        for row_i in reader:
            csv_rwo_list = []
            for item in row_i:
                csv_rwo_list.append(item)
            process_func(csv_rwo_list, **params)



# ________________________________________________________________________________________________________
# Read a csv content from a csv file and return the numeric list
# T*
def read_csv_as_num(csv_path):
    return str2dlist_2_num2dlist(read_csv(csv_path))


# ________________________________________________________________________________________________________
# Write a csv content into a csv file with one row
# T*
def write_csv_row(csv_path, data):
    create_path_if_pathNul_from_filePath(csv_path)
    with open(file=csv_path, mode='w', newline=csv_newline) as f:
        writer = csv.writer(f, delimiter=csv_delimiter, quotechar=csv_quotechar, quoting=csv_quoting)
        writer.writerow(data)
  

# ________________________________________________________________________________________________________
# Write a csv content into a csv file with rows
# T*
def write_csv_rows(csv_path, data, csvdelimi=csv_delimiter, csvquote=csv_quotechar, csvquoting=csv_quoting):
    create_path_if_pathNul_from_filePath(csv_path)
    with open(file=csv_path, mode='w', newline=csv_newline) as f:
        writer = csv.writer(f, delimiter=csvdelimi, quotechar=csvquote, quoting=csvquoting)
        writer.writerows(data)


# ________________________________________________________________________________________________________
# Copy the csv content from a copied csv file
# T*
def copy_csv(pre_csv_path, new_csv_path):
    write_csv_rows(new_csv_path, read_csv(pre_csv_path))


# ________________________________________________________________________________________________________
# Read a csv content and change it to a dict
# T*
def read_csv_2_dict(csv_path):
     with open(file=csv_path, newline=csv_newline) as f:
        reader = csv.DictReader(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
        d = {}
        index = 0
        for i in reader:
            d[index] = i
            index += 1
        return d


# ________________________________________________________________________________________________________
# Read a csv content from a csv file as a dict
# Dict Example: d = {0: {'1': '4', '2': '5', '3': '6'}, 1: {'1': '7', '2': '8', '3': '9'}}
# T*
def write_dict_in_csv(csv_path, dict):
    create_path_if_pathNul_from_filePath(csv_path)
    with open(file=csv_path, mode='w', newline=csv_newline) as f:
        fieldnames = []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        head = False
        for i in dict:
            if not head:
                for j in dict[i]:
                    fieldnames.append(j)
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                head = True
            else:
               break
        for i in dict:
            writer.writerow(dict[i])  
    

# ________________________________________________________________________________________________________
# Change str to csv list
# T*
def str_2_csvList(string):
    csv_list = []
    line_tiems = string.split('\n')
    for i_line in line_tiems:
        csv_items = i_line.split(',')
        csv_list.append(csv_items)
    return csv_list


# ________________________________________________________________________________________________________
# Change csv list to str
# T*
def csvList_2_str(csv_list):
    list_str = ''
    len_column = len(csv_list[0])
    for r_i in csv_list:
        r_i_str = ''
        for c_i_i in range(len_column):
            if c_i_i < len_column-1:
                r_i_str += r_i[c_i_i] + ','
            else:
                r_i_str += r_i[c_i_i] + '\n'
        list_str += r_i_str
    return list_str
        

# ________________________________________________________________________________________________________
# Read txt file to list variable
# T*
def read_csvTxt_2_list(txt_path):
    txt_str = read_txt(txt_path)
    return str_2_csvList(txt_str)


# ________________________________________________________________________________________________________
# Change txt file to csv file 
# T*
def txt_2_csv(txt_path, csv_path, csv_delimiter=csv_delimiter):     
    write_csv_rows(csv_path, read_csvTxt_2_list(txt_path), csvdelimi=csv_delimiter)


# ________________________________________________________________________________________________________
# Change csv file to txt file 
# T*
def csv_2_txt(csv_path, txt_path, delimiter=csv_delimiter):     
    csv_list = read_csv(csv_path)
    csv_str = ''
    for item_row in csv_list:
        csv_str_row = ''
        for item_column in item_row:
            csv_str_row += str(item_column) + delimiter
        csv_str += csv_str_row + '\n'
    write_txt(txt_path, csv_str[:len(csv_str)-1])


# ________________________________________________________________________________________________________
# Change txt file to csv file by changing extension
# T*
def txt_2_csv_exten(txt_path, csv_path):
    txt = read_txt(txt_path)
    write_txt(csv_path, txt)


# ________________________________________________________________________________________________________
# Change csv file to txt file by changing extension
# T*
def csv_2_txt_exten(csv_path, txt_path):
    csv = read_csv(csv_path)
    write_txt(txt_path, csvList_2_str(csv))



# =====================================================================================================================
# =====================================================================================================================
# Other files
# ________________________________________________________________________________________________________
# Write a file with its path
# T*
def write_file(f_path, txt_str):
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="w", encoding=txt_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
# Write to add a file with its path behind the end of the file
# T*
def write_file_add(f_path, txt_str):
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="a", encoding=txt_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
# Read a file with its path
# T*
def read_file(f_path):
    with open(file=f_path, mode="r", encoding=txt_encoding) as f:
        file_str = f.read()
        return file_str


# ________________________________________________________________________________________________________
# Read a file with its path, with multiple lines
# T*
def readLines_file(f_path):
    with open(file=f_path, mode="r", encoding=txt_encoding) as f:
        file_str_list = f.readlines()
        return file_str_list


# ________________________________________________________________________________________________________
# Run mutiple codes in a list orderly
# T*
def run_codes(codes):
    codes = strsList_2_str_and(codes)
    os_codes = subprocess.Popen(codes, shell=True)
    return os_codes


# ________________________________________________________________________________________________________
# Run mutiple codes in a list orderly
# T*
def run_codes_os(codes):
    codes = strsList_2_str_and(codes)
    os.system(codes)



# ________________________________________________________________________________________________________
# Last dir name of the path
# T*
def last_dir(path):
    return path.split('/')[-1]


# ________________________________________________________________________________________________________
# First dir name of the path
# T*
def first_dir(path):
    return path.split('/')[0]


# ________________________________________________________________________________________________________
# Combine the strs in a list to a big str
# T*
def strsList_2_str(strs_list):
    big_str = ''
    for str_i in strs_list:
        big_str += str_i
    return big_str


# ________________________________________________________________________________________________________
# Combine the strs in a list to a big str, with and
# T*
def strsList_2_str_and(strs_list):
    big_str = ''
    for i in range(len(strs_list)):
        if i < len(strs_list)-1:
            big_str += strs_list[i] + ' & '
        else:
            big_str += strs_list[i]
    return big_str


# ________________________________________________________________________________________________________
# Combine the strs in a list to a big str, without space
# T*
def strsList_2_str_noSpace(strs_list):
    big_str = ''
    for str_i in strs_list:
        big_str += str_i.strip()
    return big_str


# ________________________________________________________________________________________________________
# Combine the strs in a list to a big str, with specific split
# T*
def strsList_2_str_split(strs_list, split=' '):
    big_str = ''
    for str_i in strs_list:
        big_str += str_i.strip() + split
    return big_str


# ________________________________________________________________________________________________________
# Combine the strs in a list to a big str, with specific split
# T*
def strsList_to_noSpace(strs_list):
    big_strList = []
    for str_i in strs_list:
        big_strList.append(str_i.strip())
    return big_strList


# ________________________________________________________________________________________________________
# Return if a str is a annotaiton or not
# T*
def if_annota(str, annota='#'):
    if first_char(str) == annota:
        return True
    else: return False


# ________________________________________________________________________________________________________
# Return the first char of a str
# T*
def first_char(str):
    for char in str:
        if char not in ['', '\n', ' ']:
            return char

            
# ________________________________________________________________________________________________________
# Get a pure str from a str, delete the space and newline symbol
# T*
def str_noSpace(str):
    new_str = ''
    for i in str:
        if i not in [' ']:
            new_str += i
    return new_str


# ________________________________________________________________________________________________________
# Delete any spaces in a str: Delete the br and space on the two end of a str
# T*
def str_pure(str):
    new_str = ''
    for i in str:
        if i not in [' ', '\n']:
            new_str += i
    return new_str


# ________________________________________________________________________________________________________
# Delete br line str in str list and strip the space of the NOBR str
# T*
def delete_br_space_in_strList(strList):
    bigStrList = []
    for str_i in strList:
        if str_i.strip() not in ['\n', '']:
            bigStrList.append(str_pure(str_i))
    return bigStrList




# ________________________________________________________________________________________________________
# Check if the substr is purely inside the str
# T*
def if_subStr_pureIn_str(subStr, str, able=['', ' ', '=', '\n']):
    subStr = subStr.strip()
    if subStr in str:
        subStr_ind = str.index(subStr)
        if subStr_ind != 0:
            front_bit = str[subStr_ind-1:subStr_ind]
        else:
            front_bit = ''
        if subStr_ind != len(str)-len(subStr):
            back_bit = str[subStr_ind+len(subStr):subStr_ind+len(subStr)+1]
        else:
            back_bit = ''
        if front_bit in able and back_bit in able:
            return True
        else:
            return False
    else:
        return False



# ________________________________________________________________________________________________________
# Print item in str list one by one BR
# T*
def print_br_strList(strList):
    for item in strList:
        print(item)



# ________________________________________________________________________________________________________
# Get the middle str that is between two special strs
# T*
def str_between_2strs(astr, str1, str2):
    ind1 = 0
    ind2 = 0
    if str1 in astr and str2 in astr:
        ind1 = astr.index(str1)
        ind2 = astr.index(str2)
        return astr[ind1+len(str1):ind2]
    


# ________________________________________________________________________________________________________
# Get the json files list in a sprcial dir
# T* 
def json_filesList_in_dir(dir):
    files_list = os.listdir(dir)
    # print(f"{files_list = }")
    json_f_list = []
    for file in files_list:
        if file_extension(file) == 'json':
            json_f_list.append(file)
    return json_f_list



# ________________________________________________________________________________________________________
# Get the json file names list in a sprcial dir
# T* 
def json_fileListNames_in_dir(dir):
    files_list = os.listdir(dir)
    # print(f"{files_list = }")
    json_f_name_list = []
    for file in files_list:
        if file_extension(file) == 'json':
            json_f_name_list.append(file.split('.')[0])
    return json_f_name_list



# ________________________________________________________________________________________________________
# Make split operation for each item in list
# T*
def split_items_in_strList(strList, asplit, ind):
    new_list = []
    for it in strList:
        new_list.append(it.split(asplit)[ind])
    return new_list


# ________________________________________________________________________________________________________
# Make split operation for each item in list
# T*
def split_items_in_strList_bySplitList(strList, splitList, ind):
    new_list = []
    for it in strList:
        for item in splitList:
            if item in it:
                new_list.append(it.split(item)[ind])
                break
    return new_list


















# ========================================================
# ========================================================
