import setting
from setting import IP, HEADERS
from tools.logger import GetLogger

logger = GetLogger.get_logger()
class ApiOrder:
    def __init__(self):
        logger.info('开始获取order的url地址')
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'
        logger.info('order的url地址是%s' % self.url)


    def order(self,session):
        '''
        发起下订单的请求
        :param session:
        :return:
        '''
        data = {
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',

        }
        logger.info('发起order请求，请求的参数是{},headers是{}'.format(data,HEADERS))
        resp_order = session.post(self.url,data=data,headers=HEADERS)
        logger.info('order请求的响应：%s' %resp_order.json())

        # 产生数据->并把数据放到setting当中(注意要使用setting.JUMP_URL= xxx)
        logger.info('获取order请求的响应值中的jump_url')
        setting.JUMP_URL = resp_order.json().get('data').get('jump_url')
        logger.info('order请求的响应值中的jump_url为%s' %setting.JUMP_URL)
        return resp_order
