# files + modules 

# libraries: eg standard library, multiple packages
# packages: directory of modules 
# modules: just python files 

# files:
    #   - logs,
    #   - storing/accessing data,
    #   - configuration files,
    #   - scripts,

# types: 
    # text files: .txt, .csv, .json, .xml
    # json 
    # image files: .jpg, .png, .gif
    # audio files: .mp3, .wav
    # video files: .mp4, .avi
    # document files: .pdf, .docx

# read + write (append)

#opening
# file = open("lines.txt", "r") # r (read), w (write + make a file), a (append + make a file)

# commands:

# read() reads an entire file
# readline() reads a single line and moves to the next line
# readlines() reads all lines and returns them as a list
# seek(n) defaults to first line. 

# write() writes an entire string 
# writelines() writes a list to the file

# file = open("lines.txt", "r")

# l = file.readlines()

# print(l)

# file.close()

# file = open("lines-new.txt", "w")

# for n in range(11):
#     newline = "this is new line number " + str(n) + "\n"
#     file.write(newline)     

# file.close() 