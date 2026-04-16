# How to publish this profile

GitHub auto-renders a README from a repo named **exactly** the same as your username. So you need a repo called `g8tsz/g8tsz`.

## Option A — fastest (web UI, 60 seconds)

1. Go to https://github.com/new
2. Repository name: `g8tsz` (yes, same as your username — GitHub will show a "special" banner)
3. Set it **Public**, check **Add a README**, create.
4. Open the new `README.md`, click the pencil, paste the contents of `README.md` from this folder, commit.
5. Create `.github/workflows/snake.yml` in that repo, paste the contents from this folder, commit.
6. Go to the repo's **Actions** tab → run the `generate contribution snake` workflow once manually. After ~30s an `output` branch will be created with the snake SVGs — the README references them automatically.
7. Visit https://github.com/g8tsz — your new profile is live.

## Option B — via terminal (if you want git locally)

```bash
cd C:\Users\nickh\g8tsz-profile
git init
git add .
git commit -m "feat: profile readme"
git branch -M main
gh auth login            # one-time
gh repo create g8tsz --public --source=. --push
```

Then trigger the snake workflow once from the Actions tab.

## Optional personalization

Open `README.md` and tweak:

- **email / x / discord links** at the bottom (currently placeholders like `hello@g8tsz.dev`)
- **the `whoami` code block** — change `role`, `focus`, `currently` to match what you're actually doing
- **color theme** — every `&theme=tokyonight` and `&color=8b5cf6` can be swapped. Popular alternates:
  - `dracula`, `radical`, `catppuccin_mocha`, `synthwave`, `gruvbox`
- **tech stack icons** — edit the `skillicons.dev/icons?i=...` list. Full list at https://skillicons.dev

That's it. The README uses nothing but public GitHub/Vercel services — no tokens, no self-hosting.
