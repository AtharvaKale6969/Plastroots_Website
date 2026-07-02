import re
import os

file_path = r"D:\Plastroots_Website\src\data\ProductsServicesData.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the replacements for each section
# We will use targeted loremflickr with lock parameters to ensure stable, relevant images
sections = [
    {
        "id": "mrf-operations",
        "overview": "https://loremflickr.com/800/600/factory,recycling?lock=1",
        "gallery": [
            ("Sorting Line", "https://loremflickr.com/800/600/factory,worker?lock=10"),
            ("Baling Press", "https://loremflickr.com/800/600/machine,industrial?lock=11"),
            ("Conveyor System", "https://loremflickr.com/800/600/conveyor,belt?lock=12"),
            ("Material Segregation", "https://loremflickr.com/800/600/plastic,recycling?lock=13"),
            ("Facility Control", "https://loremflickr.com/800/600/control,room?lock=14")
        ]
    },
    {
        "id": "env-infra",
        "overview": "https://loremflickr.com/800/600/infrastructure,green?lock=20",
        "gallery": [
            ("Water Treatment", "https://loremflickr.com/800/600/water,treatment?lock=21"),
            ("Waste to Energy", "https://loremflickr.com/800/600/energy,plant?lock=22"),
            ("Green Buildings", "https://loremflickr.com/800/600/green,building?lock=23"),
            ("Smart Grid", "https://loremflickr.com/800/600/solar,panels?lock=24"),
            ("Sustainable Layout", "https://loremflickr.com/800/600/sustainable,city?lock=25")
        ]
    },
    {
        "id": "civil-infra",
        "overview": "https://loremflickr.com/800/600/construction,site?lock=30",
        "gallery": [
            ("Road Construction", "https://loremflickr.com/800/600/road,construction?lock=31"),
            ("Bridge Work", "https://loremflickr.com/800/600/bridge,construction?lock=32"),
            ("Excavation", "https://loremflickr.com/800/600/excavator?lock=33"),
            ("Structural Concrete", "https://loremflickr.com/800/600/concrete,building?lock=34"),
            ("Heavy Machinery", "https://loremflickr.com/800/600/crane,construction?lock=35")
        ]
    },
    {
        "id": "gardening",
        "overview": "https://loremflickr.com/800/600/garden,park?lock=40",
        "gallery": [
            ("Landscape Design", "https://loremflickr.com/800/600/landscaping?lock=41"),
            ("Urban Gardening", "https://loremflickr.com/800/600/urban,garden?lock=42"),
            ("Plant Nursery", "https://loremflickr.com/800/600/nursery,plants?lock=43"),
            ("Lawn Maintenance", "https://loremflickr.com/800/600/lawn,mower?lock=44"),
            ("Greenhouse", "https://loremflickr.com/800/600/greenhouse?lock=45")
        ]
    },
    {
        "id": "fire-smartcity",
        "overview": "https://loremflickr.com/800/600/fire,truck?lock=50",
        "gallery": [
            ("Smart Surveillance", "https://loremflickr.com/800/600/security,camera?lock=51"),
            ("Fire Safety Systems", "https://loremflickr.com/800/600/fire,extinguisher?lock=52"),
            ("Command Center", "https://loremflickr.com/800/600/smart,city,control?lock=53"),
            ("Emergency Response", "https://loremflickr.com/800/600/ambulance,emergency?lock=54"),
            ("Smart Lighting", "https://loremflickr.com/800/600/street,light?lock=55")
        ]
    },
    {
        "id": "pet-bale",
        "overview": "https://loremflickr.com/800/600/plastic,bottles?lock=60",
        "gallery": [
            ("PET Sorting", "https://loremflickr.com/800/600/plastic,sorting?lock=61"),
            ("Baling Process", "https://loremflickr.com/800/600/baler,machine?lock=62"),
            ("Stacked Bales", "https://loremflickr.com/800/600/plastic,bales?lock=63"),
            ("Quality Inspection", "https://loremflickr.com/800/600/inspector,factory?lock=64"),
            ("Loading", "https://loremflickr.com/800/600/forklift,loading?lock=65")
        ]
    },
    {
        "id": "recycled-granules",
        "overview": "https://loremflickr.com/800/600/plastic,pellets?lock=70",
        "gallery": [
            ("Extrusion Process", "https://loremflickr.com/800/600/extruder,machine?lock=71"),
            ("Granule Washing", "https://loremflickr.com/800/600/washing,machine,industrial?lock=72"),
            ("Packaging", "https://loremflickr.com/800/600/packaging,factory?lock=73"),
            ("Quality Testing", "https://loremflickr.com/800/600/laboratory,testing?lock=74"),
            ("Melt Filtration", "https://loremflickr.com/800/600/melting,plastic?lock=75")
        ]
    },
    {
        "id": "plastic-grinding",
        "overview": "https://loremflickr.com/800/600/shredder,industrial?lock=80",
        "gallery": [
            ("Shredding Machine", "https://loremflickr.com/800/600/shredder,machine?lock=81"),
            ("Plastic Flakes", "https://loremflickr.com/800/600/plastic,flakes?lock=82"),
            ("Sorting Bin", "https://loremflickr.com/800/600/recycling,bins?lock=83"),
            ("Blade Maintenance", "https://loremflickr.com/800/600/mechanic,tools?lock=84"),
            ("Material Feed", "https://loremflickr.com/800/600/hopper,industrial?lock=85")
        ]
    },
    {
        "id": "industrial-scrap",
        "overview": "https://loremflickr.com/800/600/scrap,metal?lock=90",
        "gallery": [
            ("Metal Scrap", "https://loremflickr.com/800/600/rust,metal?lock=91"),
            ("Sorting Yard", "https://loremflickr.com/800/600/junkyard?lock=92"),
            ("Scrap Loading", "https://loremflickr.com/800/600/excavator,scrap?lock=93"),
            ("Heavy Lifting", "https://loremflickr.com/800/600/crane,lifting?lock=94"),
            ("Transport", "https://loremflickr.com/800/600/truck,transport?lock=95")
        ]
    }
]

new_content = content
for sec in sections:
    sec_id = sec['id']
    overview_img = sec['overview']
    
    # regex to find the section block
    # We will find `"id": "sec_id"` and then within that block replace imagePath and gallery items.
    # To do this safely, we will split by `"id": "sec_id"` to find the specific block, modify it, and put it back.
    
    parts = new_content.split(f'"id": "{sec_id}",')
    if len(parts) > 1:
        block = parts[1]
        
        # replace imagePath
        block = re.sub(r'"imagePath":\s*"[^"]+"', f'"imagePath": "{overview_img}"', block, count=1)
        
        # replace gallery items
        for i in range(5):
            old_name_pattern = f'"name": "Service Area {i+1}"'
            new_name = f'"name": "{sec["gallery"][i][0]}"'
            
            # The img tag is right after the name tag usually
            # let's just do a manual replace for the Service Area 1 to 5 blocks
            # We look for:
            # "name": "Service Area X",
            # "img": "..."
            pattern = r'"name":\s*"Service Area ' + str(i+1) + r'",\s*"img":\s*"[^"]+"'
            replacement = f'"name": "{sec["gallery"][i][0]}",\n                                "img": "{sec["gallery"][i][1]}"'
            
            block = re.sub(pattern, replacement, block)
            
        new_content = parts[0] + f'"id": "{sec_id}",' + block

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Images updated successfully!")
