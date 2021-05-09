import re
import scrapy

class DaNang(scrapy.Spider):
    name = "DaNang"
    start_urls=[
        "https://danangaz.com/diem-den-da-nang/dia-diem-du-lich-da-nang/"
    ]

    def parse(self, response, **kwargs):
        title = response.css("h2 strong::text").extract()
        title = [t for t in title if not re.match("\xa0Đà Nẵng", t)]
        title = [t for t in title if not re.match("Đà Nẵng", t)]
        title.pop(6)
        title[1:3] = ["".join(title[1:3])]

        address = "h2 strong::text, .td-post-content div strong::text , p:nth-child(47) strong::text , h2+ p strong::text ," \
                  " p strong~ strong+ strong::text , p:nth-child(7)::text , p:nth-child(47)::text , h2+ div::text , ul+ p::text , " \
                  "p:nth-child(180)::text , p:nth-child(182)::text , h2+ p::text"
        source = response.css(address).extract()[:-6]
        source = [s for s in source if not re.match("\xa0Đà Nẵng", s)]
        source = [s for s in source if not re.match("Đà Nẵng", s)]
        source[9:11] = ["".join(source[9:11])]
        
        imgs = response.css('figure img::attr(src), p img::attr(src)').extract()
        imgs = [img for img in imgs if bool(re.match('jpg', img[-3:]))]
        imgs = imgs[:-2]

        n = len(source)
        i = 0
        while i < n and len(title) > 0:
            name = title[0].split(".")[1].strip().split("–")[0].strip()
            tmp_img = []
            tmp_img.append(imgs[0])
            imgs.pop(0)
            if len(title) > 1:
                idx = source.index(title[1])
                title.pop(0)
                description = "".join(source[i + 1:idx])
                i = idx
            else:
                description = "".join(source[i + 1:n])
                title.pop(0)
                i = n

            yield {
                "name": name,
                "description": description,
                "link": response.url,
                "image": tmp_img,
                "Province": "Đà Nẵng",
                "DATA_LEVEL": "HIGH_LEVEL"
            }