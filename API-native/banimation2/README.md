# DJZ-Onion-Layers

A desktop application for composing, aligning, and exporting PNG frame sequences for hand-drawn or digitally-painted animation. Includes AI-powered background removal and a paint-to-restore brush for fixing removal artifacts. All processing happens locally — no files are ever uploaded to a server.

## What It Does

DJZ-Onion-Layers lets animators load a batch of image frames, position and scale each one inside a uniform square canvas, and use **onion skin overlay** to compare frames against their neighbors — the classic technique borrowed from traditional cel animation.

When finished, export all adjusted frames as RGBA PNG files packed into a single ZIP archive with custom sequential naming.

## Installation

1. Go to the [Releases](https://github.com/MushroomFleet/djz-onion-layers-web-dev/releases) page
2. Download the latest installer for your platform:
   - **`DJZ-Onion-Layers_x.x.x_x64_en-US.msi`** — MSI installer (recommended for Windows)
   - **`DJZ-Onion-Layers_x.x.x_x64-setup.exe`** — NSIS installer (alternative)
3. Run the installer and follow the prompts
4. Launch **DJZ-Onion-Layers** from your Start Menu or desktop

The MODNet background removal model is bundled inside the application — no additional downloads required.

## Features

### Core Tools
- **Batch Image Load** — Drag-and-drop or file picker for PNG, JPG, and WebP files (up to 200 frames), auto-sorted by filename
- **Spritesheet Import** — Load a spritesheet image by specifying rows and columns; cells are sliced left-to-right, top-to-bottom and loaded as individual frames in animation order
- **Square Canvas Container** — Configurable export resolution from 64px to 4096px (default 512px)
- **Per-Frame Transforms** — X/Y offset sliders with nudge buttons, and scale percentage for each frame independently
- **Transform Presets** — Save per-frame transform settings (X, Y, Scale, Fit Mode) as named presets stored locally in IndexedDB; apply a saved preset to new frame sequences for consistent alignment across batches
- **ZIP Export** — All frames exported as RGBA PNGs with custom prefix naming (`walk_001.png`, `walk_002.png`, ...)

### Onion Skin Modes
- **Single-Frame Onion Skin** — Shows the previous frame behind the current frame at adjustable opacity (10%-90%)
- **Multi-Frame Onion Skin** — Shows the previous frame tinted blue and the next frame tinted red using hue blending, both at adjustable opacity

### Background Removal
- **MODNet Background Removal** — One-click batch background removal powered by MODNet via ONNX Runtime Web (WebAssembly), producing transparent RGBA output per frame

### Hole Fix (Mask Painting)
- **Paint-to-Restore Brush** — After background removal, paint directly on the canvas to restore original image pixels where the AI cut too aggressively (hair, fingers, translucent details)
- **Brush Controls** — Adjustable brush size (1-100px), Hard or Soft edge, Paint or Erase mode
- **Per-Frame Masks** — Each frame stores its own restoration mask independently; masks persist when switching between frames
- **Mask Undo/Redo** — Ctrl+Z / Ctrl+Y undo and redo individual brush strokes while Hole Fix mode is active
- **Non-Destructive** — The original image and BG-removed result are preserved; only the mask layer controls which original pixels show through
- **Export-Ready** — Exported PNGs automatically include the mask-restored regions

### Animation Workflow
- **Frame Timeline Strip** — Horizontal scrollable thumbnail strip showing all frames with status badges
- **Drag-to-Reorder** — Drag thumbnails in the timeline to re-sequence frames
- **Frame Duplication** — Right-click any thumbnail for x2 or x3 frame interpolation (duplicates every frame in sequence)
- **Fit Modes** — Three transform modes per frame: Contain (default), Cover (fill + crop), Free (native pixel size)
- **Playback Preview** — Play/Pause button cycles through frames at configurable FPS (1-30)
- **Undo/Redo** — Full undo/redo stack (Ctrl+Z / Ctrl+Y) for all transform and fit mode changes

## How To Use

### Basic Frame Alignment

1. Click **Load Frames** or drag image files onto the drop zone
2. Set your desired **Container** size (e.g. 1024px)
3. Click a frame in the timeline strip to select it
4. Enable **Onion Skin** to see the previous frame behind the current one
5. Adjust **X Offset**, **Y Offset**, and **Scale** to align frames
6. Step through all frames, adjusting alignment as needed
7. Enter an **Export prefix** (e.g. `walk`) and click **Export ZIP**

### Loading a Spritesheet

1. Click **Load Spritesheet** in the toolbar
2. Enter the number of **Rows** and **Columns** in the popup
3. Click **Select File** and choose your spritesheet image
4. The spritesheet is automatically sliced into individual frames (left-to-right, top-to-bottom) and loaded into the timeline

### Using Transform Presets

When processing multiple batches of sprites that need the same alignment adjustments:

1. Load a frame sequence and adjust all transforms as needed
2. In the **Transform** panel, click **Save** under Presets
3. Enter a name for the preset (e.g. `walk-cycle-offsets`)
4. Later, load a new frame sequence and select the preset from the dropdown
5. Click **Apply** to apply the saved transforms to the new frames
6. If the preset has a different frame count than the loaded sequence, transforms are applied to matching positions and a warning is shown
7. Click **Del** to remove a preset you no longer need

### Background Removal

1. Load your frames
2. Click **Remove BG (MODNet)** — a progress bar shows each frame being processed
3. Thumbnails update to show transparent backgrounds on a checker pattern
4. Align and export as usual — exported PNGs will have transparent backgrounds

### Hole Fix (Restoring Lost Details)

After background removal, some frames may have "holes" — areas where the subject (hair edges, fingers, semi-transparent clothing) was accidentally removed. The Hole Fix tool lets you paint those details back in:

1. Run **Remove BG** on your frames first
2. Select a frame that has a hole you want to fix
3. The **Hole Fix** toolbar row appears with a status message: *"Ready — click Hole Fix to paint restoration mask"*
4. Click **Hole Fix: OFF** to activate paint mode — it becomes **Hole Fix: ON** and the brush toolbar appears
5. A dashed cyan circle follows your cursor over the canvas — this is your brush preview
6. **Click and drag** over the area where details were lost — the original image pixels are painted back through the transparent regions
7. Use the brush toolbar to adjust:
   - **Size slider** (1-100px) — controls brush diameter
   - **Hard / Soft** — hard gives a clean circle edge, soft gives a feathered gradient
   - **Paint / Erase** — paint restores original pixels, erase removes your restoration
   - **Clear Mask** — resets all painting on the current frame (asks for confirmation)
8. Press **Ctrl+Z** to undo a brush stroke, **Ctrl+Y** to redo (while Hole Fix is active)
9. Click **Hole Fix: ON** again to exit paint mode — your restoration is preserved
10. Frames with a mask show a **"Masked"** badge in the timeline strip
11. **Export ZIP** — the exported PNGs include your restored regions automatically

### Frame Reordering and Duplication

- **Reorder:** Drag any thumbnail in the timeline strip to a new position
- **Duplicate:** Right-click a thumbnail and select **Duplicate x2** or **Duplicate x3** to interpolate the entire sequence
- **Remove:** Right-click and select **Remove Frame**, or click the X on error frames

### Playback Preview

1. Set your desired **FPS** (1-30, default 12)
2. Click **Play** to cycle through frames in the canvas
3. The timeline strip auto-scrolls to follow the active frame
4. Click **Pause** to stop on the current frame

### Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `Ctrl+Z` | Undo (brush stroke when Hole Fix active, otherwise transform change) |
| `Ctrl+Y` / `Ctrl+Shift+Z` | Redo (brush stroke when Hole Fix active, otherwise transform change) |
| `Escape` | Close help modal or context menu |

---

## Citation

### Academic Citation

If you use this codebase in your research or project, please cite:

```bibtex
@software{djz_onion_layers,
  title = {DJZ-Onion-Layers: Client-Side Frame Sequence Alignment and Animation Tool},
  author = {Drift Johnson},
  year = {2025},
  url = {https://github.com/MushroomFleet/djz-onion-layers-web-dev},
  version = {1.0.0}
}
```

### Donate:

[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)
