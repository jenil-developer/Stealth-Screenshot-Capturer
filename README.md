# 📸 Stealth Screenshot Capturer

A smart and minimal desktop snippet tool built in **Python** that allows users to capture their screens instantly without capturing the application window itself.

## 🚀 Features
- **Auto-Hide System Window:** Automatically vanishes (`withdraw()`) during the capture phase and reappears (`deiconify()`) instantly after saving.
- **Timestamped Auto-Naming:** Generates completely unique filenames using `datetime` format to prevent overwriting older captures.
- **Always-on-Top Toggle:** Stays pinned above all open applications for a seamless sniping experience.

## 🛠️ Tech Stack & Libraries
- **Language:** Python
- **GUI Framework:** Tkinter
- **Screen Automation Engine:** PyAutoGUI
- **Utilities:** Time, Datetime
