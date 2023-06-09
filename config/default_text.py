DEFAULT_DOMAIN = "helloworld.com"
DEFAULT_EMAIL = "email@address.com"


def COPY_CMD_0(domain_input: str):
    return (
        f"cd live/{domain_input}\n"
        f"sudo nano cert.pem\n"
    )


COPY_CMD_1 = "sudo nano privkey.pem\n"

DEFAULT_CERT = """-----BEGIN CERTIFICATE-----
BmeBDAECATA3BgsrBgEEAYLfEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3Bz
LmxldHNlbmNyeXB0Lm9yZzCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB2AHoyjFTY
ty22IOo44FIe6YQWcDIThU070ivBOlejUutSAAABhzXJQRgAAAQDAEcwRQIhAMxH
4gfn8RSP3CQYLzhqZglk1o6wfuLUw83gwugVd6sMAiADZN6SqK46WV2M3fyzhjHB
ynejNhCK8V4p9GVmmmeuzgB2AK33vvp8/xDIi509nB4+GGq0Zyldz7EMJMqFhjTr
3IKKAAABhzXJQU4AAAQDAEcwRQIhAL1gvfINwMIxPv1FSAHTnhNWaWVICurbvXU9
BmeBDAECATA3BgsrBgEEAYLfEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3Bz
LmxldHNlbmNyeXB0Lm9yZzCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB2AHoyjFTY
ty22IOo44FIe6YQWcDIThU070ivBOlejUutSAAABhzXJQRgAAAQDAEcwRQIhAMxH
4gfn8RSP3CQYLzhqZglk1o6wfuLUw83gwugVd6sMAiADZN6SqK46WV2M3fyzhjHB
ynejNhCK8V4p9GVmmmeuzgB2AK33vvp8/xDIi509nB4+GGq0Zyldz7EMJMqFhjTr
3IKKAAABhzXJQU4AAAQDAEcwRQIhAL1gvfINwMIxPv1FSAHTnhNWaWVICurbvXU9
BmeBDAECATA3BgsrBgEEAYLfEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3Bz
LmxldHNlbmNyeXB0Lm9yZzCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB2AHoyjFTY
ty22IOo44FIe6YQWcDIThU070ivBOlejUutSAAABhzXJQRgAAAQDAEcwRQIhAMxH
4gfn8RSP3CQYLzhqZglk1o6wfuLUw83gwugVd6sMAiADZN6SqK46WV2M3fyzhjHB
ynejNhCK8V4p9GVmmmeuzgB2AK33vvp8/xDIi509nB4+GGq0Zyldz7EMJMqFhjTr
3IKKAAABhzXJQU4AAAQDAEcwRQIhAL1gvfINwMIxPv1FSAHTnhNWaWVICurbvXU9
BmeBDAECATA3BgsrBgEEAYLfEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3Bz
LmxldHNlbmNyeXB0Lm9yZzCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB2AHoyjFTY
ty22IOo44FIe6YQWcDIThU070ivBOlejUutSAAABhzXJQRgAAAQDAEcwRQIhAMxH
4gfn8RSP3CQYLzhqZglk1o6wfuLUw83gwugVd6sMAiADZN6SqK46WV2M3fyzhjHB
ynejNhCK8V4p9GVmmmeuzgB2AK33vvp8/xDIi509nB4+GGq0Zyldz7EMJMqFhjTr
3IKKAAABhzXJQU4AAAQDAEcwRQIhAL1gvfINwMIxPv1FSAHTnhNWaWVICurbvXU9
BmeBDAECATA3BgsrBgEEAYLfEwEBATAoMCYGCCsGAQUFBwIBFhpodHRwOi8vY3Bz
LmxldHNlbmNyeXB0Lm9yZzCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB2AHoyjFTY
ty22IOo44FIe6YQWcDIThU070ivBOlejUutSAAABhzXJQRgAAAQDAEcwRQIhAMxH
4gfn8RSP3CQYLzhqZglk1o6wfuLUw83gwugVd
-----END CERTIFICATE-----"""

