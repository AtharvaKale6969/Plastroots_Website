import re
import json

file_path = r"D:\Plastroots_Website\src\data\ProductsServicesData.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

fixes = {
    "pet-bale": {
        "gallery": [
            ("PET Sorting & Segregation", "https://loremflickr.com/800/600/plastic,sorting?lock=61"),
            ("PET Baling Process", "https://loremflickr.com/800/600/baler,plastic?lock=62"),
            ("Quality Assessed Bales", "https://loremflickr.com/800/600/plastic,bales?lock=63"),
            ("Inventory & Storage", "https://loremflickr.com/800/600/warehouse,inventory?lock=64"),
            ("Loading & Dispatch", "https://loremflickr.com/800/600/forklift,loading?lock=65")
        ]
    },
    "recycled-granules": {
        "gallery": [
            ("Plastic Extrusion", "https://loremflickr.com/800/600/extruder,plastic?lock=71"),
            ("Granule Washing", "https://loremflickr.com/800/600/industrial,washing?lock=72"),
            ("Finished PP/PE Granules", "https://loremflickr.com/800/600/plastic,pellets?lock=73"),
            ("Quality Testing", "https://loremflickr.com/800/600/laboratory,testing?lock=74"),
            ("Bagging & Packaging", "https://loremflickr.com/800/600/packaging,sacks?lock=75")
        ]
    },
    "plastic-grinding": {
        "gallery": [
            ("Plastic Shredding", "https://loremflickr.com/800/600/shredder,machine?lock=81"),
            ("Grinding Operations", "https://loremflickr.com/800/600/grinder,industrial?lock=82"),
            ("High-Quality Plastic Chips", "https://loremflickr.com/800/600/plastic,flakes?lock=83"),
            ("Material Sorting", "https://loremflickr.com/800/600/recycling,sorting?lock=84"),
            ("Bulk Material Feed", "https://loremflickr.com/800/600/hopper,feed?lock=85")
        ]
    },
    "industrial-scrap": {
        "gallery": [
            ("Copper & Aluminium Scrap", "https://loremflickr.com/800/600/copper,wire?lock=91"),
            ("Tyre Waste Aggregation", "https://loremflickr.com/800/600/tires,waste?lock=92"),
            ("Industrial Plastic Scrap", "https://loremflickr.com/800/600/plastic,scrap?lock=93"),
            ("Heavy Metal Scrap Yard", "https://loremflickr.com/800/600/scrap,metal,yard?lock=94"),
            ("Scrap Loading & Transport", "https://loremflickr.com/800/600/truck,scrap?lock=95")
        ]
    }
}

for sec_id, data in fixes.items():
    # Find the block for sec_id
    pattern = r'("id"\s*:\s*"' + sec_id + r'")'
    parts = re.split(pattern, content)
    if len(parts) > 2:
        pre = parts[0]
        id_str = parts[1]
        post = parts[2]
        
        # We need to replace the gallery array entirely.
        gallery_match = re.search(r'"gallery"\s*:\s*\[.*?\]', post, flags=re.DOTALL)
        if gallery_match:
            old_gallery = gallery_match.group(0)
            
            new_gallery = '"gallery": [\n'
            for idx, (name, img) in enumerate(data["gallery"]):
                new_gallery += f'                    {{\n                        "name": "{name}",\n                        "img": "{img}"\n                    }}'
                if idx < 4:
                    new_gallery += ',\n'
                else:
                    new_gallery += '\n                ]'
                    
            post = post.replace(old_gallery, new_gallery, 1)
            content = pre + id_str + post

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Product galleries fixed successfully!")
