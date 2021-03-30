import os

file = os.path.realpath('directory1/mm-official.txt')
directory = os.path.dirname(file)

print(file, directory)

files = os.listdir(directory)

# for f in files:
#     print(f)

for root, directories, files in os.walk(directory):
    for name in files:
        print(name)
    # for name in directories:
    #     print(name)