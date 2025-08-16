# Genshin Dialogue Skipper

A simple Python script that automatically skips through dialogues in **Genshin Impact**.  
It listens for a hotkey (`F8`) to toggle auto-skipping on and off.  

---

## ✨ Features
- Toggles on/off with **F8**
- Detects if the Genshin Impact window is active
- Supports English and Italian UI detection
- Skips dialogues automatically by pressing:
  - **Space** (to advance dialogue text)
  - **F** (to select dialogue options)
- Stores settings in a `genshin.json` configuration file
- If you change screen resolution or game lenguage delete the json file

---

## 📦 Requirements
Install dependencies with:

```bash
pip install pynput pyautogui pygetwindow
