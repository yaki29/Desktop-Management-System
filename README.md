# Desktop-Management-System
#### Cleans your System in a go and tells you which are the large file that should be removed

Language Used: Python

### Task 1:
Tell the 10 largest files - largest.py
### Task 2:
Move files according to their extensions - arrange.py

### Explanations:
Task1
* Traverse the whole target directory using breadth first search(BFS) on directory tree.
* Store the file names, their sizes and their addresses
* Sort it out and get top 10 entries

Task2
* Traverse the only target directory
* Separate the file extensions from their names and make directories of them.
* Now move the files with extensions as their destination directories.

Testing:
I have tested it on Linux(Ubuntu 16.04), but I think it would work with every operating system.