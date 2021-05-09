import re
import scrapy

class DaNang(scrapy.Spider):
    name = "QuangNam"
    start_urls=[
        "https://danangaz.com/du-lich/63-tinh-thanh/dia-diem-du-lich-quang-nam/"
    ]

    def parse(self, response, **kwargs):
        title = response.css("h2 strong::text").extract()
        title[2:4] = ["".join(title[2:4])]
        title[3:5] = ["".join(title[3:5])]
        title[5:7] = ["".join(title[5:7])]
        title[10:12] = ["".join(title[10:12])]

        address = "p:nth-child(52) strong::text , h2+ ul li::text , .td-post-content div strong::text ," \
                  " h2 strong::text , .aligncenter+ p strong::text ," \
                  ".td-post-content div::text , #attachment_17753~ p::text , h2+ p::text , p:nth-child(38)::text , .aligncenter+ p::text"
        source = response.css(address).extract()[1:-43]
        source[6:8] = ["".join(source[6:8])]
        source[11:13] = ["".join(source[11:13])]
        source[17:19] = ["".join(source[17:19])]
        source[38:40] = ["".join(source[38:40])]

        imgs = response.css('figure img::attr(src), p img::attr(src)').extract()
        imgs = [img for img in imgs if bool(re.match('jpg', img[-3:]))]

        n = len(source)
        i = 0
        while i < n and len(title) > 0:
            name = title[0].split(" ", 1)[1].strip().split("–")[0].strip()
            img = []
            img.append(imgs[0])
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
                "image": img,
                "link": response.url,
                "address": "Quảng Nam",
                "DATA_LEVEL": "HIGH_LEVEL"
            }