import re
import scrapy


class QuangNam(scrapy.Spider):
    name = "NinhThuan"
    start_urls = [
        "https://danangaz.com/du-lich/63-tinh-thanh/dia-diem-du-lich-ninh-thuan/"
    ]

    def parse(self, response, **kwargs):
        address = "h2 strong::text , strong::text , .wpipa-align-center+ p::text , p+ p::text , figure img::attr(src), p img::attr(src)"

        title = response.css("h2 strong::text").extract()

        source = response.css(address).extract()[:-7]
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
            addr = source[i + 1].split(":")[1].strip()
            price = source[i + 2].split(":")[1].strip()
            i += 2
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
                "price": price,
                "DATA_LEVEL": "HIGH_LEVEL"
            }