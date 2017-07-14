# xkcd Downloader

Ever been bored and wanted offline access to [xkcd](https://xkcd.com/)? This software downloads each comic from xkcd skipping those already downloaded without the need for SQL, complex command line arguments etc. To facilitate easier reading, comics are stored in `year/month` subdirectories. A few comic numbers might be skipped because they either don't exist or don't contain a visual.

# Installation

## Prerequisites

- [Python 3 or higher](https://www.python.org/downloads/)

## Building

1. Clone the repository: `git clone https://github.com/neelkamath/xkcd-downloader`
1. Change the directory: `cd xkcd-downloader`
1. Install the dependencies: `pip3 install -r requirements.txt`

# Usage

1. Change the directory: `cd src`
1. Run:
    - Windows: `python downloader.py`
    - Other: `python3 downloader.py`
1. If this is the first time running it, it will immediately terminate after generating the file `config.json`. If you want to change the directory it downloads comics to (by default, it downloads to `comics` located in the scripts' directory), you may do so in `config.json`. Run the script again if necessary.
1. It's also possible to have the script run each time your computer powers on so that new comics are automatically downloaded. The steps to do so are listed below but only work on Windows as other distros have varying steps to achieve this:
    1. Go to the directory `C:\Users\<YOUR_USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`, where `<YOUR_USERNAME>` is your username.
    1. Create a shortcut pointing to the location of the script.
    1. Make sure python scripts open with `Python` (so that when you open the file from File Explorer it runs the script and doesn't open the editor). You can do this by right-clicking the script, clicking `Opens with:` in the `General` tab and choosing `Python`.

# Contributing

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing](CONTRIBUTING.md)

# License

This project is under the [MIT License](LICENSE.txt).
