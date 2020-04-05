import glob
import os


def print_list(list):
    for fileName in list:
        print(fileName)
    print()


def delete_file(fileName):
    print('Inside delete_file :: Deleting file [{}] ' .format(fileName))

    # Chck if file exists beflre deleting it
    if (os.path.isfile(fileName)):
        os.remove(fileName)
        print('File [{}] deleted successfully !' .format(fileName))
    else:
        print('Error: File [{}] Not Found !!' .format(fileName))

    # Exception handling for file deletion using try: block
    # try:
    #     os.remove(fileName)
    # except OSError as e:
    #     print('Error: {}' .format(e))


# get JPG files from file system
jpgFilePath = input('Enter JPG File path: ')
# print('JPG File Path: {}' .format(jpgFilePath))
jpgFileNameList = glob.glob(jpgFilePath + '/*.JP*')
print_list(jpgFileNameList)

# get NEF files from file system
nefFilePath = input('Enter NEF File path: ')
# print('NEF File Path: {}' .format(nefFilePath))
nefFileNameList = glob.glob(nefFilePath + '/*.NEF')
print_list(nefFileNameList)


# Delete extra NEF Files
n = 0
for nefFullFileName in nefFileNameList:
    n = n+1
    print('-----')
    # basaename returns only filename without full Path
    # splitext returns filename till last . (i.e. remove extension)
    nefFileName = os.path.splitext(os.path.basename(nefFullFileName))[0]
    print('NEF File-{}: Searching file [{}] in JPG List' .format(n, os.path.basename(nefFileName)))

    j = 0
    found = False
    # search for nefFile in jpgFileNameList
    for jpgFullFileName in jpgFileNameList:
        j = j+1
        jpgFile = os.path.splitext(os.path.basename(jpgFullFileName))[0]
        print('JPG File-{}: Basename [{}] ' .format(j, jpgFile))

        if(nefFileName == jpgFile):
            # delete NEF file from file system
            print('Match Found, DO NOT DELETE: Moving to next NEF file !')
            found = True
            break
        else:
            print('NO Match: Searching next JPG File')

    if not found:
        print('NO Match: Deleting NEF File [{}]' .format(nefFullFileName))
        delete_file(nefFullFileName)
