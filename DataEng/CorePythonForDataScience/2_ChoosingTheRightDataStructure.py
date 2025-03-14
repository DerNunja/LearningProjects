# 1. Listen (list)
# Mutable (veränderbar), indizierte Elemente, lineare Suchzeit O(N)
my_list = [1, 2, 3, 4]
my_list.append(5)  # Fügt 5 ans Ende hinzu
print("Liste:", my_list)  # [1, 2, 3, 4, 5]

# 2. Tupel (tuple)
# Immutable (unveränderbar), indizierte Elemente, lineare Suchzeit O(N)
my_tuple = (1, 2, 3, 4)
print("Tupel:", my_tuple[1])  # 2

# 3. Mengen (set)
# Ungeordnet (keine Indizes), einzigartige Werte, schnelle Mitgliedschaftsprüfung O(log(N))
my_list = [1, 2, 2, 3, 4, 4]
my_set = set(my_list)
print("Menge:", my_set)  # {1, 2, 3, 4} (keine Duplikate)

# Vergleich der Suchgeschwindigkeit
big_list = [str(i) for i in range(10000000)]
print("abc" in big_list)  # Langsam (ca. 0.2 sec)
big_set = set(big_list)
print("abc" in big_set)  # Schnell (15–30 μsec)

# 4. Wörterbücher (dict)
# Key-Value-Speicher, schnelle Nachschlagezeit O(log(N))
my_dict = {"a": 1, "b": 2, "c": 3}
print("Dictionary:", my_dict["b"])  # 2

# Erstellen eines Dictionaries mit enumerate()
seq = ["alpha", "bravo", "charlie", "delta"]
print("Dict mit enumerate:", dict(enumerate(seq)))

# Erstellen eines Dictionaries mit zip()
keys = "abcd"
values = ["alpha", "bravo", "charlie", "delta"]
print("Dict mit zip:", dict(zip(keys, values)))

# 5. Generatoren
# Iteratoren, die Elemente nach Bedarf erzeugen (lazy evaluation)
my_generator = (x**2 for x in range(5))
print("Generator als Liste:", list(my_generator))  # [0, 1, 4, 9, 16]