import WebScraper as scraper



# write the main function if name is main
if __name__ == '__main__':
    dataset = scraper.getData(dataset='dataset.txt')
    scraper.uploadData(dataset)
