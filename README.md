# Trove WAM landing (Dash)

Landing site for **Trove WAM** — home page, sidebar navigation, and module directory pages.

## Run

```bash
cd C:\Users\78401\trove-wam-landing
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8000/wam/`

## Pages

| Route | File |
|---|---|
| `/` | `pages/home.py` |
| `/strategy/` | `pages/strategy.py` |
| `/strategy/market-maps/` | `pages/market_maps.py` |
| `/strategy/wealth-management-decks/` | `pages/wealth_management_decks.py` |
| `/capital-markets/` | `pages/capital_markets.py` |
| `/pi-cost/` | `pages/pi_cost.py` |
| `/et/` | `pages/et.py` |
| `/customer/` | `pages/customer.py` |
| `/ma/` | `pages/ma.py` |

## Assets

- Home images: `assets/Images_Used/`
- Sidebar icons: `assets/Icons/`
- Directory tile icons: `assets/Icons/`, `assets/Strategy_Landing/`, `assets/PICost_Landing/`, etc.

Update tile `href` / `icon` fields in each page module as destinations are wired up.
