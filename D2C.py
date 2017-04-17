#!/usr/bin/env python

from unidiff import PatchSet
import os.path
#import git

repo_path = ''
diff_file = 'tmp.diff'
patch = None
#repo = git.Repo (repo_path)

if not os.path.isfile (diff_file):
    print "%s is not found" % (diff_file)
    exit ()

try:
    patch = PatchSet.from_filename (diff_file, encoding='utf-8')
except:
    print "invlid diff file"
    exit ()

for patched_file in patch:
    src_name = patched_file.source_file
    dst_name = patched_file.target_file

    for hunk in patched_file:
        org = hunk.source

