def replace_ssl_cert(cert_input, key_input, file_input):
    with open(file_input, "r") as f:
        lines = f.readlines()
    with open(file_input, "w") as f:
        inside_cert = False
        inside_key = False
        for line in lines:
            if "-----BEGIN CERTIFICATE-----" in line:
                inside_cert = True
                f.write(cert_input)
                f.write("\n")
            elif "-----END CERTIFICATE-----" in line:
                inside_cert = False
            elif inside_cert:
                continue
            elif "-----BEGIN PRIVATE KEY-----" in line:
                inside_key = True
                f.write(key_input)
                f.write("\n")
            elif "-----END PRIVATE KEY-----" in line:
                inside_key = False
            elif inside_key:
                continue
            else:
                f.write(line)
