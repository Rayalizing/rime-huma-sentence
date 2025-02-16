import os
from collections import OrderedDict

# Function to read a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to write content to a file
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def get_aux_code_map(file_list):
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "\t" not in line:
                    continue
                params = line.strip().split('\t')
                character = params[0]
                encoding = params[1]
                if "'" not in encoding:
                    if character not in dict_data:
                        dict_data[character] = [encoding]
                    else:
                        if encoding not in dict_data[character]:
                            dict_data[character].append(encoding)
    return dict_data

def get_shouxin_aux_code_map(file_list):
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "=" not in line:
                    continue
                params = line.strip().split('=')
                character = params[0]
                encoding = params[1]
                if "'" not in encoding:
                    if character not in dict_data:
                        dict_data[character] = [encoding]
                    else:
                        if encoding not in dict_data[character]:
                            dict_data[character].append(encoding)
    return dict_data

def get_xh_aux_code_map(file_list):
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "\t" in line:
                    params = line.strip().split('\t')
                    character = params[0]
                    encoding = params[1]
                    if "'" not in encoding:
                        encoding_pre = encoding[:2]
                        encoding_post = encoding[2:]
                        if character not in dict_data:
                            dict_data[character] = [encoding_post]
                        else:
                            if encoding_post not in dict_data[character]:
                                dict_data[character].append(encoding_post)

    return dict_data

def get_zrm_aux_code_map(file_list):
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "\t" in line:
                    params = line.strip().split('\t')
                    character = params[0]
                    encoding = params[1]
                    if "'" not in encoding:
                        encoding_pre = encoding[:2]
                        encoding_post = encoding[3:]
                        if character not in dict_data:
                            dict_data[character] = [encoding_post]
                        else:
                            if encoding_post not in dict_data[character]:
                                dict_data[character].append(encoding_post)
    return dict_data

def get_shoumo_aux_code_map(file_list):
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "\t" in line:
                    line = line.strip()
                    if line == '':
                        continue
                    if '\t' not in line:
                        continue
                    params = line.strip().split('\t')
                    character = params[0]
                    encoding = params[1]
                    if "'" not in encoding:
                        shoumo_encode = encoding[0] + encoding[-1]
                        
                        if character not in dict_data:
                            dict_data[character] = [shoumo_encode]
                        else:
                            if shoumo_encode not in dict_data[character]:
                                dict_data[character].append(shoumo_encode)
    return dict_data

def get_full4_aux_code_map(file_list):
    """
    将四码方案中的字转换为全四码编码，每两码用[隔开，全码不足四码的补0。
    例如：
    字：的
    全码（虎码）：u0[00,un[id
    """
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "\t" in line:
                    params = line.strip().split('\t')
                    character = params[0]
                    encoding = params[1]
                    if "'" not in encoding:
                        encoding_pre = encoding[:2]
                        encoding_post = encoding[2:]
                        # 判定前缀长度是否不足2位，如果不足则用“0”补足
                        if len(encoding_pre) < 2:
                            encoding_pre = encoding_pre.ljust(2, '0')  # 调用 ljust（左对齐）方法，指定最终宽度为 2，向右填充字符为 '0'。

                        # 判定后缀长度是否不足2位，如果不足则用“0”补足
                        if len(encoding_post) < 2:
                            encoding_post = encoding_post.ljust(2, '0')
                        encodingfull = encoding_pre + '[' + encoding_post

                        if character not in dict_data:
                            dict_data[character] = [encodingfull]
                        else:
                            if encodingfull not in dict_data[character]:
                                dict_data[character].append(encodingfull)
    return dict_data

def get_pre2_aux_code_map(file_list):
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "\t" in line:
                    params = line.strip().split('\t')
                    character = params[0]
                    encoding = params[1]
                    if "'" not in encoding:
                        encoding_pre = encoding[:2]
                        
                        if character not in dict_data:
                            dict_data[character] = [encoding_pre]
                        else:
                            if encoding_pre not in dict_data[character]:
                                dict_data[character].append(encoding_pre)
    return dict_data

def get_hu_aux_code_map(file_list):
    dict_data = {}
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as dict_file:
            for line in dict_file:
                if "\t" in line:
                    # 的	〔白勹丶&nbsp;·&nbsp;unid〕
                    params = line.strip().split('\t')
                    character = params[0]
                    encoding = params[1][1:-1]
                    encodeings = encoding.split("&nbsp;·&nbsp;")
                    chaifen = encodeings[0]
                    all_code = encodeings[1]
                    #print(encoding)
                    shoumo = all_code[0]

                    #print(line)
                    if len(chaifen) == 1:
                        shoumo += all_code[-1]
                    else:
                        shoumo += all_code[len(chaifen)-1]
                    
                    
                    #print(shoumo)
                    
                    if character not in dict_data:
                        dict_data[character] = [shoumo]
                    else:
                        if shoumo not in dict_data[character]:
                            dict_data[character].append(shoumo)
    return dict_data


