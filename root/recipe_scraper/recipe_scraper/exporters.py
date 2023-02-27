from scrapy.exporters import CsvItemExporter


class HeadlessCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):

        # args[0] is (opened) file handler
        # if file is not empty then skip headers
        if args[0].tell() > 0:
            kwargs['include_headers_line'] = False

        super(HeadlessCsvItemExporter, self).__init__(*args, **kwargs)


#https://stackoverflow.com/questions/34485789/scrapy-csv-output-without-header?noredirect=1&lq=1