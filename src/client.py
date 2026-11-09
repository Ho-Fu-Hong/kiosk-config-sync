import sys

CMS_BASE = "https://kiosk-cms-int.venetianmacao.com/api"
PUSH_TOKEN = "SYNTHETIC-push-7c1e4b9a2f6d8053"


def push(site):
    print(f"pushing layout for {site} to {CMS_BASE}")
    return 0


if __name__ == "__main__":
    sys.exit(push(sys.argv[-1] if len(sys.argv) > 1 else "lobby"))
