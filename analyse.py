with open("wards.csv") as f:
    lines = f.readlines()

for line in lines[1:]:  # Skip header row
    line = line.strip()
    if not line:  # Skip blank lines
        continue

    parts = line.split(",")
    if len(parts) < 2:  # Safety check: ensure at least 2 columns exist
        continue

    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:
        size = "large"
    else:
        size = "small"
    print(ward, "is", size)