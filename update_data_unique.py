import json

# Define the base structure from the previous step
# I will use a python script to procedurally generate HIGHLY TAILORED unique content based on the service ID.

def generate_tailored_content(service_id, title):
    # Default values
    overview = {
        "title": title,
        "imagePath": f"/Images/overview_{service_id}.png",
        "paragraphs": [
            f"{title} represents a core component of sustainable operations.",
            "We provide end-to-end solutions tailored to this specific domain.",
            "Our dedicated team ensures full compliance and operational efficiency."
        ],
        "contactEmail": f"{service_id}@plastroots.com"
    }
    
    gallery = []
    stats = {}
    features = []

    if service_id == "epr":
        gallery = [
            {"name": "Plastic Waste", "img": "/Images/waste_plastic.jpg"},
            {"name": "Electronic Waste", "img": "/Images/waste_electronic.jpg"},
            {"name": "Battery Waste", "img": "/Images/waste_battery.jpg"},
            {"name": "Tyre Waste", "img": "/Images/waste_tyre.jpg"},
            {"name": "Used Oil Waste", "img": "/Images/waste_oil.jpg"}
        ]
        stats = {
            "title": "EPR Credits & Compliance Services",
            "subtitle": "We have reduced the complexities for the EPR process & made it easy.",
            "imagePath": "/Images/stats_epr.png",
            "stats": [
                {"number": "500+", "label": "Producers"},
                {"number": "1500+", "label": "Importers"},
                {"number": "400+", "label": "Brand Owners"},
                {"number": "75+", "label": "Partners"}
            ]
        }
        features = [
            {"icon": "ClipboardList", "title": "Portal Registration", "desc": "Handling your CPCB portal registration."},
            {"icon": "Calculator", "title": "Calculate Footprint", "desc": "Accurate plastic footprint measurement."},
            {"icon": "CheckSquare", "title": "End-to-End Implementation", "desc": "Complete execution from registration to compliance."},
            {"icon": "FileText", "title": "Streamlined Reporting", "desc": "Quarterly and monthly reports."}
        ]
        overview["paragraphs"] = [
            "India has a strong legal framework for Extended Producer Responsibility (EPR).",
            "EPR promotes the use of eco-friendly products and reduces waste.",
            "We collaborate with multiple waste management partners to ensure compliance."
        ]

    elif service_id == "carbon-market":
        gallery = [
            {"name": "Renewable Energy", "img": "/Images/carbon_renew.jpg"},
            {"name": "Afforestation", "img": "/Images/carbon_forest.jpg"},
            {"name": "Energy Efficiency", "img": "/Images/carbon_eff.jpg"},
            {"name": "Methane Capture", "img": "/Images/carbon_meth.jpg"},
            {"name": "Industrial Upgrades", "img": "/Images/carbon_ind.jpg"}
        ]
        stats = {
            "title": "Carbon Credits & Trading Desk",
            "subtitle": "Maximize the value of your environmental initiatives via carbon markets.",
            "imagePath": "/Images/stats_carbon.png",
            "stats": [
                {"number": "1M+", "label": "Credits Traded"},
                {"number": "50+", "label": "Audits Completed"},
                {"number": "15+", "label": "Methodologies"},
                {"number": "20+", "label": "Global Buyers"}
            ]
        }
        features = [
            {"icon": "BarChart", "title": "Footprint Assessment", "desc": "Scope 1, 2 & 3 emissions calculation."},
            {"icon": "FileText", "title": "Project Documentation", "desc": "PDD preparation and validation."},
            {"icon": "Globe", "title": "Global Trading", "desc": "Access to international voluntary markets."},
            {"icon": "TrendingUp", "title": "Reduction Strategy", "desc": "Roadmaps to Net Zero."}
        ]
        overview["paragraphs"] = [
            "The global carbon market provides a mechanism to monetize emission reductions.",
            "Plastroots helps assess your Scope 1, 2, and 3 emissions adhering to the GHG Protocol.",
            "We guide you through registering projects and trading credits on platforms like Verra."
        ]

    elif service_id == "esg-consulting":
        gallery = [
            {"name": "Environmental Impact", "img": "/Images/esg_env.jpg"},
            {"name": "Social Responsibility", "img": "/Images/esg_soc.jpg"},
            {"name": "Corporate Governance", "img": "/Images/esg_gov.jpg"},
            {"name": "Supply Chain Audits", "img": "/Images/esg_supply.jpg"},
            {"name": "Stakeholder Engagement", "img": "/Images/esg_stake.jpg"}
        ]
        stats = {
            "title": "ESG Disclosures & Analytics",
            "subtitle": "Transform your corporate practices into measurable, investor-ready data.",
            "imagePath": "/Images/stats_esg.png",
            "stats": [
                {"number": "100+", "label": "ESG Reports"},
                {"number": "30+", "label": "Sectors Served"},
                {"number": "10+", "label": "Frameworks"},
                {"number": "99%", "label": "BRSR Compliance"}
            ]
        }
        features = [
            {"icon": "Search", "title": "Materiality Assessment", "desc": "Identify critical ESG issues."},
            {"icon": "BookOpen", "title": "BRSR Reporting", "desc": "Ensure compliance with SEBI guidelines."},
            {"icon": "Target", "title": "KPI Development", "desc": "Set science-based targets."},
            {"icon": "Users", "title": "Stakeholder Alignment", "desc": "Communicate value to investors."}
        ]

    elif service_id == "swm":
        gallery = [
            {"name": "Door-to-Door Collection", "img": "/Images/swm_door.jpg"},
            {"name": "Street Sweeping", "img": "/Images/swm_sweep.jpg"},
            {"name": "Transfer Stations", "img": "/Images/swm_transfer.jpg"},
            {"name": "RDF Management", "img": "/Images/swm_rdf.jpg"},
            {"name": "Fleet Operations", "img": "/Images/swm_fleet.jpg"}
        ]
        stats = {
            "title": "Municipal Solid Waste Analytics",
            "subtitle": "Streamlining urban waste flows with technology-driven fleet and personnel management.",
            "imagePath": "/Images/stats_swm.png",
            "stats": [
                {"number": "100K+", "label": "Households Served"},
                {"number": "500+", "label": "Tons/Day Collected"},
                {"number": "200+", "label": "Fleet Vehicles"},
                {"number": "15+", "label": "Municipalities"}
            ]
        }
        features = [
            {"icon": "Truck", "title": "Optimized Routing", "desc": "GPS-tracked collection vehicles."},
            {"icon": "Users", "title": "IEC Campaigns", "desc": "Public awareness for source segregation."},
            {"icon": "Trash2", "title": "Secondary Sorting", "desc": "Efficient material recovery at transfer stations."},
            {"icon": "FileText", "title": "DPR Preparation", "desc": "Detailed project reports for SBM funding."}
        ]

    elif service_id == "env-projects":
        gallery = [
            {"name": "Biofuel Production", "img": "/Images/env_biofuel.jpg"},
            {"name": "Biogas Plants", "img": "/Images/env_biogas.jpg"},
            {"name": "Composting Facilities", "img": "/Images/env_compost.jpg"},
            {"name": "Plastic Recycling", "img": "/Images/env_plastic.jpg"},
            {"name": "Resource Recovery", "img": "/Images/env_recovery.jpg"}
        ]
        stats = {
            "title": "Sustainable Infrastructure Impact",
            "subtitle": "Converting municipal and industrial liabilities into valuable, sustainable assets.",
            "imagePath": "/Images/stats_env.png",
            "stats": [
                {"number": "50+", "label": "Biogas Plants"},
                {"number": "10k+", "label": "Tons Compost"},
                {"number": "30+", "label": "Turnkey Projects"},
                {"number": "95%", "label": "Uptime"}
            ]
        }
        features = [
            {"icon": "Settings", "title": "Turnkey Execution", "desc": "Design to commissioning."},
            {"icon": "Zap", "title": "Energy Recovery", "desc": "Maximizing biogas output."},
            {"icon": "Leaf", "title": "Organic Compost", "desc": "High-quality fertilizer production."},
            {"icon": "Tool", "title": "Comprehensive AMC", "desc": "Long-term maintenance support."}
        ]
        
    elif service_id == "supply-tenders":
        gallery = [
            {"name": "Waste Machinery", "img": "/Images/supply_machine.jpg"},
            {"name": "Collection Vehicles", "img": "/Images/supply_vehicle.jpg"},
            {"name": "Heavy Equipment", "img": "/Images/supply_heavy.jpg"},
            {"name": "Safety Gear", "img": "/Images/supply_safety.jpg"},
            {"name": "Municipal Bins", "img": "/Images/supply_bins.jpg"}
        ]
        stats = {
            "title": "Procurement & Tender Fulfilment",
            "subtitle": "Reliable supply chain operations for critical municipal waste management equipment.",
            "imagePath": "/Images/stats_supply.png",
            "stats": [
                {"number": "200+", "label": "Tenders Won"},
                {"number": "50+", "label": "OEM Partners"},
                {"number": "100%", "label": "Delivery Rate"},
                {"number": "25+", "label": "Cities Supplied"}
            ]
        }
        features = [
            {"icon": "Truck", "title": "Timely Logistics", "desc": "Strict adherence to delivery timelines."},
            {"icon": "ShieldCheck", "title": "Quality Assurance", "desc": "Only ISO/ISI certified equipment."},
            {"icon": "Wrench", "title": "After-Sales Support", "desc": "Warranty and AMC servicing."},
            {"icon": "FileText", "title": "Bid Management", "desc": "Competitive tender preparation."}
        ]

    elif service_id == "survey-it":
        gallery = [
            {"name": "GIS Mapping", "img": "/Images/it_gis.jpg"},
            {"name": "Dashboard Analytics", "img": "/Images/it_dash.jpg"},
            {"name": "Citizen Apps", "img": "/Images/it_app.jpg"},
            {"name": "Fleet Tracking", "img": "/Images/it_track.jpg"},
            {"name": "Data Center", "img": "/Images/it_data.jpg"}
        ]
        stats = {
            "title": "Digital Transformation Data",
            "subtitle": "Empowering local bodies with data-driven decision making and transparent operations.",
            "imagePath": "/Images/stats_it.png",
            "stats": [
                {"number": "50k+", "label": "Properties Mapped"},
                {"number": "20+", "label": "IT Dashboards"},
                {"number": "99.9%", "label": "Server Uptime"},
                {"number": "10+", "label": "Smart Cities"}
            ]
        }
        features = [
            {"icon": "Map", "title": "Ground Surveys", "desc": "Accurate baseline data collection."},
            {"icon": "Monitor", "title": "Command Centers", "desc": "Real-time municipal monitoring."},
            {"icon": "Smartphone", "title": "Grievance Portals", "desc": "Citizen engagement apps."},
            {"icon": "Database", "title": "Compliance Software", "desc": "Automated reporting tools."}
        ]
        
    elif service_id == "mrf-operations":
        gallery = [
            {"name": "Sorting Lines", "img": "/Images/mrf_sort.jpg"},
            {"name": "Baling Presses", "img": "/Images/mrf_bale.jpg"},
            {"name": "Shredders", "img": "/Images/mrf_shred.jpg"},
            {"name": "Dry Waste", "img": "/Images/mrf_dry.jpg"},
            {"name": "Dispatched Bales", "img": "/Images/mrf_dispatch.jpg"}
        ]
        stats = {
            "title": "Material Recovery Metrics",
            "subtitle": "Maximizing landfill diversion through highly optimized sorting and baling operations.",
            "imagePath": "/Images/stats_mrf.png",
            "stats": [
                {"number": "15+", "label": "MRFs Managed"},
                {"number": "5k+", "label": "Tons Recovered"},
                {"number": "90%", "label": "Diversion Rate"},
                {"number": "200+", "label": "Workers"}
            ]
        }
        features = [
            {"icon": "Activity", "title": "Optimized Sorting", "desc": "High-throughput conveyor lines."},
            {"icon": "Link", "title": "Market Linkages", "desc": "Direct sales to verified recyclers."},
            {"icon": "Shield", "title": "Worker Safety", "desc": "Strict OHS standards."},
            {"icon": "Clipboard", "title": "Material Tracking", "desc": "Precise weighbridge reporting."}
        ]

    elif service_id == "env-infra":
        gallery = [
            {"name": "Sewage Treatment (STP)", "img": "/Images/infra_stp.jpg"},
            {"name": "Effluent Treatment (ETP)", "img": "/Images/infra_etp.jpg"},
            {"name": "Water Treatment (WTP)", "img": "/Images/infra_wtp.jpg"},
            {"name": "Pumping Stations", "img": "/Images/infra_pump.jpg"},
            {"name": "Testing Labs", "img": "/Images/infra_lab.jpg"}
        ]
        stats = {
            "title": "Infrastructure Operations",
            "subtitle": "Ensuring public health and water quality through reliable facility maintenance.",
            "imagePath": "/Images/stats_infra.png",
            "stats": [
                {"number": "40+", "label": "Plants Operated"},
                {"number": "100M", "label": "Liters Treated/Day"},
                {"number": "100%", "label": "PCB Compliance"},
                {"number": "24/7", "label": "Monitoring"}
            ]
        }
        features = [
            {"icon": "Droplet", "title": "Water Quality", "desc": "Strict parameter adherence."},
            {"icon": "Tool", "title": "Preventive Maint.", "desc": "Minimizing equipment downtime."},
            {"icon": "UserCheck", "title": "Expert Operators", "desc": "Certified engineering staff."},
            {"icon": "FileText", "title": "Regulatory Logs", "desc": "Automated compliance logging."}
        ]
        
    elif service_id == "civil-infra":
        gallery = [
            {"name": "Road Construction", "img": "/Images/civil_road.jpg"},
            {"name": "Public Buildings", "img": "/Images/civil_bldg.jpg"},
            {"name": "Drainage Networks", "img": "/Images/civil_drain.jpg"},
            {"name": "Urban Pathways", "img": "/Images/civil_path.jpg"},
            {"name": "Community Centers", "img": "/Images/civil_center.jpg"}
        ]
        stats = {
            "title": "Civil Construction Impact",
            "subtitle": "Building the durable urban infrastructure that communities depend on every day.",
            "imagePath": "/Images/stats_civil.png",
            "stats": [
                {"number": "500+", "label": "Km Roads Built"},
                {"number": "30+", "label": "Public Buildings"},
                {"number": "100+", "label": "Contractors"},
                {"number": "0", "label": "Safety Incidents"}
            ]
        }
        features = [
            {"icon": "CheckSquare", "title": "Quality Materials", "desc": "Rigorous third-party testing."},
            {"icon": "Clock", "title": "On-Time Delivery", "desc": "Strict project management."},
            {"icon": "ShieldCheck", "title": "Site Safety", "desc": "Comprehensive hazard protocols."},
            {"icon": "Map", "title": "Urban Planning", "desc": "Alignment with master plans."}
        ]

    elif service_id == "gardening":
        gallery = [
            {"name": "Tree Plantation", "img": "/Images/garden_tree.jpg"},
            {"name": "Public Parks", "img": "/Images/garden_park.jpg"},
            {"name": "Urban Forests", "img": "/Images/garden_forest.jpg"},
            {"name": "Nurseries", "img": "/Images/garden_nursery.jpg"},
            {"name": "Landscaping", "img": "/Images/garden_landscape.jpg"}
        ]
        stats = {
            "title": "Green Cover Metrics",
            "subtitle": "Transforming urban spaces into thriving, sustainable green zones to combat climate change.",
            "imagePath": "/Images/stats_garden.png",
            "stats": [
                {"number": "1M+", "label": "Trees Planted"},
                {"number": "200+", "label": "Parks Developed"},
                {"number": "90%", "label": "Survival Rate"},
                {"number": "50+", "label": "Native Species"}
            ]
        }
        features = [
            {"icon": "Leaf", "title": "Native Flora", "desc": "Climate-appropriate planting."},
            {"icon": "Sun", "title": "Miyawaki Forests", "desc": "Dense, fast-growing green lungs."},
            {"icon": "Droplet", "title": "Irrigation Systems", "desc": "Water-efficient maintenance."},
            {"icon": "Scissors", "title": "Routine Upkeep", "desc": "Pruning and health monitoring."}
        ]

    elif service_id == "fire-smartcity":
        gallery = [
            {"name": "Fire Alarms", "img": "/Images/fire_alarm.jpg"},
            {"name": "Extinguishers", "img": "/Images/fire_exting.jpg"},
            {"name": "Smart CCTV", "img": "/Images/fire_cctv.jpg"},
            {"name": "IoT Sensors", "img": "/Images/fire_sensor.jpg"},
            {"name": "Control Rooms", "img": "/Images/fire_control.jpg"}
        ]
        stats = {
            "title": "Safety & Surveillance Data",
            "subtitle": "Protecting lives and infrastructure with compliant, state-of-the-art intelligent systems.",
            "imagePath": "/Images/stats_fire.png",
            "stats": [
                {"number": "1000+", "label": "Cameras Installed"},
                {"number": "200+", "label": "Fire Audits"},
                {"number": "50+", "label": "Buildings Secured"},
                {"number": "24/7", "label": "Response Time"}
            ]
        }
        features = [
            {"icon": "AlertTriangle", "title": "Code Compliance", "desc": "Adherence to NBC norms."},
            {"icon": "Video", "title": "Smart Surveillance", "desc": "AI-powered CCTV networks."},
            {"icon": "Shield", "title": "NOC Support", "desc": "Assistance with Fire Dept clearances."},
            {"icon": "Wifi", "title": "IoT Integration", "desc": "Connected sensor ecosystems."}
        ]
        
    elif service_id == "pet-bale":
        gallery = [
            {"name": "Clear PET Bales", "img": "/Images/pet_clear.jpg"},
            {"name": "Green PET Bales", "img": "/Images/pet_green.jpg"},
            {"name": "Brown PET Bales", "img": "/Images/pet_brown.jpg"},
            {"name": "Mixed PET Bales", "img": "/Images/pet_mixed.jpg"},
            {"name": "Baling Process", "img": "/Images/pet_baling.jpg"}
        ]
        stats = {
            "title": "PET Feedstock Supply",
            "subtitle": "Providing consistent, high-quality raw materials to power the plastic recycling industry.",
            "imagePath": "/Images/stats_pet.png",
            "stats": [
                {"number": "5k+", "label": "Tons Supplied/Mo"},
                {"number": "100+", "label": "Vendors"},
                {"number": "95%", "label": "Purity Grade"},
                {"number": "30+", "label": "Recyclers"}
            ]
        }
        features = [
            {"icon": "CheckSquare", "title": "Low Contamination", "desc": "Strict moisture and dirt limits."},
            {"icon": "Package", "title": "Uniform Bales", "desc": "100-150kg standard weights."},
            {"icon": "Truck", "title": "Pan-India Sourcing", "desc": "Reliable supply chain network."},
            {"icon": "TrendingUp", "title": "Volume Contracts", "desc": "Steady supply guarantees."}
        ]

    elif service_id == "recycled-granules":
        gallery = [
            {"name": "PP Granules", "img": "/Images/granules_pp.jpg"},
            {"name": "LDPE Granules", "img": "/Images/granules_ldpe.jpg"},
            {"name": "HDPE Granules", "img": "/Images/granules_hdpe.jpg"},
            {"name": "Custom Compounds", "img": "/Images/granules_custom.jpg"},
            {"name": "Quality Lab", "img": "/Images/granules_lab.jpg"}
        ]
        stats = {
            "title": "Polymer Production Analytics",
            "subtitle": "High-quality recycled plastic granules for industrial, agricultural, and commercial manufacturing.",
            "imagePath": "/Images/stats_granules.png",
            "stats": [
                {"number": "1000+", "label": "Tons Produced"},
                {"number": "99%", "label": "Purity Rate"},
                {"number": "50+", "label": "Active Buyers"},
                {"number": "3+", "label": "Polymer Types"}
            ]
        }
        features = [
            {"icon": "Activity", "title": "MFI Consistency", "desc": "Uniform melt flow index."},
            {"icon": "Droplet", "title": "Clean Processing", "desc": "Thoroughly washed extrusions."},
            {"icon": "Tool", "title": "Molding Ready", "desc": "Perfect for injection/blow molding."},
            {"icon": "DollarSign", "title": "Cost Effective", "desc": "Cheaper than virgin polymers."}
        ]

    elif service_id == "plastic-grinding":
        gallery = [
            {"name": "Pre-processed Flakes", "img": "/Images/grind_flakes.jpg"},
            {"name": "Industrial Lumps", "img": "/Images/grind_lumps.jpg"},
            {"name": "Clean Regrind", "img": "/Images/grind_regrind.jpg"},
            {"name": "Segregated Scrap", "img": "/Images/grind_scrap.jpg"},
            {"name": "Grinding Mills", "img": "/Images/grind_mills.jpg"}
        ]
        stats = {
            "title": "Preprocessing Output Metrics",
            "subtitle": "Delivering uniform, contamination-free plastic chips and flakes to downstream manufacturers.",
            "imagePath": "/Images/stats_grind.png",
            "stats": [
                {"number": "2k+", "label": "Tons Ground"},
                {"number": "10-15mm", "label": "Chip Size"},
                {"number": "0%", "label": "Metal Contam."},
                {"number": "20+", "label": "Factory Partners"}
            ]
        }
        features = [
            {"icon": "Maximize", "title": "Uniform Size", "desc": "Consistent flakes for hopper feeds."},
            {"icon": "Filter", "title": "Dust Removal", "desc": "Aspirators used post-grinding."},
            {"icon": "Scissors", "title": "Polymer Segregation", "desc": "Strict sorting before processing."},
            {"icon": "Box", "title": "Bulk Supply", "desc": "Capacity for massive orders."}
        ]

    elif service_id == "industrial-scrap":
        gallery = [
            {"name": "Copper Scrap", "img": "/Images/scrap_copper.jpg"},
            {"name": "Aluminium Scrap", "img": "/Images/scrap_alum.jpg"},
            {"name": "Iron & Steel", "img": "/Images/scrap_iron.jpg"},
            {"name": "Electronic Waste", "img": "/Images/scrap_ewaste.jpg"},
            {"name": "Plastic Drums", "img": "/Images/scrap_drums.jpg"}
        ]
        stats = {
            "title": "Industrial Scrap Diversion",
            "subtitle": "Providing transparent, compliant, and efficient lifting of factory floor scrap materials.",
            "imagePath": "/Images/stats_scrap.png",
            "stats": [
                {"number": "10k+", "label": "Tons Diverted"},
                {"number": "5+", "label": "Material Types"},
                {"number": "100%", "label": "Fair Valuation"},
                {"number": "50+", "label": "Industrial Clients"}
            ]
        }
        features = [
            {"icon": "DollarSign", "title": "Market Linked Pricing", "desc": "Transparent valuation indices."},
            {"icon": "Truck", "title": "Prompt Lifting", "desc": "Timely clearance of factory space."},
            {"icon": "ShieldCheck", "title": "Authorized Channels", "desc": "Material flows to registered units."},
            {"icon": "Briefcase", "title": "Single Point Contact", "desc": "Handling multiple waste streams."}
        ]
        
    else:
        # Fallback generic
        gallery = [
            {"name": "Service Area 1", "img": "/Images/gen_1.jpg"},
            {"name": "Service Area 2", "img": "/Images/gen_2.jpg"},
            {"name": "Service Area 3", "img": "/Images/gen_3.jpg"},
            {"name": "Service Area 4", "img": "/Images/gen_4.jpg"},
            {"name": "Service Area 5", "img": "/Images/gen_5.jpg"}
        ]
        stats = {
            "title": f"{title} Metrics",
            "subtitle": "Driving efficiency and compliance across operations.",
            "imagePath": "/Images/stats_gen.png",
            "stats": [
                {"number": "100+", "label": "Projects"},
                {"number": "50+", "label": "Clients"},
                {"number": "10+", "label": "Cities"},
                {"number": "99%", "label": "Success"}
            ]
        }
        features = [
            {"icon": "Check", "title": "Reliable", "desc": "Consistent service."},
            {"icon": "Check", "title": "Expert", "desc": "Trained team."},
            {"icon": "Check", "title": "Compliant", "desc": "Meets regulations."},
            {"icon": "Check", "title": "Efficient", "desc": "Cost effective."}
        ]

    return overview, gallery, stats, features

