def detectFailedLogins(logs):
    """Returns all log lines with failed login attempts."""
    return [line for line in lofs if "Failed password" in line]

def failedLoginByIP(logs):
    """returns a dictionary with failed logins for each IP."""
    counts = {}
    for line in logs:
            if "Failed password" in line:
                ip = line.split()[-4] #extracts the IP
                counts[ip] = counts.get(ip, 0) + 1
    return counts