import setting
from tools.logger import GetLogger
logger = GetLogger().get_logger()

class ApiQueryToken:
    def __init__(self):
        logger.info('获取发起query_bank请求的url')
        self.url = 'http://192.168.1.106:8080/pinter/bank/api/query2'
        logger.info('query_bank请求的url是%s' % self.url)
    def query_bank(self,session):
        logger.info('开始发起针对pinter的query请求')
        params = {'userName':'admin'}
        token = setting.TOKEN
        #print(token)
        header = {'testfan-token': token}
        resp = session.get(self.url,params = params,headers = header)
        logger.info('针对pinter的query请求的响应值是%s' % resp.json())
        return resp
