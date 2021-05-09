import scrapy
from googletrans import Translator
import re


class Technology(scrapy.Spider):
    name = "tech"
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_emerging_technologies"
    ]

    def getParent(self, response):
        return response.css(".toctext::text").extract()[:-3]

    def createID(self, raw_name):
        id = raw_name.lower()
        id = id.replace(" ", "_")
        id = id.replace("-", "_")
        return id

    def parse(self, response):
        parents = self.getParent(response=response)
        translator_bot = Translator()

        src_address = ".mw-headline::text, td:nth-child(1) > a::text"
        source = response.css(src_address).extract()[:-3]

        i = 0
        while len(parents) != 0:
            id = self.createID(parents[0])

            yield {
                "id": id,
                "parent_id": None,
                "name": parents[0],
                "names": {
                    "en": parents[0],
                    "vi": translator_bot.translate(parents[0], dest="vi", src="en").text,
                },
                "synonyms": {
                    "en": [],
                    "vi": []
                },
                "types": [
                    "technology"
                ],
                "level": 1,
                "source": "wikipedia",
                "source_url": "https://en.wikipedia.org/wiki/List_of_emerging_technologies"
            }
            current_parent = parents[0]
            parents.pop(0)
            try:
                next_parent = parents[0]
            except:
                next_parent = None
            i += 1
            try:
                next_index = parents.index(next_parent)
            except:
                next_index = 100000

            while i < len(source) and i <= next_index:
                id = self.createID(source[i])

                yield {
                    "id": id,
                    "parent_id": self.createID(current_parent) + "_technology",
                    "name": source[i],
                    "names": {
                        "en": source[i],
                        "vi": translator_bot.translate(source[i], dest="vi", src="en").text,
                    },
                    "synonyms": {
                        "en": [],
                        "vi": []
                    },
                    "types": [
                        "technology"
                    ],
                    "level": 2,
                    "source": "wikipedia",
                    "source_url": "https://en.wikipedia.org/wiki/List_of_emerging_technologies"
                }
                i += 1
