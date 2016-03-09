#!/usr/local/bin/python

import subprocess
import os
class File(object):

    def __init__(self, path = subprocess.check_output(["pwd"]), ls_string = subprocess.check_output(["ls"]), file_list = []):
        self.Path = path[:len(path)-1]
        self.LsString = ls_string
        self.FileList = file_list

    def getLsString(self):
        return self.LsString

    def grabFile(self, found_file):
        self.FileList.append(found_file)

    def getFoundFileList(self):
        return self.FileList

    def moveUpLevel(self):
        os.chdir("..")
        self.Path = subprocess.check_output(["pwd"])

    def moveIntoDir(self, level):
        cur_path = self.Path
        new_path = cur_path + "/" + str(level)
        new_path = self.parseWrd(new_path, "\n")
        os.chdir(new_path)
        self.Path = subprocess.check_output(["pwd"])

    def getIndexedList(self):
        self.updateList()
        counter = 0
        for i in self.FileList:
            print(str(counter) + ". " + self.FileList[counter])
            counter += 1

    def getCurDir(self):
        print ("\n" + self.Path)

    def addDir(self, name):
        os.system("sudo mkdir " + str(name))
        self.updateList()

    def addFile(self, name):
        os.system("sudo touch " + str(name))
        self.updateList()

    def delFile(self, num):
        os.system("sudo rm -r " + str(self.FileList[num]))
        self.updateList()
        
    def clearList(self):
        self.FileList = []
        self.LsString = subprocess.check_output(["ls"])

    def updateList(self):
        self.clearList()
        self.parseFilesList("\n")

    def getNewLsString(self):
        return subprocess.check_output(["ls"])

    def parseFilesList(self, char):
        self.clearList()
        files = self.LsString
        thisFile= ''
        for i in range(0, len(files)):
            if files[0] == "\n":
                i = 1
            while files[i] != char:
                thisFile += files[i]
                i+=1
            self.grabFile(thisFile)
            thisFile = ""
            files = files[i:]
            if (len(files) <= 1):
                return

    def parseWrd(self, word, char1):
        parsedWord = ""
        for i in range(0, len(word)):
            if (word[i] != char1):
                parsedWord += word[i]
                i += 1
        return (parsedWord)

