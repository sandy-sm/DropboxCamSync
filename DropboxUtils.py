import dropbox
import re

class DropboxUtils:
    dropbox_client = None

    def __init__(self, access_token):
        self.dropbox_client = dropbox.Dropbox(access_token)
        print "Initialized Dropbox Client"

    # Upload file to dropbox
    def uploadFile(self, file_path):
        print 'Uploading file.. {}'.format(file_path)
        file_name = re.sub(r'.*/', r'/', file_path)
        print "File..{}".format(file_name)
        file_object = open(file_path)
        response = self.dropbox_client.files_upload(file_object.read(), file_name,
                                                    mode=dropbox.files.WriteMode('overwrite'))
        file_object.close()
        print "File Uploaded!"

    def deleteFile(self, file_name):
        file_name = re.sub(r'.*/', r'/', file_name)
        print "Deleting File {}".format(file_name)
        self.dropbox_client.files_delete(file_name)
        print "File Deleted!!"