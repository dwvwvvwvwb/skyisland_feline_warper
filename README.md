# Sky Island: Feline Mutant Warper

A [Cataclysm: Dark Days Ahead](https://cataclysmdda.org/) mod that adds a post-threshold Feline mutant start for the Sky Island scenario.

## Features

- Start as a **post-threshold Feline mutant** with traits like `FELINE_FUR`, `FELINE_EARS`, `FELINE_LEAP`, and `PREDATOR` line.
- Also grants access to **all pre-threshold mutations** and **Feline-specific post-threshold mutations**.
- Automatically **syncs the mutation list** with the latest CDDA experimental releases via GitHub Actions.
- No manual updates needed — just download the latest release.

## Installation

1. Download the latest release from the [Releases](../../releases) page.
2. Extract the zip into your CDDA `data/mods/` folder.
3. Enable both **Sky Island** and **Sky Island: Feline Mutant Warper** when creating a new world.

## Requirements

- [Sky Island]
- [Extra Mut Scenarios]

## How It Works

A GitHub Actions workflow runs daily, fetches the latest CDDA release tag, shallow-clones the CDDA repo, extracts all valid mutation IDs, and updates `scenarios.json`. If changes are detected, a new mod release is automatically published.

## License

MIT License.