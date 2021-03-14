from werobot import WeRoBot
import requests
robot=WeRoBot(enable_session=False,
                token='qidong123',
                APP_ID='wxbdffa8b28352f100',
                APP_SECRET='591bfdbc7c387a0f34a46730664c806c')

client=robot.client
acceaccess_token = client.grant_token()
acceaccess_token = client.get_access_token()
url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + str(acceaccess_token)

menu={
    "button":[
        {
            "type":"click",
            "name":"今日歌曲",
            "key":"V1001_TODAY_MUSIC"
        },
        {
            "type":"click",
            "name":"歌手简介",
            "key":"V1001_TODAY_SINGER"
        },
        {
            "name":"菜单",
            "sub_button":[
                {
                    "type":"view",
                    "name":"搜索",
                    "url":"http://www.soso.com/"
                },
                {
                    "type":"view",
                    "name":"视频",
                    "url":"http://v.qq.com/"
                },
                {
                    "type":"click",
                    "name":"赞一下我们",
                    "key":"V1001_GOOD"
                }
            ]
        }
    ]
}

bacg = client.create_menu(menu_data=menu)
response = requests.post(url,bacg)
print(response.text)
