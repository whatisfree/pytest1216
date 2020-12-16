import setting

from tools.logger import GetLogger
logger = GetLogger.get_logger()

class ApiPay:
    def __init__(self):
        logger.info('开始获取pay请求的url地址')
        self.url = setting.JUMP_URL
        logger.info('pay请求的url是%s' % self.url)
    def pay(self,session):
        # 对302接口禁止重定向 allow_redirects=False
        logger.info('使用session发起get请求,并设置allow_redirects=False')
        resp = session.get(self.url,allow_redirects=False)
        logger.info('get请求的响应值为: %s' % resp.text)
        # 提取响应头中的location,对location后面的地址发起请求，
        # 然后获取响应，以便testcase中做断言
        logger.info('获取get请求后的响应头名为location的值，并作为url进行get请求')
        resp_pay = session.get(resp.headers['location'])
        logger.info('响应头名为location的值为%s' % resp.headers['location'])
        logger.info('上述url发起请求后的响应结果太长，响应状态为%s' % resp_pay.status_code)
        return resp_pay
