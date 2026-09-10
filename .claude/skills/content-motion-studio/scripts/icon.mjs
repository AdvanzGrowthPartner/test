#!/usr/bin/env node
// Simple Icons helper — resolve a brand icon by slug/name and emit an SVG.
//
// Usage:
//   node icon.mjs <slug|name> [--color <hex|brand|currentColor>] [--size <px>] [-o out.svg]
//   node icon.mjs --search <query>          # list matching icons (slug — title — #hex)
//
// Examples:
//   node icon.mjs shopify                   # brand-colored Shopify glyph -> stdout
//   node icon.mjs "google ads" --size 64 -o ads.svg
//   node icon.mjs meta --color currentColor # inherit CSS color (for buttons/nav)
//   node icon.mjs --search whats            # find the right slug
//
// The emitted SVG has viewBox="0 0 24 24". `--color brand` (default) uses the
// official brand hex; `currentColor` makes it inherit the surrounding text color.

import * as icons from "simple-icons";
import { writeFileSync } from "node:fs";

const ALL = Object.values(icons).filter((i) => i && i.path && i.slug);
const argv = process.argv.slice(2);

function opt(name, short) {
  const i = argv.findIndex((a) => a === name || (short && a === short));
  if (i === -1) return undefined;
  return argv[i + 1];
}
const norm = (s) => String(s).toLowerCase().replace(/[^a-z0-9]/g, "");

const searchQ = opt("--search");
if (searchQ) {
  const q = norm(searchQ);
  const hits = ALL.filter((i) => norm(i.title).includes(q) || i.slug.includes(q)).slice(0, 40);
  if (!hits.length) {
    console.error(`No icons match "${searchQ}".`);
    process.exit(1);
  }
  for (const i of hits) console.log(`${i.slug}\t${i.title}\t#${i.hex}`);
  process.exit(0);
}

const query = argv.find((a) => !a.startsWith("-") && argv[argv.indexOf(a) - 1] !== "--color" && argv[argv.indexOf(a) - 1] !== "--size" && argv[argv.indexOf(a) - 1] !== "-o");
if (!query) {
  console.error("Missing icon slug/name. Try: node icon.mjs --search <query>");
  process.exit(1);
}

const q = norm(query);
const icon =
  ALL.find((i) => i.slug === query) ||
  ALL.find((i) => norm(i.title) === q) ||
  ALL.find((i) => i.slug === q) ||
  ALL.find((i) => norm(i.title).includes(q) || i.slug.includes(q));

if (!icon) {
  console.error(`Icon "${query}" not found. Try: node icon.mjs --search ${query}`);
  process.exit(1);
}

const size = opt("--size") || "24";
let color = opt("--color") || "brand";
if (color === "brand") color = `#${icon.hex}`;

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 24 24" fill="${color}" role="img" aria-label="${icon.title}"><title>${icon.title}</title><path d="${icon.path}"/></svg>`;

const out = opt("-o", "--out");
if (out) {
  writeFileSync(out, svg + "\n");
  console.error(`Wrote ${icon.title} (#${icon.hex}) -> ${out}`);
} else {
  process.stdout.write(svg + "\n");
}
