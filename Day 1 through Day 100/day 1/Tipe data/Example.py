# Program Profil Pengguna Sederhana

# 1. Definisi Data
user = {
    "username": "coder_pemula",
    "age": 20,                # int
    "height": 168.5,          # float
    "skills": ["Python", "Git"], # list
    "is_verified": False,     # bool
    "website": None           # None
}

# 2. Manipulasi Data
user["skills"].append("HTML") # Menambah skill
user["is_verified"] = True    # Mengubah status boolean

# 3. Menampilkan Informasi
print(f"User: {user['username']}")
print(f"Umur: {user['age']} tahun")
print(f"Skill: {', '.join(user['skills'])}")
print(f"Status Verifikasi: {user['is_verified']}")