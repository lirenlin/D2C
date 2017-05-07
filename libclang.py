#!/usr/bin/env python

import sys
import clang.cindex

def find_typerefs(node, typename, loc):
    if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
      print node.displayname
      print node.extent
      if node.extent.start.line <= loc and node.extent.end.line >= loc:
        print "in this function"
    else:
      for c in node.get_children():
          find_typerefs(c, typename, loc)

index = clang.cindex.Index.create()
tu = index.parse(sys.argv[1])
find_typerefs(tu.cursor, sys.argv[2], 13)
