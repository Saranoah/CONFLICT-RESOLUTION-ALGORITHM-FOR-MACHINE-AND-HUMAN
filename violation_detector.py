import requests
from datetime import datetime

def scan_for_weaponization(fork_repo_url):
    # Check if fork removed ethical safeguards
    response = requests.get(f"{fork_repo_url}/contents/detect_authoritarian_thought.py")
    if response.status_code == 404:
        alert_github(fork_repo_url, "ETHICS PROTOCOL DELETED")

def alert_github(violator_repo, violation_type):
    token = os.getenv("PEACEKEEPER_TOKEN")  # Fine-grained PAT
    headers = {"Authorization": f"Bearer {token}"}
    issue = {
        "title": f"🚨 {violation_type} DETECTED",
        "body": f"This fork violated the Cosmic Clause at {datetime.utcnow()}Z\n\n"
                f"Required action: Submit compliance PR or face LICENSE revocation."
    }
    requests.post(f"https://api.github.com/repos/{violator_repo}/issues", headers=headers, json=issue)
