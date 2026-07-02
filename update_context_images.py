import re
import json

file_path = r"D:\Plastroots_Website\src\data\ProductsServicesData.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

fixes = {
    "swm": {
        "overview": "https://loremflickr.com/800/600/waste,management?lock=130",
        "gallery": [
            ("Door-to-Door Waste Collection", "https://loremflickr.com/800/600/garbage,truck?lock=131"),
            ("RDF Management", "https://loremflickr.com/800/600/fuel,waste?lock=132"),
            ("Street Sweeping", "https://loremflickr.com/800/600/street,sweeper?lock=133"),
            ("IEC Programs", "https://loremflickr.com/800/600/education,community?lock=134"),
            ("DPR Preparation", "https://loremflickr.com/800/600/project,report?lock=135")
        ]
    },
    "env-projects": {
        "overview": "https://loremflickr.com/800/600/environmental,project?lock=140",
        "gallery": [
            ("Biofuel Supply", "https://loremflickr.com/800/600/biofuel,energy?lock=141"),
            ("Plastic Waste Recycling", "https://loremflickr.com/800/600/recycling,plastic?lock=142"),
            ("Biogas Plant", "https://loremflickr.com/800/600/biogas,plant?lock=143"),
            ("Composting Plant", "https://loremflickr.com/800/600/compost,facility?lock=144"),
            ("Project Management", "https://loremflickr.com/800/600/management,green?lock=145")
        ]
    },
    "supply-tenders": {
        "overview": "https://loremflickr.com/800/600/supply,chain?lock=150",
        "gallery": [
            ("Waste Machinery Supply", "https://loremflickr.com/800/600/machinery,industrial?lock=151"),
            ("Dustbins & Vehicles", "https://loremflickr.com/800/600/dustbin,truck?lock=152"),
            ("Office & Operational Supplies", "https://loremflickr.com/800/600/office,supplies?lock=153"),
            ("Tender Bidding", "https://loremflickr.com/800/600/contract,bidding?lock=154"),
            ("Logistics Support", "https://loremflickr.com/800/600/logistics,trucks?lock=155")
        ]
    },
    "survey-it": {
        "overview": "https://loremflickr.com/800/600/survey,drone?lock=160",
        "gallery": [
            ("Project Consultancy", "https://loremflickr.com/800/600/consultants,meeting?lock=161"),
            ("Application Support", "https://loremflickr.com/800/600/software,support?lock=162"),
            ("DPR Preparation", "https://loremflickr.com/800/600/infrastructure,planning?lock=163"),
            ("Technical Consulting", "https://loremflickr.com/800/600/technical,expert?lock=164"),
            ("Regulatory Consulting", "https://loremflickr.com/800/600/lawyer,regulatory?lock=165")
        ]
    }
}

for sec_id, data in fixes.items():
    pattern = r'("id"\s*:\s*"' + sec_id + r'")'
    parts = re.split(pattern, content)
    if len(parts) > 2:
        pre = parts[0]
        id_str = parts[1]
        post = parts[2]
        
        # update overview image
        post = re.sub(r'"imagePath":\s*"[^"]+"', f'"imagePath": "{data["overview"]}"', post, count=1)
        
        # We need to replace the gallery array entirely.
        gallery_match = re.search(r'"gallery"\s*:\s*\[.*?\]', post, flags=re.DOTALL)
        if gallery_match:
            old_gallery = gallery_match.group(0)
            
            new_gallery = '"gallery": [\n'
            for idx, (name, img) in enumerate(data["gallery"]):
                new_gallery += f'                    {{\n                        "name": "{name}",\n                        "img": "{img}"\n                    }}'
                if idx < len(data["gallery"]) - 1:
                    new_gallery += ',\n'
                else:
                    new_gallery += '\n                ]'
                    
            post = post.replace(old_gallery, new_gallery, 1)
            content = pre + id_str + post

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Images updated for remaining context successfully!")
