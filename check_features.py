import re
import json

with open('D:/Plastroots_Website/src/data/ProductsServicesData.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Since parsing raw JS is tricky, we'll try to find the "features" lines
lines = text.split('\n')
in_features = False
features_content = []
for i, line in enumerate(lines):
    if '"features": [' in line or 'features: [' in line:
        in_features = True
        features_content.append(f"--- Line {i} ---")
    if in_features:
        features_content.append(line.strip())
        if '],' in line or ']' in line and not line.strip().endswith('{'):
            # simple heuristic
            if line.strip() == '],' or line.strip() == ']':
                in_features = False

print('\n'.join(features_content))
