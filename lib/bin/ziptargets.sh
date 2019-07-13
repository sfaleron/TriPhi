#!/bin/sh

WORKTREE=$(git worktree list --porcelain 2>/dev/null)

if [ $? -eq 0 ]; then
  cd `echo $WORKTREE|head -1|cut -d " " -f 2`
  find . \( -name "*.mml" -and -not -name "*.in.mml" \) -or -name "*.svg" | \
    grep -v glyph|zip -FS -@ lib/targets
else
  echo "Failed!"
fi
