import re

import scrapy


class DakNong(scrapy.Spider):
    name = "DakNong"
    start_urls = [
        "https://danangaz.com/du-lich/63-tinh-thanh/dia-diem-du-lich-dak-nong/"
    ]

    def parse(self, response, **kwargs):
        address = "p em strong::text , h2 strong:nth-child(1)::text , .td-post-content li::text , p::text , figure img::attr(src), p img::attr(src)"

        title = response.css("h2 strong:nth-child(1)::text").extract()

        source = response.css(address).extract()[3:-10]
        source = [s for s in source if not bool(re.findall(r"^>>>", s))]

        imgs = response.css("figure img::attr(src), p img::attr(src)").extract()
        imgs = [img for img in imgs if not bool(re.match('gif', img[-3:]))]

        n = len(source)
        i = 0
        while i < n and len(imgs) > 0:
            if (re.match(r"(\d*)\.\xa0", title[0])):
                name = title[1].split("–")[0].strip()
                title.pop(0)
                i += 1
            # elif(re.match(r"30\. \w+", title[0])):
            #     name = title[0].split('.')[1].strip()
            #     title.pop(0)
            #     i += 1
            else:
                name = title[0].split('.')[1].strip().split("–")[0].strip()
                name = re.sub("\xa0", " ", name)

            description = ""
            title.pop(0)
            img = []
            addr = re.sub("\xa0", " ", source[i + 1])
            i += 1
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
                    source[j] = re.sub("\xa0", " ", source[j])
                    description += source[j]
                j += 1
            i = idx
            yield {
                "name": name,
                "description": description,
                "link": response.url,
                "image": img,
                "Province": addr,
                "DATA_LEVEL": "HIGH_LEVEL"
            }
