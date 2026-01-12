from rules import detectFailedLogins, failedLoginByIP

def read_logs(path):
    """Reads a log file and returns a list"""
    with open(path, "r") as f:
        return f.readlines()

logs = read_logs("sample_logs/auth.log")

failed = detectFailedLogins(logs)
ipCounts = failedLoginByIP(logs)

print("Failed login attempts:", len(failed))
print("Attempts by IP:", ipCounts)
    