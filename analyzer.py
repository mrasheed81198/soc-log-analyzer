from rules import detectFailedLogins, failedLoginByIP, assessRisk

def read_logs(path):
    """Reads a log file and returns a list"""
    with open(path, "r") as f:
        return f.readlines()

logs = read_logs("sample_logs/auth.log")

failed = detectFailedLogins(logs)
ipCounts = failedLoginByIP(logs)
riskLevels = assessRisk(ipCounts)

print("--- SOC Log Analysis---")
print("Failed login attempts:", len(failed))
print("Attempts by IP:", ipCounts)

print("\nRisk Aseessment:")
for ip, level in riskLevels.items():
    print(f"{ip}: {level}")
    