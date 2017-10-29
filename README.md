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
    
If using [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en), you can specify the path to be `./../../storage/pictures/xkcd` so that it shows up in Google Photos.

You can optionally have the script run each time your computer boots using the following steps.
- Windows:
    1. Go to the directory `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `<YOUR_USERNAME>` is your username.
    1. Create a shortcut pointing to the location of the script.
    1. Make sure python scripts open with `Python` (so that when you open the file from Windows Explorer it runs the script and doesn't open the editor). You can do this by right-clicking the script, clicking `Opens with:` in the `General` tab and choosing `Python`.
- Linux:
    1. Make the file executable: `chmod +x downloader.py`
    1. Create a new cron job: `crontab -e`
    1. Add the line: `@reboot <PATH>`, where `<PATH>` is the absolute path to `downloader.py`

# Contributing

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing](CONTRIBUTING.md)

# License

This project is under the [MIT License](LICENSE.txt).
