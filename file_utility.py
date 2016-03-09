#!/usr/local/bin/python

import File

f = File.File()
f.parseFilesList("\n")

def menu():
    option = str(raw_input("\nChoose One of the Following Options:\n\nv: view all contents in current directory\np: view the current path you are in\nmu: move up a level\nmd: move down into a specified directory\naf: add a folder\nafl: add a file\nd: delete a folder/file\ns: spam a machine by specifying a number of files that will be added to the folder\nq: quit application\n\n"))
    return option

def main():
    print("Welcome to Ashhad's File Utility!")
    option = menu()
    while (option != "q"):
        if(option == "v"):
            f.getIndexedList()
            option = menu()
        if(option == "p"):
            f.getCurDir()
            option = menu()
        if(option == "mu"):
            f.moveUpLevel()
            option = menu()
        if(option == "md"):
            level = str(raw_input("Please enter the name of the directory that you would like to access: "))
            f.moveIntoDir(level)
            option = menu()
        if(option == "af"):
            subOption = str(raw_input("Please enter a name for the new folder: "))
            f.addDir(subOption)
            option = menu()
        if(option == "afl"):
            subOption = str(raw_input("Please enter a name for the new file: "))
            f.addFile(subOption)
            option = menu()
        if(option == "d"):
            subOption = int(raw_input("Please enter the number associated with the file you would like to delete: "))
            f.delFile(subOption)
            f.getIndexedList()
            option = menu()
        if(option == "s"):
            counter = 1
            name = str(raw_input("Please enter a name for the new files to be added: "))
            limit = int(raw_input("Please enter  the number of files to be populated: "))
            for i in range(counter, limit+1):
                f.addFile(name + str(counter))
                counter += 1
            option = menu()

main()
