GIT has ability to tag specific points in a repository's history as being important. We can do this by creating tags in git.
1 =>
To get the list of the presrrent tags we use the command |git tag|.And this will list all the present tags in alphabetical orders.

HOW TO CREATE TAGS?
In eneral there are two type of tags lightweight and annotated. But we will use annotated tags as it contains many information like tagger name,email,date and also contains a tagging message.

git tag -a v1.4 -m"My version 1.4"

This will create a new annotated tag, if we want to know the innformation of above tag then we have to do

git show tag_name
in this case tag name is v1.4

---

\$ git show change1
tag change1
Tagger: Prakhar <prakhars156@gmail.com>
Date: Fri Apr 10 22:35:56 2020 +0530

Restarting git

commit f0248847a1c1a463d7a841dedb0b7f841b938718 (HEAD -> master, tag: change1, origin/master, origin/HEAD)
Author: Prakhar <prakhars156@gmail.com>
Date: Fri Apr 10 20:46:36 2020 +0530

    updating notes

diff --git a/README.md b/README.md
index 58366f4..a1c38d5 100644
--- a/README.md
+++ b/README.md
@@ -220,4 +220,45 @@ We created a .css file in our workspace and then put all our css styles into tha

---

We can also tag later into our commit history
for that we have to do |git tag -a <tagname> commit_id|

One last thing, git push doesn't push the tags to the remote repository we have to explicitly push tags after we have created them by using command |git push origin <tagname>|
