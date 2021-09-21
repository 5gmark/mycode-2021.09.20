#!/usr/bin/env python3

'''
   Date: September 21, 2021
    rom: Mark Mollere, mmollere@alta3.com
Subject: push_it.py
     To: You

push_it.py is a simple process to knock out a "git push" to GitHub. This code is
imperfect. The intent is for you to gaze upon the building blocks and engage in
critcal thinking for the next iteration...
'''
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import os

commit_message    = input('Commit Comment: ')
working_directory = 'cd ~/mycode'
git_add           = 'git add *'
git_commit        = 'git commit -m "' + commit_message + '"'
git_push          = 'git push origin main'

os.system(working_directory)
os.system(git_add)
os.system(git_commit)
os.system(git_push)
