# Kiosk Config Sync

Pulls kiosk layouts and service settings for Venetian Macao guest services from
`kiosk-cms-int.venetianmacao.com` and pushes them to the lobby kiosks.

## Usage

1. Fill in `config/kiosk.yaml`.
2. Run `python src/client.py --site lobby`.