# Function to update missing encodings in the file
def update_missing_encodings(file_path, write_file_path, dict_data):
    # Read the file content
    file_content = read_file(file_path)

    # Split the content into lines
    lines = file_content.split('\n')

    # Create an updated content variable
    updated_content = ''

    # Process each line
    for line in lines:
        if '\t' not in line or line.startswith("#"):
            updated_content += line + '\n'
            continue

        frequency = None
         # 检查分割出的值是否足够
        chucks = line.split('\t')
        num_chucks = len(chucks)
        if num_chucks <= 3:
            character = chucks[0]
            encoding = chucks[1]
            frequency = chucks[2] if num_chucks > 2 else None
            rest = None
        # elif len(chucks) == 2:
        #     character = chucks[0]
        #     encoding = chucks[1]
        else:
            character = chucks[0]
            encoding = chucks[1]
            frequency = chucks[2]
            rest = chucks[3:]
            rest = '\t'.join(rest)
            
        
        if "tencent" in file_path :
            updated_line = f"{character}\t99"
            updated_content += updated_line + '\n'
            continue
        else:
            if encoding == "100":
                updated_content += line + '\n'
                continue

        pinyin_list = encoding.split(" ")
        double_list = ""
        pinyin_index = 0
        #print(line)
        for pinyin in pinyin_list:
            # double_pinyin = pinyin
            double_pinyin = pinyin.split(";")[0]  # 只取万象词库中第一个;前的拼音（它是个全拼）。
            
            clean_character = character.replace("·", "")
            #print(line)
            character_encoding_pre = clean_character[pinyin_index]
            
            encoding_post_list = ''
            for key, value in dict_data.items():
                if character_encoding_pre not in value:
                    encoding_post_list += ';'
                    continue
                    
                encoding_post_list += ','.join(value.get(character_encoding_pre))
                encoding_post_list += ';'

            
            double_list += f"{double_pinyin};{encoding_post_list} "
            pinyin_index += 1
        
        double_list = double_list[:-1]

        if "[[" in double_list:
            # updated_content += line + '\n'
            pass

        if "tencent" in file_path :
            updated_line = f"{character}\t99"
        else:
            if frequency is not None:
                if rest is not None:
                    updated_line = f"{character}\t{double_list}\t{frequency}\t{rest}"
                else:
                    updated_line = f"{character}\t{double_list}\t{frequency}"                
            else:
                if rest is not None:
                    updated_line = f"{character}\t{double_list}\t{rest}"
                else:
                    updated_line = f"{character}\t{double_list}"
        updated_content += updated_line + '\n'

    # Write the updated content back to the file
    print(write_file_path)
    write_file(write_file_path, updated_content)


dict_data = {}
# file_list = ['8105.dict.yaml', '41448.dict.yaml', 'base.dict.yaml', 'ext.dict.yaml', 'others.dict.yaml']
file_list = ['associational.dict.yaml', 'base.dict.yaml', 'chars.dict.yaml', 'compatible.dict.yaml', 'corrections.dict.yaml', 'correlation.dict.yaml', 'division.dict.yaml', 'people.dict.yaml', 'poetry.dict.yaml' ]
# file_list = [ 'tencent.dict.yaml']
# Load the dict data from the provided file

dict_data['moqi'] = get_aux_code_map(['./opencc/moqi_chaifen.txt','./opencc/moqi_chaifen_rongcuo.txt'])
dict_data['xh'] = get_xh_aux_code_map(['./program/flypydz.yaml','./program/flypydz_g.yaml'])
dict_data['zrm'] = get_zrm_aux_code_map(['./program/moran.chars.dict.yaml'])
# dict_data['jdh'] = get_aux_code_map(['./program/简单鹤有理版V6.0.3手心辅助码.txt'])

# dict_data['cj'] = get_shoumo_aux_code_map(['./program/cangjie5.dict.yaml'])
# dict_data['hm'] = get_hu_aux_code_map(['./program/hu_cf.txt'])
# dict_data['wb'] = get_pre2_aux_code_map(['./program/wubi86.dict.yaml'])
# dict_data['hx'] = get_shouxin_aux_code_map(['./program/汉心手心辅助码双码.txt'])
dict_data['hm_full4'] = get_full4_aux_code_map(['./program/tiger.dict.yaml'])

print(dict_data['moqi']['火'])
print(dict_data['xh']['火'])
print(dict_data['zrm']['火'])
# print(dict_data['hm']['装'])
# print(dict_data['hx']['火'])
print(dict_data['hm_full4']['装'])
print(dict_data['hm_full4']['的'])
print(dict_data['hm_full4']['火'])

for file_name in file_list:
    # File paths
    # cn_dicts_path = os.path.expanduser("~/vscode/rime-frost/cn_dicts")
    root_path = "/mnt/e/Projects/My_Rime/000-workspace/词库设计"
    cn_dicts_path = os.path.join(root_path, "cn_dicts_ori")
    yaml_file_path = os.path.join(cn_dicts_path, file_name)
    write_file_path = os.path.join(root_path, "cn_dicts", file_name)

    print(yaml_file_path)
    # Update missing encodings in the file
    update_missing_encodings(yaml_file_path, write_file_path, dict_data)

# # 细胞词库
# for file_name in os.listdir(os.path.expanduser("~/vscode/rime-frost/cn_dicts_cell")):
#     # File paths
#     cn_dicts_path = os.path.expanduser("~/vscode/rime-frost/cn_dicts_cell")
#     yaml_file_path = os.path.join(cn_dicts_path, file_name)
#     write_file_path = os.path.join('cn_dicts_cell', file_name)

#     print(yaml_file_path)
#     # Update missing encodings in the file
#     update_missing_encodings(yaml_file_path, write_file_path, dict_data)
