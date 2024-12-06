# cd into /Users/kip/Downloads
import os
os.chdir('/Users/kip/Downloads')

# rename all files ending in .txt to .text
for file in os.listdir():
    if file.endswith('.txt'):
        file_name, file_ext = os.path.splitext(f)
        new_name = file_name + '.text'
        os.rename(f, new_name)

# print done to the console
print('Files renamed!')