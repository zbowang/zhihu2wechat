import math
from settings import TOPIC_URL
from spiders.spider import Spider


class TopicSpider(Spider):

    def __init__(self, topic_id, num):
        '''
        inherit: num token result data headers check
        '''
        super(TopicSpider, self).__init__(num)
        self.topic_id = topic_id

    def get_tokens(self):
        '''
        construct url with `self.topic_id`
        control url number with `self.num`
        loop the urls to get author infomation
        call `self.parse` to get token of every author
        '''
        if self.check:
            self.check_url(mytype='topic', input_id=self.topic_id)
        if self.before_num < 1000:
            iter_page = math.ceil(min(self.num, 1000)/20)
            for i in range(0 + self.before_num//20, iter_page):
                url = TOPIC_URL.format(self.topic_id, 20, 20*i)
                print('getting', url)
                data = self.start_requests(url)
                self.parse(data)

    def parse(self, data):
        '''get the token of every author and store into a thread-safely set
        :param data: author infomation dict
        '''
        for i in data['data']:
            token = i['target']['author']['url_token']
            if token:
                print(token)
                self.token.put(token)



