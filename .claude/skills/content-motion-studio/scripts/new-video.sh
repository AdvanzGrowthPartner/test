#!/usr/bin/env bash
# Scaffold a Remotion video project under videos/<name>/.
# Reuses the repo-root node_modules (remotion, react, simple-icons) — no extra install.
#
# Usage: bash new-video.sh <name> ["Optional Title"]
set -euo pipefail

NAME="${1:-}"
TITLE="${2:-Advanz}"
if [[ -z "$NAME" ]]; then
  echo "Usage: bash new-video.sh <name> [\"Title\"]" >&2
  exit 1
fi

# Resolve repo root (two levels up from .claude/skills/content-motion-studio/scripts)
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
DIR="$ROOT/videos/$NAME"
if [[ -e "$DIR" ]]; then
  echo "videos/$NAME already exists — pick another name." >&2
  exit 1
fi
mkdir -p "$DIR/src" "$DIR/out"

cat > "$DIR/src/index.ts" <<'EOF'
import { registerRoot } from "remotion";
import { RemotionRoot } from "./Root";
registerRoot(RemotionRoot);
EOF

cat > "$DIR/src/Root.tsx" <<EOF
import React from "react";
import { Composition } from "remotion";
import { Scene } from "./Scene";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Main"
      component={Scene}
      durationInFrames={150}
      fps={30}
      width={1080}
      height={1920}
      defaultProps={{
        title: "$TITLE",
        subtitle: "Growth para ecommerce DTC",
        iconSlug: "shopify",
        bg: "#0B0B0F",
        accent: "#7AB55C",
      }}
    />
  );
};
EOF

cat > "$DIR/src/Scene.tsx" <<'EOF'
import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import * as icons from "simple-icons";

export type SceneProps = {
  title: string;
  subtitle: string;
  iconSlug: string;
  bg: string;
  accent: string;
};

const findIcon = (slug: string) => {
  const all = Object.values(icons).filter((i: any) => i && i.path && i.slug);
  return (
    (all.find((i: any) => i.slug === slug) as any) ||
    (all.find((i: any) => i.title.toLowerCase() === slug.toLowerCase()) as any)
  );
};

export const Scene: React.FC<SceneProps> = ({
  title,
  subtitle,
  iconSlug,
  bg,
  accent,
}) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const icon = findIcon(iconSlug);

  // Spring entrance for the icon.
  const pop = spring({ frame, fps, config: { damping: 12, mass: 0.6 } });
  const iconScale = interpolate(pop, [0, 1], [0.2, 1]);
  const iconRot = interpolate(pop, [0, 1], [-25, 0]);

  // Title slides up + fades in slightly after the icon.
  const tIn = interpolate(frame, [15, 40], [0, 1], { extrapolateRight: "clamp" });
  const titleY = interpolate(tIn, [0, 1], [60, 0]);

  const sIn = interpolate(frame, [30, 55], [0, 1], { extrapolateRight: "clamp" });

  // Accent bar wipe.
  const barW = interpolate(frame, [40, 70], [0, 220], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor: bg, fontFamily: "Inter, system-ui, sans-serif" }}>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", gap: 48, padding: 80 }}>
        {icon && (
          <svg
            width={width * 0.32}
            height={width * 0.32}
            viewBox="0 0 24 24"
            style={{ transform: `scale(${iconScale}) rotate(${iconRot}deg)` }}
          >
            <path d={icon.path} fill={accent} />
          </svg>
        )}
        <div
          style={{
            transform: `translateY(${titleY}px)`,
            opacity: tIn,
            color: "#fff",
            fontSize: 96,
            fontWeight: 800,
            textAlign: "center",
            letterSpacing: -2,
            lineHeight: 1.02,
          }}
        >
          {title}
        </div>
        <div style={{ height: 8, width: barW, backgroundColor: accent, borderRadius: 4 }} />
        <div style={{ opacity: sIn, color: "#9aa0aa", fontSize: 40, textAlign: "center", fontWeight: 500 }}>
          {subtitle}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
EOF

cat > "$DIR/README.md" <<EOF
# $NAME (Remotion video)

Preview live:   npx remotion studio videos/$NAME/src/index.ts
Render MP4:     bash .claude/skills/content-motion-studio/scripts/render-video.sh videos/$NAME/src/index.ts Main
Render GIF:     bash .claude/skills/content-motion-studio/scripts/render-video.sh videos/$NAME/src/index.ts Main --gif

Edit src/Scene.tsx to change the animation. Props (title/subtitle/iconSlug/bg/accent)
live in src/Root.tsx defaultProps — or pass --props '{"title":"..."}' when rendering.
EOF

echo "Scaffolded videos/$NAME"
echo "  Studio:  npx remotion studio videos/$NAME/src/index.ts"
echo "  Render:  bash .claude/skills/content-motion-studio/scripts/render-video.sh videos/$NAME/src/index.ts Main"
