#!/usr/bin/env bash
# Genera un .zip por skill en dist/ para subir en claude.ai → Settings → Capabilities → Skills.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/dist"
cd "$ROOT/skills"
for s in */; do
  s="${s%/}"
  rm -f "$ROOT/dist/$s.zip"
  zip -qr "$ROOT/dist/$s.zip" "$s"
  echo "✓ dist/$s.zip"
done
