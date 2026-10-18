# social-videos

Kurzvideos von NetSecure.Media, StageDisplay und TechnikDruck für Instagram, TikTok und YouTube Shorts.
Metricool holt die Dateien von hier ab und veröffentlicht sie zum geplanten Termin.

- **[VIDEOPLAN.md](VIDEOPLAN.md):** alle Videos mit Termin, Status, Hook, Sprechertext, Szenen und Caption
- **[plan.json](plan.json):** derselbe Plan maschinenlesbar

## Ablauf

1. **Video erstellen:** Die Design-Instanz nimmt das nächste offene Video aus dem Plan und baut es im passenden Marken-Stil.
2. **Hochladen:** Das fertige Video kommt nach `videos/1_neu/`, benannt wie im Plan, z. B. `NSM-02_Smart-TV-im-Firmennetz.mp4`.
   Optional daneben: `NSM-02_cover.jpg` (eigenes Vorschaubild) und `NSM-02_caption.txt` (eigene Caption).
3. **Bescheid geben:** Dominik sagt der Planungs-Instanz „neue Videos sind da“.
4. **Einplanen:** Die Planungs-Instanz prüft das Video, plant es in Metricool zum Termin aus dem Plan ein (plus Instagram-Story am selben Tag um 18:00), verschiebt es nach `videos/2_eingeplant/` und setzt den Status im Plan auf `Eingeplant`.
5. **Nach dem Posten:** Videos, deren Termin vorbei ist, wandern nach `videos/3_veroeffentlicht/`, und der Status wird `Gepostet`.

Kommt ein Video früher als geplant, bleibt es beim Termin aus dem Plan. Fehlt ein Video zum Termin, rückt das nächste fertige nach.

## Ordner

| Ordner | Inhalt |
|---|---|
| `videos/1_neu/` | Fertig, aber noch nicht eingeplant. Hier wird hochgeladen. |
| `videos/2_eingeplant/` | In Metricool terminiert, noch nicht veröffentlicht |
| `videos/3_veroeffentlicht/` | Bereits gepostet (Archiv) |

## Vorgaben für die Videos

- **Format:** 1080 × 1920 (9:16), 30 fps, MP4 mit H.264 und AAC-Ton
- **Farbe:** SDR (BT.709). HDR/HLG-Exporte werden auf Instagram und TikTok oft zu hell; die werden vor dem Einplanen umgewandelt.
- **Länge:** ideal 15–30 Sekunden, höchstens 90 Sekunden
- **Dateigröße:** unter 50 MB (GitHub erlaubt maximal 100 MB pro Datei)
- **Hook:** Die Kernaussage steht schon im ersten Bild als Text, nicht erst in der Caption.
- **Endkarte:** höchstens 3 Sekunden, damit möglichst viele bis zum Ende schauen
- **Sichere Zone:** Wichtige Texte nicht in die oberen 250 px, die unteren 450 px und die rechten 140 px legen; dort liegen die Bedienelemente von TikTok und Instagram.

## Hochladen ohne Git

Auf github.com im Repo `videos/1_neu/` öffnen → **Add file** → **Upload files** → Video hineinziehen → **Commit changes**.
