import React from "react";
import {
  AbsoluteFill,
  OffthreadVideo,
  Sequence,
  staticFile,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import * as icons from "simple-icons";

/* ---------- design tokens ---------- */
const CORAL = "#D97757"; // Claude
const INK = "#FFFFFF";
const FONT = '800 1em "Segoe UI", system-ui, Roboto, Helvetica, Arial, sans-serif';
const W = 720;

const findPath = (slug: string) => {
  const all = Object.values(icons).filter((i: any) => i && i.path && i.slug);
  return (all.find((i: any) => i.slug === slug) as any)?.path as string | undefined;
};
const NOTION = findPath("notion")!;
const CLAUDE = findPath("claude")!;

const Icon: React.FC<{ d: string; fill: string; size: number }> = ({ d, fill, size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    <path d={d} fill={fill} />
  </svg>
);

/* ---------- persistent: progress bar ---------- */
const Progress: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const pct = interpolate(frame, [0, durationInFrames - 1], [0, 100], {
    extrapolateRight: "clamp",
  });
  return (
    <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 7, background: "rgba(255,255,255,0.14)" }}>
      <div style={{ height: "100%", width: `${pct}%`, background: CORAL }} />
    </div>
  );
};

/* soft gradient so top text stays legible over the bright video */
const TopScrim: React.FC = () => (
  <div
    style={{
      position: "absolute",
      top: 0,
      left: 0,
      right: 0,
      height: 300,
      background: "linear-gradient(180deg, rgba(0,0,0,0.62) 0%, rgba(0,0,0,0) 100%)",
    }}
  />
);

/* ---------- 0–5s intro title ---------- */
const Intro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame, fps, config: { damping: 14, mass: 0.7 } });
  const y = interpolate(s, [0, 1], [-70, 0]);
  const out = interpolate(frame, [110, 140], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", top: 78, left: 40, right: 40, transform: `translateY(${y}px)`, opacity: out }}>
      <div style={{ font: FONT, fontWeight: 800, fontSize: 20, letterSpacing: 4, color: CORAL }}>NOTION + IA</div>
      <div style={{ font: FONT, fontWeight: 800, fontSize: 52, lineHeight: 1.02, color: INK, marginTop: 8, textShadow: "0 2px 14px rgba(0,0,0,.5)" }}>
        El sistema que uso
      </div>
      <div style={{ height: 6, width: interpolate(s, [0, 1], [0, 150]), background: CORAL, borderRadius: 3, marginTop: 14 }} />
    </div>
  );
};

/* ---------- 6–16s: my stack (Notion + Claude) ---------- */
const StackChip: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inn = spring({ frame, fps, config: { damping: 16 } });
  const out = interpolate(frame, [270, 300], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const chip = (delay: number, node: React.ReactNode, label: string) => {
    const p = spring({ frame: frame - delay, fps, config: { damping: 12, mass: 0.6 } });
    return (
      <div style={{ display: "flex", alignItems: "center", gap: 12, background: "rgba(20,20,26,0.92)", border: "1px solid rgba(255,255,255,0.12)", borderRadius: 16, padding: "14px 20px", transform: `scale(${interpolate(p, [0, 1], [0.4, 1])})`, opacity: p }}>
        {node}
        <span style={{ font: FONT, fontWeight: 700, fontSize: 30, color: INK }}>{label}</span>
      </div>
    );
  };
  return (
    <div style={{ position: "absolute", top: 92, left: 0, right: 0, display: "flex", flexDirection: "column", alignItems: "center", gap: 16, opacity: Math.min(inn, out) }}>
      <div style={{ font: FONT, fontWeight: 800, fontSize: 18, letterSpacing: 5, color: CORAL }}>MI STACK</div>
      <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
        {chip(0, <Icon d={NOTION} fill={INK} size={34} />, "Notion")}
        <span style={{ font: FONT, fontWeight: 800, fontSize: 34, color: CORAL, opacity: interpolate(spring({ frame: frame - 8, fps }), [0, 1], [0, 1]) }}>+</span>
        {chip(16, <Icon d={CLAUDE} fill={CORAL} size={34} />, "Claude")}
      </div>
    </div>
  );
};

