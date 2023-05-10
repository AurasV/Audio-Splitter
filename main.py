from tkinter import filedialog
import subprocess
import shutil
import os
from pathlib import Path
import spleeter


def execute():
    """
    @article{spleeter2020,
    doi = {10.21105/joss.02154},
    url = {https://doi.org/10.21105/joss.02154},
    year = {2020},
    publisher = {The Open Journal},
    volume = {5},
    number = {50},
    pages = {2154},
    author = {Romain Hennequin and Anis Khlif and Felix Voituret and Manuel Moussallam},
    title = {Spleeter: a fast and efficient music source separation tool with pre-trained models},
    journal = {Journal of Open Source Software},
    note = {Deezer Research}
    }
    https://github.com/deezer/spleeter
    """
    amount = 5
    command = "python3 -m spleeter separate -p spleeter:" + str(
        amount) + "stems -o " + filesave + " " + '"' + fileopen + '"'
    print(command)
    subprocess.run(command)


def archive_make():
    archive = shutil.make_archive(filesave + "/" + file_name, 'zip', filesave + "/" + file_name_no_extension)
    shutil.rmtree(filesave + "/" + file_name_no_extension)


fileopen = filedialog.askopenfilename(  # get file path
    initialdir="C:/",  # initial dir = root folder (windows folder)
    title="Select audio file",  # title of the search window
    filetypes=(  # allowed formats
        ("Audio Files", ".wav .aiff .flac .mp3 .m4a .ogg"),
    ))
file_name = os.path.basename(fileopen)
file_name_no_extension = Path(fileopen).stem
filesave = filedialog.askdirectory(
    initialdir="C:/",  # initial dir = root folder (windows folder)
    title="Select where to save the split files"  # title of the search window
)
execute()
archive_make()
