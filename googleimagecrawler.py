from icrawler.builtin import GoogleImageCrawler
google_Crawler = GoogleImageCrawler(storage = {'root_dir': r'C:\Users\katar\OneDrive\Desktop\Netflix'})
sisend = "friends"
google_Crawler.crawl(keyword = sisend, max_num=1)

 
