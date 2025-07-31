import os
import yaml
import settings
# 读取yaml文件的函数封装
def read_yaml(yamlpath):
    '''读取yaml数据'''
    if not os.path.isfile(yamlpath):
        raise FileNotFoundError("文件路径不存在，请检査路径是否正确:{}".format(yamlpath))
    # open读取uqml,获取文本内容
    with open(yamlpath, 'r', encoding='utf-8') as f:
        cfg = f.read()
        content = yaml.load(cfg, Loader=yaml.FullLoader)
        return content

# if __name__ == '__main__':
#     yaml_data = read_yaml(settings.TEST_YAML_FILE)
#     print(yaml_data)