import pandas as pd
import numpy as np
import os
from pathlib import Path
import shutil
from tqdm import tqdm

current_path = Path("./").resolve()
save_path = current_path.joinpath("organized_files")
csv_path = current_path.joinpath("answers.csv")
data = pd.read_csv(csv_path)
audio_rows = data[~data["audio"].isnull()]
unique_modules = np.unique(audio_rows["module_name"].tolist())
unique_participants = np.unique(audio_rows["email"].tolist())
report = []
for module in tqdm(unique_modules, total=len(unique_modules), desc="Modules"):
    for participant in tqdm(unique_participants, total=len(unique_participants), desc="Participants in the module"):
        os.makedirs(save_path.joinpath(f"{module}/{participant}"), exist_ok = True)
        participant_rows = audio_rows.loc[(audio_rows["email"] == participant) & (audio_rows["module_name"] == module)]
        audio_files = participant_rows["audio"].tolist()
        audio_files = [x.split("/")[1] for x in audio_files]
        for af in audio_files:
            file_save_path = save_path.joinpath(f"{module}/{participant}/{af}")
            file_source_path = current_path.joinpath(f"{af}")
            if (file_source_path.is_file() is True and file_save_path.is_file() is False):
                shutil.copyfile(current_path.joinpath(f"{af}"), save_path.joinpath(f"{module}/{participant}/{af}"))
                report.append({"audio_file": af, "participant": participant, "module": module, "status": "File successfully copied"})
            elif (file_source_path.is_file() is True and file_save_path.is_file() is True):
                report.append({"audio_file": af, "participant": participant, "module": module, "status": "Not copied because already exists"})
            elif file_source_path.is_file() is False:
                report.append({"audio_file": af, "participant": participant, "module": module, "status": "Recording not found and was not copied"})

report_df = pd.DataFrame(report)
len_copied = len(report_df[report_df["status"] == "File successfully copied"])
len_skipped = len(report_df[report_df["status"] == "Not copied because already exists"])
len_not_found = len(report_df[report_df["status"] == "Recording not found and was not copied"])

print("-------------------------------")
print("File Copy Report")
print(f"{len_copied} files were successfully copied.")
print(f"{len_skipped} files weres skipped because they already existed.")
print(f"{len_not_found} files were not copied because they were not found.")
report_df.to_csv(current_path.joinpath("report.csv"))