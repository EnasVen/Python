import colorama
import pyquery
import requests
import mylog
import re

def get_realtime_news(url):
    response = requests.get(
        url=url,
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4400.0 Iron Safari/537.36'
        }
    )
    if response.status_code != 200:
        print(f'request is failed ({response.status_code}).')
        return
    print(f'request is successful.')

    # with open('applenews.html', 'wb') as f:
    #     f.write(response.content)

    doc = pyquery.PyQuery(response.text)

    title = doc('div#article-header h1.text_medium').text()
    print(f'新聞標題：{title}')

    contents = re.findall(r'"content":"(?P<CONTENT>.+?)"}', response.text)
    contents = [
        content
        for content in contents
        if not content.startswith('<a') and not content.endswith('a>')
    ]
    content = '\n'.join(contents)
    content = f'<div id="content">{content}</div>'
    doc = pyquery.PyQuery(content)
    content = doc('div#content').text()
    print(f'新聞內容：\n{content}')

    match = re.search(r'"originalUrl":"(?P<URL>.+?)"', response.text)
    if match is None:
        mylog.red('image is not found')
    else:
        image = match.group('URL')
        print(f'新聞圖檔：{image}')

        response = requests.get(
            url=image,
            headers={
                'referer': url,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4400.0 Iron Safari/537.36',
            }
        )
        with open('test.jpg', 'wb') as f:
            f.write(response.content)




def get_realtime_news_list():
    response = requests.get(
        url='https://tw.appledaily.com/realtime/new/',
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4400.0 Iron Safari/537.36'
        }
    )
    if response.status_code != 200:
        print(f'request is failed ({response.status_code}).')
        return
    print(f'request is successful.')

    with open('applenews.html', 'wb') as f:
        f.write(response.content)

    doc = pyquery.PyQuery(response.text)
    elements_div = list(doc('div[id^="stories-container"] > div.flex-feature').items())
    for element_div in elements_div:
        url = element_div('a.story-card').attr('href')
        url = f'https://tw.appledaily.com{url}'
        print(f'{colorama.Fore.YELLOW}{url}{colorama.Style.RESET_ALL}')
        title = element_div('span.headline').text()
        print(title)
        get_realtime_news(url)
        break

# get_realtime_news_list()

if __name__ == '__main__':
    get_realtime_news_list()