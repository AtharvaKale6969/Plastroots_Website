import re
import json

file_path = r"D:\Plastroots_Website\src\data\ProductsServicesData.js"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define specific replacements for intros, taglines, and closings
# We'll use regex to find the blocks and replace the specific fields

replacements = {
    # 1. Corporate Compliance
    "corporate-compliance": {
        "intro": "Helping businesses meet regulatory requirements while advancing their sustainability goals.",
    },
    "epr": {
        "detailTagline": "Stay ahead of evolving regulatory obligations with end-to-end EPR compliance support.",
        "features": [
            ("EPR Registration & Authorization", "Comprehensive support for registration and authorizations."),
            ("EPR Credit Procurement & Fulfilment", "Procurement and fulfilment of required EPR credits."),
            ("Documentation & Record Management", "Detailed management of records and documentation."),
            ("Return Filing & Compliance Monitoring", "Ongoing monitoring and filing of regulatory returns."),
            ("Regulatory Liaison & Audit Support", "Expert liaison with authorities and audit support.")
        ],
        "closing": "We ensure seamless compliance across every stage of your EPR journey.",
        "gallery_titles": ["Registration & Authorization", "Credit Procurement", "Record Management", "Compliance Monitoring", "Audit Support"]
    },
    "carbon-market": {
        "detailTagline": "Turn sustainability initiatives into measurable environmental and business value.",
        "features": [
            ("Carbon Footprint Assessment", "Detailed assessment of your carbon footprint."),
            ("Greenhouse Gas (GHG) Inventory Preparation", "Preparation of comprehensive GHG inventories."),
            ("Carbon Credit Advisory", "Expert advisory on carbon credits."),
            ("Emission Reduction Planning", "Strategic planning for emission reduction."),
            ("Sustainability Documentation", "Comprehensive sustainability documentation."),
            ("Carbon Credit Trading Support", "Support for carbon credit trading.")
        ],
        "closing": "Helping organizations measure, manage, and monetize their carbon performance.",
        "gallery_titles": ["Footprint Assessment", "GHG Inventory", "Credit Advisory", "Reduction Planning", "Trading Support"]
    },
    "esg-consulting": {
        "detailTagline": "Supporting businesses in building responsible, resilient, and future-ready operations.",
        "features": [
            ("ESG Assessments & Gap Analysis", "Thorough assessments and gap analysis."),
            ("Sustainability Reporting", "Comprehensive sustainability reporting."),
            ("ESG Framework Alignment", "Alignment with major ESG frameworks."),
            ("KPI Development & Performance Monitoring", "Development and monitoring of key performance indicators."),
            ("Impact Assessment & Disclosure", "Detailed impact assessment and disclosure.")
        ],
        "closing": "Developing practical ESG strategies that align business performance with stakeholder expectations.",
        "gallery_titles": ["Assessments & Gap Analysis", "Sustainability Reporting", "Framework Alignment", "KPI Monitoring", "Impact Assessment"]
    },

    # 2. Government Services
    "government-services": {
        "intro": "Comprehensive waste management, environmental, infrastructure, and consulting solutions for Gram Panchayats, Municipal Councils, and Municipal Corporations.",
    },
    "section-a": {
        "description": "All services listed under Section A are executed directly by Plastroots through its in-house team and operational network."
    },
    "section-b": {
        "description": "Services under Section B are delivered through approved and experienced partner organizations, with project coordination, management, and support provided by Plastroots wherever applicable."
    },
    "swm": {
        "features": [
            ("Door-to-Door Waste Collection & Transportation", "Efficient collection and transportation services."),
            ("Refuse Derived Fuel (RDF) Management", "Comprehensive management of RDF."),
            ("Street Sweeping Services", "Dedicated street sweeping services."),
            ("IEC (Information, Education & Communication) Programs", "Public awareness and education programs."),
            ("DPR Preparation for SWM Projects", "Detailed Project Report preparation."),
            ("End-to-End SWM Consulting & Project Support", "Complete consulting and project support.")
        ]
    },
    "env-projects": {
        "features": [
            ("Biofuel Supply Contracts", "Reliable biofuel supply contracts."),
            ("Plastic Waste Recycling Operations", "Efficient plastic waste recycling."),
            ("Biogas Plant Establishment & AMC", "Establishment and maintenance of biogas plants."),
            ("Composting Plant Setup & Management", "Setup and management of composting plants.")
        ]
    },
    "supply-tenders": {
        "features": [
            ("Waste Management Machinery Supply", "Supply of advanced waste management machinery."),
            ("Dustbins, Collection Vehicles & Equipment", "Supply of collection vehicles and equipment."),
            ("Office & Operational Supplies", "Comprehensive operational supplies.")
        ]
    },
    "survey-it": {
        "features": [
            ("Project Consultancy", "Expert project consultancy services."),
            ("Application Support Services", "Dedicated application support."),
            ("DPR Preparation for Infrastructure & Environmental Projects", "Preparation of Detailed Project Reports."),
            ("Technical & Regulatory Consulting Services", "Technical and regulatory consulting.")
        ]
    },
    "mrf-operations": {
        "detailTagline": "Efficient operation and management of Material Recovery Facilities to maximize resource recovery and minimize landfill disposal."
    },
    "env-infra": {
        "features": [
            ("Sewage Treatment Plant (STP) Operations", "Operation of Sewage Treatment Plants."),
            ("Environmental Facility Management", "Comprehensive environmental facility management.")
        ]
    },
    "civil-infra": {
        "features": [
            ("Road Construction (CC & Asphalt Roads)", "Construction of CC and Asphalt roads."),
            ("Institutional & Public Building Construction", "Construction of public and institutional buildings."),
            ("Footpath Development & Urban Beautification", "Development of footpaths and urban beautification.")
        ]
    },
    "gardening": {
        "features": [
            ("Tree Plantation & Supply", "Supply and plantation of trees."),
            ("Garden Development & Maintenance", "Development and maintenance of gardens."),
            ("Landscape Material Supply", "Supply of landscape materials.")
        ]
    },
    "fire-smartcity": {
        "features": [
            ("Fire-Fighting System Installation", "Installation of fire-fighting systems."),
            ("Fire Alarm & Detection Systems", "Installation of alarm and detection systems."),
            ("Fire Safety Audits & Compliance", "Comprehensive fire safety audits."),
            ("Fire Equipment Supply", "Supply of fire safety equipment.")
        ]
    },

    # 3. Products
    "products": {
        "intro": "Reliable sourcing, processing, and supply of recyclable materials to support India's growing circular economy."
    },
    "pet-bale": {
        "detailTagline": "We procure PET bale material through an extensive network of small and medium-scale vendors across India. After quality assessment and aggregation, the material is supplied to leading recycling companies and processors.",
        "closing": "Our sourcing network ensures a consistent supply of quality PET feedstock to the recycling industry."
    },
    "recycled-granules": {
        "detailTagline": "We manufacture and trade high-quality recycled plastic granules for industrial and commercial applications.",
        "features": [
            ("PP (Polypropylene)", "High-quality PP granules."),
            ("LDPE (Low-Density Polyethylene)", "High-quality LDPE granules."),
            ("HDPE (High-Density Polyethylene)", "High-quality HDPE granules.")
        ],
        "closing": "Our operations include sourcing recyclable plastic waste, processing through advanced recycling systems, and supplying finished granules to manufacturers across India."
    },
    "plastic-grinding": {
        "detailTagline": "We source plastic scrap from industrial units, scrap dealers, and recycling channels, processing it into high-quality plastic chips through specialized grinding operations.",
        "closing": "These materials are supplied to recyclers, manufacturers, and preprocessing units across the country."
    },
    "industrial-scrap": {
        "detailTagline": "We deal in a wide range of industrial scrap and recyclable materials, supporting responsible resource recovery and material reuse.",
        "features": [
            ("Copper Scrap", "High-quality copper scrap."),
            ("Aluminium Scrap", "High-quality aluminium scrap."),
            ("Tyre Waste", "Tyre waste for recycling."),
            ("Plastic Drums", "Used plastic drums."),
            ("Industrial Plastic Scrap", "Scrap from industrial processes."),
            ("Mixed Recyclable Materials", "Various recyclable materials.")
        ],
        "closing": "Through responsible sourcing and supply, we help divert valuable materials from landfills and return them to productive use."
    }
}

