# D2C

python unidiff: parse the diff file to get a structured representation of the
change.

for PatchedFile in PatchSet:
  for Hunk in PatchedFile:
    for Line in Hunk:
      if Line.is_context:
        continue


python libclang: extract source code syntax information about the change from
the change hunk.
