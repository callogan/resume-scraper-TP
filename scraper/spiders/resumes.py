import scrapy
from scrapy.http import Response


class ResumesSpider(scrapy.Spider):
    name = "resumes"
    allowed_domains = ["robota.ua"]
    start_urls = ["https://robota.ua/candidates/all/ukraine"]

    def parse(self, response: Response, **kwargs):
        filename = f"resumes.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
