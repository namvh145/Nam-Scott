import scrapy
import re


class HaTinh(scrapy.Spider):
    name = "HaTinh"
    start_urls = [
        "https://sayhi.vn/blog/dia-diem-du-lich-ha-tinh/"
    ]

    def parse(self, response, **kwargs):
        address = "b::text , p::text , strong::text, span::text"
        source = response.css(address).extract()[16:-33]

        pattern = re.compile(r'^>')
        source = [line for line in source if not pattern.match(line)]

        pattern = re.compile(r"^([0-9]|[0-9][0-9])\. \w+")

        n = len(source)
        i = 0
        name = ""
        description = ""
        address = ""
        price = ""
        while i < n:
            if bool(re.match(r'20\.', source[i])):
                name = source[i].split('. ')[1].split(' – ')[0].strip()
                address = source[i + 2].split(":")[1].strip()
                price = source[i + 3].split(":")[1].strip()
                description = ""
                i += 3
            elif bool(re.match(r'(21|22)\.', source[i])):
                name = source[i].split('. ')[1].split(' – ')[0].strip()
                address = source[i + 2].strip()
                price = source[i + 3].split(":")[1].strip()
                description = ""
                i += 3
            elif bool(pattern.match(source[i])):
                name = source[i].split('. ')[1].split(' – ')[0].strip()
                address = source[i + 1].split(":")[1].strip()
                price = source[i + 2].split(":")[1].strip()
                description = ""
                i += 2
            else:
                if i + 1 < n and bool(pattern.match(source[i + 1])):
                    description += source[i]
                    yield {
                        "Name": name,
                        "Address": address,
                        "Price": price,
                        "Description": description
                    }
                else:
                    description += source[i]
            i += 1
