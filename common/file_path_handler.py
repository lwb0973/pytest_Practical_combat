import os
import settings

def init_file_path(pic_path):
    path = []
    for root, dirs, files in os.walk(pic_path):
        for file_name in files:
            if '.' in file_name:
                key = file_name.rsplit('.', 1)[0]
                full_path = os.path.join(root, file_name)
                file_info = {key: full_path}
                path.append(file_info)

    return path

def is_file_exist(file_path,yamlName):
    abs_path = file_path.get(yamlName)
    if not abs_path:
        raise FileNotFoundError(f'{yamlName}不存在文件名')
    return abs_path



# if __name__ == '__main__':
#     files_path = init_file_path(settings.TEST_TATA_ALL)
#     print(files_path)