DEFAULT_KEY = """-----BEGIN PRIVATE KEY-----
n1uroaYmKumi+i1qh8ktBFR/PYWj+aepDUHNF+9F9Sa1omgGWnGoL18wUJyBbQdf
n94iagW1UqXKtbOMi9woirAXzCqeJT9MO3gsrD/ePGX2Gi5s3BAh0qhi3lStIgNC
cA/DlaJqUQH+KNOLQU4FwLPIawKBgQDs/oOIuKetm8wjRVWDRisVSJmlBWmI1HzZ
HdCEDRJx3PZkHTzocKheLYLqEhQSfu3D/j6fhXt6g8TB46DwTE3ACnKtJa6p0hmw
4CoaQDkhhQfPG+uiXni8QjKACNqO2w8iYWGGt2WCvqtyG3iF/2yODV10Kh3smHXU
n1uroaYmKumi+i1qh8ktBFR/PYWj+aepDUHNF+9F9Sa1omgGWnGoL18wUJyBbQdf
n94iagW1UqXKtbOMi9woirAXzCqeJT9MO3gsrD/ePGX2Gi5s3BAh0qhi3lStIgNC
cA/DlaJqUQH+KNOLQU4FwLPIawKBgQDs/oOIuKetm8wjRVWDRisVSJmlBWmI1HzZ
HdCEDRJx3PZkHTzocKheLYLqEhQSfu3D/j6fhXt6g8TB46DwTE3ACnKtJa6p0hmw
4CoaQDkhhQfPG+uiXni8QjKACNqO2w8iYWGGt2WCvqtyG3iF/2yODV10Kh3smHXU
n1uroaYmKumi+i1qh8ktBFR/PYWj+aepDUHNF+9F9Sa1omgGWnGoL18wUJyBbQdf
n94iagW1UqXKtbOMi9woirAXzCqeJT9MO3gsrD/ePGX2Gi5s3BAh0qhi3lStIgNC
cA/DlaJqUQH+KNOLQU4FwLPIawKBgQDs/oOIuKetm8wjRVWDRisVSJmlBWmI1HzZ
HdCEDRJx3PZkHTzocKheLYLqEhQSfu3D/j6fhXt6g8TB46DwTE3ACnKtJa6p0hmw
4CoaQDkhhQfPG+uiXni8QjKACNqO2w8iYWGGt2WCvqtyG3iF/2yODV10Kh3smHXU
n1uroaYmKumi+i1qh8ktBFR/PYWj+aepDUHNF+9F9Sa1omgGWnGoL18wUJyBbQdf
n94iagW1UqXKtbOMi9woirAXzCqeJT9MO3gsrD/ePGX2Gi5s3BAh0qhi3lStIgNC
4CoaQDkhhQfPG+uiXni8QjKACNqO2w8iYWGGt2WCvqtyG3iF/2yODV10Kh3smHXU
n1uroaYmKumi+i1qh8ktBFR/PYWj+aepDUHNF+9F9Sa1omgGWnGoL18wUJyBbQdf
4CoaQDkhhQfPG+uiXni8QjKACNqO2w8iYWGGt2WCvqtyG3iF/2yODV10Kh3smHXU
n1uroaYmKumi+i1qh8ktBFR/PYWj+aepDUHNF+9F9Sa1omgGWnGoL18wUJyBbQdf
n94iagW1UqXKtbOMi9woirAXzCqeJT9MO3gsrD/ePGX2Gi5s3BAh0qhi3lStIgNC
cA/DlaJqUQH+KNOLQU4FwLPIawKBgQDs/oOIuKetm8wjRVWDRisVSJmlBWmI1HzZ
HdCEDRJx3PZkHTzocKheLYLqEhQSfu3D/j6fhXt6g8TB46DwTE3ACnKtJa6p0hmw
4CoaQDkhhQfPG+uiXni8QjKACNqO2w8iYWGGt2WCvqtyG3iF/2yODV10Kh3smHXU
vWJKKE7EnKP6Jbnm4i5M6n7W
-----END PRIVATE KEY-----"""
