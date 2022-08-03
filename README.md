<img src="https://i.imgur.com/BulaX89.png" width="200" height="200" align="right">

Instagram Data
=================
[![PyPI](https://img.shields.io/pypi/v/instagram-data.svg)](https://pypi.python.org/pypi/instagram-data) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/instagram-data) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/instagram-data)

instagram-data is a command-line application written in Python that scrapes the top 200 Instagram influencers' username and follower count and downloads their profile pictures.

Install
-------
To install instagram-data:
```bash
$ pip install instagram-data
```

To update instagram-scraper:
```bash
$ pip install instagram-data --upgrade
```
Alternatively, you can clone the project and run the following command to install:
Make sure you cd into the *instagram-data-master* folder before performing the command below.
```
$ python setup.py install
```


Usage
-----

To scrape a user's media:
```bash
$ instagram-data         
```

You will then be prompted to enter your username:
```bash
Enter your username:
```

Then your password:
```bash
Enter your password:
```

If credentials are incorrect an error message will pop up, and you will be prompted to retry:
```bash
Password does not match with that username. Try again.
Enter your username:
```

If everything is done correctly, the program will begin processing each index:
```bash
Processing index: 0/199
```

Once the program is finished it will output:
```bash
Done
```

*The data will be placed as an array of dictionaries for JS in `instagram_data/data.txt`.*

*Downloaded profile pictures will be placed in `instagram_data/img`.*

Usage as library
----------------
```python
from instagram_data import scrape

scrape("USERNAME", "PASSWORD") # Replace USERNAME and PASSWORD with your Instagram credentials
```

Contributing
------------
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository and make your changes
3. Send a pull request

License
-------

MIT License

Copyright (c) 2022 Eric Wong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
