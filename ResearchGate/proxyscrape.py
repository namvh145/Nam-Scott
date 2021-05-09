import random
from itertools import cycle

PROXY_JSON_PATH = 'adhoc_tasks/data/proxy_list.json'


def get_proxies_free_proxy():
    """
    lấy proxy được lưu ở local trước, nếu có thì dùng, nếu không có thì lấy online
    """
    # 1. lấy proxy được lưu trước,
    proxy_list = []
    if os.path.exists(PROXY_JSON_PATH):
        proxy_dict = read_json_file(PROXY_JSON_PATH)
        proxy_list = [proxy for proxy, failure_times in proxy_dict.items() if failure_times < 4]

    if len(proxy_list) > 0:
        return proxy_list, proxy_dict

    url = 'http://free-proxy.cz/en/proxylist/country/all/https/speed/all'
    proxies = set()
    table = xtract_from_url(url, '//*[@id="proxy_list"]')
    rows = xtract(table[0], '..//tbody/tr')
    if rows:
        for tr in rows:
            td = xtract(tr, './/td')
            if len(td) == 11:
                td_ip_tag_str = remove_html_tag(td[0])
                port = remove_html_tag(td[1])
                try:
                    ip = base64.b64decode(td_ip_tag_str).decode('UTF-8')
                except:
                    ip = td_ip_tag_str
                if ip and port:
                    proxy = ':'.join([ip, port])
                    proxies.add(proxy)
    # lưu proxies vào file read_json_file
    proxies_json = {item: 0 for item in proxies}
    write_json_file(PROXY_JSON_PATH, proxies_json)
    return proxies, proxies_json


def xtract_from_url_with_proxy(url, xpath):
    proxies, proxies_json = get_proxies_free_proxy()
    random.shuffle(proxies)
    proxy_pool = cycle(proxies)
    SLEEP = 5
    cnt = len(proxies)
    while cnt > 0:
        proxy = next(proxy_pool)
        try:
            page = requests.get(url, proxies={"http": 'http://%s' % proxy, "https": 'https://%s' % proxy}, timeout=10)
            cnt = 0
        except Exception as ex:
            print(ex)
            print("Skipping. Connnection error with proxy %s" % proxy)
            cnt -= 1
            # update proxy bị lỗi
            proxies_json[proxy] = proxies_json[proxy] + 1
            write_json_file(PROXY_JSON_PATH, proxies_json)
            time.sleep(SLEEP)

    tree = html.fromstring(page.text)
    return tree.xpath(xpath)
