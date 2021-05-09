import re
import scrapy

class QuangNgai(scrapy.Spider):
    name = "QuangNgai"
    start_urls=[
        "https://danangaz.com/du-lich/63-tinh-thanh/dia-diem-du-lich-quang-ngai/"
    ]

    def mapping(self, line):
        line = line.sub('', "\xa03")
        return line

    def parse(self, response, **kwargs):
        title = response.css("h2 strong::text").extract()
        title = [line for line in title]

        address = "h2+ ul strong::text , #wpipa-8076-container+ p::text, .aligncenter+ p::text ," \
                  "h2 strong::text , .aligncenter+ p strong::text"
        source = response.css(address).extract()

        imgs = response.css('figure img::attr(src), p img::attr(src)').extract()
        imgs = [img for img in imgs if bool(re.match('jpg', img[-3:]))]
        imgs = imgs[:-3]

        n = len(source)
        i = 0
        while i < n and len(title) > 0:
            name = title[0].split(" ", 1)[1].strip().split("–")[0].strip()
            img = []
            img.append(imgs[0])
            imgs.pop(0)
            if len(title) > 1:
                try:
                    idx = source.index(title[1])
                except ValueError:
                    idx = 9
                title.pop(0)
                if re.match(pattern="Địa chỉ:", string=source[i + 1]):
                    destination = source[i + 1].split(":")[1].strip()
                    description = "".join(source[i + 2:idx])
                else:
                    destination = "Quảng Ngãi"
                    description = "".join(source[i + 1:idx])
                i = idx
            else:
                destination = source[i + 1].split(":")[1].strip()
                description = "".join(source[i + 2:n])
                title.pop(0)
                i = n

            yield {
                "name": name,
                "address": destination,
                "description": description,
                "link": "https://danangaz.com/du-lich/63-tinh-thanh/dia-diem-du-lich-quang-ngai/",
                "image": img,
                "DATA_LEVEL": "HIGH_LEVEL"
            }