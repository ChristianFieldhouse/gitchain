import urllib.request, time
import git

repo = git.Repo()
number = 0

print(repo.head.object.hexsha)

while number < 1000:
    with open("mine.txt", "w") as f:
        f.write(number)
    repo.index.add("mine.txt")
    print(repo.head.object.hexsha)

repo.index.commit("commit altered to make a nicer hash")
repo.remotes.origin.push()
print("sucessfully changed the hash")