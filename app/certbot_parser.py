def parse_certbot_manual_challenge(email_input: str, domain_input: str):
    return (
        f"sudo certbot certonly "
        f"--manual --preferred-challenges=dns "
        f"--email {email_input} "
        f"--server https://acme-v02.api.letsencrypt.org/directory "
        f"--work-dir=. --config-dir=. --logs-dir=. --agree-tos "
        f"-d {domain_input}"
    )
