symptoms = []
temperatures = []

for _ in range(3):
    symptom, temp = input().split()
    symptoms.append(symptom)
    temperatures.append(int(temp))

A_count = sum([1 for s, t in zip(symptoms, temperatures) if s == 'Y' and t >= 37])
B_count = sum([1 for s, t in zip(symptoms, temperatures) if s == 'N' and t >= 37])
C_count = sum([1 for s, t in zip(symptoms, temperatures) if s == 'Y' and t < 37])
D_count = sum([1 for s, t in zip(symptoms, temperatures) if s == 'N' and t < 37])

emergency = 'E' if A_count >= 2 else ''

print(f"{A_count} {B_count} {C_count} {D_count} {emergency}")