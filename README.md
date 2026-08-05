# Trove WAM landing (Dash)

Minimal landing replica of Trove Banking patterns for **Trove WAM**.

## Project layout

```
trove-wam-landing/
├── app.py                 # Dash app shell, callbacks, entry point
├── python_compat.py       # Python 3.14 pkgutil.find_loader patch
├── fix_icon_bg.py         # Sidebar icon transparency fix (runs on startup)
├── top_navbar.py          # Top bar (brand, What's New, Contact us)
├── navigation_bar.py      # Collapsible sidebar + page container
├── whats_new_popup.py     # What's New popup component
├── page_helpers.py        # Shared placeholder page helper
├── requirements.txt
├── pages/
│   ├── home.py            # / — hero + image tiles
│   ├── strategy.py        # /strategy/
│   ├── market_maps.py     # /strategy/market-maps/
│   ├── capital_markets.py # /capital-markets/
│   ├── pi_cost.py         # /pi-cost/
│   ├── et.py              # /et/
│   └── customer.py        # /customer/ (placeholder)
└── assets/
    ├── css/app.css
    ├── custom.js
    ├── Images_Used/       # Home hero + tile images
    └── Icons/             # Sidebar + directory tile icons
```

## Run

```bash
cd C:\Users\78401\trove-wam-landing
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8000/wam/`

> **Note:** On Python 3.14, older Dash crashes on `pkgutil.find_loader`.
> `python_compat.py` patches that before Dash starts. `app.py` runs with `debug=False` for stability.

## Pages

| Route | File |
|---|---|
| `/` | `pages/home.py` |
| `/strategy/` | `pages/strategy.py` |
| `/strategy/market-maps/` | `pages/market_maps.py` |
| `/capital-markets/` | `pages/capital_markets.py` |
| `/pi-cost/` | `pages/pi_cost.py` |
| `/et/` | `pages/et.py` |
| `/customer/` | `pages/customer.py` |

## Git

The repo is structured for git but not initialized here. When you are ready:

```bash
cd C:\Users\78401\trove-wam-landing
git init
git add .
git status
```

`.gitignore` excludes `.venv/`, `.idea/`, `__pycache__/`, and generated `*_clear.png` icon files (rebuilt at runtime).

## Assets

Put home images in `assets/Images_Used/` and icons in `assets/Icons/`.
Update tile `href` / `icon` fields in each page module as destinations are wired up.
Update the Contact us mailto in `top_navbar.py` to your real address.