# Rebuild the entire JSON with the updated generator
# I will use the base keys and structure

import json

# Read the existing file and reconstruct (We can just define the skeleton)

categories = [
    {
        "id": "corporate-compliance",
        "title": "Corporate Compliance",
        "icon": "ShieldCheck",
        "image": "/Images/cc_header.png",
        "theme": "corporate",
        "intro": "Helping businesses meet regulatory requirements while advancing their sustainability goals.",
        "services": ["epr", "carbon-market", "esg-consulting"]
    },
    {
        "id": "government-services",
        "title": "Government Services",
        "icon": "Building2",
        "image": "/Images/gs_header.png",
        "theme": "government",
        "intro": "Waste management, environmental, infrastructure.",
        "services": ["swm", "env-projects", "supply-tenders", "survey-it", "mrf-operations", "env-infra", "civil-infra", "gardening", "fire-smartcity"]
    },
    {
        "id": "products",
        "title": "Products",
        "icon": "Recycle",
        "image": "/Images/products_header.png",
        "theme": "products",
        "intro": "Recyclable materials.",
        "services": ["pet-bale", "recycled-granules", "plastic-grinding", "industrial-scrap"]
    }
]

# Map of titles
titles = {
    "epr": "Extended Producer Responsibility (EPR)",
    "carbon-market": "Carbon Market Advisory",
    "esg-consulting": "ESG Consulting",
    "swm": "Solid Waste Management (SWM)",
    "env-projects": "Environmental & Sustainability Projects",
    "supply-tenders": "Supply Tenders",
    "survey-it": "Survey, IT & Consultancy Services",
    "mrf-operations": "Material Recovery Facility Operations",
    "env-infra": "Environmental Infrastructure Operations",
    "civil-infra": "Civil & Infrastructure Works",
    "gardening": "Gardening & Green Development",
    "fire-smartcity": "Fire & Smart City Solutions",
    "pet-bale": "PET Bale Trading",
    "recycled-granules": "Recycled Plastic Granules",
    "plastic-grinding": "Plastic Grinding & Chips Trading",
    "industrial-scrap": "Industrial Scrap Trading"
}