/* ---------- keyword pop callouts ---------- */
const Keyword: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const p = spring({ frame, fps, config: { damping: 10, mass: 0.5 } });
  const scale = interpolate(p, [0, 1], [0.3, 1]);
  const rot = interpolate(p, [0, 1], [-6, -3]);
  const out = interpolate(frame, [130, 155], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", top: 120, left: 0, right: 0, display: "flex", justifyContent: "center", opacity: out }}>
      <div style={{ transform: `scale(${scale}) rotate(${rot}deg)`, background: CORAL, color: "#1a1206", font: FONT, fontWeight: 800, fontSize: 46, letterSpacing: 1, padding: "10px 26px", borderRadius: 14, boxShadow: "0 10px 30px rgba(0,0,0,.45)" }}>
        {text}
      </div>
    </div>
  );
};

/* ---------- 30s–end: CTA ---------- */
const CTA: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const rise = spring({ frame, fps, config: { damping: 15, mass: 0.8 } });
  const y = interpolate(rise, [0, 1], [260, 0]);
  const pulse = 1 + 0.05 * Math.sin((frame / fps) * 6);
  const bounce = Math.abs(Math.sin((frame / fps) * 4)) * 14;
  return (
    <>
      <div style={{ position: "absolute", left: 0, right: 0, bottom: 0, height: 420, background: "linear-gradient(0deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0) 100%)" }} />
      {/* bouncing chevron pointing to the comment box */}
      <svg width={54} height={54} viewBox="0 0 24 24" style={{ position: "absolute", left: W / 2 - 27, bottom: 250 + 14 - bounce, opacity: rise }}>
        <path d="M12 16.5 4.5 9l1.4-1.4L12 13.7l6.1-6.1L19.5 9z" fill={CORAL} />
      </svg>
      <div style={{ position: "absolute", left: 36, right: 36, bottom: 70, transform: `translateY(${y}px)`, background: "rgba(15,15,20,0.94)", border: `2px solid ${CORAL}`, borderRadius: 22, padding: "26px 28px", boxShadow: "0 20px 50px rgba(0,0,0,.5)" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 12, flexWrap: "wrap" }}>
          <span style={{ font: FONT, fontWeight: 800, fontSize: 40, color: INK }}>Comenta</span>
          <span style={{ display: "inline-block", transform: `scale(${pulse})`, background: CORAL, color: "#1a1206", font: FONT, fontWeight: 800, fontSize: 40, padding: "4px 18px", borderRadius: 12 }}>
            DIAGRAMA
          </span>
        </div>
        <div style={{ font: FONT, fontWeight: 600, fontSize: 30, color: "rgba(255,255,255,0.82)", marginTop: 10 }}>
          y te mando cómo construirlo
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginTop: 18 }}>
          <Icon d={NOTION} fill={INK} size={26} />
          <Icon d={CLAUDE} fill={CORAL} size={26} />
          <span style={{ font: FONT, fontWeight: 700, fontSize: 20, letterSpacing: 3, color: "rgba(255,255,255,0.6)" }}>SISTEMA CON IA</span>
        </div>
      </div>
    </>
  );
};

/* ---------- composition ---------- */
export const Reel: React.FC = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <OffthreadVideo src={staticFile("source.mp4")} />

      <TopScrim />
      <Progress />

      <Sequence from={8} durationInFrames={140}>
        <Intro />
      </Sequence>

      <Sequence from={190} durationInFrames={310}>
        <StackChip />
      </Sequence>

      {/* "proyecto y ..." beat (~17.5s) */}
      <Sequence from={520} durationInFrames={160}>
        <Keyword text="PROYECTOS" />
      </Sequence>

      {/* "tareas," beat (~24s) */}
      <Sequence from={700} durationInFrames={160}>
        <Keyword text="TAREAS" />
      </Sequence>

      <Sequence from={900}>
        <CTA />
      </Sequence>
    </AbsoluteFill>
  );
};
