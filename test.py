#!/usr/bin/env python

import clang.cindex, asciitree, sys

index = clang.cindex.Index.create()
translation_unit = index.parse(sys.argv[1], ['-x', 'c++'])

print asciitree.draw_tree(translation_unit.cursor,
  lambda n: n.get_children(),
  lambda n: "%s (%s)" % (n.spelling or n.displayname, str(n.kind).split(".")[1]))

