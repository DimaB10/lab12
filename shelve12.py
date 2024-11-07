import shelve
D1 = {
    'Toyota Camry': 203,
    'Honda Accord': 192,
    'Ford Focus': 160,
    'Chevrolet Malibu': 250,
    'Nissan Altima': 188,
    'Mazda 6': 227,
    'Volkswagen Passat': 174
}
with shelve.open('file1.dat') as db:
    db['D1'] = D1
with shelve.open('file1.dat', writeback=True) as db:
    for _ in range(3):
        model = input("Введіть назву моделі автомобіля: ")
        power = int(input("Введіть потужність двигуна (в к.с.): "))
        db['D1'][model] = power
    db.sync()
print("Словник оновлено та збережено у файл file1.dat.")
with shelve.open('file1.dat') as db:
    loaded_dict = db['D1']
print("Зчитаний словник:")
for model, power in loaded_dict.items():
    print(f"{model}: {power} к.с.")
