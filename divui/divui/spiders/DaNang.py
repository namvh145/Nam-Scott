import re
import scrapy


class DaNang(scrapy.Spider):
    name = "DaNang"
    start_urls = [
        "http://divui.com/blog/47-dia-diem-du-lich-da-nang-dep-den-man-quen-loi-ve/"
    ]

    def parse(self, response, **kwargs):
        address = ".td-post-content li::text , .td-post-content p::text , .td-post-content h3::text"
        source = response.css(address).extract()

        title = response.css(".td-post-content h3::text").extract()

        pattern1 = re.compile(r"Địa chỉ:")
        pattern2 = re.compile(r"Giá vé:")

        imgs = response.css('figure img::attr(src)').extract()
        imgs = [img for img in imgs if imgs.index(img) % 2 != 0]
        n = len(source)
        i = 0
        while i < n and len(title) > 0:
            idx = source.index(title[0])
            name = title[0]
            title.pop(0)
            img = []
            if pattern1.match(source[idx - 1]) and not pattern2.match(source[idx - 2]):
                destination = source[idx - 1].split(":")[1].strip()
                price = "Miễn phí"
            elif pattern1.match(source[idx - 1]) and pattern2.match(source[idx - 2]):
                destination = source[idx - 1].split(":")[1].strip()
                price = source[idx - 2].split(":")[1].strip()
            else:
                destination = "Đà Nẵng"
                price = "Miễn phí"
            description = "".join(source[i + 1:idx - 1])
            img.append(imgs[0])
            imgs.pop(0)
            DATA_LEVEL = "HIGH_LEVEL"
            i = idx

            yield {
                "name": name,
                "address": destination,
                "price": price,
                "link": response.url,
                "description": description,
                "image": img,
                "DATA_LEVEL": DATA_LEVEL
            }
