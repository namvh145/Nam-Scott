import re
import scrapy


class DakLak(scrapy.Spider):
    name = "DakLak"
    start_urls = [
        "https://danangaz.com/du-lich/63-tinh-thanh/dia-diem-du-lich-dak-lak/"
    ]

    def parse(self, response, **kwargs):
        address = "h2 strong:nth-child(1)::text , .aligncenter~ p em::text , .td-post-content li::text , p::text , figure img::attr(src), p img::attr(src) ," \
                  "p:nth-child(8)::text , p:nth-child(13)::text , p:nth-child(39)::text , p:nth-child(55)::text , p:nth-child(83)::text , " \
                  "p:nth-child(98)::text , p:nth-child(107)::text , p:nth-child(116)::text , .aligncenter+ p::text"

        title = response.css("h2 strong::text").extract()
        title = [t for t in title if bool(re.findall(r"\d\.", t))]

        source = response.css(address).extract()[:-10]
        source = [s for s in source if not bool(re.findall(r"^>>>", s))]

        imgs = response.css("figure img::attr(src), p img::attr(src)").extract()
        imgs = [img for img in imgs if not  bool(re.match('gif', img[-3:]))][:-3]

        n = len(source)
        i = 0
        while i < n and len(imgs) > 0:
            name = title[0].split('.')[1].strip().split("–")[0].strip()
            description = ""
            title.pop(0)
            img = []
            addr = "Đắk Lắk"
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
                "Province": addr,
                "DATA_LEVEL": "HIGH_LEVEL"
            }