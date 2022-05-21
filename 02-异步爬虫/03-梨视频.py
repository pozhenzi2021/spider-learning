import requests
from lxml import etree
from multiprocessing.dummy import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
}


def get_video_data(dic):
    video_url = dic['url']
    print(dic['name'], '正在下载...')
    data = requests.get(url=video_url, headers=headers).content
    with open('../videoLibs/' + dic['name'], 'wb') as fp:
        fp.write(data)
        print(dic['name'], '下载成功！！')


def get_urls():
    url = 'https://www.pearvideo.com/category_5'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="categoryList"]/li')
    urls = []
    for li in li_list:
        # 开始拼视频地址，格式https://www.pearvideo.com/videoStatus.jsp?contId=1749830&mrd=0.3355423128227104
        detail_url = 'https://www.pearvideo.com/videoStatus.jsp'
        contId = li.xpath('./div/a/@href')[0].split("_")[-1]
        param = {
            'contId': contId,
            'mrd': 0.3355423128227104
        }
        # Referer https://www.pearvideo.com/video_1749830
        referer_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        headers['Referer'] = referer_url
        detail_json = requests.get(url=detail_url, params=param, headers=headers).json()
        # 解析出视频下载地址 https://video.pearvideo.com/mp4/short/20220418/1650639210575-15863669-hd.mp4
        video = detail_json["videoInfo"]['videos']['srcUrl']
        # 替换成 https://video.pearvideo.com/mp4/short/20220418/cont-1749830-15863669-hd.mp4 形式
        first = video.split('-')[0].split('/')[:-1]
        second = video.split('-')[1:]
        video_url = 'https://video.pearvideo.com/mp4/' + first[-2] + '/' + first[
            -1] + '/cont-' + contId + '-' + '-'.join(second)
        # 视频名称 xxx.mp4
        video_name = li.xpath('./div/a/div[@class="vervideo-title"]/text()')[0] + '.mp4'
        dic = {
            'name': video_name,
            'url': video_url
        }
        urls.append(dic)
    return urls


if __name__ == '__main__':
    pool = Pool(9)
    pool.map(get_video_data, get_urls())
    pool.close()
    pool.join()
