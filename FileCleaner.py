import DropboxUtils
import ConfigService
import os
from sys import argv

#accessToken = ConfigService.fetchAccessToken()
#print "Fetched AccessToken {}".format(accessToken)
#dropboxUtils = DropboxUtils.DropboxUtils(accessToken)
#dropboxUtils.deleteFile(argv[1])


class FileCleaner:
    def deleteFile(self, filePath):
        if os.path.exists(filePath):
            os.remove(filePath)
