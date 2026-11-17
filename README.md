# Quote Compare

An offline iPhone app (a web app you add to your Home Screen) for collecting quotes from
businesses, taking dictated notes and photos on site, rating each one, comparing them
side by side and marking a final choice.

Plain HTML/JS, no frameworks, no server, no account. All data stays on the phone (IndexedDB).

## Files
- `index.html` — the whole app
- `sw.js` — offline cache (bump `VERSION` after changing `index.html`)
- `manifest.webmanifest`, `icon-*.png` — Home Screen install (`python make_icons.py` regenerates the icons)

## Install on iPhone (one time, needs internet)
1. Host these files on any HTTPS site (e.g. GitHub Pages).
2. Open the URL in **Safari** → Share → **Add to Home Screen**.
3. Open it once from the Home Screen icon. From then on it works in airplane mode.

## Using it
- One **project** per thing you're buying → add each **business** → fill price, terms, ratings.
- **Dictation:** tap the notes box, then the 🎤 key on the iPhone keyboard. Tap **Add note** to save it with a timestamp.
  For dictation without signal: Settings → General → Keyboard → make sure Dictation is on (recent iPhones dictate on-device).
- **Compare** shows all businesses side by side; lowest price and best rating are highlighted.
- **Backup** (top right on the home screen): export now and then to Files / iCloud Drive.
  Data lives only in this app on this phone. Deleting the Home Screen icon deletes the data.
