# xkcd Downloader

[![Known Vulnerabilities](https://snyk.io/test/github/neelkamath/xkcd-downloader/badge.svg)](https://snyk.io/test/github/neelkamath/xkcd-downloader)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

Ever been bored and wanted offline access to [xkcd](https://xkcd.com/)? This software downloads each comic from xkcd skipping those already downloaded without the need for SQL, complex command line arguments etc. To facilitate easier reading, comics are stored in `year/month` subdirectories. A few comic numbers might be skipped because they either don't exist or don't contain a visual.

# Installation

## Prerequisites

- [Python 3 or higher](https://www.python.org/downloads/)

## Building

```shell
git clone https://github.com/neelkamath/xkcd-downloader.git
cd xkcd-downloader
pip3 install -r requirements.txt
```

# Usage

1. Change the directory: `cd src`
1. Run:
    - Windows: `python downloader.py`
    - Other: `python3 downloader.py`

If you're using [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en), you can have the comics show up in Google Photos on your device by running `termux-setup-storage` and specifying the path to be `./../../storage/pictures/xkcd`.

You can optionally have the script run each time your computer boots using the following steps:
- Windows:
    1. Go to the directory `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `<YOUR_USERNAME>` is your username.
    1. Create a shortcut pointing to the location of the script.
    1. Make sure python scripts open with `Python` (so that when you open the file from Windows Explorer it runs the script and doesn't open the editor). You can do this by right-clicking the script, clicking `Opens with:` in the `General` tab and choosing `Python`.
- Other:
    1. Make the script executable: `chmod +x downloader.py`
    1. Schedule it:
        1. `crontab -e`
        1. At the end of the file, add: `@reboot <PATH>`, where `<PATH>` is the path to the script

# Contributing

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing](CONTRIBUTING.md)