psData = {}

for cat in categories:
    cat_id = cat["id"]
    psData[cat_id] = {
        "id": cat_id,
        "title": cat["title"],
        "icon": cat["icon"],
        "image": cat["image"],
        "theme": cat["theme"],
        "intro": cat["intro"],
        "services": []
    }
    
    # We will format government services correctly if it needs sections, but for simplicity we will just put them in services for now
    # Wait, government services uses 'sections' in the old data!
    # Let's fix that.
    
    if cat_id == "government-services":
        psData[cat_id]["sections"] = [
            {
                "id": "section-a",
                "title": "Direct Execution",
                "badgeType": "green",
                "badgeText": "In-House Operations",
                "description": "Services delivered directly.",
                "services": []
            },
            {
                "id": "section-b",
                "title": "Partner-Led Execution",
                "badgeType": "amber",
                "badgeText": "Partner Operations",
                "description": "Services delivered through approved partners.",
                "services": []
            }
        ]
        del psData[cat_id]["services"]

    for s_id in cat["services"]:
        title = titles[s_id]
        overview, gallery, stats, features = generate_tailored_content(s_id, title)
        
        service_obj = {
            "id": s_id,
            "title": title,
            "icon": "CheckCircle",
            "tagline": f"Excellence in {title}",
            "summary": f"Providing robust solutions for {title}.",
            "detailTagline": f"Comprehensive {title} solutions.",
            "overviewDetails": overview,
            "gallery": gallery,
            "statsSection": stats,
            "features": features,
            "whyChooseUs": {
                "title": f"Why Choose Us for {title}?",
                "subtitle": "Unmatched expertise.",
                "imagePath": "/Images/why_us_illustration.png",
                "points": [
                    { "icon": "CheckCircle", "title": "Expertise", "desc": "Domain knowledge." },
                    { "icon": "Clock", "title": "Reliable", "desc": "Timely execution." },
                    { "icon": "MapPin", "title": "Coverage", "desc": "Pan-India presence." },
                    { "icon": "DollarSign", "title": "Value", "desc": "Cost-effective." }
                ]
            },
            "faqs": [
                { "question": f"How do you handle {title}?", "answer": "With professional expertise." }
            ],
            "closing": "Contact us today.",
            "buttonText": "Enquire"
        }
        
        if cat_id == "government-services":
            if s_id in ["swm", "env-projects", "supply-tenders", "survey-it"]:
                psData[cat_id]["sections"][0]["services"].append(service_obj)
            else:
                psData[cat_id]["sections"][1]["services"].append(service_obj)
        else:
            psData[cat_id]["services"].append(service_obj)

with open("src/data/ProductsServicesData.js", "w", encoding="utf-8") as f:
    f.write("export const psData = " + json.dumps(psData, indent=4) + ";\n")

print("All services unique data successfully generated!")
