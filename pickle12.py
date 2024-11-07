import pickle
def generate_progression(a, d, n):
    return [a + i * d for i in range(n)]
progression1 = generate_progression(0.7, 2.7, 40)
progression2 = generate_progression(4.3, 5.2, 38)
common_elements = set(progression1) & set(progression2)
with open('digits.bin', 'wb') as f:
    pickle.dump(common_elements, f)
with open('digits.bin', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)