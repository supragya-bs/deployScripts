import os

```
PATH EXAMPLES:

"http://s3.amazonaws.com/bs-platform/windows/browsers/edge/81.0.410.1_edge_installer.exe"
"http://s3.amazonaws.com/bs-platform/windows/browsers/edge/80.0.361.32_edge_installer.exe"
"http://s3.amazonaws.com/bs-platform/mac/browsers/edge/80.0.361.32_edge_installer.pkg"

```

dld = [
    {
        "Name": "Mac - Edge 82 Dev",
        "Url": "https://officecdn-microsoft-com.akamaized.net/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/MicrosoftEdgeDev-82.0.425.3.pkg?platform=Mac&Consent=1&channel=Dev",
        "S3path": "http://s3.amazonaws.com/bs-platform/mac/browsers/edge/MicrosoftEdgeDev-82.0.425.3.pkg"
    },
    {
        "Name": "Mac - Edge 81 Beta",
        "Url": "https://officecdn-microsoft-com.akamaized.net/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/MicrosoftEdgeBeta-81.0.416.12.pkg?platform=Mac&Consent=1&channel=Beta",
        "S3path": "http://s3.amazonaws.com/bs-platform/mac/browsers/edge/MicrosoftEdgeBeta-81.0.416.12.pkg"
    }
]

def download_using_wget(dct):
    print "==> Downloading using WGET"
    print dct["Url"]
    choice = input("Type 1 to proceed: ")
    if choice != 1:
        print "Ending"
        exit()
    os.system("wget "+dct["Url"]+" -O ~/supragya/wget_temp/wgetdownload")

def s3cmd_upload(dct):
    print "==> Uploading to s3 using s3cmd"
    print "File info:"
    os.system("ls -lh1 ~/supragya/wget_temp/wgetdownload")
    print "Uploading as: "
    print dct["S3path"]
    choice = input("Type 1 to proceed: ")
    if choice != 1:
        print "Ending"
        exit()
    os.system("s3cmd put ~/supragya/wget_temp/wgetdownload "+dct["S3path"])

def s3cmd_ls(dct):
    print "==> s3cmd LS"
    os.system("s3cmd ls "+dct["S3path"])

if __name__ == "__main__":
    print "=> GET BROWSERS"
    for b in dld:
        print "-------------------------------------------------------------"
        print b["Name"]
        print "==> Step 1"
        download_using_wget(b)
        print "==> Step 2"
        s3cmd_upload(b)
        print "==> Step 3"
        s3cmd_ls(b)
        print "-------------------------------------------------------------"

