def detectFailedLogins(logs):
    """Returns all log lines with failed login attempts."""
    return [line for line in logs if "Failed password" in line]

def failedLoginByIP(logs):
    """returns a dictionary with failed logins for each IP."""
    counts = {}
    for line in logs:
        if "Failed password" in line:
            ip = line.split()[-3] #extracts the IP
            counts[ip] = counts.get(ip, 0) + 1

    return counts

def assessRisk(ipCounts):
    """ Risk levels based each IP's failed login count"""

    riskLevels = {}

    for ip, count in ipCounts.items():
        if count >= 5:
            riskLevels[ip] = "High"
        elif count >= 3:
            riskLevels[ip] = "Medium"
        else:
            riskLevels[ip] = "Low"
    
    return riskLevels
        
