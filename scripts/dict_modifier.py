import re

def replace_pattern_in_file(file_path: str, pattern: str, replacement: str):
    """
    在指定文件中替换所有匹配正则表达式模式的字符串。

    :param file_path: 文件路径
    :param pattern: 正则表达式模式
    :param replacement: 替换字符串
    """
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式替换内容
        new_content = re.sub(pattern, replacement, content)

        # 将新内容写回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
 
        print(f"模式 {pattern} 已替换。")

    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except Exception as e:
        print(f"处理文件时发生错误：{e}")

# 将一码单字在词中的编码部分替换为一码+;的形式：
def modify_1code_characters(file_path):
    characters = [
        {"都": "qo"}, {"得": "wo"}, {"也": "ey"}, {"了": "rl"}, {"我": "tu"}, 
        {"到": "yp"}, {"的": "un"}, {"为": "is"}, {"是": "ot"}, {"行": "px"},
        {"来": "ah"}, {"说": "sh"}, {"中": "dg"}, {"一": "fi"}, {"就": "gy"},
        {"道": "ho"}, {"人": "jr"}, {"能": "kv"}, {"而": "le"}, {"可": "zk"},
        {"和": "xd"}, {"不": "cb"}, {"要": "vb"}, {"如": "bd"}, {"在": "ng"}, {"大": "md"}
    ]
    # 正则表达式模式示例：
    """ 
    pattern1 = r'(.+了\t.+r)l'     # e.g. 免不了	985	wcr;
    pattern2 = r'(了.\t\d+\tr)l'    # e.g. 了然	990	rlvm
    """
    # 正则表达式模式(将characters中的key和value套用至pattern示例中)：
    def pattern1_generator(key: str, value: str):
        return rf'(.+{key}\t.+{value[0]}){value[1]}'
    def pattern2_generator(key: str, value: str):
        return rf'({key}.\t\d+\t{value[0]}){value[1]}'
    
    # 替换后的字符串
    replacement1 = r'\1;'
    replacement2 = r'\1;'
    # 遍历字典中的每一项
    for character in characters:
        for key, value in character.items():
            pattern1 = pattern1_generator(key, value)
            replace_pattern_in_file(file_path, pattern1, replacement1)
            pattern2 = pattern2_generator(key, value)
            replace_pattern_in_file(file_path, pattern2, replacement2)

if __name__ == '__main__':
    # 文件路径
    file_path = 'C:/Users/user/AppData/Roaming/Rime/cn_dicts_tiger/tigress_ci.dict.yaml'

    modify_1code_characters(file_path)
    print("替换完成。")