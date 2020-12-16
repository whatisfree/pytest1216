import allure
import pytest
import requests

from api.apiLoginToken import ApiLoginToken
from api.apiQueryToken import ApiQueryToken

class TestQuery:

    def setup_class(self):
        #获取session对象
        self.session = requests.session()
        #调用成功登陆pinter网站的接口
        ApiLoginToken().login_token_success(self.session)
        #创建query对象
        self.query_obj = ApiQueryToken()
    @allure.title('查询pinter银行余额的测试用例')
    @allure.feature('查询功能')
    @allure.story('通过token关联，查询pinter系统用户的银行余额')
    @allure.severity('blocker')
    def test_querybank(self):

        resp = self.query_obj.query_bank(self.session)
        #print(resp.json())
        assert resp.json()['message'] == 'success'
