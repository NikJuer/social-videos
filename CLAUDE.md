# Hinweise für Claude

Dieses Repo ist die Ablage für Dominiks Social-Media-Videos. Ablauf, Ordner und Video-Vorgaben stehen in `README.md`, der Plan in `VIDEOPLAN.md` und `plan.json` (`plan.json` ist die Quelle, `VIDEOPLAN.md` wird daraus erzeugt und muss mit ihr übereinstimmen).

## Rolle „Design“ (Videos erstellen)
- Nimm das nächste Video mit Status `Offen` (bzw. `Material nötig`, sobald Dominik das Material geliefert hat) in Terminreihenfolge.
- Lege fertige Videos nur in `videos/1_neu/` ab, mit dem Dateinamen aus dem Plan. Verschiebe oder lösche nichts in den anderen Ordnern und ändere den Status nicht selbst.
- Weicht der Text vom Plan ab, lege `<ID>_caption.txt` mit der fertigen Caption daneben.
- Sprecherstimme (ElevenLabs) je Marke: **Helmut** für NetSecure.Media und StageDisplay, **„Junger Mann aus Ostfriesland“** für TechnikDruck (ab TD-02). Grundlage ist der A/B-Test bei NSM-02 (siehe `videos/3_veroeffentlicht/NSM-02_INFO.md`).
- ElevenLabs nur mit **Eleven v4** (`model_id: "eleven_v4"`). `eleven_multilingual_v2` nicht verwenden, das klingt laut Dominik schlecht.
- NetSecure.Media-Videos: Den Markennamen mit „Punkt“ sprechen lassen („NetSecure Punkt Media“) und am Ende den Slogan „Technik, die funktioniert.“ **flüstern** – im Sprechertext `[whispers] Technik, die funktioniert.` (Eleven-v4-Audio-Tag, wird nicht mitgesprochen).

## Rolle „Planung“ (Einplanen in Metricool, Brand-ID 7358750, Zeitzone Europe/Berlin)
1. Neue Dateien in `videos/1_neu/` prüfen: 1080×1920, H.264/AAC, SDR. HDR/HLG mit Tonemapping nach BT.709 umwandeln.
2. Termin aus `plan.json` nehmen (immer 10:00). Liegt der Termin in der Vergangenheit, den nächsten freien Di/Fr-Termin nehmen und den Plan nachziehen.
3. In Metricool einplanen: Instagram `REEL`, TikTok (Titel Pflicht, `commercialContentOwnBrand: true`), YouTube `short` (`madeForKids: false`). Medien-URL: `https://raw.githubusercontent.com/NikJuer/social-videos/main/videos/1_neu/<Datei>`; Vorschaubild über `videoThumbnailUrl` (falls `<ID>_cover.jpg` existiert) oder `videoCoverMilliseconds` auf das Hook-Bild.
   Zusätzlich am selben Tag um 18:00 eine Instagram-Story mit demselben Video einplanen (nur `instagram`, `instagramData.type: "STORY"`, ohne Text; als Medien-URL die `static.metricool.com`-Adresse aus dem eben eingeplanten Post). TikTok-Storys kann Metricool nicht posten.
4. Erst **nach** erfolgreichem Einplanen (Metricool kopiert die Datei zu sich) nach `videos/2_eingeplant/` verschieben, in `plan.json` `status: "Eingeplant"` und `file` setzen, `VIDEOPLAN.md` neu erzeugen, committen und pushen.
5. Bei jedem Durchlauf: Videos mit vergangenem Termin nach `videos/3_veroeffentlicht/` verschieben und auf `Gepostet` setzen.
