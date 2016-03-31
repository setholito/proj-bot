#!/usr/bin/env python

'''
##############

PROJ-BOT 1.0.1

##############
'''

from easygui import *
import os
import shutil
import sys
import time
import urllib

# LIST VARIABLES =========================================

# Individual Files
psdUrlList = [
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/featured-banner-template.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/featured-banner-content.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/featured-banner-sale.psd",
            "https://github.com/livingdirectcreative/psd-templates/raw/master/email/skinny-banner-template.psd"
            ]

# Directories
assetsUrlList = []

# CREATE PROJECT =========================================

# Null > String
def initProj():
    # Project hub
    projStorage =  "/Users/sdavis/Documents/_jira-tasks/"
    
    # Easygui text box
    dateString = time.strftime("%Y%m%d-")
    projFolderName = enterbox("Enter Name of Project", "Proj-Bot: Name Your Project", dateString)
    print ("PROJECT NAME: " + projFolderName)

    # Path location & folder creation
    fullProjPath = projStorage + projFolderName

    return fullProjPath

# CREATE DIRECTORIES =====================================

# Null > Null
def createDirectories(dirPath):
    # Folder list
    projFolderList = ['_resources','_working','deliverables']

    # Create project folder
    print "Your folder has been created at: " + dirPath
    os.mkdir( dirPath );

    # Loop through folder list
    for projFolder in projFolderList:
       os.mkdir( dirPath + "/" + projFolder );
       print 'Folder Added: ' + projFolder
    print ("-" * 40)

# DOWNLOAD FILES =========================================

<<<<<<< HEAD
# String, String > Null
def genericDownloader(src, dst):
    fileName = src.split("/")[-1]
    print ("Downloading \"" + fileName + "\"...")
    urllib.urlretrieve(src, dst + fileName)
=======
# STRING, STRING > NULL
def genericDownloader(urlToDownload, projLocation):
    print ("-"*40)
    fileName = urlToDownload.split("/")[-1]
    print ("Downloading \"" + fileName + "\"...")
    urllib.urlretrieve(urlToDownload, projLocation + fileName)
>>>>>>> 162e70a997335a384851c8b113c8d2c79ad2e887
    print ("Successfully Downloaded: " + fileName)
    print ("-" * 40)

<<<<<<< HEAD
# String, String > Null
def svnDownloader(src, dst):
    fileName = src.split("/")[-1]
    print ("SVN Downloading \"" + fileName + "\"...")
    os.system("SVN export " + src + " " + dst)
=======
# STRING, STRING > NULL
def svnDownloader(urlToDownload, projLocation):
    fileName = urlToDownload.split("/")[-1]
    print ("-"*40)
    print ("SVN Downloading \"" + fileName + "\"...")
    os.system("svn export " + urlToDownload + " " + projLocation)
>>>>>>> 162e70a997335a384851c8b113c8d2c79ad2e887
    print ("SVN Successfully Downloaded: " + fileName)
    print ("-" * 40)

def downloadFiles(dList, dst):
    # Easygui multichoice box
    dialogTitle = "Proj Bot: File Picker"
    dialogMsg = "Choose one or multiple files. Go for it!"

    # List of modified/pretty file names
    displayChoices = []

    # Int used to number files
    itemNum = 1

    # Loop through URLs in download list
    for url in dList:
        # Make it pretty
        displayChoices.append(url.split("/")[-1])
        itemNum += 1

    # List of selected files
    selectedFiles = multchoicebox(dialogMsg, dialogTitle, displayChoices)
    print ("Selected Files: " + str(selectedFiles))

    # Loop through list of selected files 
    # Download'em using the genericDownloader function
    for sFile in selectedFiles:
        sIndex = displayChoices.index(sFile)
        genericDownloader(dList[sIndex], dst)

# RENAMER =========================================

# String, String > String
def renameFile(oName, nName):
    os.rename(oName, nName)

# GENERATE PROJECT =========================================

# Null > Null
def generateProj():
    # Initialize project 
    projPath = initProj()
    print "PROJECT PATH: ", projPath

    # Create list of directories
    createDirectories(projPath)

    # Download files
    resourcePath = projPath + "/_resources/"

    # Pass in list of selected files to download
    # Add to desired location
    downloadFiles(psdUrlList, resourcePath)

    # Returns True or False
    addAnotherProj = ynbox("Add another project?", "Proj Bot: Another Project")
    while addAnotherProj == True:
        print ("==== ### ADDING NEW PROJECT ### ====")
        # Run generateProj function again
        generateProj()
        # Reset addAnotherProj
        addAnotherProj = ""

generateProj()

print ("<<< DONE! >>>")
