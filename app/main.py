import os
from pathlib import Path
from pydub import AudioSegment

main_folder = r"C:\Users\your_user\Music\source"
convert_folder = main_folder + r"\mp3"

Path(convert_folder).mkdir(parents=True, exist_ok=True)

ls_folder = os.listdir(main_folder)

files = [f for f in ls_folder if os.path.isfile(os.path.join(main_folder, f))]

for file in files:
    extension = Path(file).suffix
    if (extension == '.ogg'):
        filename = Path(file).stem + ".mp3"
        filepath = main_folder + '\\' + file
        audio_ogg = AudioSegment.from_ogg(filepath)
        mp3_path = os.path.join(convert_folder, filename)
        audio_ogg.export(mp3_path, format="mp3")
