import os

# Windows: 

dld = [
    {
        "Name": "Windows - Edge 80 stable",
        "Url": "https://www.google.com",
        "S3path": "http://s3.amazonaws.com/bs-platform/windows/browsers/edge/81.0.410.1_edge_installer.exe"
    }
]

def download_using_wget(dct):
    print "==> Downloading using WGET"
    print dct["Url"]
    os.system("wget "+dct["Url"]+" -O ~/supragya/wget_temp/wgetdownload")

def s3cmd_upload(dct):
    print "==> Uploading to s3 using s3cmd"
    print dct["S3path"]

def s3cmd_ls(dct):
    print "==> s3cmd LS"

if __name__ == "__main__":
    print "=> GET BROWSERS"
    for b in dld:
        print "-------------------------------------------------------------"
        print b["Name"]
        choice = input("Type 1 to proceed: ")
        if choice != 1:
            print "Ending"
            exit()
        print "==> Step 1"
        download_using_wget(b)
        print "==> Step 2"
        s3cmd_upload(b)
        print "==> Step 3"
        s3cmd_ls(b)
        print "-------------------------------------------------------------"

