'''
File Name:index
Author:SongHao
Email:5868037@qq.com
Wechat:songhao8080
Blog:https://www.168seo.cn
公众号:zeropython
date:2020/5/12
'''

import requests


if __name__ == '__main__':
    url = "http://www.baidu.com bew" \
          ""
    r = requests.get(url)
    print(r.url)