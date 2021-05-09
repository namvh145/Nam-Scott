import re
import scrapy


class QuangTri(scrapy.Spider):
    name = "QuangTri"
    start_urls = [
        "https://toplist.vn/top-list/dia-diem-du-lich-hap-dan-nhat-tinh-quang-tri-3429.htm"
    ]

    def parse(self, response, **kwargs):
        address = ".media-body p::text , strong::text , .item_dsp_row .media-heading::text"

        source = response.css(address).extract()
        title = response.css(".item_dsp_row .media-heading::text").extract()

        n = len(source)
        pattern = r"Địa chỉ:"

        name = ""
        description = ""
        address = ""
        for i in range(n):
            if source[i] in title:
                name = source[i]
                title.remove(name)
                description = ""
            else:
                if bool(re.match(pattern, source[i])):
                    address = source[i].split(":")[1].strip()
                    yield {
                        "Name": name,
                        "Address": address,
                        "Description": description
                    }
                else:
                    description += source[i]