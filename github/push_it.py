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
  comment1     = ""
  options      = "c:hmsv"
  long_options = ["comment","help","man-page","symbolic-link","version"]
  version      = '1.6'
  try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
      if currentArgument in ("-c", "--comment"):
        comment1 = currentValue
        print(comment1)
      elif currentArgument in ("-h", "--help"):
        print ("WIP: Help me...")
      elif currentArgument in ("-m", "--man-page"):
        print ("WIP: Install " + os.path.basename(sys.argv[0]) + " man page.")
      elif currentArgument in ("-s", "--symbolic-link"):
        print ("WIP: Symbolic link...")
      elif currentArgument in ("-v", "--version"):
        print (os.path.basename(sys.argv[0]), version)
  except:
    pass

  if len(sys.argv) == 1 or comment1:
    print(bool(comment1))
    if bool(comment1):
      commit_message    = comment1
    else:
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
