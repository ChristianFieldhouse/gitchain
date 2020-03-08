import urllib.request, time
import git

repo = git.Repo()
number = 0

while number < 10:
    with open("mine.txt", "w") as f:
        f.write(str(number))
        number += 1
    repo.index.add("mine.txt")
    repo.index.commit("testing " + str(number))
    print(repo.head.object.hexsha)
    repo.head.reference = repo.commit("master^")
    repo.head.reset(index=True, working_tree=True)

#repo.index.commit("commit altered to make a nicer hash")
#repo.remotes.origin.push()
#print("sucessfully changed the hash")