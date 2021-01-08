import requests
from pprint import pprint

# github username
username = "navyad"
# url to request repositories of Github
url = f"https://api.github.com/users/{username}/repos?per_page=1000&type=owner"
# make the request and return the json
repo_data = requests.get(url).json()
user_data = f"https://api.github.com/users/{username}"


# 1st Question
# pprint(repo_data)

def reposOfUser():
    repos_list = []
    for r in range(0, len(repo_data)):
        repo = repo_data[r]
        keys = ('name', 'private', 'description',
                'size', 'language', 'stargazers_count')
        repo_data_modified = {k: repo[k] for k in keys}
        repos_list.append(repo_data_modified)
    return repos_list


print('No. of repositories: ', requests.get(user_data).json()['public_repos'])

# 2nd Question
repos = reposOfUser()


def repoWithMaxStars(repos):

    lst = []
    for i in range(len(repos)):
        lst.append(repos[i])
    return (max(lst, key=lambda fun: fun['stargazers_count']))


# 3rd Question
url1 = f"https://api.github.com/users/{username}/followers?per_page=1000&type=owner"
# make the request and return the json
user_followers_data = requests.get(url1).json()


def countOfFollowers(user):
    url2 = f"https://api.github.com/users/{user}"
    user_followers_data = requests.get(url2).json()
    return (user_followers_data['followers'])


def followerDetails():
    followers_list = []
    for follower in range(len(user_followers_data)):
        fol = user_followers_data[follower]
        keys = ('login', 'id')
        followers_data_modified = {k: fol[k] for k in keys}
        followers_list.append(followers_data_modified)
    return followers_list


# 4th Question
def highestFollowers():
    countOfFoll = []
    for i in range(len(user_followers_data)):
        countOfFoll.append(followerDetails()[i]['login'])
    follCount_names = {}
    for i in range(len(countOfFoll)):
        follCount_names[countOfFoll[i]] = countOfFollowers(countOfFoll[i])
    a = max(follCount_names, key=follCount_names.get)
    b = max(follCount_names.values())
    return ('{} have {} Followers.'.format(a, b))


# 5th Question
def updateDescription(name_of_repo, content):
    d = list(filter(lambda person: person['name'] == name_of_repo, repos))
    d[0]['description'] = content
    return d


print('{1} has {0} followers.'.format(
    requests.get(user_data).json()['followers'], username))

# 1st Answer
pprint(reposOfUser())

# 2nd Answer
pprint(repoWithMaxStars(repos))

# 3rd Answer
pprint(followerDetails())

# 4th Answer
pprint(highestFollowers())

# 5th Answer
name_of_repo = input('Enter name of Repository to update Description.')
contentOfDescription = input('Enter Description to update.')
pprint(updateDescription(name_of_repo, contentOfDescription))
