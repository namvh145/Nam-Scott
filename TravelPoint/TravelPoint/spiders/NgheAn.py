import scrapy
import re


class NgheAnSpider(scrapy.Spider):
    name = "NgheAn"
    start_urls = [
       "https://dulichchaovietnam.com/top-9-diem-du-lich-hap-dan-o-nghe-an.html"
    ]
    def parse(self, response, **kwargs):
        address = "p:nth-child(32) span:nth-child(1)::text , p:nth-child(29) span::text ," \
                  " p:nth-child(26) span::text , p:nth-child(23) span::text , p:nth-child(20) span::text , " \
                  "p:nth-child(17) span::text , p:nth-child(14) span::text , p:nth-child(11) span::text ," \
                  " p:nth-child(7) span::text , strong~ span::text , br+ span strong::text , .item strong span::text, span img::attr(src), p img::attr(src)"

        source = response.css(address).extract()
        source = [s for s in source if not bool(re.findall("images", s))]

        imgs = response.css("span img::attr(src), p img::attr(src)").extract()[:-1]
        title = response.css("br+ span strong::text , .item strong span::text").extract()

        n = len(source)

        i = 0
        while i < n and len(imgs) > 0:
            name = title[0].split('.')[1].strip().split('-')[0].strip()
            description = ""
            title.pop(0)
            img = []
            if len(title) >= 1:
                idx = source.index(title[0])
            else:
                idx = n
            j = i + 1
            while j < idx:
                if source[j] in imgs:
                    img.append(source[j])
                    imgs.pop(0)
                else:
                    description += source[j]
                j += 1
            i = idx
            yield {
                "name": name,
                "description": description,
                "link": response.url,
                "image": img,
                "Province": "Nghệ An",
                "DATA_LEVEL": "HIGH_LEVEL"
            }