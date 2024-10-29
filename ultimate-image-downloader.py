from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
import os

def main():
    # Prompt for keyword
    keyword = input("Enter the name/keyword: ").strip()
    
    # Prompt for number of images
    while True:
        try:
            max_num = int(input("Enter the number of images to download: ").strip())
            if max_num > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Prompt for image type: portrait or full body
    while True:
        image_type = input("Do you want 'portrait' or 'full body' images? ").strip().lower()
        if image_type in ['portrait', 'full body']:
            break
        else:
            print("Please enter 'portrait' or 'full body'.")
    
    # Prompt for site selection
    print("Which site(s) to download from? Options: google, bing, baidu, all")
    site_input = input("Enter your choice: ").strip().lower()
    if site_input == 'all':
        sites = ['google', 'bing', 'baidu']
    else:
        sites = [site.strip() for site in site_input.split(',') if site.strip() in ['google', 'bing', 'baidu']]
        if not sites:
            print("No valid sites selected. Exiting.")
            return
    
    # Filters for high-quality large images
    google_filters = {
        'size': 'large',
    }
    bing_filters = {
        'size': 'large',
    }
    baidu_filters = {
    }
    
    # Adjust filters based on image type
    if image_type == 'portrait':
        google_filters['type'] = 'face'
        bing_filters['people'] = 'face'
        baidu_filters['type'] = 'face'
    elif image_type == 'full body':
        # For full body, we avoid setting 'face' filters
        pass  # No additional filters needed
        # Optionally, you can set 'type' to 'photo' to get general images
        google_filters['type'] = 'photo'
        bing_filters['type'] = 'photo'
        baidu_filters['type'] = 'static'  # 'static' to exclude animations
    
    # Create root directory for images
    root_dir = f'{keyword}_images'
    os.makedirs(root_dir, exist_ok=True)
    
    # Start crawling for each selected site
    if 'google' in sites:
        print("Starting Google Image Crawler...")
        storage = {'root_dir': os.path.join(root_dir, 'google')}
        google_crawler = GoogleImageCrawler(
            feeder_threads=1,
            parser_threads=1,
            downloader_threads=4,
            storage=storage
        )
        google_crawler.crawl(
            keyword=keyword,
            filters=google_filters,
            max_num=max_num,
            min_size=(500, 500)
        )
    
    if 'bing' in sites:
        print("Starting Bing Image Crawler...")
        storage = {'root_dir': os.path.join(root_dir, 'bing')}
        bing_crawler = BingImageCrawler(
            downloader_threads=4,
            storage=storage
        )
        bing_crawler.crawl(
            keyword=keyword,
            filters=bing_filters,
            max_num=max_num,
            min_size=(500, 500)
        )
    
    if 'baidu' in sites:
        print("Starting Baidu Image Crawler...")
        storage = {'root_dir': os.path.join(root_dir, 'baidu')}
        baidu_crawler = BaiduImageCrawler(
            storage=storage
        )
        baidu_crawler.crawl(
            keyword=keyword,
            filters=baidu_filters,
            max_num=max_num,
            min_size=(500, 500)
        )

if __name__ == "__main__":
    main()
