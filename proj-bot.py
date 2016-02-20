#!/usr/bin/env python

'''
########

PROJ-BOT

########
'''

import shutil
import time
import os, sys
import urllib

# NULL > STRING
def initProj():
    projStorage =  "/Users/sdavis/Documents/_jira-tasks/"
    projFolderName = raw_input('\nProject Name: ')

    # PATH LOCATION & FOLDER CREATION
    projPath = projStorage + (time.strftime("%Y%m%d-")) + projFolderName
    return projPath

# STRING, STRING > NULL
def genericDownloader(urlToDownload, projLocation):
    print ("-"*40)
    fileName = urlToDownload.split("/")[-1]
    print ("Downloading \"" + fileName + "\"...")
    urllib.urlretrieve(urlToDownload, projLocation + fileName)
    print ("Successfully Downloaded: " + fileName)
    print ("-"*40)

# STRING, STRING > NULL
def svnDownloader(urlToDownload, projLocation):
    fileName = urlToDownload.split("/")[-1]
    print ("-"*40)
    print ("SVN Downloading \"" + fileName + "\"...")
    os.system("svn export " + urlToDownload + " " + projLocation)
    print ("SVN Successfully Downloaded: " + fileName)
    print ("-"*40)

# STRING > STRING
def renameFile(oldName, newName):
    os.rename(oldName, newName)

# STRING > RETURN NULL
def addEmailAssets(emailDestination):

    siteAbbrev = raw_input('Site Abbreviation? ').lower()   
    emailDestinationString = str(emailDestination)

    # PROJECT
    projWorkingFolderPath = emailDestinationString + "/_working/"
    projResourcesFolderPath = emailDestinationString + "/_resources/"

    # ACCESS URLLIB OPENER
    theOpener = urllib.URLopener()

    # VARIABLES FOR GITHUB
    gitEmailParentDirectory = "https://github.com/livingdirectcreative/2015-responsive-email-templates/trunk/_working/" + siteAbbrev + "-email-template"
    gitEmailImagesPath = gitEmailParentDirectory + "/images"
    gitEmailShellPath = "https://raw.githubusercontent.com/livingdirectcreative/2015-responsive-email-templates/master/_working/" + siteAbbrev + "-email-template/" + siteAbbrev + "-email-template-shell.html"
    
    # PROJECT VARIABLES
    projDirName = gitEmailParentDirectory.split("/")[-1]
    projImageDirName = gitEmailImagesPath.split("/")[-1]

    # DESTINATION VARIABLES 
    projTemplateDestination = projWorkingFolderPath + "/" + projDirName
    projTemplateImageDestination = projWorkingFolderPath + "/" + projImageDirName
    projEmailShellDestination = projWorkingFolderPath

    # DOWNLOAD SHELL
    genericDownloader(gitEmailShellPath, projEmailShellDestination)
    
    # DOWNLOAD IMAGES
    svnDownloader(gitEmailImagesPath, projTemplateImageDestination)
    
    # RENAME FILE VARIABLES
    intermediateProjFolderName = os.path.dirname(projWorkingFolderPath)
    targetFileName = projWorkingFolderPath + siteAbbrev + "-email-template-shell.html"
    renameEmailToProjName = intermediateProjFolderName.split("/")[-2] + ".html"
    
    # CALL RENAME FUNCTION
    renameFile(targetFileName, projWorkingFolderPath + renameEmailToProjName)
    print ("Renamed Email:"), renameEmailToProjName
    
    # COPY SNIPPETS TO RESOURCES?
    addSnippets = raw_input('Snippets? y/n: ').lower()

    if addSnippets == "y":
        # SNIPPET VARIABLES
        fileToDownload = "https://github.com/livingdirectcreative/2015-responsive-email-templates/trunk/_working/_snippets"
        parsedFileName = fileToDownload.split("/")[-1]
        fileDestination = projResourcesFolderPath + parsedFileName
        
        # DOWNLOAD SNIPPETS VIA SVN
        svnDownloader(fileToDownload, fileDestination)

    # COPY PSDS TO RESOURCES?
    addEmailPsdTemplate = raw_input('Banner PSD? y/n: ').lower()

    # PSDS TO DOWNLOAD
    emailBannerCollection = [
                             "https://github.com/livingdirectcreative/psd-templates/raw/master/email/featured-banner-template.psd",
                             "https://github.com/livingdirectcreative/psd-templates/raw/master/email/skinny-banner-template.psd"
                            ]

    if addEmailPsdTemplate == "y":
        for emailPsdUrl in emailBannerCollection:
            # DOWNLOAD PSDS USING THE GENERIC DOWNLOADER
            genericDownloader(emailPsdUrl, projResourcesFolderPath)

# NULL > NULL
def generateProj():
    
    # INITIALIZE PROJECT 
    projPath = initProj()
    print "PROJECT PATH: ", projPath

    # FOLDER LIST
    projFolderList = ['_resources','_working','deliverables']

    # CREATE PROJECT FOLDER
    print "Your folder has been created at: " + projPath
    os.mkdir( projPath );

    for projFolder in projFolderList:
       os.mkdir( projPath + "/" + projFolder );
       print 'Folder Added: ' + projFolder

    print "------"
    
    # ADD EMAIL TEMPLATES
    addEmailTemplate = raw_input('Add email templates? y/n: ').lower()
    if addEmailTemplate == "y":
        # ADD EMAIL ASSETS
        addEmailAssets(projPath)

    # ADD ANOTHER PROJECT?
    addAnotherProj = raw_input('Add another project? y/n: ').lower()
    while addAnotherProj == "y":
        print "------"
        # CREATE NEW PROJECT
        generateProj()
        # RESET TO CONTINUE LOOP
        addAnotherProj = ""

generateProj()

print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>\n<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nPROJECT CREATION COMPLETE!\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<\n>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
