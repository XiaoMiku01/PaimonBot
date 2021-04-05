from httpx import AsyncClient
import requests
def ghs_pic() -> str:

        try:
            req_url = "https://api.lolicon.app/setu/"
            params = {"apikey": '60809624605afe54ba0993',
                      "r18": 0,
                      "size1200": 'true',
                      'proxy' : 'disable'}
            res = requests.get(req_url, params=params)
            setu_title = res.json()['data'][0]['title']
            setu_url = res.json()['data'][0]['url']
            setu_pid = res.json()['data'][0]['pid']
            setu_author = res.json()['data'][0]['author']
            local_img_url = "title:" + setu_title + "[CQ:image,file=" + setu_url + "]" + "pid:" + str(
                setu_pid) + " 画师:" + setu_author
            return setu_url
            # return local_img_url
        except Exception as e:
            print(e)
            return "阿这，出了一点问题"

def downPic(url):
    hearders={

    }



if __name__ == '__main__':
    print(ghs_pic())