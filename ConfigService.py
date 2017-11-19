#Pick Credentials
def fetchAccessToken() :
    credentialsFile = open('resources/credentials.properties', 'r')
    credential = credentialsFile.readlines()[0]
    return credential.split("=")[1]