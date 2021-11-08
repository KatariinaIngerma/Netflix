from icrawler.builtin import GoogleImageCrawler
google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\katar\OneDrive\Desktop\Netflix'})
google_Crawler.crawl(keyword = 'kass', max_num = 1)

