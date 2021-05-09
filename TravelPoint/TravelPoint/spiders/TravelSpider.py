import scrapy
import re

class TravelSpider(scrapy.Spider):
    name = "ThanhHoa"
    start_urls = [
        "https://dulichchaovietnam.com/13-diem-du-lich-hap-dan-nhat-thanh-hoa.html"
    ]

    def parse(self, response, **kwargs):
        source = response.css("p > span::text, .item strong::text , span img::attr(src), p img::attr(src)").extract()
        source = source[1:]
        source = [s for s in source if not bool(re.findall("images", s))]

        imgs = response.css("span img::attr(src), p img::attr(src)").extract()[:-1]
        title = response.css(".item strong::text").extract()
        title.pop(7)

        n = len(source)

        i = 0
        while i < n and len(imgs) > 0:
            name = title[0].split('.')[1].strip()
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
                "Province": "Thanh Hóa",
                "DATA_LEVEL": "HIGH_LEVEL"
            }