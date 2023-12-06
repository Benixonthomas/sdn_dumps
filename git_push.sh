

#!/bin/bash

# Set the path to your local Git repository

echo "Pushing the files to GIT"

local_repo_path="/home/student/git_repo/sdn_dumps/dumps"

# Set the name of the file you want to push

#file_to_push="dumps.txt"
 

# Navigate to the local repository

#cd "$local_repo_path" || exit

# Add the file to the staging area

git add .
#git add ryu*.log

# Commit the changes

git commit -m "Adding the files"

# Push the changes to the remote repository

git push -u origin
