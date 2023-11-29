import os

# Define source directory and subdirectories
source_dir = "/Users/irfanali/Downloads"
folders = {
    'Videos': 'Videos',
    'Audios': 'Audios',
    'Images': 'Images',
    'Documents': 'Documents',
}

# Create folders if they don't exist
for folder_name in folders.values():
    folder_path = os.path.join(source_dir, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move files based on their extensions
def move_files(file_extensions, target_dir):
    def is_valid_extension(filename):
        basename, extension = os.path.splitext(filename)
        return extension in file_extensions

    with os.scandir(source_dir) as entries:
        for entry in entries:
            if entry.is_file() and is_valid_extension(entry.name):
                os.rename(entry.path, os.path.join(target_dir, entry.name))

# Move images
image_extensions = ['.jpeg', '.jpg', '.HEIC', '.png']
move_files(image_extensions, folders['Images'])

# Move videos
video_extensions = ['.mkv', '.mp4', '.mov']
move_files(video_extensions, folders['Videos'])

# Move documents
document_extensions = ['.pdf', '.doc', '.docx', '.xlsx']
move_files(document_extensions, folders['Documents'])

# Move audio files
audio_extensions = ['.mp3']
move_files(audio_extensions, folders['Audios'])
