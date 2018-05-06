import requests
import argparse 
import os
import json
import copy
from settings import *
from queues import SetQueue, ListQueue
from threading import Thread
from operator import itemgetter
import re


class Spider(object):

    def __init__(self, num):
        self.num = num             # <number> input
        self.token = SetQueue()    # storing token for this time
        self.result = ListQueue()  # storing info of author with '公众号'
        self.headers = HEADERS     # headers for requests
        self.check = False         # controlled by `self.set_check`
        self.before_num = 0        # controlled by `self.check_url`, used to omit input <number> before
        self.before_token = []     # controlled by `self.check_token`, omit token in the json file

    def start_requests(self, url):
        '''request webpage with fixed headers and return a python object
        '''
        return requests.get(url, headers=self.headers).json()

    def get_user_info(self):
        '''get token and request person api, put info of author with '公众号' into queue
        '''
        while self.token.queue:
            token = self.token.get()
            if token not in self.before_token:
                print(token)
                url = PEOPLE_URL.format(token)
                data = self.start_requests(url)
                result = {
                    'name': data['name'],
                    'homepage': PEOPLE_HOMEPAGE.format(token),
                    'headline': data['headline'],
                    'upvote': data['voteup_count'],
                    'description': data['description']
                }
                s = result['headline'] + result['description']
                has_gzh = re.search('公众号', s)
                if has_gzh:
                    self.result.put(result)

    def get_data(self):
        '''run functions before and start multiple threading
        :return: info list sorted by upvote
        '''
        self.set_check()
        self.get_tokens()
        if self.check:
            self.check_token()

        if self.token.queue:
            ths = []
            for _ in range(THREAD_NUM):
                th = Thread(target=self.get_user_info)
                th.start()
                ths.append(th)
            for th in ths:
                th.join()

            if self.result.queue:
                return sorted(self.result.queue, key=itemgetter('upvote'), reverse=True)
        return None

    def get_html(self):
        '''transform every dict to be html code to display
        '''
        data = self.get_data()
        if data is None:
            return 'no new infomation'
        else:
            if self.check:
                self.write_gzh(data)
            s = ''
            for datai in data:
                attr_dict = {
                    'href': datai['homepage'],
                    'name':datai['name'],
                    'upvote':datai['upvote'],
                    'headline': datai['headline'].replace('公众号', '<font color="red">公众号</font>'),
                    'description': datai['description'].replace('公众号', '<font color="red">公众号</font>')  
                }
                s += HTML.format(**attr_dict)
                s += '-'*70
            return BASE_HTML.format(body=s)

    def set_check(self):
        '''whether to check duplicate
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--check', help = 'whether to check duplicate')
        args = parser.parse_args()
        if args.check:
            self.check = True

    def check_url(self, mytype, input_id):
        '''when `self.check=True`, update(create if not existing) the check_url.json file
        with {'question/topic'+id: max input number until now}(create if the key not existing)
        '''
        key = mytype + input_id
        if not os.path.isfile(CHECK_URLNAME):
            with open(CHECK_URLNAME, 'w', encoding='utf8') as f:
                f.write(json.dumps({key: self.num}, ensure_ascii=False, indent=4))
            return

        with open(CHECK_URLNAME, 'r', encoding='utf8') as f:
            check_url_str = f.read()
        if not check_url_str:
            check_url_dict[key] = self.num
        else:
            check_url_dict = json.loads(check_url_str)
            if key in check_url_dict:
                self.before_num = check_url_dict[key]
                check_url_dict[key] = max(self.num, check_url_dict[key])
            else:
                check_url_dict[key] = self.num
        with open(CHECK_URLNAME, 'w', encoding='utf8') as f:
            f.write(json.dumps(check_url_dict, ensure_ascii=False, indent=4))


    def check_token(self):
        '''when `self.check=True`, update check_token.json, make sure to display new '公众号' each time
        '''
        if not os.path.isfile(CHECK_TOKENNAME):
            with open(CHECK_TOKENNAME, 'w', encoding='utf8') as f:
                f.write(json.dumps(list(self.token.queue), ensure_ascii=False, indent=4))
            return

        with open(CHECK_TOKENNAME, 'r', encoding='utf8') as f:
            check_token_str = f.read()
        if not check_token_str:
            check_token_list = list(self.token.queue)
        else:
            check_token_set = set(json.loads(check_token_str))
            self.before_token = copy.deepcopy(check_token_set)
            check_token_set.update(self.token.queue)
            check_token_list = list(check_token_set)
        with open(CHECK_TOKENNAME, 'w', encoding='utf8') as f:
            f.write(json.dumps(check_token_list, ensure_ascii=False, indent=4))

    def write_gzh(self, data):
        '''store all '公众号' infomation into a json file, 
        for convience of seeing infomation dispalyed before(it will never display individuals ever displayed)
        unless delete all json files and restart run.py
        '''
        if not os.path.isfile(CHECK_INFONAME):
            with open(CHECK_INFONAME, 'w', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False, indent=4))
            return

        with open(CHECK_INFONAME, 'r', encoding='utf8') as f:
            check_info_str = f.read()
        if not check_info_str:
            check_info_list = list(self.token.queue)
        else:
            check_info_list = json.loads(check_info_str)
            check_info_list.extend(data)
        with open(CHECK_INFONAME, 'w', encoding='utf8') as f:
            f.write(json.dumps(check_info_list, ensure_ascii=False, indent=4))



        
            

