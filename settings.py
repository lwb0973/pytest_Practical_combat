import os

# 获取项目根路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 获取测试数据路径excel
TEST_EXCEL_FILE = os.path.join(BASE_DIR, 'test_data', 'ExcelDriver', 'case_data.xls')
# 获取日志配置等级路径
TEST_LOG_FILE = os.path.join(BASE_DIR, 'config.ini')
# 存储yaml文件路径
READ_YAML_FILE = os.path.join(BASE_DIR, 'config.yaml')
# 存储ini文件路径
INI_FILE = os.path.join(BASE_DIR, 'config.ini')
# 获取测试数据路径yaml文件
TEST_YAML_FILE = os.path.join(BASE_DIR, 'test_data', 'YamlDriver', 'case_data.yaml')
# 获取测试数据文件夹路径
TEST_TATA_ALL = os.path.join(BASE_DIR, 'test_data')
# allure本地绝对路径
ALLURE_FILE = r'D:\allure\allure-2.10.0\bin\allure.bat'