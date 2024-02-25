import json
import requests
import re

def getRepos(userID):
    
    repos = requests.get(f"https://api.github.com/users/{userID}/repos")

    if repos.status_code == 200:
        repos = repos.json()

        for repo in repos:
            repo_name = repo['name']
    
            commits_response = requests.get(f"https://api.github.com/repos/{userID}/{repo_name}/commits")
            
            if commits_response.status_code == 200:
                commits = commits_response.json()
                commitsNum = len(commits)
                print(f"Repository: {repo_name} Number of Commits: {commitsNum}")
            else:
                print(f"Failed to retrieve commits for {repo_name}. Status code: {commits_response.status_code}")
    else:
        print(f"Failed to retrieve repositories. Status code: {repos.status_code}")
            


def getUserID():
    print("Enter a Github user ID:\n")
    userID = input()
    while not re.match(r'^[A-Za-z0-9-]+$', userID):
        print("Invalid Github user ID:\n")
        userID = input()

    getRepos(userID)
    

    
    

getUserID()