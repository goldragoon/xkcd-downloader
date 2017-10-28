# xkcd Downloader

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c4934e37fee44c27a3e8848974c907b7)](https://www.codacy.com/app/neelkamath/xkcd-downloader?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=neelkamath/xkcd-downloader&amp;utm_campaign=Badge_Grade)
[![Known Vulnerabilities](https://snyk.io/test/github/neelkamath/xkcd-downloader/badge.svg)](https://snyk.io/test/github/neelkamath/xkcd-downloader)

Ever been bored and wanted offline access to [xkcd](https://xkcd.com/)? This software downloads each comic from xkcd skipping those already downloaded without the need for SQL, complex command line arguments etc. To facilitate easier reading, comics are stored in `year/month` subdirectories. A few comic numbers might be skipped because they either don't exist or don't contain a visual.

# Installation

## Prerequisites

- [Python 3 or higher](https://www.python.org/downloads/)

## Building

```shell
git clone https://github.com/neelkamath/xkcd-downloader
cd xkcd-downloader
pip3 install -r requirements.txt
```

# Usage

1. Change the directory: `cd src`
1. Run:
    - Windows: `python downloader.py`
    - Other: `python3 downloader.py`

# Contributing

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing](CONTRIBUTING.md)

# License

This project is under the [MIT License](LICENSE.txt).
