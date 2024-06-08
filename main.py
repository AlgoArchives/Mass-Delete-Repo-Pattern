import requests

# Replace with your GitHub personal access token and organization name
GITHUB_TOKEN = 'your-token'
ORG_NAME = 'your-org-username'

def delete_repo(repo_name):
    url = f'https://api.github.com/repos/{ORG_NAME}/{repo_name}'
    response = requests.delete(url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    
    if response.status_code == 204:
        print(f'Successfully deleted repository: {repo_name}')
    else:
        print(f'Failed to delete repository: {repo_name}. Status code: {response.status_code}')
        print(response.json())

def list_repos():
    url = f'https://api.github.com/orgs/{ORG_NAME}/repos'
    response = requests.get(url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to retrieve repositories. Status code: {response.status_code}')
        return []

def main():
    repos = list_repos()
    matching_repos = [repo['name'] for repo in repos if repo['name'].startswith('wireshark-introduction-')]
    
    print(f'Number of repositories to be deleted: {len(matching_repos)}')
    print('Repositories:')
    for repo_name in matching_repos:
        print(repo_name)
    
    # Uncomment the lines below to enable deletion
    # for repo_name in matching_repos:
    #     delete_repo(repo_name)

if __name__ == '__main__':
    main()