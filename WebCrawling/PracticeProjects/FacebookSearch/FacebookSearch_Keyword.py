import datetime
import json
import re

import munch
import requests

import mylog



def extract_data(data, expr, target):
    match = re.search(expr, data)
    if match is None:
        mylog.red(f'[Find {target}] failure')
        return None
    mylog.green(f'[Find {target}] success')
    return match


def search_page(keyword):
    cookie = None
    # 讀取個人 Cookie 檔內容
    with open('test32.cookie', 'r') as f:
        cookie = f.read()
    if cookie is None or cookie == '':
        mylog.red(f'read cookie: failure')
        return
    mylog.green(f'read cookie: success')

    storage = munch.munchify({})

    # 主動維護 Cookie 的 Session 物件
    session = requests.Session()

    # 更新 Session 物件裡的 Headers
    session.headers.update({
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'cookie': cookie,
        'dnt': '1',
        'pragma': 'no-cache',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4400.0 Iron Safari/537.36',
        'viewport-width': '1920',
    })

    # 送出首頁請求
    response = session.get(
        url='https://www.facebook.com/'
    )
    if response.status_code != 200:
        mylog.red(f'request: failure ({response.status_code}).')
        return
    mylog.green(f'request: success')

    with open('facebook.html', 'wb') as f:
        f.write(response.content)

    find_targets = munch.munchify([{
        # Find DTSG
        # ["DTSGInitialData",[],{"token":"AQGjlSSdzb5Xk5w:32:1623119773"},258]
        'expr': r'\["DTSGInitialData",\[\],\{"token":"(?P<dtsg>.+?)"\},\d+\]',
        'name': 'dtsg',
    }, {
        # Find USERID
        'expr': r'"USER_ID":"(?P<userid>\d+?)"',
        'name': 'userid',
    }, {
        'expr': r'"LSD",\[\],{"token":"(?P<lsd>.+?)"}',
        'name': 'lsd',
    }])

    for find_target in find_targets:
        match = extract_data(response.text, find_target.expr, find_target.name)
        if match is None:
            return
        storage[find_target.name] = match.group(find_target.name)
        print(f' {find_target.name.upper()}: {storage[find_target.name]}')

    # Find SPINX
    match = extract_data(response.text, r'"__spin_r":(?P<SPINR>\d+?),"__spin_b":"(?P<SPINB>\w+?)"', 'SPINX')
    if match is None:
        return

    storage.spin = munch.munchify({})

    storage.spin.r = match.group('SPINR')
    print(f' SPIN.R: {storage.spin.r}')
    storage.spin.b = match.group('SPINB')
    print(f' SPIN.B: {storage.spin.b}')
    storage.spin.t = int(datetime.datetime.now().timestamp())
    print(f' SPIN.T: {storage.spin.t}')

    # Find REVISION
    match = extract_data(response.text, r'"consistency":{"rev":(?P<REVISION>\d+?)}', 'REVISION')
    if match is None:
        return

    storage.revision = match.group('REVISION')
    print(f' REVISION: {storage.revision}')

    # Find JAZOEST
    match = extract_data(response.text, r'jazoest=(?P<JAZOEST>\d+?)', 'JAZOEST')
    if match is None:
        return

    storage.jazoest = match.group('JAZOEST')
    print(f' JAZOEST: {storage.jazoest}')

    response = session.get(
        url=f'https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/eBEI14fGLDc.js'
    )
    if response.status_code != 200:
        mylog.red(f'[Get JS File] {response.status_code}')
        return
    mylog.green(f'[Get JS File] success')

    with open(f'doc.post.js', 'wb') as f:
        f.write(response.content)

    for line in response.text.split('\n'):
        if line.startswith('__d("SearchCometResultsInitialResultsQuery_facebookRelayOperation"'):
            # Find DOCID
            match = extract_data(line, r'e.exports="(?P<DOCID>\d+)"', 'DOCID')
            if match is None:
                return
            mylog.green(f'[Find DOCID] success')
            storage.docid = match.group('DOCID')
            break

    print(f' DOCID: {storage.docid}')

    # 發出搜尋關鍵字請求
    url = f'https://www.facebook.com/api/graphql/'

    data = {
        'av': storage.userid,
        '__user': storage.userid,
        '__a': '1',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': storage.revision,
        '__comet_req': '1',
        'fb_dtsg': storage.dtsg,
        'jazoest': storage.jazoest,
        'lsd': storage.lsd,
        '__spin_r': storage.spin.r,
        '__spin_b': storage.spin.b,
        '__spin_t': storage.spin.t,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
        'variables': json.dumps({
            'count': 5,
            'allow_streaming': False,
            'args': {
                'callsite': 'COMET_GLOBAL_SEARCH',
                'config': {
                    'bootstrap_config': None,
                    'exact_match': False,
                    'high_confidence_config': None,
                    'intercept_config': None,
                    'sts_disambiguation': None,
                    'watch_config': None
                },
                'experience': {
                    'encoded_server_defined_params': None,
                    'fbid': None,
                    'type': 'GLOBAL_SEARCH'
                },
                'filters': [],
                'text': keyword
            },
            'cursor': None,
            'feedbackSource': 23,
            'fetch_filters': True,
            'renderLocation': 'search_results_page',
            'scale': 1,
            'stream_initial_count': 0,
            'useDefaultActor': False,
            '__relay_internal__pv__FBReelsEnableDeferrelayprovider': False
        }),
        'server_timestamps': True,
        'doc_id': storage.docid,
    }
    # print(data)
    response = session.post(
        url=url,
        data=data
    )
    if response.status_code != 200:
        mylog.red(f'[Search] {response.status_code}')
        return
    mylog.green(f'[Search] success')

    # with open('facebook.search.json', 'wb') as f:
    #     f.write(response.content)

    # 將取回的 JSON 內容轉成 dict，再透過 munch 轉成 object
    body = munch.munchify(response.json())
    # 搜尋結果位於 .data.serpResponse.results.edges[1].relay_rendering_strategy.result_rendering_strategies 這個 JSON Array 裡
    for strategy in body.data.serpResponse.results.edges[1].relay_rendering_strategy.result_rendering_strategies:
        name = strategy.view_model.profile.name
        url = strategy.view_model.profile.url
        mylog.yellow(name)
        print(url)



if __name__ == '__main__':
    keyword = 'python'
    search_page(keyword)