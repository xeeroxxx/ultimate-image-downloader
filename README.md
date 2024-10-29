# Ultimate Image Downloader

Ultimate Image Downloader is a Python-based tool designed to download images from popular search engines like Google, Bing, and Baidu. It offers options for downloading both portrait and full-body images based on user-provided keywords, and it allows users to select specific sites or download from all available sources.

## Features

- **Search from multiple sources:** Google, Bing, Baidu, or all three.
- **Download high-quality images:** Fetches large-sized images.
- **Image type filters:** Choose between portrait or full-body images.
- **User-defined settings:** Specify the number of images and the site(s) to download from.
- **Easy-to-use interface:** Simple prompts for user input.

## Requirements

Before you run the script, ensure you have the following dependencies installed:

- Python 3.x
- iCrawler

Install the dependencies using:

```bash
pip install icrawler
```

## How to Use

1. Clone this repository:

   ```bash
   git clone https://github.com/xeeroxxx/ultimate-image-downloader.git
   cd ultimate-image-downloader
   ```

2. Run the script:

   ```bash
   python ultimate-image-downloader.py
   ```

3. Follow the prompts:
   - **Enter the name/keyword**: Provide the search term for the images you want to download.
   - **Enter the number of images to download**: Specify the number of images.
   - **Choose image type**: Select either 'portrait' or 'full body'.
   - **Choose site(s)**: Select from Google, Bing, Baidu, or all.

## Directory Structure

The downloaded images will be saved in a directory named after the keyword provided, organized by the site:

```
keyword_images/
    ├── google/
    ├── bing/
    └── baidu/
```

## Example

```bash
python ultimate-image-downloader.py
```

**Output:**
```
Enter the name/keyword: cats
Enter the number of images to download: 10
Do you want 'portrait' or 'full body' images? portrait
Which site(s) to download from? Options: google, bing, baidu, all
Enter your choice: all
```

The images will be downloaded and saved in a directory named `cats_images`, with subdirectories for Google, Bing, and Baidu.

