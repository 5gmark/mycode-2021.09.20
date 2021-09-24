#!/usr/bin/env python3

'''
   Date: September 21, 2021
   From: Mark Mollere, mmollere@alta3.com
Subject: push_it.py
     To: You

push_it.py is a simple process to knock out a "git push" to GitHub. This code is
imperfect. The intent is for you to gaze upon the building blocks and engage in
critcal thinking for the next iteration...
'''
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import getopt
import os
import sys

def main():
  argumentList = sys.argv[1:]
  options      = "v"
  long_options = ["version"]
  version      = '1.5'
  try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
      if currentArgument in ("-v", "--version"):
        print (os.path.basename(sys.argv[0]), version)
  except:
    pass

  if len(sys.argv) == 1:
    commit_message    = input('Commit Comment: ')
    working_directory = '/home/student/mycode'
    git_add           = 'git add *'
    git_commit        = 'git commit -m "' + commit_message + '"'
    git_push          = 'git push origin'

    os.chdir(working_directory)
    os.system(git_add)
    os.system(git_commit)
    os.system(git_push)

if __name__ == "__main__":
    main()
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
