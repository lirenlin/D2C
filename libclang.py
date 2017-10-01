#!/usr/bin/env python

import sys
import clang.cindex
import collections

Loc = collections.namedtuple('Loc','start end')

def find_context (file, node, loc):
  if not node.displayname:
    return None
  if node.location.file != file:
    return None

  # clang.cindex.CursorKind.TRANSLATION_UNIT:
  print node.displayname, node.extent.start.line, \
      node.extent.end.line

  if node.extent.start.line <= loc.start \
      and node.extent.end.line >= loc.end:
      for c in node.get_children():
        res = find_context (file, c, loc)
        if res:
          return res;
      return node
  else:
    return None;

def list_context (file, node, loc):
  # clang.cindex.CursorKind.TRANSLATION_UNIT:
  print node.displayname, node.extent.start.line, \
      node.extent.end.line

  for c in node.get_children():
    list_context (file, c, loc)

index = clang.cindex.Index.create()
tu = index.parse(sys.argv[1])
loc = Loc (int (sys.argv[2]), int (sys.argv[3]))
#node = find_context (tu.cursor, loc)
#print node.displayname
list_context (sys.argv[1], tu.cursor, loc)
#extent = clang.cindex.SourceRange (loc.start, loc.end)
#node = tu.get_tokens (extent)
#print node.displayname
