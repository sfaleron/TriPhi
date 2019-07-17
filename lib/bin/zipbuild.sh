#!/bin/sh

WORKTREE=$(git worktree list --porcelain 2>/dev/null)

if [ $? -eq 0 ]; then
  cd `echo $WORKTREE|head -1|cut -d " " -f 2`; cd lib
  find . \( -name "*.mml" -and -not -name "*.in.mml" \) -or -name "*.svg" | \
     grep -v glyph | grep -v node_modules |  zip -FS -@ build
else
  echo "Failed!"
fi
