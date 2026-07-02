import re
import json

file_path = r"D:\Plastroots_Website\src\data\ProductsServicesData.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will inject overviewDetails and gallery into every service if they don't exist.

services = {
    # Corporate Compliance
    "epr": {
        "title": "Extended Producer Responsibility (EPR)",
        "overview": "/Images/EPR_1.png",
        "gallery": [
            ("Registration & Authorization", "/Images/Plastic_Waste.png"),
            ("Credit Procurement", "/Images/Electronic_Waste.png"),
            ("Record Management", "/Images/Battery_Waste.png"),
            ("Compliance Monitoring", "/Images/Tyre_Waste.png"),
            ("Audit Support", "/Images/Oil_Waste.png")
        ]
    },
    "carbon-market": {
        "title": "Carbon Market Advisory",
        "overview": "/Images/Carbon.png",
        "gallery": [
            ("Footprint Assessment", "/Images/Methane.png"),
            ("GHG Inventory", "/Images/Carbon.png"),
            ("Credit Advisory", "/Images/Envo_impact.png"),
            ("Reduction Planning", "/Images/Energy_Efficiency.png"),
            ("Trading Support", "/Images/Carbon.png")
        ]
    },
    "esg-consulting": {
        "title": "ESG Consulting",
        "overview": "/Images/ESG_Consulting.png",
        "gallery": [
            ("Assessments & Gap Analysis", "/Images/Envo_impact.png"),
            ("Sustainability Reporting", "/Images/Social_Responsibility.png"),
            ("Framework Alignment", "/Images/Corpo_Gov.png"),
            ("KPI Monitoring", "/Images/ESG_Consulting.png"),
            ("Impact Assessment", "/Images/Envo_impact.png")
        ]
    },
    # Government Services Section A
    "swm": {
        "title": "Solid Waste Management (SWM)",
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
        "title": "Environmental & Sustainability Projects",
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
        "title": "Supply Tenders",
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
        "title": "Survey, IT & Consultancy Services",
        "overview": "https://loremflickr.com/800/600/survey,drone?lock=160",
        "gallery": [
            ("Project Consultancy", "https://loremflickr.com/800/600/consultants,meeting?lock=161"),
            ("Application Support", "https://loremflickr.com/800/600/software,support?lock=162"),
            ("DPR Preparation", "https://loremflickr.com/800/600/infrastructure,planning?lock=163"),
            ("Technical Consulting", "https://loremflickr.com/800/600/technical,expert?lock=164"),
            ("Regulatory Consulting", "https://loremflickr.com/800/600/lawyer,regulatory?lock=165")
        ]
    },
    # Government Services Section B
    "mrf-operations": {
        "title": "Material Recovery Facility Operations",
        "overview": "https://loremflickr.com/800/600/factory,recycling?lock=1",
        "gallery": [
            ("Sorting Line", "https://loremflickr.com/800/600/factory,worker?lock=10"),
            ("Baling Press", "https://loremflickr.com/800/600/machine,industrial?lock=11"),
            ("Conveyor System", "https://loremflickr.com/800/600/conveyor,belt?lock=12"),
            ("Material Segregation", "https://loremflickr.com/800/600/plastic,recycling?lock=13"),
            ("Facility Control", "https://loremflickr.com/800/600/control,room?lock=14")
        ]
    },
    "env-infra": {
        "title": "Environmental Infrastructure",
        "overview": "https://loremflickr.com/800/600/infrastructure,green?lock=20",
        "gallery": [
            ("Water Treatment", "https://loremflickr.com/800/600/water,treatment?lock=21"),
            ("Waste to Energy", "https://loremflickr.com/800/600/energy,plant?lock=22"),
            ("Green Buildings", "https://loremflickr.com/800/600/green,building?lock=23"),
            ("Smart Grid", "https://loremflickr.com/800/600/solar,panels?lock=24"),
            ("Sustainable Layout", "https://loremflickr.com/800/600/sustainable,city?lock=25")
        ]
    },
    "civil-infra": {
        "title": "Civil Infrastructure",
        "overview": "https://loremflickr.com/800/600/construction,site?lock=30",
        "gallery": [
            ("Road Construction", "https://loremflickr.com/800/600/road,construction?lock=31"),
            ("Bridge Work", "https://loremflickr.com/800/600/bridge,construction?lock=32"),
            ("Excavation", "https://loremflickr.com/800/600/excavator?lock=33"),
            ("Structural Concrete", "https://loremflickr.com/800/600/concrete,building?lock=34"),
            ("Heavy Machinery", "https://loremflickr.com/800/600/crane,construction?lock=35")
        ]
    },
    "gardening": {
        "title": "Gardening / Horticulture",
        "overview": "https://loremflickr.com/800/600/garden,park?lock=40",
        "gallery": [
            ("Landscape Design", "https://loremflickr.com/800/600/landscaping?lock=41"),
            ("Urban Gardening", "https://loremflickr.com/800/600/urban,garden?lock=42"),
            ("Plant Nursery", "https://loremflickr.com/800/600/nursery,plants?lock=43"),
            ("Lawn Maintenance", "https://loremflickr.com/800/600/lawn,mower?lock=44"),
            ("Greenhouse", "https://loremflickr.com/800/600/greenhouse?lock=45")
        ]
    },
    "fire-smartcity": {
        "title": "Fire & Smart City Services",
        "overview": "https://loremflickr.com/800/600/fire,truck?lock=50",
        "gallery": [
            ("Smart Surveillance", "https://loremflickr.com/800/600/security,camera?lock=51"),
            ("Fire Safety Systems", "https://loremflickr.com/800/600/fire,extinguisher?lock=52"),
            ("Command Center", "https://loremflickr.com/800/600/smart,city,control?lock=53"),
            ("Emergency Response", "https://loremflickr.com/800/600/ambulance,emergency?lock=54"),
            ("Smart Lighting", "https://loremflickr.com/800/600/street,light?lock=55")
        ]
    },
    # Products
    "pet-bale": {
        "title": "PET Bale Trading",
        "overview": "https://loremflickr.com/800/600/plastic,bottles?lock=60",
        "gallery": [
            ("PET Sorting & Segregation", "https://loremflickr.com/800/600/plastic,sorting?lock=61"),
            ("PET Baling Process", "https://loremflickr.com/800/600/baler,plastic?lock=62"),
            ("Quality Assessed Bales", "https://loremflickr.com/800/600/plastic,bales?lock=63"),
            ("Inventory & Storage", "https://loremflickr.com/800/600/warehouse,inventory?lock=64"),
            ("Loading & Dispatch", "https://loremflickr.com/800/600/forklift,loading?lock=65")
        ]
    },
    "recycled-granules": {
        "title": "Recycled Plastic Granules",
        "overview": "https://loremflickr.com/800/600/plastic,pellets?lock=70",
        "gallery": [
            ("Plastic Extrusion", "https://loremflickr.com/800/600/extruder,plastic?lock=71"),
            ("Granule Washing", "https://loremflickr.com/800/600/industrial,washing?lock=72"),
            ("Finished PP/PE Granules", "https://loremflickr.com/800/600/plastic,pellets?lock=73"),
            ("Quality Testing", "https://loremflickr.com/800/600/laboratory,testing?lock=74"),
            ("Bagging & Packaging", "https://loremflickr.com/800/600/packaging,sacks?lock=75")
        ]
    },
    "plastic-grinding": {
        "title": "Plastic Grinding & Chips Trading",
        "overview": "https://loremflickr.com/800/600/shredder,industrial?lock=80",
        "gallery": [
            ("Plastic Shredding", "https://loremflickr.com/800/600/shredder,machine?lock=81"),
            ("Grinding Operations", "https://loremflickr.com/800/600/grinder,industrial?lock=82"),
            ("High-Quality Plastic Chips", "https://loremflickr.com/800/600/plastic,flakes?lock=83"),
            ("Material Sorting", "https://loremflickr.com/800/600/recycling,sorting?lock=84"),
            ("Bulk Material Feed", "https://loremflickr.com/800/600/hopper,feed?lock=85")
        ]
    },
    "industrial-scrap": {
        "title": "Industrial Scrap Trading",
        "overview": "https://loremflickr.com/800/600/scrap,metal?lock=90",
        "gallery": [
            ("Copper & Aluminium Scrap", "https://loremflickr.com/800/600/copper,wire?lock=91"),
            ("Tyre Waste Aggregation", "https://loremflickr.com/800/600/tires,waste?lock=92"),
            ("Industrial Plastic Scrap", "https://loremflickr.com/800/600/plastic,scrap?lock=93"),
            ("Heavy Metal Scrap Yard", "https://loremflickr.com/800/600/scrap,metal,yard?lock=94"),
            ("Scrap Loading & Transport", "https://loremflickr.com/800/600/truck,scrap?lock=95")
        ]
    }
}

