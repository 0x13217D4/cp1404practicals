FILENAME = "wimbledon.csv"
records = []
with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for line in in_file:
        record = line.strip().split(",")
        records.append(record)
champion_to_count = {}
countries = set()
for record in records:
    country = record[1]
    champion = record[2]
    if champion in champion_to_count:
        champion_to_count[champion] += 1
    else:
        champion_to_count[champion] = 1
    countries.add(country)
print("Wimbledon Champions:")
for champion, count in champion_to_count.items():
    print(f"{champion} {count}")
print(f"\nThese {len(countries)} countries have won Wimbledon:")
print(", ".join(sorted(countries)))