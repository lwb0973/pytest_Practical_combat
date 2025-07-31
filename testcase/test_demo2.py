import json

from common.config_loader import ConfigLoader
from common.log_handler import setup_logger
import pytest
import settings
from common.data_excel_handler import dict_data
import requests
import allure

config = ConfigLoader(settings.INI_FILE)
logger = setup_logger(config)
dict_datas = dict_data(settings.TEST_EXCEL_FILE, 'Sheet1')


@allure.story('测试模块')
class TestCase:
    @classmethod
    def setup_class(cls):
        logger.info('开始执行用例')

    @classmethod
    def teardown_class(cls):
        logger.info('测试用例结束')

    def test_04(self):
        print("---用例4执行---")
        assert False

    def test_05(self):
        print("---用例5执行---")

    def test_06(self):
        print("---用例6执行---")
