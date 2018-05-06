import math
from settings import QUESTION_URL
from spiders.spider import Spider


class QuestionSpider(Spider):

    def __init__(self, question_id, num):
        '''
        inherit: num token result data headers check
        '''
        super(QuestionSpider, self).__init__(num)
        self.question_id = question_id
        

    def get_tokens(self):
        '''
        construct url with `self.question_id`
        control url number with `self.num`
        loop the urls to get author infomation
        call `self.parse` to get token of every author
        '''
        if self.check:
            self.check_url(mytype='question', input_id=self.question_id)
        url = QUESTION_URL.format(self.question_id, 0, 1)
        # print('getting', url)
        total = self.start_requests(url)['paging']['totals']
        if self.before_num < total:
            iter_page = math.ceil(min(self.num, total)/20)
            for i in range(0 + self.before_num//20, iter_page):
                url = QUESTION_URL.format(self.question_id, i*20, 20)
                # print('getting', url)
                data = self.start_requests(url)
                self.parse(data)

    def parse(self, data):
        '''get the token of every author and store into a thread-safely set
        :param data: author infomation dict
        '''
        for i in data['data']:
            token = i['author']['url_token']
            if token:
                self.token.put(token)