def update_section(content, section_id, data):
    # Find the block for the given ID. We will search for `"id": "section_id"` or `"id": 'section_id'`
    pattern = r'("id"\s*:\s*"' + section_id + r'")'
    parts = re.split(pattern, content)
    if len(parts) < 3:
        return content
    
    pre = parts[0]
    id_str = parts[1]
    post = parts[2]
    
    # We will only apply regex to the 'post' part up to the next major 'id' or end of block, 
    # but since it's hard to find boundaries reliably, we'll replace the first occurrence of fields 
    # within a reasonable character limit (e.g., next 3000 chars)
    
    # helper function to replace a specific key
    def replace_key(text, key, new_val):
        # looks for "key": "old_val" or "key": [old_val]
        # For strings:
        if isinstance(new_val, str):
            escaped_val = new_val.replace('"', '\\"')
            return re.sub(r'("' + key + r'"\s*:\s*")[^"]*(")', r'\g<1>' + escaped_val + r'\g<2>', text, count=1)
        return text

    def replace_paragraphs(text, new_val):
        # For detailTagline, we might want to just replace the first paragraph in overviewDetails if detailTagline doesn't exist
        # But actually in this file structure detailTagline exists.
        return replace_key(text, "detailTagline", new_val)
        
    def replace_features(text, features_list):
        # find "features": [ ... ]
        # we will replace the whole array.
        feat_str = '"features": [\n'
        for title, desc in features_list:
            feat_str += f'                    {{\n                        "icon": "CheckCircle",\n                        "title": "{title}",\n                        "desc": "{desc}"\n                    }},\n'
        # remove last comma
        feat_str = feat_str.rstrip(",\n") + '\n                ]'
        
        # replace old features array
        # regex to match "features": [ ... ] where ... can be anything until the matching bracket
        # Since regex for nested brackets is hard, we can assume features doesn't have nested arrays.
        text = re.sub(r'"features"\s*:\s*\[.*?\]', feat_str, text, flags=re.DOTALL, count=1)
        return text
        
    def replace_gallery_titles(text, titles):
        # replace the "name": "..." for the first N gallery items
        for i, title in enumerate(titles):
            # This is a bit tricky, we will find "name": "something" and replace them in order
            # We will use a lambda function with a counter
            pass # skipping this as I already renamed galleries to good names in the previous step,
                 # but for EPR/Carbon/ESG the user specifically provided bullet points.
                 # Actually, it's fine to leave the gallery titles I just created, or update them.
                 # Let's update them if provided.
        if titles:
            def replacer(match):
                replacer.count += 1
                if replacer.count <= len(titles):
                    return f'"name": "{titles[replacer.count - 1]}"'
                return match.group(0)
            replacer.count = 0
            text = re.sub(r'"name"\s*:\s*"[^"]+"', replacer, text, count=len(titles))
        return text

    # Apply updates
    if "intro" in data:
        post = replace_key(post, "intro", data["intro"])
    if "description" in data:
        post = replace_key(post, "description", data["description"])
    if "detailTagline" in data:
        post = replace_key(post, "detailTagline", data["detailTagline"])
    if "closing" in data:
        post = replace_key(post, "closing", data["closing"])
    if "features" in data:
        post = replace_features(post, data["features"])
    if "gallery_titles" in data:
        # Extract the gallery block first to not mess up other names
        gallery_match = re.search(r'"gallery"\s*:\s*\[.*?\]', post, flags=re.DOTALL)
        if gallery_match:
            gallery_block = gallery_match.group(0)
            new_gallery_block = replace_gallery_titles(gallery_block, data["gallery_titles"])
            post = post.replace(gallery_block, new_gallery_block, 1)

    return pre + id_str + post

new_content = content
for sec_id, data in replacements.items():
    new_content = update_section(new_content, sec_id, data)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Content updated successfully!")
