#!/usr/bin/env bash
# Copia todas las skills a ~/.claude/skills (Claude Code, uso personal).
# Uso: ./scripts/install.sh            -> instala todas
#      ./scripts/install.sh ecomm-meta-ads ecomm-google-ads  -> solo esas
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$DEST"
if [ "$#" -gt 0 ]; then SKILLS=("$@"); else SKILLS=($(ls "$ROOT/skills")); fi
for s in "${SKILLS[@]}"; do
  [ -f "$ROOT/skills/$s/SKILL.md" ] || { echo "No existe: $s" >&2; exit 1; }
  rm -rf "$DEST/$s" && cp -r "$ROOT/skills/$s" "$DEST/$s"
  echo "✓ $s"
done
echo "Instaladas en $DEST"
