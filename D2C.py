#!/usr/bin/env python

from unidiff import PatchSet
import git
import os

repo_path = ''
diff_file = '/work/oban-work/src/gcc/gcc/0001-fix-the-type-of-stackadj_tree-it-should-be-an-intege.patch'
#repo = git.Repo (repo_path)
patch = PatchSet.from_filename (diff_file, encoding='utf-8')

for patched_file in patch:
    file_name = patched_file.source_file
    for hunk in patched_file:
        print dir (hunk)
