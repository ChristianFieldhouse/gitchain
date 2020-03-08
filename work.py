import urllib.request, time
import git

repo = git.Repo()
number = 0

while number < 1000:
    with open("mine.txt", "w") as f:
        f.write(str(number))
        number += 1
    repo.index.add("mine.txt")
    repo.index.commit("mining, try " + str(number))
    print(repo.head.object.hexsha)
    if repo.head.object.hexsha.startswith("cf"):
        break
    repo.branches[0].reference = repo.commit("master^")

repo.remotes.origin.push()
print("sucessfully changed the hash")