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




txt_encoding = 'utf-8'
# _____________________________________
json_encoding = 'utf-8'
json_indent = 3
json_ensure_ascii = False
# _____________________________________
csv_newline = ''
csv_delimiter = ','
csv_quotechar = ' '
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
exec(get_v_name_code())
print(f'{get_v_name(VNAME_N) = }')
'''
# T*
def get_v_name_code():
    lambda_coda = '''
get_v_name_lambda = lambda v: [key for key, variable in globals().items() if variable == VNAME_V]
VNAME_N = get_v_name_lambda(VNAME_V)
'''
    return lambda_coda

# ________________________________________________________________________________________________________
# Get the name of value
# T*
def get_v_name(VNAME_N):
    return VNAME_N[len(VNAME_N)-1]


# ________________________________________________________________________________________________________
# Get the code of: get the name of the function 
# T*
def get_fname_code():
    return 'sys._getframe().f_code.co_name' 


# ________________________________________________________________________________________________________
# Get the code of: get the f_locals dict of the function 
# T*
def get_flocals_dic_code():
    return 'sys._getframe().f_locals' 


# ________________________________________________________________________________________________________
# Get the value by its id
# T*
def get_value_by_id(obj_id):
    return ctypes.cast(obj_id, ctypes.py_object).value



# =========================================================================================================
# String
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
# Reverse the string
# T*
def reverse_str(str):
    return str[::-1]


# ________________________________________________________________________________________________________
# Get two ends of the string with range
# T*
def two_ends_of_str(str, front_c, end_c):
    return [str[:front_c], str[-end_c:]]

# ________________________________________________________________________________________________________
# Get two chars of the ends of the string with range
# T*
def two_end_chars_of_str(str):
    return two_ends_of_str(str, 1, 1)


# ________________________________________________________________________________________________________
# Check if the str is quotation marks str
# T*
def if_quots_str(str):
    if two_end_chars_of_str(str) == ['\'', '\''] or \
        two_end_chars_of_str(str) == ['\"', '\"']:
        return True
    else:
        return False


# ________________________________________________________________________________________________________
# Delete the quotation marks of the str
# T*
def delect_quots_of_str(quot_str):
    return quot_str[1:-1]


# ________________________________________________________________________________________________________
# Get the middle string by two ends strings
# T*
def get_b_from_abc(str_abc, str_a, str_c):
    return str_abc.strip(str_a).strip(str_c)


# ________________________________________________________________________________________________________
# Add a c to b to make abc
# T*
def add_ac_to_b_abc(str_a, str_b, str_c):
    return str_a + str_b + str_c


# ________________________________________________________________________________________________________
# Add new a c to b to make new abc
# T*
def change_mid_num_str(str_abc, str_a, str_c, new_a, new_c):
    b = get_b_from_abc(str_abc, str_a, str_c)
    new_num_str = add_ac_to_b_abc(new_a, num_str_2_num(b), new_c)
    return new_num_str


# ________________________________________________________________________________________________________
#  Change the int str to int variable
# T*
def int_str_2_int(int_str):
    if int_str.isdigit():
        int_str = int_str[::-1]
        result = 0
        for i in range(len(int_str)):
            result += (10 ** i) * int(int_str[i]) 
        return result
    else:
        return False


# ________________________________________________________________________________________________________
#  Make a judgement that whether a string is a float numeric string 
# T*
def if_float_str(float_str):
    str_split = float_str.split('.')
    # print(f'{str_split = }')
    if len(str_split) != 2:
        return False
    else:
        if str_split[0].isdigit() and str_split[1].isdigit():
            return [str_split[0], str_split[1]]
        elif str_split[0].isdigit() and str_split[1] == '':
            return [str_split[0], '0']


# ________________________________________________________________________________________________________
#  Change the float str to float variable
# T*
def float_str_2_float(float_str):
    float_s = if_float_str(float_str)
    if float_s:
        head_str = float_s[0]
        end_str = float_s[1]
        int_num = int_str_2_int(head_str)
        decimals_num = int_str_2_int(end_str) / (10 ** len(end_str)) 
        return int_num + decimals_num
    else:
        return False


# ________________________________________________________________________________________________________
# Change numeric string to numeric variable
# T*
def num_str_2_num(num_str):
    try:
        if num_str.isdigit():
           return int_str_2_int(num_str)
        elif if_float_str(num_str):
            return float_str_2_float(num_str)
        else:
            return False
    except:
        return num_str


# =========================================================================================================
# Print 
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
# Print x with f'{x = }'
# T*
def printf(input):
    print(f'{input = }')


# ________________________________________________________________________________________________________
# Print input with f'{input = }' and its type
# T*
def printt(input):
    print(f'type({input}) = {type(input)}')


# ________________________________________________________________________________________________________
# Print input with f'{input = }' and its type
# T*
def printft(input):
    print(f'input = {input}, type({input}) = {type(input)}')



# =========================================================================================================
# Path
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
# Get now path 
# T*
def get_now_path():
    return os.getcwd()


# ________________________________________________________________________________________________________
# Judge is the path or file is existed or null 
# T*
def if_path_or_file_exist(path):
    return True if os.path.exists(path) else False


# ________________________________________________________________________________________________________
# Judge is the path or file is null, if null then create
# T*
def if_path_not_exist_create(path):
    if not if_path_or_file_exist(path):
        os.makedirs(path)


# ________________________________________________________________________________________________________
# Get the extension of the file
# T*
def get_extension(file_name):
    rev_file_name = reverse_str(file_name)
    return reverse_str(rev_file_name.split('.')[0])


# ________________________________________________________________________________________________________
# Get the pure and name of the file
# T*
def get_pure_fileName(file_name):
    rev_file_name = reverse_str(file_name)
    return reverse_str(rev_file_name.split('.')[1])


# ________________________________________________________________________________________________________
# Get the extension and name of the file
# T*
def get_fileName_extension(file_name):
    rev_file_name = reverse_str(file_name)
    return [reverse_str(rev_file_name.split('.')[1]), reverse_str(rev_file_name.split('.')[0])]


# ________________________________________________________________________________________________________
# Get the path of the file
# T*
def get_file_path(file_path_name):
    return file_path_name[:-(reverse_str(file_path_name).index("/"))]


# =========================================================================================================
# Dir and Path
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
# If path not exist then create
# T*
def create_path_if_pathNul_from_filePath(file_path):
    if_path_not_exist_create(get_file_path(file_path))


# ________________________________________________________________________________________________________
# List all files on the dir
# T*
def list_dir(path):
    dir_list = os.listdir(path)
    return dir_list


# ________________________________________________________________________________________________________
# Connect path and file name
# T*
def connect_path_fileName(path, file_name):
    if path[-1] == '/':
        return path + file_name
    else:
        return path + '/' + file_name


# ________________________________________________________________________________________________________
# Clear the dir
# T*
def clear_dir(path):
    dir_list = list_dir(path)
    print(f'{dir_list = }')
    for f in dir_list:
        f_path = connect_path_fileName(path, f)
        print(f'{f_path = }')
        if '.' in f:
            os.remove(f_path)
        else:
            if len(list_dir(f_path)) == 0:
                os.rmdir(f_path)
            else:
                clear_dir(f_path)


# ________________________________________________________________________________________________________
# Delete the dir
# T*
def delete_dir(path):
    clear_dir(path)
    os.rmdir(path)
        



# =========================================================================================================
# Read and Write
# ________________________________________________________________________________________________________
# ________________________________________________________________________________________________________
# Open a txt file with its path
# T*
def read_txt(f_path):
    with open(file=f_path, mode="r", encoding=txt_encoding) as f:
        txt_str = f.read()
        return txt_str
    

# ________________________________________________________________________________________________________
# Write a txt file with its path
# T*
def write_txt(f_path, txt_str):
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="w", encoding=txt_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
# Write to add a txt file with its path behind the end of the file
# T*
def write_txt_add(f_path, txt_str):
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="a", encoding=txt_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
# Change dict to json str
# T*
def dict_2_jsonStr(dict):
    return json.dumps(dict)


# ________________________________________________________________________________________________________
# Change json dict to dict
# T*
def jsonStr_2_dict(json_str):
    return json.loads(json_str)


# ________________________________________________________________________________________________________
# Change dict to json dict obj
# json dict: all indexes are string type
# T*
def dict_2_jsonDict(dict):
    return json.loads(dict_2_jsonStr(dict)) 


# ________________________________________________________________________________________________________
# Change string list to numeric list  
# T*
def strList_2_numList(str_list):
    num_list = []
    for item in str_list:
        num_list.append(num_str_2_num(item))
    return num_list


# ________________________________________________________________________________________________________
# Change 2D string list to 2D numeric list 
# T*
def str2dlist_2_num2dlist(str_list):
    d2_num_list = []
    for item_d2 in str_list:
        d2_num_list.append(strList_2_numList(item_d2))
    return d2_num_list


# ________________________________________________________________________________________________________
# Read json str from a json file
# T*
def read_json_str(f_path):
    with open(file=f_path, mode="r", encoding=json_encoding) as f:
        txt_str = f.read()
        return txt_str


# ________________________________________________________________________________________________________
# Load json content as a dict from a json file
# T*
def read_json_as_dict(f_path):
    with open(file=f_path, mode="r", encoding=json_encoding) as f:
        return json.load(f)


# ________________________________________________________________________________________________________
# Generate dict from dict txt
# T*
def dictTxt_2_dict(dict_txt):
    return_dict = {}
    b_dict_txt = get_b_from_abc(dict_txt, '{', '}')
    b_dict_txt_list = b_dict_txt.split(',')
    for kv in  b_dict_txt_list:
        k_v = kv.split(':')
        key = k_v[0].split()[0]
        value = k_v[1].split()[0]
        if key.isdigit():
            key = num_str_2_num(key)
        return_dict[key] = value
    return return_dict


# ________________________________________________________________________________________________________
# Read str from txt file and change it to dict
# T*
def read_txt_2_dict(f_path):
    return jsonStr_2_dict(read_txt(f_path)) 


# ________________________________________________________________________________________________________
# Read str from txt file and change it to json dict
# T*
def read_txt_2_json_dict(f_path):
    return dict_2_jsonDict(jsonStr_2_dict(read_txt(f_path))) 


# ________________________________________________________________________________________________________
# Write json str into a json file
# T*
def write_str_in_json(f_path, json_str):
    write_txt(f_path, json_str)


# ________________________________________________________________________________________________________
# Write dict or json dict into a json file
# T*
def write_dict_in_json(f_path, dict):
    write_txt(f_path, dict_2_jsonStr(dict))


# ________________________________________________________________________________________________________
# Write dict or json dict into a txt file
# T*
def write_dict_in_txt(f_path, dict):
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
            csv_list.append(row_i)
        return csv_list


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










