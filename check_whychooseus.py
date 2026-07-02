import re

with open('D:/Plastroots_Website/src/data/ProductsServicesData.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'whyChooseUs:' in line:
        print(f"Line {i+1}:")
        for j in range(i, min(i+10, len(lines))):
            print(lines[j].strip())
        print("-" * 40)
