#!/usr/bin/env bash
# Render a Remotion composition to MP4 (or GIF) using the pre-installed Chromium.
#
# Usage:
#   bash render-video.sh <entry> <composition-id> [output] [--gif] [--props '<json>'] [extra remotion flags]
#
# Examples:
#   bash render-video.sh videos/promo/src/index.ts Main
#   bash render-video.sh videos/promo/src/index.ts Main videos/promo/out/promo.mp4
#   bash render-video.sh videos/promo/src/index.ts Main --gif
#   bash render-video.sh videos/promo/src/index.ts Main --props '{"title":"Nuevo lanzamiento"}'
set -euo pipefail

ENTRY="${1:-}"
COMP="${2:-}"
if [[ -z "$ENTRY" || -z "$COMP" ]]; then
  echo "Usage: bash render-video.sh <entry> <composition-id> [output] [--gif] [--props '<json>']" >&2
  exit 1
fi
shift 2

# Detect the pre-installed Chromium (Playwright bundle) so Remotion never downloads one.
CHROME=""
for c in /opt/pw-browsers/chromium-*/chrome-linux/chrome; do
  [[ -x "$c" ]] && CHROME="$c" && break
done

GIF=0
OUTPUT=""
EXTRA=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --gif) GIF=1; shift ;;
    -*) EXTRA+=("$1"); shift ;;
    *) if [[ -z "$OUTPUT" ]]; then OUTPUT="$1"; else EXTRA+=("$1"); fi; shift ;;
  esac
done

if [[ -z "$OUTPUT" ]]; then
  base="$(dirname "$(dirname "$ENTRY")")/out/${COMP}"
  [[ "$GIF" -eq 1 ]] && OUTPUT="${base}.gif" || OUTPUT="${base}.mp4"
fi
mkdir -p "$(dirname "$OUTPUT")"

ARGS=("$ENTRY" "$COMP" "$OUTPUT")
[[ "$GIF" -eq 1 ]] && ARGS+=(--codec=gif)
[[ -n "$CHROME" ]] && ARGS+=("--browser-executable=$CHROME")
# Chrome runs as root inside the container — disable the sandbox.
ARGS+=(--chrome-mode=chrome-for-testing)
ARGS+=("${EXTRA[@]}")

echo "Rendering $COMP -> $OUTPUT"
[[ -n "$CHROME" ]] && echo "Using Chromium: $CHROME" || echo "No pre-installed Chromium found; Remotion will fetch one."
REMOTION_CHROME_EXECUTABLE="${CHROME:-}" npx remotion render "${ARGS[@]}"
echo "Done: $OUTPUT"
