Ultimate Image Downloader

Ultimate Image Downloader is a powerful command-line tool that allows you to download high-quality images from popular search engines like Google, Bing, and Baidu. Whether you're looking for portraits or full-body images, this tool provides an interactive experience to customize your image search and download preferences.
Table of Contents

Features

    High-Quality Images: Downloads large images (minimum size of 500x500 pixels) for better quality.
    Customizable Image Type: Choose between portrait (face) images or full-body images.
    Multi-Site Support: Download images from Google, Bing, Baidu, or all simultaneously.
    User-Friendly Interaction: The script interacts with you to get necessary inputs through the terminal.
    Organized Storage: Images are saved in a directory named after your keyword, with subdirectories for each site.
    Flexible Configuration: Adjust filters and settings easily within the script.

Demo

Note: The demo shows the script in action, downloading images based on user input.
Installation

    Clone the Repository

    bash

git clone https://github.com/yourusername/ultimate-image-downloader.git
cd ultimate-image-downloader

Create a Virtual Environment (Optional but Recommended)

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies

bash

pip install -r requirements.txt

If requirements.txt is not present, install icrawler directly:

bash

    pip install icrawler

Usage
Running the Script

Run the script using Python:

bash

python ultimate_image_downloader.py

Sample Interaction

    Enter the Name/Keyword

    bash

Enter the name/keyword: John Doe

Enter the Number of Images to Download

css

Enter the number of images to download: 50

Choose Image Type

arduino

Do you want 'portrait' or 'full body' images? portrait

Select Site(s) to Download From

mathematica

    Which site(s) to download from? Options: google, bing, baidu, all
    Enter your choice: all

    Download Progress

    The script will start downloading images and display progress messages for each selected site.

Project Structure

arduino

ultimate-image-downloader/
├── ultimate_image_downloader.py
├── README.md
├── LICENSE
├── .gitignore
└── images/
    ├── John Doe_images/
        ├── google/
        ├── bing/
        └── baidu/

    ultimate_image_downloader.py: The main script to run.
    images/: Directory where downloaded images are stored, organized by keyword and site.

Requirements

    Python 3.6 or higher

    icrawler

    Install via pip:

    bash

pip install icrawler
