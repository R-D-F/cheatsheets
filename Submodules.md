Git Submodules 

GitHub submodules are also beneficial in terms of adhering to the "Don't Repeat Yourself" (DRY) software principle. By utilizing submodules, developers can avoid duplicating code across multiple projects or repositories. Instead of copying and pasting code from one project to another, they can simply include the shared codebase as a submodule, ensuring that any updates or improvements made to the submodule are automatically reflected across all projects using it. This promotes code reusability and reduces the risk of inconsistencies that may arise from maintaining similar code in multiple places. As a result, submodules contribute to a more efficient and organized development process, as developers can focus on improving the shared codebase once rather than updating it in multiple locations, enhancing collaboration, and code maintenance. 

The [geo_utils](https://github.com/QuantumSpatialInc/geo_utils/) repository is a good place to start when implementing a submodule workflow. It contains functions for Kibana logging, data type conversions, and other handy steps that can be utilized across multiple projects. 

Setting Up a Submodule 

Start by navigating to your project directory. This is the place where your repository is cloned. 

To add a submodule, use the command: git submodule add <repository-url>. This creates a new file called .gitmodules which tracks your submodules configurations. It also clones the submodule repository into your project. 

Commit and push the .gitmodules file and the cloned submodule repository to your main repository: git commit -m "Added a new submodule" and then git push. 

Updating a Submodule 

Navigate to the submodule directory and pull in the changes from the original repository: cd <submodule_directory> and git pull origin master. 

Navigate back to the main project and commit these changes: git commit -am "Updated submodule" , and git push. 

Cloning a Repository with Submodules 

Use git clone --recurse-submodules <repository-url> to clone the repository and all its submodules. 

If you've already cloned a project and then want to load its submodules, use git submodule update --init --recursive. 

Updating Files after Changes to Main Repo or Submodule Repo 

When files in the main repository are updated, a normal git pull will suffice to get the updates. But, if the submodules are updated, the procedure is different: 

Pull changes in the main repository: git pull. 

Update the submodules: git submodule update --remote --merge. 

The --remote option makes sure you're updating to the latest commit in the submodule's remote repository. The --merge option prevents the submodule to enter into a 'detached HEAD' state. 

Finally, commit and push the changes: git commit -am "Updated submodules" and git push. 

Potential Gotchas and Issues 

Submodule Detached HEAD: The most common issue is a submodule stuck in a 'detached HEAD' state. This means the submodule isn't tracking its own latest commit, and is instead at a specific commit. Always remember to checkout to a branch (usually master) after pulling changes in the submodule: git checkout master. 

Forget to Init and Update: When you clone a repository which includes submodules, but forget the --recurse-submodules option, then the submodule directories will be there, but will be empty. You will need to run git submodule update --init --recursive to pull the data. 

Out of Sync Submodules: Submodules don't automatically stay in sync with the main repo. If you want the latest version of your submodule's code, you must manually go into each submodule and pull the latest changes.