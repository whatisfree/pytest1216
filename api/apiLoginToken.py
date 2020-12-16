import setting
from tools.logger import GetLogger
logger = GetLogger().get_logger()
class ApiLoginToken:
    def __init__(self):
        logger.info('开始获取pinter的login的url地址:')
        self.url = 'http://192.168.1.106:8080/pinter/bank/api/login2'
        logger.info('pinter系统登陆url是:%s' % self.url)

    def login_token_success(self,session):
        logger.info('准备发起针对pinter系统成功login的请求')
        data = {'userName': 'admin', 'password': '1234'}
        logger.info('成功登陆pinter系统的data是{}'.format(data))
        resp = session.post(self.url,data)
        logger.info('成功登陆pinter系统的响应值是{}'.format(resp.json()))
        logger.info('开始设置成功登陆后要用到的token')
        setting.TOKEN = resp.json()['data']
        logger.info('token值为%s' % setting.TOKEN)
        return resp