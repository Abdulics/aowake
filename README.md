
# AOwake - Always On

**AOwake** is a lightweight, cross-platform desktop app that prevents your computer from sleeping by keeping the system awake **and randomly moving the mouse**. Whether you're watching long videos, downloading big files, or just want to stay online, AOwake keeps you "awake."

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App

```bash
python main.py
```

---

## 📦 Build Executable for Distribution

### 🪟 For Windows:

```bash
pyinstaller main.py --name AOwake --windowed --icon=icon.ico
```

### 🍏 For macOS:

```bash
pyinstaller main.py --name AOwake --windowed --icon=icon.icns
```

> After build, check the `dist/` folder for your distributable app.

---

## 🧪 How It Works

- When you hit **Start**:
  - The system is prevented from going idle.
  - The mouse moves slightly every few seconds in random directions.
- When you hit **Stop**:
  - Mouse activity stops.
  - Sleep prevention is disabled.
- Works quietly in the background with a user-friendly interface.

---

## 🚧 TODO

- [ ] Add system tray support  
- [ ] Add auto-start on boot  
- [ ] Add dark mode/theme switch  
- [ ] Add timer option (stay awake for X minutes)  
- [ ] Show running status in taskbar  

---

## 📸 Preview

(Screenshots or GIFs coming soon)

---

## 🧾 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Feel free to fork this repo and submit a pull request. Suggestions, ideas, and issues are always welcome!

---

## 🙌 Acknowledgments

- Python 💙  
- Tkinter GUI  
- PyAutoGUI for mouse simulation  
- PyInstaller for packaging  
