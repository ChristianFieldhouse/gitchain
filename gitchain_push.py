import urllib.request, time
import git

repo = git.Repo()
number = 0
file_to_alter = "mine.txt"
signature = input("signature (hex) > ")


while number < 10000:
    with open(file_to_alter, "w") as f:
        f.write(str(number))
        number += 1
    repo.index.add(file_to_alter)
    repo.index.commit("mining, try " + str(number))
    #print(repo.head.object.hexsha)
    if repo.head.object.hexsha.startswith(signature):
        break
    repo.branches[0].reference = repo.commit("master^")

repo.remotes.origin.push()
print("sucessfully changed the hash")