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
  options      = "c:hv"
  long_options = ["comment","help","version"]
  version      = '1.6'
  try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
      if currentArgument in ("-c", "--comment"):
        print (("Git Comment: (% s)") % (currentValue))
#        print (("Comment... (%s)") % (comment1))
      elif currentArgument in ("-h", "--help"):
        print ("Help me...")
      elif currentArgument in ("-v", "--version"):
        print (os.path.basename(sys.argv[0]), version)
  except:
    pass

  if len(sys.argv) == 1 or currentValue:
    print(bool(currentValue))
    if bool(currentValue):
      commit_message    = input('Commit Comment: ')
    else:
      commit_message    = currentValue
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
