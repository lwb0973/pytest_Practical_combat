import json
import allure
from common.config_loader import ConfigLoader
from common.log_handler import setup_logger
import pytest
import settings
from common.data_excel_handler import dict_data
import requests

config = ConfigLoader(settings.INI_FILE)
logger = setup_logger(config)
dict_datas = dict_data(settings.TEST_EXCEL_FILE, 'Sheet1')

@allure.feature('测试数据')
@allure.story('测试模块1111')
class TestCase:
    @classmethod
    def setup_class(cls):
        logger.info('开始执行用例1')

    @classmethod
    def teardown_class(cls):
        logger.info('测试用例结束')

    # @pytest.mark.parametrize('data_case', dict_datas)
    # def test_demo1(self, data_case, login_demo):
    #     try:
    #         json_data = json.loads(data_case['parmas'])
    #         res = requests.request(
    #             url=data_case['url'],
    #             method=data_case['method'],
    #             json=json_data,
    #             headers=login_demo)
    #         assert res.status_code == data_case['code']
    #     except Exception as f:
    #         logger.error(f)
    def test_01(self):
        print("---用例1执行---")
        assert False

    def test_02(self):
        print("---用例2执行---")

    def test_03(self):
        print("---用例3执行---")



