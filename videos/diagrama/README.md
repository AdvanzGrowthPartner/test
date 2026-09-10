# diagrama — annotated reel (content-motion-studio example)

Overlays animated with Remotion on top of a source vertical reel (720x1280, 30fps),
preserving the original audio. Motion layers: top progress bar, intro title,
"Notion + Claude" stack chip, keyword pops synced to the script (PROYECTOS / TAREAS),
and an end CTA card ("Comenta DIAGRAMA").

## Reproduce
1. Drop the source clip at `public/source.mp4` (git-ignored — it's a heavy input asset).
2. Render:
   bash ../../.claude/skills/content-motion-studio/scripts/render-video.sh \
     src/index.ts Reel out/diagrama_animado.mp4 --public-dir=public
Edit `src/Reel.tsx` to retime/restyle the overlays.
