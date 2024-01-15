import os

destination = str(input('Enter path to organize: '))

fileFormat = {
    "Videos": ["mp4", "mov", "wmv", "avi", "avchd", "mkv"],
    "Images": ["jpeg", "jpg", "png", "gif", "tiff"],
    "Audio": ["mp3", "acc", "ogg", "flac", "alac", "wav", "aiff", "dsd", "pcm", ],
    "Compressed": ["zip", "rar", "rar4", "7z", "iso", "tar", "gz", "dmg", "xar"],
    "Documents": ["pdf", "doc", "docx", "txt"],
    "Web": ["htm", "html"]
}

if not os.path.isdir(destination):
    print('Destination ' + destination + ' is invaild')
else:
    for folder in fileFormat:
        if not os.path.exists(destination + '\\' + folder):
            os.mkdir(os.path.join(destination, folder))
            print('Creating folder: ' + folder)

    for file in os.listdir(destination):
        for folder in fileFormat:
            for fileType in fileFormat[folder]:
                if file[file.find('.') + 1:] == fileType:
                    try:
                        if not os.path.exists(destination + '\\'+ folder +'\\' + file):
                            os.replace(destination + '\\' + file, destination + '\\' + folder + '\\' + file)
                            print('File \'' + file + '\' moved to ' + destination + '\\' + folder)
                        else:
                            print('[ERROR] Could not move file: ' + file + ' is already in dir ' + destination + '\\' + folder)
                    except FileNotFoundError:
                        print('[ERROR] ' + file + 'could not be located')