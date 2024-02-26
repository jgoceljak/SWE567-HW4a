import json
import requests
import re

def getRepos():

    print("Enter a Github user ID:\n")
    user = input()
    while not re.match(r'^[A-Za-z0-9-]+$', user):
        print("Invalid Github user ID")
        user = input()
    
    repo_response = requests.get(f"https://api.github.com/users/{user}/repos")

    # Check if the request was successful (status code 200)
    if repo_response.status_code == 200:
        # Parse the JSON response
        repos = repo_response.json()

        # Print the names of the repositories and the number of commits for each
        for repo in repos:
            repo_name = repo['name']
            
            # Make a GET request to the GitHub API to retrieve commits for the repository
            commits_response = requests.get(f"https://api.github.com/repos/{user}/{repo_name}/commits")
            
            # Check if the request for commits was successful (status code 200)
            if commits_response.status_code == 200:
                commits = commits_response.json()
                num_commits = len(commits)
                print(f"Repository: {repo_name}, Number of Commits: {num_commits}")
            else:
                print(f"Failed to retrieve commits for {repo_name}. Status code: {commits_response.status_code}")
    else:
        print(f"Failed to retrieve repositories. Status code: {repo_response.status_code}")
            




getRepos()
 