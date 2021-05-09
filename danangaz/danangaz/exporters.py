from scrapy.exporters import JsonItemExporter


class UTF8JsonExporter(JsonItemExporter):
    def __init__(self, file, **kwargs):
        super(UTF8JsonExporter, self).__init__(
            file, ensure_ascii=False, **kwargs
        )
