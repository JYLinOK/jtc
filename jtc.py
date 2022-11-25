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



open_encoding = 'utf-8'
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
"""
# Menu:
VNAME_V = varible
exec(v_name_code())
print(f'{v_name(VNAME_N) = }')
"""

def v_name_code():
    """
    Return the code to get the name of a value
    """
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
def reverse_str(astr:str):
    """
    Reverse the string
    """
    return astr[::-1]


# ________________________________________________________________________________________________________
def change_all_subStr_in_str(astr:str, pre_subStr:str, new_subStr:str):
    """
    Change all of the same special subStr in a astr, rewrite the astr
    """
    new_str = ''
    while pre_subStr in astr:
        pre_subStr_ind = astr.index(pre_subStr)
        new_str += astr[:pre_subStr_ind]+new_subStr
        astr = astr[pre_subStr_ind+len(pre_subStr):]
    new_str += astr
    return new_str



# ________________________________________________________________________________________________________
def two_ends_of_str(astr, front_ind:int, end_ind:int):
    """
    Get two ends of the string with range
    """
    return [astr[:front_ind], astr[-end_ind:]]


# ________________________________________________________________________________________________________
def two_end_chars_of_str(astr:str):
    """
    Get two chars of the ends of the string with range
    """
    return two_ends_of_str(astr, 1, 1)


# ________________________________________________________________________________________________________
def if_quots_str(astr:str):
    """
    Check if the two ends of a astr is quotations 
    """
    if two_end_chars_of_str(astr) == ['\'', '\''] or \
        two_end_chars_of_str(astr) == ['\"', '\"']:
        return True
    else:
        return False


