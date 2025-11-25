# Deja Vu — Visual Novel (Ren'Py)

Deja Vu is a Ren'Py visual novel about Yuki, a woman trapped in a looping day inside a mysterious bar. The story explores memory, loss, and the choices that shape identity.

## Quick start
- Open this project folder in the Ren'Py launcher and start the project.
- The game begins at [`label start`](game/script.rpy) in [game/script.rpy](game/script.rpy).
- A minigame is available from the main menu via [`label start3`](game/minigame.rpy) in [game/minigame.rpy](game/minigame.rpy).

## Gameplay overview
- Play through scenes and make choices via menus to uncover Yuki's past.
- Important branches and scenes:
  - Piano loop and investigation: [`label chapter_4_piano`](game/chapter4.rpy) — [game/chapter4.rpy](game/chapter4.rpy)
  - Day 1 introduction and bar scenes: [`label day1`](game/chapter1.rpy) — [game/chapter1.rpy](game/chapter1.rpy)
  - Chapter 3 progression and key discovery: [`label chapt3_start`](game/chapt3.rpy) — [game/chapt3.rpy](game/chapt3.rpy)
  - Multiple endings: [`label ending_a`](game/chapter4.rpy), [`label ending_b`](game/chapter4.rpy), [`label ending_c`](game/chapter4.rpy) — see [game/chapter4.rpy](game/chapter4.rpy)

## Characters (defined)
- [`yuki`](game/script.rpy) — player character (defined in [game/script.rpy](game/script.rpy))
- [`kai`](game/script.rpy) — important NPC (defined in [game/script.rpy](game/script.rpy))
- [`bartender`](game/script.rpy) — bar keeper (defined in [game/script.rpy](game/script.rpy))

## Notable files
- Story / scenes:
  - [game/script.rpy](game/script.rpy) — general definitions and start point (`label start`)
  - [game/chapter1.rpy](game/chapter1.rpy) — opening bar & day one (`label day1`, menus)
  - [game/chapt2.rpy](game/chapt2.rpy) — chapter 2 content
  - [game/chapt3.rpy](game/chapt3.rpy) — chapter 3 (`label chapt3_start`)
  - [game/chapter4.rpy](game/chapter4.rpy) — piano, journal, choices, and endings (`label chapter_4_piano`)
  - [game/chapt5.rpy](game/chapt5.rpy) — day2 (`label day2`)
- UI and configuration:
  - [game/gui.rpy](game/gui.rpy) — GUI sizing, fonts, layout
  - [game/options.rpy](game/options.rpy) — game options and build settings
  - [game/screens.rpy](game/screens.rpy) — screen definitions and menus
  - [game/variables.rpy](game/variables.rpy) — image definitions and character declarations
- Audio and assets:
  - [game/audio/](game/audio/) — music and sound effects referenced by scenes (e.g. "sad piano.ogg", "creepy.ogg")

## How to play
- Use mouse / keyboard (Enter / Space) to advance dialogue.
- Select choices when menus appear to follow different branches.
- Access Save / Load / Preferences from the in-game menu (see [game/screens.rpy](game/screens.rpy) and [game/gui.rpy](game/gui.rpy)).

## Structure & branching hints
- The piano scene in [game/chapter4.rpy](game/chapter4.rpy) branches depending on the player's choices and selected song, then leads to the journal and investigation paths.
- Journal interactions use the `show screen journal` pattern and variables like `textjurnal`/`textjournal` in [game/chapter4.rpy](game/chapter4.rpy) and [game/chapt2.rpy](game/chapt2.rpy).
- Endings are reached via menus at [`label embrace_or_resist`](game/chapter4.rpy) and its piano variant.

## Development notes
- Character images and scene art are defined in [game/script.rpy](game/script.rpy) and [game/variables.rpy](game/variables.rpy) (im.Scale calls).
- GUI layout and responsive variants (phone / touch) are in [game/gui.rpy](game/gui.rpy) and [game/screens.rpy](game/screens.rpy).
- Save directory is configured in [game/options.rpy](game/options.rpy) (`define config.save_directory`).

## Credits & license
- Built with Ren'Py. See the About screen implemented in [game/screens.rpy](game/screens.rpy) for Ren'Py credits.
- Include your own licensing or credit details here if you distribute the game.

