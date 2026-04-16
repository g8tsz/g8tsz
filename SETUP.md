# Profile repo — setup & maintenance

GitHub auto-renders a README from a repo named **exactly** the same as your
username. This repo is `g8tsz/g8tsz`, so its `README.md` shows up at the top of
https://github.com/g8tsz.

---

## 1. First-time publish

Already done on this account. If you ever have to recreate it from scratch:

1. https://github.com/new → name it `g8tsz` → public → "add a README".
2. Replace that README with this folder's `README.md`.
3. Commit the rest of this folder (`.github/`, `scripts/`, `.githooks/`,
   `.gitattributes`, `.editorconfig`, `SETUP.md`).
4. Open the **Actions** tab, run `generate contribution snake` manually once.
   This creates an `output` branch with `github-snake.svg` /
   `github-snake-dark.svg`; the README references them directly from that
   branch.

---

## 2. Enable the pre-commit hook (recommended, one command)

```bash
git config core.hooksPath .githooks
```

That's it. From now on, `git commit` will refuse to stage any text file that
contains an XML-invalid control byte (0x00–0x1F except TAB/LF/CR). This is the
same class of bug that broke the banner SVG once — a stray `0x14` where an
em-dash should have been.

CI enforces the same check on every push / PR via `.github/workflows/validate.yml`,
so even if a contributor forgets to enable the hook, bad bytes never reach
`main`.

---

## 3. Third-party services this README depends on

Ordered from most to least reliable. If one of these goes down, the README
keeps working — only that specific block will show as a broken image.

| Block                    | Service                                      | Reliability | Replace with if it dies                          |
| ------------------------ | -------------------------------------------- | ----------- | ------------------------------------------------ |
| follower / stars badges  | `img.shields.io`                             | very high   | n/a, shields.io is the reference implementation  |
| tech-stack icons         | `skillicons.dev`                             | high        | static PNGs committed to `assets/`               |
| typing animation         | `readme-typing-svg.demolab.com`              | medium      | static text headline, or generate nightly        |
| repo-pin cards           | `github-readme-stats.vercel.app/api/pin`     | medium      | plain markdown links                             |
| stats / top-langs card   | `github-readme-stats.vercel.app`             | medium      | generate nightly via GH Action + commit SVG      |
| trophies                 | `github-profile-trophy.vercel.app`           | medium-low  | drop the block, or self-host the SVG nightly     |
| contribution snake       | **self-hosted** on `output` branch           | very high   | regenerated nightly by `snake.yml` — no external |

Deliberately **removed** (too fragile or low-signal):

- `github-readme-streak-stats.herokuapp.com` — Heroku free tier is gone, goes
  to sleep / times out.
- `komarev.com/ghpvc` — profile-views vanity counter, rate-limits.
- `readme-jokes.vercel.app` — hobby Vercel project, frequent 502s.
- `github-readme-activity-graph.vercel.app` — duplicates what the snake already
  shows.
- `capsule-render.vercel.app` — the service whose outage started the whole
  banner saga.

---

## 4. Known loose ends

- **`Casino-Fruad-Cheating-tracker-`** — the pinned repo name has a typo
  ("Fruad"). The pin card renders the repo name verbatim, so the only way to
  fix the spelling is to rename the repo on GitHub:
  `Settings → General → Repository name → Casino-Fraud-Cheating-tracker`.
  GitHub automatically sets up a redirect from the old URL, and this README's
  pin URL will need a matching update.
- **Discord badge** — the link to `https://discord.com/users/.eats.` was
  removed because Discord user URLs require the numeric snowflake ID, not the
  username. The badge is kept as a non-link display. If you want it clickable,
  replace `.eats.` in the badge with the real 18-digit user ID and wrap in
  `<a href="https://discord.com/users/<id>">…</a>`.

---

## 5. Theming

Everywhere `&theme=tokyonight` and the hex `8b5cf6` appear, you can swap for
any of: `dracula`, `radical`, `catppuccin_mocha`, `synthwave`, `gruvbox`.

Skillicon set: full list at https://skillicons.dev — keep `perline` at 8 or
below so the row doesn't overflow on the mobile GitHub app.
