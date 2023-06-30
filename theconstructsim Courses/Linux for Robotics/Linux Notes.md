## Unit 1: Intro to Course
- Linux = important bc ROS runs on Linux OS
### DEMO 1: BASH
- execute command on Linux Shell (allow comm w/ Linux system)
* ./ = execute
* control + C = stop bash script from executing (can now type)

## Unit 2: Linux Essentials
* cd = open file (list file path w/ backslashes)
* python (name of python file) = run python file
* pwd = where am I currently?
* cd ../ = move backwards in folder (out of current one)
* ls = see all contents of folder
* ls -la = see files hidden (have . in front of name, not visible through ls command)
* --help = see all possible commands using first part
* mkdir = make a directory (folder)
* touch = make a file (have to add file type at end)
* vi = view file (and can now make edits)
    * type i to switch to "insert mode" - can start typing
    * escape key = get out into "command mode"
    * :wq = save file and exit (write, quit)
    * :q = quit file
* rosrun <package_name> <executable_file> = run ROS file
    * NB: NEEDS PERMISSION TO RUN PYTHON FILES!
* mv <file/folder we want to move> <destination>
* cp = cp <file/folder we want to copy> <name of the new file/folder>
    * to copy folders + contents, need -r right after cp
    * NB: CAN'T BE IN THE FOLDER YOU ARE TRYING TO COPY!
* rm <file to remove>
## Unit 3: Advanced Utilities I
- Permissions: when have ls -la, see attributes of file
    - r = read (see contents)
    - w = write / modify files 
    - x = execute file or view in directory
- 3 types of permission groups (who can access?):
1. Owner (apply only to owner of file / directory) first 3 char
2. Group (group assigned file directory) middle 3 char
3. ALL users (all users running on system) last 3 char
* chmod  <groups to assign the permissions><permissions to assign/remove> <file/folder names>
    * ex: chmod u+x move_bb8_square.py (adds owner permission to execute)
* u: Owner
* g: Group
* o: Others
* a: All users.
* NB: 777 IS FOR EVEYRONE GETS EVERYTHING!
- Bash script = text file containing series of commands (always start with #!/bin/bash)
- see example in folder
- access argument inside script (just like storing variables otherwise) - $1 (first variable)
- .bashrc file type = execute whenever new shell session initialized
- Environment variables = set when open new shell sessoin
* export = see all environmental variables running
* grep = filter elements (only ones useful for ROS)
## Unit 4: Advanced Concepts II
- Process = program in execution (running instance program)
- 2 types: 
1. Foreground (init, controlled via terminal session - have to be started by user)
2. Background (not connected to terminal)
* htop (aka top): visualize data happening 
* ps: less defined htop
* ps faux | grep test_process = get test_process variables in command window
* control + z = pause process; bg = resume
* kill = kills current tasks
- ssh = secure shell (connect remote machine securely)
* ssh <user>@<host> (host = remote machine, user = account log in from)


* connecting to a robot: 
1. ps faux | grep
2. summon robot from psfaux: sudo /usr/sbin/sshd -p 8090 -D
3. connect via IP: ssh student@127.0.0.1 -p 8090
4. connect password

- dpkg system = linux way of providing programs (no write source code)
- APT = command line tool to interact with packages
* sudo apt-get update = get all packages from database
* sudo = execute programs with privileges of root user 