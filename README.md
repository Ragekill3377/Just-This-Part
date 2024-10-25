# Just-This-Part
GitHub doesn’t have an inbuilt option to get specific folders/directories from within a repository. So, you can use this tool to download specific directories from GitHub!
# Prequisites:
1. github token
2. python and pip

# How To Get Github Token:
	1.	Log in to GitHub:
Go to GitHub and log in to your account.
	2.	Navigate to Settings:
Click on your profile picture in the upper-right corner of the page, then select “Settings” from the dropdown menu.
	3.	Go to Developer settings:
In the left sidebar, scroll down and click on “Developer settings.”
	4.	Access Personal Access Tokens:
Under the “Developer settings” menu, click on “Personal access tokens.” Then, select “Tokens (classic).”
	5.	Generate a New Token:
	•	Click on the “Generate new token” button.
	•	You will be prompted to provide a note to describe what this token is for (e.g., “Script for downloading GitHub folders”).
	•	Choose an expiration date for the token according to your needs. For security reasons, it’s often good practice to set an expiration date.
	•	Select the scopes or permissions you’d like to grant this token. For downloading content from repositories, you’ll generally need to check:
	•	repo (for full control of private repositories, if applicable)
	•	public_repo (for accessing public repositories)
	•	After selecting the appropriate scopes, click “Generate token.”
	6.	Copy the Token:
Once the token is generated, copy it immediately. You will not be able to see it again after you leave the page.


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
