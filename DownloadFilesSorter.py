import os
path = "C:/Users/giggl/Downloads/"
invalid_extensions = ()
for subdir, dirs, files in os.walk(path):
    for file in files:
        print(f'Checking file {file}')
        file_extension = os.path.splitext(file)[1]
        if file_extension not in invalid_extensions:
            print(f'File extention {file_extension} is valid')
            if not os.path.isdir(path + file_extension):
                print(f'Folder {file_extension} does not exist. Creating.')
                os.mkdir(path + file_extension)
            try:
                origin = path + file
                destination = path+file_extension+'/'+file
                print(f'Moving file {file} from {origin} to {destination}')
                os.rename(origin,destination)
                print(f'Successfully moved file\n')
            except Exception as e:
                print(e + '\n')
        else:
            print(f'File {extension} not tracked; leaving it alone.\n')
            continue
    #We break here because we only want files in the parent directory. If we
    #let it continue, it will traverse subdirectories
    break
