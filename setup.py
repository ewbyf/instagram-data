from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Scrapes the name and followers of 200 of the top Instagram influencers and puts it in array of dictionaries for JS. It also saves their profile pictures in an img folder.'

# Setting up
setup(
    name="instagram-data",
    version=VERSION,
    description=DESCRIPTION,
    url="https://github.com/ewbyf/instagram-data",
    author="ewbyf (Eric Wong)",
    author_email="ewbyf@umsystem.edu",
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'requests', 'instagrapi', 'pillow'],
    entry_points={
        'console_scripts': ['instagram-data=instagram_data.app:main'],
    },
    keywords=['instagram', 'scraper', 'download', 'media', 'followers'],
)