from citypulse.database.repository import ComplaintRepository

repository = ComplaintRepository()

complaints = repository.get_all_complaints()

print(f"Found {len(complaints)} complaints\n")

for complaint in complaints[:5]:
    print(complaint)