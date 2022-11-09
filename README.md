### jtc
Processsing for json txt and csv.

## Version 1.0.3 Updation:


# NAME
    jtc

# Author
    Jinwei Lin

# Update:
1. Normalize the commnets and definitions of the functions and function values.


# DESCRIPTION
    @Author: Jinwei Lin
    @ORCID: 0003 0558 6699
    @Time: 2022/07/25
    @Description: Processsing libarary for json txt and csv.


# FUNCTIONS
    abcStr_change_mid_num(str_abc: str, prestr_a: str, prestr_c: str, new_a: str, new_c: str)
        Change the middle num value of a abcStr
    
    add_ac_to_b_abcStr(startstr_a: str, midstr_b: str, endstr_c: str)
        Add startstr_a endstr_c to midstr_b to make str abc
    
    b_from_abcStr(str_abc: str, substr_a: str, substr_c: str)
        Get the middle string by two end substrings
    
    clear_dir(path: str)
        Clear the dir
    
    connect_path_fileName(path: str, file_name: str)
        Connect path and file name
    
    copy_csv(pre_csv_path: str, new_csv_path: str)
        Copy the csv content from a copied csv file
    
    create_path_if_pathNul_from_filePath(path: str)
        If path not exist then create
    
    csvList_2_str(csv_list: list)
        Change csv list to str
    
    csv_2_txt(csv_path: str, txt_path: str, delimiter=',')
        Change csv file to txt file
    
    csv_2_txt_exten(csv_path: str, txt_path: str)
        Change csv file to txt file by changing extension
    
    delect_quots_of_str(quot_str: str)
        Delete the two ends quotation marks of the str
    
    delete_br_space_in_strList(strList: list)
        Delete br line str in str list and strip the space of the NOBR str
    
    delete_dir(path: str)
        Delete the dir
    
    dictTxt_2_dict(dict_txt: str)
        Generate dict from dict txt
    
    dict_2_jsonDict(dict: dict)
        Change dict to json dict obj
        json dict: all indexes are string type
    
    dict_2_jsonStr(dict: dict)
        Change dict to json str
    
    fileName_fileExtension(file_path: str)
        Get the extension and name of a file
    
    file_extension(file_path: str)
        Get the extension of a file
    
    file_path(file_path_name: str)
        Get the exist dir of a file
    
    file_path_noSprit(file_path_name: str)
        Get the path of the file with no sprit symbol
    
    first_char(str: str)
        Return the first char of a str
    
    first_dir(path: str)
        First dir name of the path
    
    floatStr_2_float(floatStr: str)
        Change the float str to float variable
    
    flocals_dic_code()
        Get the code of: get the f_locals dict of the function
    
    fname_code()
        Get the code of: get the name of the function
    
    if_annota(str: str, annota: str = '#')
        Return if a str is a annotaiton or not
    
    if_file_not_exist_create(file_path: str, default_write: str = '')
        "
        Judge is a file is null, if null then create
    
    if_file_not_exist_create_judge(file_path: str, default_write: str = '')
        Judge if a file is null, if null then create, and return the judge result
    
    if_floatStr(floatStr: str)
        Make a judgement that whether a string is a float numeric string
    
    if_path_not_exist_create(path: str)
        Judge is a path is null, if null then create
    
    if_path_not_exist_create_judge(path: str)
        Judge is a path is null, if null then create, and return the judge result
    
    if_path_or_file_exist(path: str)
        Judge is a path or file is existed or null
    
    if_quots_str(str: str)
        Check if the two ends of a str is quotations
    
    if_subStr_pureIn_str(subStr: str, str: str, able: list = ['', ' ', '=', '\n'])
        Check if the substr is purely inside the str
    
    intStr_2_int(int_str: str)
        Change the int str to int variable
    
    jsonStr_2_dict(json_str: str)
        Change json dict to dict
    
    json_fileListNames_in_dir(dir: str)
        Get the json file names list in a sprcial dir
    
    json_filesList_in_dir(dir: str)
        Get the json files list in a sprcial dir
    
    last_dir(path: str)
        Last dir name of the path
    
    list_dir(path: str)
        List all files and folders on the dir
    
    now_path()
        Get now working path
    
    numStr_2_num(numStr: str)
        Change numeric string to numeric variable
    
    only_fileName(file_path: str)
        Get the only and diret pure file name of a file
    
    path_fileName(file_path: str)
        Get the path and file name of a file
    
    print_br_strList(strList: list)
        Print item in str list one by one BR
    
    printf(input)
        Print x with f'{x = }'
    
    printft(input)
        "
        Print input with f'{input = }' and its type
    
    printt(input)
        Print input with f'{input = }' and its type
    
    readLines_file(f_path: str)
        Read a file with its path, with multiple lines
    
    readLines_txt(f_path: str)
        Read a txt file with its path, in multiple lines
    
    read_csv(csv_path: str)
        Read a csv content from a csv file
    
    read_csvTxt_2_list(txt_path: str)
        Read txt file to list variable
    
    read_csv_2_dict(csv_path: str)
        Read a csv content and change it to a dict
    
    read_csv_as_num(csv_path: str)
        Read a csv content from a csv file and return the numeric list
    
    read_csv_process_eachLine_func(csv_path: str, process_func, **params)
        Read a csv content from a csv file, and do process for each line, not return
    
    read_file(f_path: str)
        Read a file with its path
    
    read_json_as_dict_or_list(f_path: str)
        Load json content as a dict or a list from a json file
    
    read_json_str(f_path: str)
        Read json str from a json file
    
    read_txt(f_path: str)
        Open a txt file with its path
    
    read_txt_2_dict(f_path: str)
        Read str from txt file and change it to dict
    
    read_txt_2_json_dict(f_path: str)
        Read str from txt file and change it to json dict
    
    reverse_str(str: str)
        Reverse the string
    
    run_codes(codes: str)
        Run mutiple codes in a list orderly
    
    run_codes_os(codes: str)
        Run mutiple codes in a list orderly
    
    split_items_in_strList(strList: list, asplit: str, ind: int)
        Make split operation for each item in list
    
    split_items_in_strList_bySplitList(strList: list, splitList: list, ind: int)
        Make split operation for each item in list
    
    str2dlist_2_num2dlist(str_list: list)
        Change 2D string list to 2D numeric list
    
    strList_2_numList(str_list: list)
        Change string list to numeric list
    
    str_2_csvList(string: str)
        Change str to csv list
    
    str_between_2strs(astr: str, str1: str, str2: str)
        Get the middle str that is between two special strs
    
    str_noSpace(str: str)
        Get a pure str from a str, delete the space and newline symbol
    
    str_pure(str: str)
        Delete any spaces in a str: Delete the br and space on the two end of a str
    
    strsList_2_str(strs_list: list)
        "
        Combine the strs in a list to a big str
    
    strsList_2_str_and(strs_list: list)
        Combine the strs in a list to a big str, with and
    
    strsList_2_str_noSpace(strs_list: list)
        Combine the strs in a list to a big str, without space
    
    strsList_2_str_split(strs_list: list, split: str = ' ')
        Combine the strs in a list to a big str, with specific split
    
    strsList_to_noSpace(strs_list: list)
        Combine the strs in a list to a big str, with specific split
    
    two_end_chars_of_str(str: str)
        Get two chars of the ends of the string with range
    
    two_ends_of_str(str, front_ind: int, end_ind: int)
        Get two ends of the string with range
    
    txt_2_csv(txt_path: str, csv_path: str, csv_delimiter=',')
        Change txt file to csv file
    
    txt_2_csv_exten(txt_path: str, csv_path: str)
        Change txt file to csv file by changing extension
    
    v_name(VNAME_N: object)
        Get the name of value
    
    v_name_code()
        Return the code to get the name of a value
    
    value_by_id(obj_id)
        Get the value by its id
    
    write_csv_row(csv_path: str, data)
        Write a csv content into a csv file with one row
    
    write_csv_rows(csv_path: str, data, csvdelimi=',', csvquote='|', csvquoting=0)
        Write a csv content into a csv file with rows
    
    write_dict_in_csv(csv_path: str, dict: dict)
        Read a csv content from a csv file as a dict
        Dict Example: d = {0: {'1': '4', '2': '5', '3': '6'}, 1: {'1': '7', '2': '8', '3': '9'}}
    
    write_dict_in_json(f_path: str, dict: dict)
        Write dict or json dict into a json file
    
    write_dict_in_txt(f_path: str, dict: dict)
        Write dict or json dict into a txt file
    
    write_file(f_path: str, txt_str: str)
        Write a file with its path
    
    write_file_add(f_path: str, txt_str: str)
        Write to add a file with its path behind the end of the file
    
    write_str_in_json(f_path: str, json_str: str)
        Write json str into a json file
    
    write_txt(f_path: str, txt_str: str)
        Write a txt file with its path
    
    write_txt_add(f_path: str, txt_str: str)
        Write to add a txt file with its path behind the end of the file

# DATA
    PIPE = -1
    VNAME_N = ''
    VNAME_V = ''
    csv_delimiter = ','
    csv_newline = ''
    csv_quotechar = '|'
    csv_quoting = 0
    json_encoding = 'utf-8'
    json_ensure_ascii = False
    json_indent = 3
    pre_path = ''
    set_pre_path = False
    txt_encoding = 'utf-8'
    v = ''


### jtc by Jinwei Lin


