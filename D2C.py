#!/usr/bin/env python

import sys
import os.path
import collections
import clang.cindex
from unidiff import PatchSet

Loc = collections.namedtuple('Loc','start end')

def findContext (node, loc):
  if not node.displayname:
    return None;

  if node.extent.start.offset <= loc.start \
      and node.extent.end.offset >= loc.end:
      for c in node.get_children():
        res = findContext (c, loc)
        if res:
          return res;
      return node
  else:
    return None;

def clangFind (fileName, locList):
  index = clang.cindex.Index.create()
  tu = index.parse(fileName)
  headList = list ()
  for loc in locList:
    node = findContext (tu.cursor, loc)
    headList.append (node.displayname)

  return headList
#import git
#repo = git.Repo (repo_path)

class CLEntry (object):
  def __init__ (self, fileName, changes):
    self.fileName = fileName
    self.changes = changes

  def __init__ (self, fileName):
    self.fileName = fileName
    self.changes = list ()

  def setChanges (self, changes):
    self.changes = changes

  def genEntry (self):
    string = " " * 8 + "* " + self.fileName

    change = self.changes[0]
    if change is "New":
      string += ": New.\n"
      return string
    elif change is"Remove":
      string += ": Remove.\n"
      return string
    else:
      string += " (%s): \n" % change

    for change in self.changes[1:]:
      string += " " * 8 + "(%s): " % change

    return string


def scanDiff (repo, diffFile):
  if not os.path.isfile (diff_file):
    print "%s is not found" % (diff_file)
    exit ()

  try:
    patch = PatchSet.from_filename (diff_file, encoding='utf-8')
  except:
    print "invlid diff file"
    exit ()

  string = ""
  for patchedFile in patch:
    fileName = patchedFile.path

    entry = CLEntry (fileName)
    if patchedFile.is_added_file:
      entry.setChanges (["New"])
    elif patchedFile.is_removed_file:
      entry.setChanges (["Remove"])
    else:
      if fileName.split ('.')[-1] not in ["c", "cpp", "c++", "h", "hpp"]:
        sectionList = list ()
        for hunk in patchedFile:
          sectionList.append (hunk.section_header)
        entry.setChanges (sectionList)
      else:
        locList = list ()
        for hunk in patchedFile:
          start = hunk.source_start
          end = start + hunk.source_length
          loc = Loc(start, end)
          locList.append (loc)
        sectionList = clangFind (repo + fileName, locList)
        entry.setChanges (sectionList)

    string += entry.genEntry ()
  print string

repo_path = '/home/renlin/Documents/gcc/'
diff_file = 'tmp.diff'
patch = None

scanDiff (repo_path, diff_file)
