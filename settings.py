# 请求所带headers
HEADERS = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
	'cookie': ''}

# API配置  访问这个网址 http://localhost:1234/进入主页
API_HOST = '0.0.0.0'
API_PORT = 1234

# 知乎API，用于构造URL
QUESTION_URL = 'https://www.zhihu.com/api/v4/questions/{}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit={}&sort_by=default'
TOPIC_URL = 'https://www.zhihu.com/api/v4/topics/{}/feeds/essence?limit={}&offset={}'
PEOPLE_URL = 'https://www.zhihu.com/api/v4/members/{}?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_force_renamed%2Cis_bind_sina%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge[%3F(type%3Dbest_answerer)].topics'
PEOPLE_HOMEPAGE = 'https://www.zhihu.com/people/{}/activities'

# 线程数量，如果想要快速显示可以调大一点；如果要遍历所有回答，最好改小一点。
THREAD_NUM = 20

# 下面两个字符串用于构造展示结果的HTML代码
HTML = '''
<p><b>用户</b>：<a href="{href}">{name}</a>&nbsp;&nbsp;
赞同数：{upvote}</p>
<b>一句话介绍</b>：{headline}</p>
<p><b>详细描述</b>：{description}</p>
'''

BASE_HTML = '''
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv='content-type' value='text/html;charset=utf8'>
  <title>Find WeChat Subscription Accounts</title>
  <style type='text/css' media='all'>
  body {{font-family: Microsoft YaHei;
        font-size: 16px}}
  </style>
</head>
<body>
{body}
</body>
</html>
'''

# 运行产物json文件的文件名
CHECK_URLNAME = 'check_url.json'
CHECK_TOKENNAME = 'check_token.json'
CHECK_INFONAME = 'check_info.json'