import configparser
import os
import settings


# 读取ini文件封装方法
class ConfigLoader:
    def __init__(self, filepath: str):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"配置文件不存在: {filepath}")

        self.config = configparser.ConfigParser()
        self.config.read(filepath, encoding='utf-8')

    # 转换成字符类型
    def get(self, section: str, option: str, fallback=None):
        return self.config.get(section, option, fallback=fallback)

    # 转换整数类型
    def get_int(self, section: str, option: str, fallback=None):
        return self.config.getint(section, option, fallback=fallback)

    # 转换成浮点数类型
    def get_float(self, section: str, option: str, fallback=None):
        return self.config.getfloat(section, option, fallback=fallback)

    # 转换成布尔值类型
    def get_bool(self, section: str, option: str, fallback=None):
        return self.config.getboolean(section, option, fallback=fallback)

    # 检查配置文件中是否存在某个键（option）
    def has_option(self, section: str, option: str) -> bool:
        return self.config.has_option(section, option)

    # 返回配置文件中所有的section（段名）的列表
    def sections(self):
        return self.config.sections()

    # 列出指定section（段）下的所有option（键）
    def options(self, section: str):
        return self.config.options(section)

# 调用上面封装方法示例
# config = ConfigLoader(settings.INI_FILE)
# host = config.get('mysqldb', 'host')
# print(host)
# # 调用检查文件中是否存在某个键（option）
# if config.has_option('app', 'debug'):
#     print("debug 配置存在")
# else:
#     print("debug 配置不存在")
#
# # 调用返回配置文件中所有的section（段名）的列表
# print(config.sections())
#
# # 调用列出指定section（段）下的所有option（键）
# print(config.options('app'))
