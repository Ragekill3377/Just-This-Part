# Just-This-Part
GitHub doesn’t have an inbuilt option to get specific folders/directories from within a repository. So, you can use this tool to download specific directories from GitHub!


# Steps:
install python3 & python-pip
then:
```bash
pip3 install requests
```
# Usage:
then you can use the script as:
example: repo is **https://github.com/xybp888/iOS-SDKs**
we want a folder from it at: **https://github.com/xybp888/iOS-SDKs/tree/master/iPhoneOS18.0.sdk**
the folder is *iPhoneOS18.0.sdk*
our command will be:
```bash
python3 download_github_folder.py xybp888/iOS-SDKs iPhoneOS18.0.sdk
```


# Disclaimer:
1. Github's API has rate limiting. Don't flood the requests.
2. your token is stored in a plain text .json. Be careful with it.
