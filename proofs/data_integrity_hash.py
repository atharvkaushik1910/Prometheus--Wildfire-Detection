import hashlib

def generate_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

original_data = "temperature=45;humidity=20;wind=30"
tampered_data = "temperature=50;humidity=20;wind=30"

print("Original Hash:", generate_hash(original_data))
print("Tampered Hash:", generate_hash(tampered_data))

