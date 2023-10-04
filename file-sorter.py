import os, shutil

path = r"/Users/evynhedgpeth/repos/automated-file-sorter/"

fileName = os.listdir(path)

folderNames = ['image-files', 'csv-files', 'xlsx-files', 'json-files', 'document-files', 'zip-files']

for loop in range(0, 6):
    if not os.path.exists(path + folderNames[loop]):
        os.makedirs(path + folderNames[loop])

for file in fileName:
    if '.jpg' in file and not os.path.exists(path + "image-files/" + file):
        shutil.move(path + file, path + "image-files/" + file)
    elif '.csv' in file and not os.path.exists(path + "csv-files/" + file):
        shutil.move(path + file, path + "csv-files/" + file)
    elif '.xlsx' in file and not os.path.exists(path + "xlsx-files/" + file):
        shutil.move(path + file, path + "xlsx-files/" + file)
    elif '.json' in file and not os.path.exists(path + "json-files/" + file):
        shutil.move(path + file, path + "json-files/" + file)
    elif '.docx' in file and not os.path.exists(path + "document-files/" + file):
        shutil.move(path + file, path + "document-files/" + file)
    elif '.zip' in file and not os.path.exists(path + "zip-files/" + file):
        shutil.move(path + file, path + "zip-files/" + file)


