#!/usr/bin/env node

import { execSync } from "node:child_process";
import {
  existsSync,
  mkdirSync,
  readFileSync,
  renameSync,
  rmSync,
  writeFileSync,
} from "node:fs";
import path from "node:path";

const DEFAULT_TARGETS = [
  "docs/ELECTRICAL_AC_BOM.md",
  "docs/ELECTRICAL_fuse_schedule.md",
  "docs/ELECTRICAL_overview_diagram.md",
  "docs/SYSTEMS.md",
  "docs/PROJECT.md",
];

const MERMAID_BLOCK_REGEX = /```mermaid[^\n]*\r?\n([\s\S]*?)```/g;
function runNpx(args) {
  const cmd = `npx ${args.map(quoteArg).join(" ")}`;
  execSync(cmd, { stdio: "inherit" });
}

function quoteArg(value) {
  if (process.platform === "win32") {
    if (value.length === 0) {
      return '""';
    }
    const escaped = value.replace(/"/g, '\\"');
    return /[\s"]/u.test(escaped) ? `"${escaped}"` : escaped;
  }

  return `'${value.replace(/'/g, "'\\''")}'`;
}

function toPosixPath(value) {
  return value.split(path.sep).join("/");
}

function main() {
  const repoRoot = process.cwd();
  const targets = process.argv.length > 2 ? process.argv.slice(2) : DEFAULT_TARGETS;
  const outputRoot = path.join(repoRoot, "docs", "pdf_exports");
  const assetsRoot = path.join(outputRoot, "assets");
  const tempRoot = path.join(outputRoot, "_tmp");

  mkdirSync(outputRoot, { recursive: true });
  mkdirSync(assetsRoot, { recursive: true });
  mkdirSync(tempRoot, { recursive: true });

  const summaries = [];

  for (const relPath of targets) {
    const absPath = path.resolve(repoRoot, relPath);
    if (!existsSync(absPath)) {
      throw new Error(`Target markdown file not found: ${relPath}`);
    }

    const baseName = path.basename(relPath, ".md");
    const assetDir = path.join(assetsRoot, baseName);
    mkdirSync(assetDir, { recursive: true });

    const source = readFileSync(absPath, "utf8");
    let diagramCount = 0;

    const transformed = source.replace(MERMAID_BLOCK_REGEX, (_, blockText) => {
      diagramCount += 1;
      const idx = String(diagramCount).padStart(2, "0");
      const mmdPath = path.join(assetDir, `diagram-${idx}.mmd`);
      const svgPath = path.join(assetDir, `diagram-${idx}.svg`);
      const pdfPath = path.join(assetDir, `diagram-${idx}.pdf`);

      writeFileSync(mmdPath, `${String(blockText).trim()}\n`, "utf8");
      runNpx(["--yes", "@mermaid-js/mermaid-cli", "-i", mmdPath, "-o", svgPath]);
      runNpx(["--yes", "@mermaid-js/mermaid-cli", "-i", mmdPath, "-o", pdfPath]);

      const relSvg = toPosixPath(path.join("..", "assets", baseName, `diagram-${idx}.svg`));
      return `![${baseName} diagram ${idx}](${relSvg})`;
    });

    const tempMarkdownPath = path.join(tempRoot, `${baseName}.md`);
    writeFileSync(tempMarkdownPath, transformed, "utf8");

    runNpx([
      "--yes",
      "md-to-pdf",
      tempMarkdownPath,
      "--basedir",
      repoRoot,
      "--pdf-options",
      '{"format":"Letter","printBackground":true}',
    ]);

    const generatedPdfPath = tempMarkdownPath.replace(/\.md$/i, ".pdf");
    const finalPdfPath = path.join(outputRoot, `${baseName}.pdf`);
    rmSync(finalPdfPath, { force: true });
    renameSync(generatedPdfPath, finalPdfPath);

    summaries.push({
      markdown: relPath,
      pdf: toPosixPath(path.relative(repoRoot, finalPdfPath)),
      diagrams: diagramCount,
      diagramDir: toPosixPath(path.relative(repoRoot, assetDir)),
    });
  }

  rmSync(tempRoot, { recursive: true, force: true });

  console.log("\nExport complete:\n");
  for (const item of summaries) {
    console.log(`- ${item.markdown} -> ${item.pdf}`);
    console.log(`  diagrams exported: ${item.diagrams} (${item.diagramDir})`);
  }
}

main();
