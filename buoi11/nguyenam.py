s = "I love python"

NGUYEN_AM = "AEIOU"

kq = filter(lambda s1: str(s1).upper() in NGUYEN_AM, s)

print(f"Có{len(set(list(kq)))} nguyen am trong chuoi duoc tim thay")