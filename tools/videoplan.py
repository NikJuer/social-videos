"""Erzeugt VIDEOPLAN.md aus plan.json. Aufruf im Repo-Root: python3 tools/videoplan.py"""
import json, datetime as dt, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
plan = json.load(open(R / 'plan.json'))
BR = {'nsm': 'NetSecure.Media', 'sd': 'StageDisplay', 'td': 'TechnikDruck'}
MON = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']

def dfmt(p):
    d = dt.date.fromisoformat(p['date']); return f"{p['weekday']} {d.day:02d}.{d.month:02d}.{d.year}"

L = []
L += ['# Videoplan', '',
      'Zwei Uploads pro Woche, jeweils 10:00 Uhr auf Instagram (Reel), TikTok und YouTube (Short):',
      '**Dienstag NetSecure.Media**, **Freitag abwechselnd TechnikDruck und StageDisplay**.',
      'Wie Videos ins Repo kommen und was danach passiert, steht in der [README](README.md).', '',
      f"Stand: {dt.date.today().strftime('%d.%m.%Y')}", '',
      '**Status:** `Eingeplant` = in Metricool terminiert · `Gepostet` = veröffentlicht · `Offen` = Video fehlt noch · `Material nötig` = Video fehlt, und es braucht echte Fotos/Clips/Infos von Dominik', '',
      '## Übersicht', '',
      '| Termin | ID | Marke | Titel | Status | Dateiname |', '|---|---|---|---|---|---|']
for p in plan:
    if p.get('free'):
        L.append(f"| {dfmt(p)} | – | – | *{p['note']}* | Frei | – |")
    else:
        L.append(f"| {dfmt(p)} | {p['id']} | {BR[p['brand']]} | {p['title']} | {p['status']} | `{p['filename']}` |")
L += ['', '## Details je Video', '',
      'Hook, Sprechertext und Szenen sind **Vorschläge**. Der Stil kommt von dir bzw. deiner Design-Instanz.',
      'Wer den Text ändert, legt neben das Video eine Datei `<ID>_caption.txt` mit der gewünschten Caption, sonst wird die Caption unten verwendet.', '']
month = None
for p in plan:
    if p.get('free'): continue
    d = dt.date.fromisoformat(p['date']); m = f"{MON[d.month-1]} {d.year}"
    if m != month: L += [f'### {m}', '']; month = m
    L += [f"#### {dfmt(p)} · {p['id']} · {p['title']}", '',
          f"- **Marke:** {BR[p['brand']]} · **Serie:** {p['series']} · **Status:** {p['status']}",
          f"- **Dateiname:** `{p['filename']}`" + (f" (liegt in `{p['file'].rsplit('/',1)[0]}/`)" if p.get('file') else ''),
          f"- **Hook (erstes Bild):** {p['hook']}"]
    if p.get('note'): L.append(f"- **Hinweis:** {p['note']}")
    L += [f"- **Material:** {p['assets']}", '- **Sprechertext / Untertitel:**']
    L += [f"  {i}. {v}" for i, v in enumerate(p['voice'], 1)]
    L += ['- **Szenen:**'] + [f"  - {s}" for s in p['scenes']]
    L += [f"- **TikTok-Titel:** {p['tt_title']}", f"- **YouTube-Titel:** {p['yt_title']}", '- **Caption:**', '', '```text', p['caption'], '```', '']
open(R / 'VIDEOPLAN.md', 'w').write('\n'.join(L))
print('ok', len(plan), sum(1 for p in plan if p.get('free')), 'frei')
