#!/usr/bin/env python

'''
##############

PROJ-BOT 1.0.2

##############
'''

import os
import shutil
import sys
import time
import urllib

# LIST VARIABLES =========================================

psdUrlList = [
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/featured-banner-template.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/featured-banner-content.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/featured-banner-sale.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/skinny-banner-template.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/mosaic-1.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/mosaic-2.psd"
            ]

# CREATE PROJECT =========================================

# Null > String
def initProj():
    # Project hub
    projStorage =  "/Users/sdavis/Documents/_jira-tasks/"
    
    # Easygui text box
    dateString = time.strftime("%Y%m%d-")
    projFolderName = raw_input("\nWhat would you like to name your project? ")
    print ("\nPROJECT NAME: " + projFolderName)

    # Path location & folder creation
    fullProjPath = projStorage + dateString + projFolderName

    return fullProjPath

# CREATE DIRECTORIES =====================================

# Null > Null
def createDirectories(dirPath):
    # Folder list
    projFolderList = ['_resources','_working','deliverables']

    # Create project folder
    os.mkdir(dirPath);

    print ("-" * 40)
    # Loop through folder list
    for projFolder in projFolderList:
       os.mkdir(dirPath + "/" + projFolder);
       print 'Folder Added: ' + projFolder
    print ("-" * 40)

# DOWNLOAD FILES =========================================

# String, String > Null
def genericDownloader(src, dst):
    fileName = src.split("/")[-1]
    print ("Downloading \"" + fileName + "\"...")
    urllib.urlretrieve(src, dst + fileName)
    print ("Successfully Downloaded \"" + fileName + "\"!")

# String, String > Null
def svnDownloader(src, dst):
    dirName = src.split("/")[-1]
    print ("SVN Downloading \"" + dirName + "\"...")
    os.system("SVN export " + src + " " + dst)
    print ("Successfully Downloaded \"" + dirName + "\"!")

# List, String > Null
def downloadChosenFiles(downloadList, destination):

    # Display choices to the user
    printFileNames(downloadList)

    # String gets turned into a list if response is formatted correctly
    userNumbers = raw_input("Use numbers separated by commas to choose files: ").split(",")

    # List to store URLS
    chosenList = []

    # Loop over the userNumbers list, and append the correlating URL to chosenList
    for idx in userNumbers:
        intIdx = int(idx) -1 
        chosenList.append(downloadList[intIdx])

    # Loop through chosenList and call genericDownloader to pull assets down
    for downloadItem in chosenList:
        genericDownloader(downloadItem, destination)

# RENAMER =========================================

# String, String > String
def renameFile(oName, nName):
    os.rename(oName, nName)

# PRINT NAMES =========================================

def printFileNames(assetList):
    incNum = 1
    for asset in assetList:
        print str(incNum) + ". " + asset.split("/")[-1]
        incNum += 1

# GENERATE PROJECT =========================================

# Null > Null
def generateProj():
    # Initialize project 
    projPath = initProj()
    print "PROJECT PATH: " + projPath

    # Create list of directories
    createDirectories(projPath)

    # Download files
    resourcePath = projPath + "/_resources/"

    # Pass in list of selected files to download
    # Add to desired location
    downloadEmailPSDs = raw_input("Would you like to download some email PSDs? (y/n): ").lower()

    if downloadEmailPSDs == "y":
        downloadChosenFiles(psdUrlList, resourcePath)

    print ("-" * 40)

    # Returns True or False
    addAnotherProj = raw_input("Add another project? (y/n): ").lower()

    while addAnotherProj == "y":
        print ("\n====== NEW PROJECT ======\n")
        # Run generateProj function again
        generateProj()
        # Empty the variable
        addAnotherProj = ""

generateProj()

print ("\n<<< DONE! >>>\n")
