import re
import scrapy


class QuangTri(scrapy.Spider):
    name = "Hue"
    start_urls = [
        "https://toplist.vn/top-list/diem-du-lich-noi-tieng-xu-hue-382.htm"
    ]

    def parse(self, response, **kwargs):
        address = ".media-body li::text , .media-body p::text , strong::text , .item_dsp_row .media-heading::text"

        source = response.css(address).extract()
        title = response.css(".item_dsp_row .media-heading::text").extract()

        n = len(source)

        name = ""
        description = ""
        for i in range(n):
            if source[i] in title:
                name = source[i]
                title.remove(name)
                description = ""
            else:
                if (i + 1 < n and source[i + 1] in title) or i + 1 == n:
                    description += source[i]

                    yield {
                        "Name": name,
                        "Description": description
                    }
                else:
                    description += source[i]