# Readme

This is a project, that provides an example of the usage of github and bash.

## Requirements

- First, install  [git](https://git-scm.com/downloads) for your operating system. After the installation there is a new program called **Git Bash** available on your Windows machine. This is a basics command line interface, that works like a unix shell. If You are working on Linux or Mac, Your terminal is already a unix shell. You still have to install git.
- Second, install python on Your operating system. You can check which version on Python is installed yet by typing  ```Python -V``` in Your command line. If no Python is installed, install python 3.10 via the Windows Store or the Python [website](https://www.python.org/).

## Usage

- Clone the [git repository](https://github.com/jhumci/test_git_shell) on Your machine
    - in git bash, navigate to the folder You want to download the repository to
    - enter ```git clone https://github.com/jhumci/test_git_shell.git```
    - now, You have a copy of the repository on Your machine
    - use the windows explorer to make sure that this worked

## Tasks

- 🤓 create Your own branch using ```git branch <your_branch_name>```
- execute the file ```hello_world.py``` by entering ```python hello_world.py```. Make sure, that You are in the right directory or enter the relative file path 
- Create the file ```primes.txt``` in the subfolder data
    - navigate to the data subfolder ```cd data```
    - create a new file ```touch primes.txt```
- Try running the Python-Skript ```make_primes.py```
- Fix the problems within the Python code using the vi editor (🤓) or any other text editor on Your PC
    - You can open the editor using ```vi make_primes.py```
    - use the following [vi-commands](https://www.guru99.com/the-vi-editor.html) to edit the file
    - replace ```for n in range (x,y):``` by a reasonable range You want to find the prime number in
- Try running the Python-Skript ```make_primes.py``` again
- Check Your results in 
Show the results in ```primes.txt``` using vi
- 🤓 commit the changes to Your branch using ```git commit -m <your_commit_comment>```