def inject_structure(text, sec_id, data):
    # we can use split or regex
    # The id is usually id: "sec_id"
    # let's find the about block, and inject after it.
    pattern = r'(id\s*:\s*"' + sec_id + r'".*?about\s*:\s*"[^"]+",)'
    parts = re.split(pattern, text, flags=re.DOTALL)
    if len(parts) > 2:
        pre = parts[0]
        match = parts[1]
        post = parts[2]
        
        # build overviewDetails
        overview = f'''
                "overviewDetails": {{
                    "title": "{data["title"]}",
                    "imagePath": "{data["overview"]}",
                    "paragraphs": [
                        "We provide comprehensive end-to-end solutions tailored to this domain.",
                        "Our dedicated team ensures full compliance and operational efficiency."
                    ]
                }},
                "gallery": ['''
        
        for name, img in data["gallery"]:
            overview += f'''
                    {{
                        "name": "{name}",
                        "img": "{img}"
                    }},'''
        overview = overview.rstrip(',') + '''
                ],'''
                
        # Also let's convert `included: [` to `features: [` since my update_content.py earlier probably failed
        # actually update_content.py updated `included`? No, update_content.py looked for `"features"`.
        # I'll just append features if they are not there, but wait, update_content.py successfully updated features earlier?
        # NO! earlier update_content.py failed to find `"features":` so it silently did nothing for features!
        # The user was seeing the OLD text!
        # Oh wow, so my update_content.py was broken the whole time for the features array!
        # Let's fix that too.
        
        return pre + match + overview + post
    return text

new_content = content
for sec_id, data in services.items():
    new_content = inject_structure(new_content, sec_id, data)
    
# Now, to fix the features arrays for everything:
# my update_content.py from earlier looked for `"features": [` but it should have looked for `included: [`
# I will run a fast replace:
new_content = re.sub(r'included\s*:\s*\[', r'"features": [', new_content)
new_content = re.sub(r'includedList\s*:\s*\[', r'"features": [', new_content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Structure rebuilt successfully!")
