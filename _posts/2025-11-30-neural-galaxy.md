---
title: 'Neural Galaxy - Your Personalized AI Conversation Visualization'
date: 2025-11-26
permalink: /posts/2025/11/neural-galaxy/
tags:
  - visualization
  - ai
  - react
  - threejs
---

# Neural Galaxy - Your Personalized AI Conversation Visualization

# [Live demo](https://ktwu01.github.io/neural-galaxy/)- Supports all kinds of devices like Mac, Windows, iPhone, Android phone, and Tablets.

[![Neural Galaxy demo](https://raw.githubusercontent.com/ktwu01/neural-galaxy/main/docs/neural-galaxy-demo.gif)](https://ktwu01.github.io/neural-galaxy/)

[![GitHub stars](https://img.shields.io/github/stars/ktwu01/neural-galaxy?style=social)](https://github.com/ktwu01/neural-galaxy/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ktwu01/neural-galaxy?style=social)](https://github.com/ktwu01/neural-galaxy/fork) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/ktwu01/neural-galaxy/issues) ![License](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-informational.svg)

> A hand-controlled 3D visualization of your **AI brand conversation base**. Fly through **ChatGPT** conversations, and explore **artificial intelligence** concepts.

## Highlights

- **Instant Spacewalk** – **Zero deployment needed.** Simply open the [web app](https://ktwu01.github.io/neural-galaxy/) in your browser to explore the built-in sample conversation and experience the bloom-heavy cyberpunk UI immediately.
- **Setup Guide Wizard** – A simple guided flow (shortcut: press `I`) helps you import your own **ChatGPT** history in seconds. **Your data stays 100% local**—processing happens entirely in your browser, ensuring complete privacy.
- **Gesture + Keyboard Modes** – Switch between MediaPipe hand tracking and classic Orbit controls with one toggle; handy HUDs show what the system sees.
- **Floating Utilities** – Single-click buttons provide keyboard help, full-UI screenshots (`S` shortcut with countdown), and direct access to the onboarding wizard.
- **Python Data Builder** – Scripts in `/scripts` extract and preprocess your chats so you can regenerate `galaxy_data.json` offline with consistent colors and spacing.

## Try It in 1 Minute

Just open the browser and visit [https://ktwu01.github.io/neural-galaxy/](https://ktwu01.github.io/neural-galaxy/), Go to the link. you can try it.

## Bring Your Own Conversations

1. Export your chat history (ChatGPT JSON, Claude, Gemini, etc.).
2. In the running app, click the **Import (I)** button or press `I`.
3. Follow the Setup Guide wizard:
   - Learn how to export chats from each platform.
   - Drop your JSON file into the File Import (Upload) step.
   - Click `Import`, that's it.
4. When the success step appears, head back to the galaxy—your data is live, persistent, and ready to explore. Tap `S` for a shareable screenshot overlay (3‑second countdown included).

## Controls & Shortcuts

| Action | Keyboard / Mouse | Gesture Mode |
| --- | --- | --- |
| Toggle gesture mode | `M` or panel switch | Raise/lower hands as usual |
| Focus particle HUD | `K` | Point & pinch |
| Keyboard help | `H` | — |
| Setup/import wizard | `I` | — |
| Screenshot whole UI | `S` (or Screenshot button) | — |
| Close overlays | `ESC` | Palm to neutral |

Additional UI helpers:
- Floating import/help/screenshot buttons sit in the bottom-right corner.
- The minimap lives bottom-left, gesture info in bottom-right, focus HUD top-middle.
- Copyright notice and social links persist for easy sharing.

## Build Your Own Galaxy Data (Optional)

If you prefer preprocessing outside the browser:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install numpy sentence-transformers umap-learn hdbscan  # tweak as needed

# 1. Drop your raw export at data/conversations.json
python3 scripts/extract_messages.py  # -> data/extracted_messages.json

# 2. Adjust scripts/config.py (neighbors, distances, palette, etc.)
python3 scripts/build_galaxy.py      # -> frontend/src/assets/galaxy_data.json
```

Refreshing your browser is enough to see the regenerated dataset. Fine-tune clustering, spreads, or particle sizing inside `docs/CONFIGURATION.md`.

## Tech Stack

- **Frontend:** React + Vite + @react-three/fiber + Drei + MediaPipe Hands
- **Visualization:** Instanced particles, circular minimap, draggable gesture HUD, floating panels
- **Tooling:** ESLint, modern CSS, html2canvas-based screenshots
- **Backend Scripts:** Python + NumPy for position generation, message extraction helpers

## Contributing & Support

Ideas, issues, and PRs are more than welcome—this is a living playground for experimenting with personal data viz. Open a [GitHub issue](https://github.com/ktwu01/neural-galaxy/issues) if you run into trouble, or fork the repo and show us your own Neural Galaxy. 🚀

## Acknowledgments

- Inspired by [@Suryansh777777](https://x.com/Suryansh777777)’s [Jarvis-CV](https://github.com/Suryansh777777/Jarvis-CV), [@SarthakHuh](https://x.com/SarthakHuh)’s Neural Visualizer, and [@jinaycodes](https://x.com/jinaycodes)'s [soarxiv.org](https://soarxiv.org/). Feedback welcome!
