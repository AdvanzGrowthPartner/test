import React from "react";
import { Composition } from "remotion";
import { Reel } from "./Reel";

// Source: 720x1280, 30fps, 36.75s  ->  1102 frames.
export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Reel"
      component={Reel}
      durationInFrames={1102}
      fps={30}
      width={720}
      height={1280}
    />
  );
};