# ________________________________________________________________________________________________________
def delect_quots_of_str(quot_str:str):
    """
    Delete the two ends quotation marks of the astr
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
    Add startstr_a endstr_c to midstr_b to make astr abc
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
    Change the int astr to int variable
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
    Change the float astr to float variable
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
    with open(file=f_path, mode="r", encoding=open_encoding) as f:
        txt_str = f.read()
        return txt_str


# ________________________________________________________________________________________________________
def readLines_txt(f_path:str):
    """
    Read a txt file with its path, in multiple lines
    """
    with open(file=f_path, mode="r", encoding=open_encoding) as f:
        txt_str_list = f.readlines()
        return txt_str_list
    

# ________________________________________________________________________________________________________
def write_txt(f_path:str, txt_str:str):
    """
    Write a txt file with its path
    """
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="w", encoding=open_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
def write_txt_add(f_path:str, txt_str:str):
    """
    Write to add a txt file with its path behind the end of the file
    """
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="a", encoding=open_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
def dict_2_jsonStr(dict:dict):
    """
    Change dict to json astr
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
    Read json astr from a json file
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
    Read astr from txt file and change it to dict
    """
    return jsonStr_2_dict(read_txt(f_path)) 


# ________________________________________________________________________________________________________
def read_txt_2_json_dict(f_path:str):
    """
    Read astr from txt file and change it to json dict
    """
    return dict_2_jsonDict(jsonStr_2_dict(read_txt(f_path))) 


# ________________________________________________________________________________________________________
def write_str_in_json(f_path:str, json_str:str):
    """
    Write json astr into a json file
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
def read_csv(csv_path:str):
    """
    Read a csv content from a csv file
    """
    with open(file=csv_path, newline=csv_newline, encoding=open_encoding) as f:
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
def read_csv_process_eachLine_func(csv_path:str, process_func, **params):
    """
    Read a csv content from a csv file, and do process for each line, not return
    """
    with open(file=csv_path, newline=csv_newline, encoding=open_encoding) as f:
        reader = csv.reader(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
        # print(f'{reader = }')
        for row_i in reader:
            csv_rwo_list = []
            for item in row_i:
                csv_rwo_list.append(item)
            process_func(csv_rwo_list, **params)



# ________________________________________________________________________________________________________
def read_csv_as_num(csv_path:str):
    """
    Read a csv content from a csv file and return the numeric list
    """
    return str2dlist_2_num2dlist(read_csv(csv_path))


# ________________________________________________________________________________________________________
def write_add_new_csv_row(csv_path:str, data:list, delimiter:str=csv_delimiter, quotechar:str=csv_quotechar, quoting:str=csv_quoting):
    """
    Write to add a csv content line after the end a csv file with one row
    """
    create_path_if_pathNul_from_filePath(csv_path)
    with open(file=csv_path, mode='a', newline=csv_newline, encoding=open_encoding) as f:
        writer = csv.writer(f, delimiter=csv_delimiter, quotechar=csv_quotechar, quoting=csv_quoting)
        writer.writerow(data)
  

# ________________________________________________________________________________________________________
def write_csv_rows(csv_path:str, data:list, csvdelimi=csv_delimiter, csvquote=csv_quotechar, csvquoting=csv_quoting):
    """
    Write a csv content into a csv file with rows
    """
    create_path_if_pathNul_from_filePath(csv_path)
    with open(file=csv_path, mode='w', newline=csv_newline, encoding=open_encoding) as f:
        writer = csv.writer(f, delimiter=csvdelimi, quotechar=csvquote, quoting=csvquoting)
        writer.writerows(data)


# ________________________________________________________________________________________________________
def copy_csv(pre_csv_path:str, new_csv_path:str):
    """
    Copy the csv content from a copied csv file
    """
    write_csv_rows(new_csv_path, read_csv(pre_csv_path))


# ________________________________________________________________________________________________________
def read_csv_2_dict(csv_path:str):
    """
    Read a csv content and change it to a dict
    """
    with open(file=csv_path, newline=csv_newline, encoding=open_encoding) as f:
        reader = csv.DictReader(f, delimiter=csv_delimiter, quotechar=csv_quotechar)
        d = {}
        index = 0
        for i in reader:
            d[index] = i
            index += 1
        return d


# ________________________________________________________________________________________________________
def write_dict_in_csv(csv_path:str, dict:dict):
    """
    Write a dict into a csv file by its structure
    Dict Example: d = {0: {'1': '4', '2': '5', '3': '6'}, 1: {'1': '7', '2': '8', '3': '9'}}
    """
    create_path_if_pathNul_from_filePath(csv_path)
    with open(file=csv_path, mode='w', newline=csv_newline, encoding=open_encoding) as f:
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
def write_dict_in_csv_byLines(csv_path:str, data:dict, csvdelimi=csv_delimiter, csvquote=csv_quotechar, csvquoting=csv_quoting):
    """
    Write a dict into a csv file with one line by one line
    Example:
    a = {
        "title":["123", "abc"],
        "url":["http://123", "http://abc"],
        "content":["this content 123", "this content abc"],
    } will be writen as:
    abc,http://abc,this content abc
    abc,http://abc,this content abc
    """
    create_path_if_pathNul_from_filePath(csv_path)

    alist = []
    header = []
    content = []

    for it in data:
        header.append(it)
        content.append(data[it])
    alist.append(header)
    # alist += content
    all_contents = []
    for i in range(len(content[0])):
        a_content = []
        for it in content:
            a_content.append(it[i])
        all_contents.append(a_content)
    alist = alist + all_contents
    # print(f'{alist = }')
    write_csv_rows(csv_path, alist, csvdelimi, csvquote, csvquoting)

    

# ________________________________________________________________________________________________________
def str_2_csvList(string:str):
    """
    Change astr to csv list
    """
    csv_list = []
    line_tiems = string.split('\n')
    for i_line in line_tiems:
        csv_items = i_line.split(',')
        csv_list.append(csv_items)
    return csv_list


# ________________________________________________________________________________________________________
def csvList_2_str(csv_list:list):
    """
    Change csv list to astr
    """
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
def read_csvTxt_2_list(txt_path:str):
    """
    Read txt file to list variable
    """
    txt_str = read_txt(txt_path)
    return str_2_csvList(txt_str)


# ________________________________________________________________________________________________________
def txt_2_csv(txt_path:str, csv_path:str, csv_delimiter=csv_delimiter):     
    """
    Change txt file to csv file 
    """
    write_csv_rows(csv_path, read_csvTxt_2_list(txt_path), csvdelimi=csv_delimiter)


# ________________________________________________________________________________________________________
def csv_2_txt(csv_path:str, txt_path:str, delimiter=csv_delimiter):     
    """
    Change csv file to txt file 
    """
    csv_list = read_csv(csv_path)
    csv_str = ''
    for item_row in csv_list:
        csv_str_row = ''
        for item_column in item_row:
            csv_str_row += astr(item_column) + delimiter
        csv_str += csv_str_row + '\n'
    write_txt(txt_path, csv_str[:len(csv_str)-1])


# ________________________________________________________________________________________________________
def txt_2_csv_exten(txt_path:str, csv_path:str):
    """
    Change txt file to csv file by changing extension
    """
    txt = read_txt(txt_path)
    write_txt(csv_path, txt)


# ________________________________________________________________________________________________________
def csv_2_txt_exten(csv_path:str, txt_path:str):
    """
    Change csv file to txt file by changing extension
    """
    csv = read_csv(csv_path)
    write_txt(txt_path, csvList_2_str(csv))



# =====================================================================================================================
# =====================================================================================================================
# Other files
# ________________________________________________________________________________________________________
def write_file(f_path:str, txt_str:str):
    """
    Write a file with its path
    """
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="w", encoding=open_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
def write_file_add(f_path:str, txt_str:str):
    """
    Write to add a file with its path behind the end of the file
    """
    create_path_if_pathNul_from_filePath(f_path)
    with open(file=f_path, mode="a", encoding=open_encoding) as f:
        f.write(txt_str)


# ________________________________________________________________________________________________________
def read_file(f_path:str):
    """
    Read a file with its path
    """
    with open(file=f_path, mode="r", encoding=open_encoding) as f:
        file_str = f.read()
        return file_str


# ________________________________________________________________________________________________________
def readLines_file(f_path:str):
    """
    Read a file with its path, with multiple lines
    """
    with open(file=f_path, mode="r", encoding=open_encoding) as f:
        file_str_list = f.readlines()
        return file_str_list


# ________________________________________________________________________________________________________
def run_codes(codes:str):
    """
    Run mutiple codes in a list orderly
    """
    codes = strsList_2_str_and(codes)
    os_codes = subprocess.Popen(codes, shell=True)
    return os_codes


# ________________________________________________________________________________________________________
def run_codes_os(codes:str):
    """
    Run mutiple codes in a list orderly
    """
    codes = strsList_2_str_and(codes)
    os.system(codes)



# ________________________________________________________________________________________________________
def last_dir(path:str):
    """
    Last dir name of the path
    """
    return path.split('/')[-1]


# ________________________________________________________________________________________________________
def first_dir(path:str):
    """
    First dir name of the path
    """
    return path.split('/')[0]


# ________________________________________________________________________________________________________
def strsList_2_str(strs_list:list):
    """"
    Combine the strs in a list to a big astr
    """
    big_str = ''
    for str_i in strs_list:
        big_str += str_i
    return big_str


# ________________________________________________________________________________________________________
def strsList_2_str_and(strs_list:list):
    """
    Combine the strs in a list to a big astr, with and
    """
    big_str = ''
    for i in range(len(strs_list)):
        if i < len(strs_list)-1:
            big_str += strs_list[i] + ' & '
        else:
            big_str += strs_list[i]
    return big_str


# ________________________________________________________________________________________________________
def strsList_2_str_noSpace(strs_list:list):
    """
    Combine the strs in a list to a big astr, without space
    """
    big_str = ''
    for str_i in strs_list:
        big_str += str_i.strip()
    return big_str


# ________________________________________________________________________________________________________
def strsList_2_str_split(strs_list:list, split:str=' '):
    """
    Combine the strs in a list to a big astr, with specific split
    """
    big_str = ''
    for str_i in strs_list:
        big_str += str_i.strip() + split
    return big_str


# ________________________________________________________________________________________________________
def strsList_to_noSpace(strs_list:list):
    """
    Combine the strs in a list to a big astr, with specific split
    """
    big_strList = []
    for str_i in strs_list:
        big_strList.append(str_i.strip())
    return big_strList


# ________________________________________________________________________________________________________
def if_annota(astr:str, annota:str='#'):
    """
    Return if a astr is a annotaiton or not
    """
    if first_char(astr) == annota:
        return True
    else: return False


# ________________________________________________________________________________________________________
def first_char(astr:str):
    """
    Return the first char of a astr
    """
    for char in astr:
        if char not in ['', '\n', ' ']:
            return char

            
# ________________________________________________________________________________________________________
def str_noSpace(astr:str):
    """
    Get a pure astr from a astr, delete the space and newline symbol
    """
    new_str = ''
    for i in astr:
        if i not in [' ']:
            new_str += i
    return new_str


# ________________________________________________________________________________________________________
def str_pure(astr:str):
    """
    Delete any spaces in a astr: Delete the br and space on the two end of a astr
    """
    new_str = ''
    for i in astr:
        if i not in [' ', '\n']:
            new_str += i
    return new_str


# ________________________________________________________________________________________________________
def delete_br_space_in_strList(strList:list):
    """
    Delete br and space line astr in astr list and strip the space of the NOBR astr
    """
    bigStrList = []
    for str_i in strList:
        if str_i.strip() not in ['\n', '']:
            bigStrList.append(str_pure(str_i))
    return bigStrList



# ________________________________________________________________________________________________________
def delete_space_in_strList(strList:list):
    """
    Delete space astr in astr list and strip the space of the NOBR astr
    """
    bigStrList = []
    for str_i in strList:
        if str_i.strip() not in ['']:
            bigStrList.append(str_i)
    return bigStrList



# ________________________________________________________________________________________________________
def if_subStr_pureIn_str(subStr:str, astr:str, able:list=['', ' ', '=', '\n']):
    """
    Check if the substr is purely inside the astr
    """
    subStr = subStr.strip()
    if subStr in astr:
        subStr_ind = astr.index(subStr)
        if subStr_ind != 0:
            front_bit = astr[subStr_ind-1:subStr_ind]
        else:
            front_bit = ''
        if subStr_ind != len(astr)-len(subStr):
            back_bit = astr[subStr_ind+len(subStr):subStr_ind+len(subStr)+1]
        else:
            back_bit = ''
        if front_bit in able and back_bit in able:
            return True
        else:
            return False
    else:
        return False


# ________________________________________________________________________________________________________
def print_br_strList(strList:list):
    """
    Print item in astr list one by one BR
    """
    for item in strList:
        print(item)



# ________________________________________________________________________________________________________
def str_between_2strs(astr:str, str1:str, str2:str):
    """
    Get the middle astr that is between two special strs
    """
    ind1 = 0
    ind2 = 0
    if str1 in astr and str2 in astr:
        ind1 = astr.index(str1)
        ind2 = astr.index(str2)
        return astr[ind1+len(str1):ind2]
    


# ________________________________________________________________________________________________________
def json_filesList_in_dir(dir:str):
    """
    Get the json files list in a sprcial dir
    """
    files_list = os.listdir(dir)
    # print(f"{files_list = }")
    json_f_list = []
    for file in files_list:
        if file_extension(file) == 'json':
            json_f_list.append(file)
    return json_f_list



# ________________________________________________________________________________________________________
def json_fileListNames_in_dir(dir:str):
    """
    Get the json file names list in a sprcial dir
    """
    files_list = os.listdir(dir)
    # print(f"{files_list = }")
    json_f_name_list = []
    for file in files_list:
        if file_extension(file) == 'json':
            json_f_name_list.append(file.split('.')[0])
    return json_f_name_list



# ________________________________________________________________________________________________________
def split_items_in_strList(strList:list, asplit:str, ind:int):
    """
    Make split operation for each item in list
    """
    new_list = []
    for it in strList:
        new_list.append(it.split(asplit)[ind])
    return new_list


# ________________________________________________________________________________________________________
def split_items_in_strList_bySplitList(strList:list, splitList:list, ind:int):
    """
    Make split operation for each item in list
    """
    new_list = []
    for it in strList:
        for item in splitList:
            if item in it:
                new_list.append(it.split(item)[ind])
                break
    return new_list























# ========================================================
if __name__ == "__main__":
    # import jtc
    # print(help(jtc))
    print(f'jtc by Jinwei Lin')



# ========================================================
