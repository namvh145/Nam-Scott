import scrapy

class QuangBinh(scrapy.Spider):
    name = "QuangBinh"
    start_urls = [
        "https://toplist.vn/top-list/dia-diem-tham-quan-noi-tieng-o-quang-binh-5023.htm"
    ]

    def parse(self, response, **kwargs):
        address = ".media-body p::text , .item_dsp_row .media-heading::text, strong::text"
        title = response.css(".item_dsp_row .media-heading::text").extract()
        source = response.css(address).extract()

        name = ""
        description = ""
        n = len(source)

        for i in range(n):
            if source[i] in title:
                name = source[i]
                title.remove(name)
                description = ""
            else:
                if i + 1 < n and source[i + 1] in title:
                    description += source[i]
                    yield {
                        "Name": name,
                        "Description": description
                    }
                else:
                    description += source[i]