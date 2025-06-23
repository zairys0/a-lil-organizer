import os
import shutil

folder_path= "D:\\picnvids"

file_types={
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "videos": [".mp4", ".avi", ".mov",],
    "documents": [".pdf", ".docx", ".txt"]
}

for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path,folder), exist_ok=True)

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if file.lower().endswith(tuple(extensions)):
                    shutil.move(file_path, os.path.join(folder_path, folder, file))
                    break

print("u good nigga!")