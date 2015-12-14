#!/usr/bin/env python

'''
########

PROJ-BOT

########
'''

import shutil
import time
import os, sys

# SETUP VARIABLES
def initProj():
    projStorage =  "/Users/sdavis/Documents/_jira-tasks/"
    #projStorage =  "/Users/sdavis/Desktop/py-playground/email-task/"
    projFolderName = raw_input('\nEnter Name of Project: ')

    # PATH LOCATION & FOLDER CREATION
    projPath = projStorage + (time.strftime("%Y%m%d-")) + projFolderName

    return projPath

# FOLDER STRUCTURE CREATION
def generateProj():

    projPath = initProj()

    # FOLDER LIST
    projFolderList = ['_resources','_working','deliverables']

    print "Your folder has been created at: " + projPath
    os.mkdir( projPath );

    for projFolder in projFolderList:
       os.mkdir( projPath + "/" + projFolder );
       print 'Folder Added: ' + projFolder

    print "------"

    # EMAIL PROJ CREATION FUNCTION
    def makeEmailProj():

        siteAbbrev = raw_input('Site Abbreviation: ').lower()
        
        projWorkingFolderPath = projPath + "/_working/"
        projResourcesFolderPath = projPath + "/_resources/"

        templateWorkingFolderPath = "/Users/sdavis/Documents/repositories/2015-responsive-email-templates/_working/"
        templateEmailPath = "/Users/sdavis/Documents/repositories/2015-responsive-email-templates/_working/" + siteAbbrev + "-email-template/"
        templateResourcePath = "/Users/sdavis/Documents/repositories/2015-responsive-email-templates/_working/_featured-banners"

        # COPY FILES & FOLDERS FROM EMAIL TEMPLATE DIRECTORY
        for root, dirs, files in os.walk(templateEmailPath, topdown=False):
            # COPY EMAIL SHELL FILE
            for name in files:
                if name == siteAbbrev + "-email-template-shell.html":
                    templateShellFilePath = os.path.join(root, name)
                    shutil.copy (templateShellFilePath, projWorkingFolderPath + name)
            # COPY IMAGES FOLDER
            for name in dirs:
                if name == "images":
                    templateImagesFilePath = os.path.join(root, name)
                    shutil.copytree (templateImagesFilePath, projWorkingFolderPath + name)
        
        # COPY SNIPPETS TO RESOURCES?
        addSnippets = raw_input('Add _snippets folder to _resources? y/n: ').lower()

        if addSnippets == "y":
            # COPY SNIPPETS FROM EMAIL TEMPLATE DIRECTORY
            for root, dirs, files in os.walk(templateWorkingFolderPath, topdown=False):
                # COPY SNIPPETS FOLDER
                for name in dirs:
                    if name == "_snippets":
                        templateSnippetsPath = os.path.join(root, name)
                        shutil.copytree (templateSnippetsPath, projResourcesFolderPath + name)

        # COPY PSDS TO RESOURCES?
        addPSDTemplate = raw_input('Add PSD templates to _resources? y/n: ').lower()

        if addPSDTemplate == "y":
            # COPY PSD FROM BANNERS DIRECTORY
            for root, dirs, files in os.walk(templateResourcePath, topdown=False):
                for name in files:
                    if name == "featured-banner-template.psd" or name == "skinny-banner-template.psd":
                        templateBannerPath = os.path.join(root, name)
                        shutil.copy (templateBannerPath, projPath + "/_resources/")

    # ADD EMAIL TEMPLATES
    addEmailTemplate = raw_input('Add email templates? y/n: ').lower()
    if addEmailTemplate == "y":
        makeEmailProj()

    # ADD ANOTHER PROJECT?
    addAnotherProj = raw_input('Add another project? y/n: ').lower()
    while addAnotherProj == "y":
        print "------"
        generateProj()
        addAnotherProj = ""

generateProj()

print "\n>>>>>>>>>>>>>>>>>>>>>>>>>>\n<<<<<<<<<<<<<<<<<<<<<<<<<<\n\nPROJECT CREATION COMPLETE!\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<\n>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
