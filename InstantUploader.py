import DropboxUtils
import ConfigService
import FileCleaner
from sys import argv

#Fetch AccessToken
accessToken = ConfigService.fetchAccessToken()
print "Fetched AccessToken {}".format(accessToken)

#Initialize Dropbox Client
dropboxUtils = DropboxUtils.DropboxUtils(accessToken)

#Upload File
dropboxUtils.uploadFile(argv[1])

#delete file from file-system
fileCleaner = FileCleaner.FileCleaner()
fileCleaner.deleteFile(argv[1])
