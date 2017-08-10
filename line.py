#coding=utf-8
import urllib
import urllib2
import re
import requests
import json
import sys

#编码转换
reload(sys)
sys.setdefaultencoding('utf8')

#设置问题编号&地址
qid="35931586"
qurl="https://www.zhihu.com/api/v4/questions/35931586/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=1&offset="

#设置头文件信息
headers={'accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'authorization':'Bearer Mi4wQUFDQWV3NDBBQUFBSUlJRGxXSzBDeGNBQUFCaEFsVk4tLXFQV1FDSkRxNmIwNVlUblNXX29CRy0ycXJ3dkxZZXJB|1500012027|545cebd577416f44d42279d4f8c7fe070a3721e3',
'Connection':'keep-alive',
'Cookie':'d_c0="ACCCA5VitAuPTj8X1WjmPx7iQr4m7e76rkM=|1493863999"; _zap=efefd39d-918b-44a5-9019-ea2d43d6cc3b; aliyungf_tc=AQAAANa3hGrTHwQAkLV5ykRiYiVQTYkK; s-t=autocomplete; r_cap_id="MGEwMDk5OWIwZmUzNDc1YzgyNGNiYjMwNjBlOTk4MWM=|1500012022|be07187da2b8716f8e16b30cdecf23db6f1f81e7"; cap_id="MDlmYWE4ZWYzNDM0NDM2ODlmZDg3Yzg2MTAxMTVjOTM=|1500012022|7889ee1695689e3d55f8d1647b404333b149dbee"; z_c0=Mi4wQUFDQWV3NDBBQUFBSUlJRGxXSzBDeGNBQUFCaEFsVk4tLXFQV1FDSkRxNmIwNVlUblNXX29CRy0ycXJ3dkxZZXJB|1500012027|545cebd577416f44d42279d4f8c7fe070a3721e3; q_c1=ddeb4f4a957a4d4aa4680248cfb56935|1501936107000|1493812080000; s-q=%E4%B8%8A%E6%B5%B7%E5%85%AC%E5%85%B1%E6%88%B7%E5%8F%A3; s-i=1; sid=n02uko58; __utma=155987696.236675253.1502340934.1502340934.1502340934.1; __utmc=155987696; __utmz=155987696.1502340934.1.1.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/28425804; _xsrf=a93c7a7f7c46a68f7544dc899d07fd23',
'Host':'www.zhihu.com',
'Referer':'https://www.zhihu.com/question/35931586',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
}
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener=urllib2.build_opener()
opener.adheaders=headall
urllib2.install_opener(opener)

i=0
num=1
for i in range(0,5516):
    url=qurl+str(i)
    data=requests.get(url,headers=headers)
    json_data=json.loads(data.text)
    con_data=json_data['data'][0]['content']
    user_name=json_data['data'][0]['author']['name']
    #图片url正则匹配
    imgpat='data-original=\"https://(.{56})\"'
    imglist=re.compile(imgpat, re.S).findall(con_data)
    #去掉重复连接
    imglista=list(set(imglist))
    imglista.sort(key=imglist.index)
    for img in imglista:
        imagename="/Users/gritzou/Documents/crawler/"+user_name+'_'+str(num)+".jpg"
        imageurl="http://"+img
        print num,i
        print img,imageurl
        try:
            urllib.urlretrieve(imageurl,filename=imagename)
        except urllib2.URLError as e:
            if hasattr(e,"code"):
                num+=1
            if hasattr(e,"reason"):
                num+=1
        except BaseException as ex:
            print(ex.args)
            num+=1
        num+=1