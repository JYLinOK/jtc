import json
import csv
from cv2 import split

from nbformat import read




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















# ________________________________________________________________________________________________________
# Open a txt file with its path
def read_txt(f_path):
    with open(file=f_path, mode="r", encoding=txt_encoding) as f:
        txt_str = f.read()
        return txt_str


# ________________________________________________________________________________________________________
# Write a txt file with its path
def write_txt(f_path, txt_str):
    with open(file=f_path, mode="w", encoding=txt_encoding) as f:
        f.write(txt_str)



# ________________________________________________________________________________________________________
# Write to add a txt file with its path behind the end of the file
def write_txt_add(f_path, txt_str):
    with open(file=f_path, mode="a", encoding=txt_encoding) as f:
        f.write(txt_str)



# ________________________________________________________________________________________________________
# Change dict to json str
def dict_2_json_str(dict):
    return json.dumps(dict)



# ________________________________________________________________________________________________________
# Change json dict to dict
def json_str_2_dict(json_str):
    return json.loads(json_str)



# ________________________________________________________________________________________________________
# Change dict to json dict obj
# json dict: all indexes are string type
def dict_2_json_dict(dict):
    return json.loads(dict_2_json_str(dict)) 



# ________________________________________________________________________________________________________
#  Change the int str to int variable
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
def num_str_2_num(num_str):
    try:
        if num_str.isdigit():
           return int_str_2_int(num_str)
        elif if_float_str(num_str):
            return float_str_2_float(num_str)
    except:
        return num_str



# ________________________________________________________________________________________________________
# Change string list to numeric list 
def str_list_2_num_list(str_list):
    num_list = []
    for item in str_list:
        num_list.append(num_str_2_num(item))
    return num_list



# ________________________________________________________________________________________________________
# Change string list to numeric list 
def str_2dlist_2_num_2dlist(str_list):
    d2_num_list = []
    for item_d2 in str_list:
        d2_num_list.append(str_list_2_num_list(item_d2))
    return d2_num_list



# ________________________________________________________________________________________________________
# Change dict to json dict obj
# If the str index of item is number string, change it to number
def json_dict_2_dict(json_dict):
    for i in json_dict:
        if not i.isalpha():
            if i.isdigit():
                print(f'{i = } is an int number')
    return json.load(dict_2_json_str(dict)) 



# ________________________________________________________________________________________________________
# Read json str from a json file
def read_json_str(f_path):
    with open(file=f_path, mode="r", encoding=json_encoding) as f:
        txt_str = f.read()
        return txt_str


# ________________________________________________________________________________________________________
# Load json content as a dict from a json file
def read_json_dict(f_path):
    with open(file=f_path, mode="r", encoding=json_encoding) as f:
        return json.load(f)


# ________________________________________________________________________________________________________
# Read str from txt file and change it to dict
def read_txt_2_dict(f_path):
    return json_str_2_dict(read_txt(f_path)) 



# ________________________________________________________________________________________________________
# Read str from txt file and change it to json dict
def read_txt_2_json_dict(f_path):
    return dict_2_json_dict(json_str_2_dict(read_txt(f_path))) 



# ________________________________________________________________________________________________________
# Write json str into a json file
def write_str_in_json(f_path, json_str):
    with open(file=f_path, mode="w", encoding=json_encoding) as f:
        json.dump(json_str, f, indent=json_indent, ensure_ascii=json_ensure_ascii)



# ________________________________________________________________________________________________________
# Write dict or json dict into a txt file
def write_dict_in_json(f_path, dict):
    write_txt(f_path, dict_2_json_str(dict))


# ________________________________________________________________________________________________________
# Write dict or json dict into a txt file
def write_dict_in_txt(f_path, dict):
    write_txt(f_path, dict_2_json_str(dict))



# =====================================================================================================================
# =====================================================================================================================
# CSV
# ________________________________________________________________________________________________________
# Read a csv content from a csv file
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
def read_csv_as_num(csv_path):
    return str_2dlist_2_num_2dlist(read_csv(csv_path))



# ________________________________________________________________________________________________________
# Write a csv content into a csv file with one row
def write_csv_row(csv_path, data):
    with open(file=csv_path, mode='w', newline=csv_newline) as f:
        writer = csv.writer(f, delimiter=csv_delimiter, quotechar=csv_quotechar, quoting=csv_quoting)
        writer.writerow(data)
  


# ________________________________________________________________________________________________________
# Write a csv content into a csv file with rows
def write_csv_rows(csv_path, data, csvdelimi=csv_delimiter, csvquote=csv_quotechar, csvquoting=csv_quoting):
    with open(file=csv_path, mode='w', newline=csv_newline) as f:
        writer = csv.writer(f, delimiter=csvdelimi, quotechar=csvquote, quoting=csvquoting)
        writer.writerows(data)



# ________________________________________________________________________________________________________
# Copy the csv content from a copied csv file
def copy_csv(pre_csv_path, new_csv_path):
    write_csv_rows(new_csv_path, read_csv(pre_csv_path))



# ________________________________________________________________________________________________________
# Read a csv content and change it to a dict
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
def write_csv_as_dict(csv_path, dict):
     with open(file=csv_path, mode='w', newline=csv_newline) as f:
        fieldnames = []
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # print(f'{dict = }')
        head = False
        for i in dict:
            if not head:
                # print(f'{dict[i] = }')
                for j in dict[i]:
                    fieldnames.append(j)
                    # print(f'{j = }')
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                head = True
            else:
               break
        for i in dict:
            writer.writerow(dict[i])  
    

# ________________________________________________________________________________________________________
# Split multiple lines string variable to multiple sublist list variable 
def str_2_csv_list(string):
    csv_list = []
    line_tiems = string.split('\n')
    for i_line in line_tiems:
        csv_items = i_line.split(',')
        csv_list.append(csv_items)
    return csv_list


# ________________________________________________________________________________________________________
# Read txt file to list variable
def read_txt_2_list(txt_path):
    txt_str = read_txt(txt_path)
    return str_2_csv_list(txt_str)



# ________________________________________________________________________________________________________
# Change txt file to csv file 
def txt_2_csv(txt_path, csv_path, csv_delimiter=csv_delimiter):     
    write_csv_rows(csv_path, read_txt_2_list(txt_path), csvdelimi=csv_delimiter)

       
# ________________________________________________________________________________________________________
# Change csv file to txt file 
def csv_2_txt(csv_path, txt_path, delimiter=csv_delimiter):     
    csv_list = read_csv(csv_path)
    csv_str = ''
    for item_row in csv_list:
        csv_str_row = ''
        for item_column in item_row:
            csv_str_row += str(item_column) + delimiter
        csv_str += csv_str_row + '\n'
    write_txt(txt_path, csv_str[:len(csv_str)-1])



























# Test
# =================================================================================
