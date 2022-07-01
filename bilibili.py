import requests
class Bilibili:
    def __init__(self):
        self.cookies = cookies = {
            'buvid3': 'A425DCF5-0C68-136F-9BE8-902987495ECE02513infoc',
            '_uuid': 'D1DA1E69-1379-1A45-2D64-3BD521014EC3103819infoc',
            'buvid_fp_plain': 'undefined',
            'CURRENT_BLACKGAP': '0',
            'nostalgia_conf': '-1',
            'rpdid': '|(JJmYR|Ykul0J\'uYR~~RYmJ)',
            'LIVE_BUVID': 'AUTO6716479582963705',
            'is-2022-channel': '1',
            'hit-dyn-v2': '1',
            'blackside_state': '0',
            'fingerprint3': 'e897c10d096bbffe77fa900d57024647',
            'bp_article_offset_663127116': '673764456356905000',
            'CURRENT_FNVAL': '4048',
            'PVID': '2',
            'buvid4': '3FB6BFB9-D6CC-0DD1-C521-43676A4967A203755-022032011-0wUJZf2fFJuBoCUgao%2Bxbg%3D%3D',
            'CURRENT_QUALITY': '80',
            'innersign': '0',
            'b_lsid': '94D103E6D_181BA13BBFA',
            'i-wanna-go-back': '-1',
            'b_ut': '7',
            'bp_video_offset_102750155': '677925364699234300',
            'b_timer': '%7B%22ffp%22%3A%7B%22333.851.fp.risk_A425DCF5%22%3A%22181BA13C0F2%22%2C%22333.1007.fp.risk_A425DCF5%22%3A%22181BA13E3C7%22%2C%22333.885.fp.risk_A425DCF5%22%3A%22181BA13ED5D%22%2C%22333.42.fp.risk_A425DCF5%22%3A%22181BA13F8B1%22%2C%22333.130.fp.risk_A425DCF5%22%3A%22181BA1796FE%22%7D%7D',
            'fingerprint': '4d49dd1eae7c0651813cc85e7eb61758',
            'SESSDATA': '60cdcef1%2C1672236535%2C9a35b%2A71',
            'bili_jct': '4bab4a2f3468e57ba1e2d0f898d4e2ed',
            'DedeUserID': '663127116',
            'DedeUserID__ckMd5': '06a0c0c3b51a424b',
            'sid': 'bs5w8cpv',
            'bp_video_offset_663127116': '677864483533619300',
            'buvid_fp': '4d49dd1eae7c0651813cc85e7eb61758',
        }
    def process_data(self,raw_data_list):
        '''
            用来处理get——data传过来的json列表，拿到每个视频的标题、封面、bvid、播放量、点赞量、收藏量
        '''
        data_list = []
        for item in raw_data_list:
            title = item.get("Archive").get("title")
            cover = item.get("Archive").get("cover")
            bvid = item.get("Archive").get("bvid")
            view = item.get("stat").get("view")
            like = item.get("stat").get("like")
            collect = item.get("stat").get("favorite")
            audio = {
                "title":title,
                "cover":cover,
                "bvid":bvid,
                "view":view,
                "like":like,
                "collect":collect
            }
            data_list.append(audio)
        return data_list

    def get_data(self):
        params = {
            'status': 'is_pubing,pubed,not_pubed',
            'pn': '1', 
            'ps': '10', 
            'coop': '1',
            'interactive': '1',
        }
        response = requests.get('https://member.bilibili.com/x/web/archives', params=params, cookies=self.cookies)
        page = int(response.json().get("data").get("page").get("count"))//10+1 #页数
        # 循环获取数据
        audio_data_list = []
        for cur_page in range(1,page+1):
            params = {
                'status': 'is_pubing,pubed,not_pubed',
                'pn': str(cur_page), #页数
                'ps': '10', 
                'coop': '1',
                'interactive': '1',
            }
            response = requests.get('https://member.bilibili.com/x/web/archives', params=params, cookies=self.cookies)
            #获取数据
            audio_data = response.json().get("data").get("arc_audits")
            # 数据加到总列表中
            for item in audio_data:
                audio_data_list.append(item)
            # 数据处理
            new_audio_data_list = self.process_data(audio_data_list)
        return new_audio_data_list
bi = Bilibili()
a = bi.get_data()
print(a)