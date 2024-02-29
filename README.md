# How to use this code?
1. Clone this repository to your computer. You will get a folder named `file_organization`.
2. Copy this folder inside the folder that has the interface files (the folder that has the `answers.csv` and all the WAV files).
3. Make sure that `pandas` and `numpy` are install on your system. To install them, you can run the following:
```console
pip install pandas
pip install numpy
```
4. Go to the folder that contains the interface files in your terminal (mac users) or CMD (windows users).
5. Type the following command:
```console
python file_organization
```


# Note
- After the copying is completed, you will see a summary report of the files that were copied, skipped, or failed to copy. A complete report is also saved in the same folder as the interface files called `report.csv`. This file will not be inside the organized folders, but at the same level as `answers.csv` and WAV files.
- All the audio files will be in a folder named `organized_files`. However, the original files will be left intact.
- You can run this script as many times as you wish. The script will simply ignore the files that are already copied.
- It is important that the folder containing the script `file_organization` is inside interface files folder at the same level as `answers.csv` and audio WAV files.