import os
import json
import requests
import sys

# Disclaimer: GitHub’s API has rate limiting, so don’t flood it with requests.
# Warning: Token is stored in plaintext in token.json. Be Careful.

def load_github_token():
    if os.path.exists('token.json'):
        with open('token.json', 'r') as file:
            data = json.load(file)
            return data.get('GITHUB_TOKEN')
    
    token = input("Enter your GitHub personal access token: ")
    with open('token.json', 'w') as file:
        json.dump({'GITHUB_TOKEN': token}, file)
    
    return token

def download_file(url, dest_folder, token):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers, stream=True)

    if response.status_code == 200:
        filename = os.path.join(dest_folder, url.split('/')[-1])
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

def download_folder(repo_url, folder_path, token):
    api_url = f"https://api.github.com/repos/{repo_url}/contents/{folder_path}"
    headers = {'Authorization': f'token {token}'}

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        contents = response.json()
        for item in contents:
            if item['type'] == 'file':
                download_file(item['download_url'], folder_path, token)
            elif item['type'] == 'dir':
                download_folder(repo_url, os.path.join(folder_path, item['name']), token)
    else:
        print(f"Failed to access {api_url}: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 download_github_folder.py <repo_owner/repo_name> <folder_path>")
        sys.exit(1)

    repo = sys.argv[1]
    folder = sys.argv[2]

    token = load_github_token()
    download_folder(repo, folder, token)
