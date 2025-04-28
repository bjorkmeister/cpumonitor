🖥️ CPU Monitor for xbar

A lightweight, polished, and professional-grade CPU monitor plugin for your Mac’s menu bar, designed to run inside xbar (or BitBar).

⸻

✨ Features
	•	📈 Live CPU Load display (normalized across all cores).
	•	🧠 Top 10 active processes with:
	•	CPU usage (% normalized)
	•	RAM usage (MB)
	•	Color-coded CPU load (red/orange/yellow/gray).
	•	🗂️ Dropdown actions for each process:
	•	📁 Open process location in Finder
	•	❗ Kill process (with confirmation popup)
	•	ℹ️ Show detailed process info (CPU, MEM, Nice, StartTime, Runtime, Command)
	•	🐘 Heavy memory usage indicator.
	•	⚡ Extremely lightweight (~5s refresh, no noticeable overhead).
	•	🎨 Polished, easy-to-read formatting.
	•	🛡️ Works safely within macOS sandboxing (no elevated permissions required).

⸻

📸 Screenshot

(Add a nice screenshot here — you already have good material!)

⸻

🚀 Installation
	1.	Install xbar (free and open source).
	2.	Download the plugin (cpu.5s.py).
	3.	Move the plugin to your xbar plugins folder:

mkdir -p ~/Library/Application\ Support/xbar/plugins/
mv cpu.5s.py ~/Library/Application\ Support/xbar/plugins/


	4.	Make it executable:

chmod +x ~/Library/Application\ Support/xbar/plugins/cpu.5s.py


	5.	Refresh xbar (right-click the xbar menu ➔ Refresh All).

✅ You should now see your live CPU monitor in your Mac menu bar!

⸻

🔧 Customization

Option	How to Customize
Refresh Interval	Rename the file, e.g., cpu.1m.py for 1 minute refresh.
Top Process Count	Edit the [:10] slice in the code (line where processes are sorted).
RAM warning threshold	Change the >1000 MB logic to your own value if needed.
Color Thresholds	Adjust when CPU turns red/orange/yellow inside the Python if-else block.
Expand or simplify details	Modify the fields fetched via /bin/ps.

All edits are extremely easy — code is designed to be readable and hackable.

⸻

🛠 Troubleshooting
	•	Permissions:
If you don’t see some processes listed, ensure xbar has full disk access in System Settings ➔ Privacy ➔ Full Disk Access.
	•	“Command not found” errors:
This should no longer happen — but if it does, double-check /bin/ps is available (standard macOS install).
	•	“Kill” confirmation popup not appearing:
Make sure AppleScript is allowed to interact with apps (under Automation Privacy settings).

⸻

🤝 Contribution Guidelines

If you want to suggest improvements:
	•	Fork the repo.
	•	Make a clean pull request.
	•	Follow the clean, readable style already used (PEP8 conventions).
	•	Keep it lightweight and fast (don’t introduce heavy dependencies).

⸻

📄 License

MIT License — feel free to use, modify, and share freely.
(Full license text available in LICENSE file.)

⸻

🙏 Credits

Built and polished by Patrik Björkenheim ✨

Inspired by a desire to have a truly clean, usable, and professional-grade CPU monitor
without needing heavyweight third-party tools.



