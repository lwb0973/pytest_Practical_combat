import pytest
import uuid


@pytest.fixture(scope='session')
def login_demo():
    # 模拟登录获取token
    random_uuid = uuid.uuid4()
    random_uuid_token = {'token': random_uuid}
    return random_uuid_token
