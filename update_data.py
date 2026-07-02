import json
import os

# Helper to generate standard filler text
def gen_overview(title):
    return {
        "title": title,
        "imagePath": "/Images/overview_illustration.png",
        "paragraphs": [
            f"India has a strong legal framework for {title}, managed by relevant regulatory bodies. This system ensures that stakeholders take responsibility for the entire lifecycle of their operations from start to finish.",
            f"Implementing robust {title} promotes the use of eco-friendly and sustainable practices, helps reduce waste, and supports the creation of a circular economy. At Plastroots, we go beyond basic compliance to ensure complete accountability via our channel Partners.",
            "The government has introduced several policies and initiatives to strengthen implementation. To support this mission, we collaborate with multiple partners to ensure end-to-end compliance from collection and transportation to processing, or safe disposal."
        ],
        "contactEmail": "business@plastroots.com"
    }

def gen_gallery():
    return [
        { "name": "Plastic Waste", "img": "/Images/waste_plastic.jpg" },
        { "name": "Electronic Waste", "img": "/Images/waste_electronic.jpg" },
        { "name": "Battery Waste", "img": "/Images/waste_battery.jpg" },
        { "name": "Tyre Waste", "img": "/Images/waste_tyre.jpg" },
        { "name": "Used Oil Waste", "img": "/Images/waste_oil.jpg" }
    ]

def gen_stats(title):
    return {
        "title": f"{title} Credits & Compliance Services",
        "subtitle": "We have reduced the complexities for the process & made it easy. Keeping up with environmental regulations can be a headache, but we've got your back. Our team stays on top of all the latest rules and regulations, ensuring that our clients are always in compliance.",
        "imagePath": "/Images/stats_illustration.png",
        "stats": [
            { "number": "500+", "label": "Producers" },
            { "number": "1500+", "label": "Importers" },
            { "number": "400+", "label": "Brand Owners" },
            { "number": "75+", "label": "Partners" }
        ]
    }

def gen_features():
    return [
        { "icon": "ClipboardList", "title": "Registration on the Portal", "desc": "Let us handle your registration process seamlessly." },
        { "icon": "Calculator", "title": "Calculate your Footprint", "desc": "Our expert team will assist you in accurately measuring your impact." },
        { "icon": "CheckSquare", "title": "End-to-End Implementation", "desc": "Complete execution from registration to compliance and reporting." },
        { "icon": "FileText", "title": "Streamlined Reporting", "desc": "Fulfil your reporting requirements with quarterly and monthly reports." }
    ]

# Original data structure with the new fields
psData = {
    "corporate-compliance": {
        "id": "corporate-compliance",
        "title": "Corporate Compliance",
        "icon": "ShieldCheck",
        "image": "/Images/cc_header.png",
        "theme": "corporate",
        "intro": "Helping businesses meet regulatory requirements while advancing their sustainability goals.",
        "services": [
            {
                "id": "epr",
                "title": "Extended Producer Responsibility (EPR)",
                "icon": "ClipboardCheck",
                "tagline": "Stay ahead of evolving regulatory obligations.",
                "summary": "End-to-end EPR compliance support.",
                "detailTagline": "Stay ahead of evolving regulatory obligations.",
                "overviewDetails": gen_overview("Extended Producer Responsibility"),
                "gallery": gen_gallery(),
                "statsSection": gen_stats("EPR"),
                "features": gen_features(),
                "whyChooseUs": {
                    "title": "Why Choose Us for EPR?",
                    "subtitle": "Fast, affordable EPR registration.",
                    "imagePath": "/Images/why_us_illustration.png",
                    "points": [
                        { "icon": "CheckCircle", "title": "98% Approval Rate", "desc": "High success rate." },
                        { "icon": "Clock", "title": "End-to-End Compliance", "desc": "Complete support." },
                        { "icon": "MapPin", "title": "Pan-India Coverage", "desc": "Across India." },
                        { "icon": "DollarSign", "title": "Cost-Effective Packages", "desc": "Affordable plans." }
                    ]
                },
                "faqs": [
                    { "question": "Who needs EPR registration?", "answer": "Producers, importers, brand owners." },
                    { "question": "What is the penalty?", "answer": "Heavy fines." }
                ],
                "closing": "Seamless compliance.",
                "buttonText": "Get Expert Assistance"
            },
            {
                "id": "carbon-market",
                "title": "Carbon Market Advisory",
                "icon": "Leaf",
                "tagline": "Turn sustainability into value.",
                "summary": "Carbon footprint assessment.",
                "detailTagline": "Turn sustainability into value.",
                "overviewDetails": gen_overview("Carbon Market Advisory"),
                "gallery": gen_gallery(),
                "statsSection": gen_stats("Carbon"),
                "features": gen_features(),
                "whyChooseUs": {
                    "title": "Why Choose Us?",
                    "subtitle": "Verifiable credits.",
                    "imagePath": "/Images/why_us_illustration.png",
                    "points": [
                        { "icon": "CheckCircle", "title": "Expert Analysts", "desc": "Deep knowledge." },
                        { "icon": "Clock", "title": "End-to-End Advisory", "desc": "Calculations to trading." },
                        { "icon": "MapPin", "title": "Verified", "desc": "Strict standards." },
                        { "icon": "DollarSign", "title": "Value Max", "desc": "Optimized strategies." }
                    ]
                },
                "faqs": [
                    { "question": "What are scopes?", "answer": "Direct vs indirect emissions." }
                ],
                "closing": "Manage and monetize.",
                "buttonText": "Enquire"
            },
            {
                "id": "esg-consulting",
                "title": "ESG Consulting",
                "icon": "BarChart",
                "tagline": "Build responsible operations.",
                "summary": "ESG assessments.",
                "detailTagline": "Supporting businesses.",
                "overviewDetails": gen_overview("ESG Consulting"),
                "gallery": gen_gallery(),
                "statsSection": gen_stats("ESG"),
                "features": gen_features(),
                "whyChooseUs": {
                    "title": "Why Choose Us?",
                    "subtitle": "Tailored strategies.",
                    "imagePath": "/Images/why_us_illustration.png",
                    "points": [
                        { "icon": "CheckCircle", "title": "Frameworks", "desc": "GRI, BRSR." },
                        { "icon": "Clock", "title": "Actionable Insights", "desc": "Roadmaps." },
                        { "icon": "MapPin", "title": "Holistic", "desc": "E, S, and G." },
                        { "icon": "DollarSign", "title": "Reports", "desc": "Clear disclosures." }
                    ]
                },
                "faqs": [
                    { "question": "What is BRSR?", "answer": "Mandatory ESG disclosure." }
                ],
                "closing": "Practical ESG strategies.",
                "buttonText": "Enquire"
            }
        ]
    },
    "government-services": {
        "id": "government-services",
        "title": "Government Services",
        "icon": "Building2",
        "image": "/Images/gs_header.png",
        "theme": "government",
        "intro": "Waste management, environmental, infrastructure.",
        "sections": [
            {
                "id": "section-a",
                "title": "Direct Execution",
                "badgeType": "green",
                "badgeText": "In-House Operations",
                "description": "Services delivered directly.",
                "services": [
                    {
                        "id": "swm",
                        "title": "Solid Waste Management (SWM)",
                        "icon": "Trash2",
                        "badge": "Direct Execution",
                        "badgeType": "green",
                        "tagline": "Integrated solid waste solutions.",
                        "summary": "Door-to-door collection.",
                        "detailTagline": "Integrated solid waste solutions.",
                        "overviewDetails": gen_overview("Solid Waste Management"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("SWM"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Reliable operations.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Tech Tracking", "desc": "GPS monitoring." },
                                { "icon": "Clock", "title": "Timely", "desc": "Strict schedules." },
                                { "icon": "MapPin", "title": "Trained", "desc": "Equipped workforce." },
                                { "icon": "DollarSign", "title": "Compliant", "desc": "SWM Rules 2016." }
                            ]
                        },
                        "faqs": [
                            { "question": "Vehicles?", "answer": "Yes, we deploy." }
                        ],
                        "executionNote": "Directly executed.",
                        "buttonText": "Enquire"
                    },
                    {
                        "id": "env-projects",
                        "title": "Environmental & Sustainability Projects",
                        "icon": "Sprout",
                        "badge": "Direct Execution",
                        "badgeType": "green",
                        "tagline": "Building sustainable infrastructure.",
                        "summary": "Biofuel supply.",
                        "detailTagline": "Building sustainable infrastructure.",
                        "overviewDetails": gen_overview("Environmental Projects"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("Environmental"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Turnkey solutions.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Tech", "desc": "Tested technologies." },
                                { "icon": "Clock", "title": "Turnkey", "desc": "End to end." },
                                { "icon": "MapPin", "title": "Recovery", "desc": "Maximized." },
                                { "icon": "DollarSign", "title": "Viability", "desc": "Sustainable economics." }
                            ]
                        },
                        "faqs": [
                            { "question": "Scale?", "answer": "1 TPD to 50 TPD." }
                        ],
                        "executionNote": "Directly executed.",
                        "buttonText": "Enquire"
                    },
                    {
                        "id": "supply-tenders",
                        "title": "Supply Tenders",
                        "icon": "Truck",
                        "badge": "Direct Execution",
                        "badgeType": "green",
                        "tagline": "Dependable supply.",
                        "summary": "Machinery supply.",
                        "detailTagline": "Dependable supply.",
                        "overviewDetails": gen_overview("Supply Tenders"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("Supply"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Reliable supply.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Quality", "desc": "Top OEMs." },
                                { "icon": "Clock", "title": "Timely", "desc": "Tender timelines." },
                                { "icon": "MapPin", "title": "Support", "desc": "AMC." },
                                { "icon": "DollarSign", "title": "Pricing", "desc": "Competitive bids." }
                            ]
                        },
                        "faqs": [
                            { "question": "Custom?", "answer": "Yes, customized." }
                        ],
                        "executionNote": "Directly executed.",
                        "buttonText": "Enquire"
                    },
                    {
                        "id": "survey-it",
                        "title": "Survey, IT & Consultancy Services",
                        "icon": "LineChart",
                        "badge": "Direct Execution",
                        "badgeType": "green",
                        "tagline": "Technical expertise.",
                        "summary": "Project consultancy.",
                        "detailTagline": "Technical expertise.",
                        "overviewDetails": gen_overview("Survey & IT Consultancy"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("Consultancy"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Bridging the gap.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Expertise", "desc": "Experienced team." },
                                { "icon": "Clock", "title": "Data", "desc": "Quantitative." },
                                { "icon": "MapPin", "title": "Policies", "desc": "Aligned." },
                                { "icon": "DollarSign", "title": "Documents", "desc": "Structured reports." }
                            ]
                        },
                        "faqs": [
                            { "question": "Support?", "answer": "Dashboards and software." }
                        ],
                        "executionNote": "Directly executed.",
                        "buttonText": "Enquire"
                    }
                ]
            },
            {
                "id": "section-b",
                "title": "Partner-Led Execution",
                "badgeType": "amber",
                "badgeText": "Partner Operations",
                "description": "Services delivered through approved partners.",
                "services": [
                    {
                        "id": "mrf-operations",
                        "title": "Material Recovery Facility Operations",
                        "icon": "ArrowRightLeft",
                        "badge": "Partner-Led",
                        "badgeType": "amber",
                        "tagline": "Resource recovery.",
                        "summary": "MRF management.",
                        "detailTagline": "Resource recovery.",
                        "overviewDetails": gen_overview("MRF Operations"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("MRF"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Professionalized.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Rates", "desc": "Optimized lines." },
                                { "icon": "Clock", "title": "Markets", "desc": "Direct connections." },
                                { "icon": "MapPin", "title": "Safety", "desc": "Standards." },
                                { "icon": "DollarSign", "title": "Reporting", "desc": "Clear tracking." }
                            ]
                        },
                        "faqs": [
                            { "question": "Equipment?", "answer": "Yes, we coordinate." }
                        ],
                        "executionNote": "Partner delivered.",
                        "buttonText": "Enquire"
                    },
                    {
                        "id": "env-infra",
                        "title": "Environmental Infrastructure",
                        "icon": "Droplets",
                        "badge": "Partner-Led",
                        "badgeType": "amber",
                        "tagline": "Reliable operation.",
                        "summary": "STP operations.",
                        "detailTagline": "Reliable operation.",
                        "overviewDetails": gen_overview("Environmental Infrastructure"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("Infrastructure"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Peak efficiency.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Expertise", "desc": "Certified operators." },
                                { "icon": "Clock", "title": "Monitoring", "desc": "24/7 oversight." },
                                { "icon": "MapPin", "title": "Maintenance", "desc": "Preventive." },
                                { "icon": "DollarSign", "title": "Adherence", "desc": "PCB norms." }
                            ]
                        },
                        "faqs": [
                            { "question": "STPs?", "answer": "SBR, MBBR, etc." }
                        ],
                        "executionNote": "Partner delivered.",
                        "buttonText": "Enquire"
                    },
                    {
                        "id": "civil-infra",
                        "title": "Civil & Infrastructure",
                        "icon": "Building",
                        "badge": "Partner-Led",
                        "badgeType": "amber",
                        "tagline": "Building urban infra.",
                        "summary": "Road construction.",
                        "detailTagline": "Building urban infra.",
                        "overviewDetails": gen_overview("Civil Infrastructure"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("Civil"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "High-quality.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Quality", "desc": "Testing." },
                                { "icon": "Clock", "title": "On-Time", "desc": "No delays." },
                                { "icon": "MapPin", "title": "Approved", "desc": "Vetted partners." },
                                { "icon": "DollarSign", "title": "Safety", "desc": "Regulations." }
                            ]
                        },
                        "faqs": [
                            { "question": "Turnkey?", "answer": "Yes." }
                        ],
                        "executionNote": "Partner delivered.",
                        "buttonText": "Enquire"
                    },
                    {
                        "id": "gardening",
                        "title": "Gardening & Green Development",
                        "icon": "Trees",
                        "badge": "Partner-Led",
                        "badgeType": "amber",
                        "tagline": "Creating greener environments.",
                        "summary": "Tree plantation.",
                        "detailTagline": "Creating greener environments.",
                        "overviewDetails": gen_overview("Green Development"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("Green"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Sustainable green zones.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Native", "desc": "Flora." },
                                { "icon": "Clock", "title": "Survival", "desc": "Care." },
                                { "icon": "MapPin", "title": "Design", "desc": "Aesthetic." },
                                { "icon": "DollarSign", "title": "Upkeep", "desc": "Maintenance." }
                            ]
                        },
                        "faqs": [
                            { "question": "Miyawaki?", "answer": "Yes." }
                        ],
                        "executionNote": "Partner delivered.",
                        "buttonText": "Enquire"
                    },
                    {
                        "id": "fire-smartcity",
                        "title": "Fire & Smart City",
                        "icon": "Flame",
                        "badge": "Partner-Led",
                        "badgeType": "amber",
                        "tagline": "Safety systems.",
                        "summary": "Fire-fighting.",
                        "detailTagline": "Safety systems.",
                        "overviewDetails": gen_overview("Smart City Solutions"),
                        "gallery": gen_gallery(),
                        "statsSection": gen_stats("Smart City"),
                        "features": gen_features(),
                        "whyChooseUs": {
                            "title": "Why Choose Us?",
                            "subtitle": "Compliant systems.",
                            "imagePath": "/Images/why_us_illustration.png",
                            "points": [
                                { "icon": "CheckCircle", "title": "Compliance", "desc": "NBC norms." },
                                { "icon": "Clock", "title": "Partners", "desc": "Licensed." },
                                { "icon": "MapPin", "title": "Audits", "desc": "Gap analysis." },
                                { "icon": "DollarSign", "title": "Equipment", "desc": "ISI marked." }
                            ]
                        },
                        "faqs": [
                            { "question": "NOCs?", "answer": "Yes." }
                        ],
                        "executionNote": "Partner delivered.",
                        "buttonText": "Enquire"
                    }
                ]
            }
        ]
    },
    "products": {
        "id": "products",
        "title": "Products",
        "icon": "Recycle",
        "image": "/Images/products_header.png",
        "theme": "products",
        "intro": "Recyclable materials.",
        "services": [
            {
                "id": "pet-bale",
                "title": "PET Bale Trading",
                "icon": "Package",
                "tagline": "Quality PET feedstock.",
                "summary": "PET bales.",
                "detailTagline": "Quality PET feedstock.",
                "overviewDetails": gen_overview("PET Bale Trading"),
                "gallery": gen_gallery(),
                "statsSection": gen_stats("PET"),
                "features": gen_features(),
                "whyChooseUs": {
                    "title": "Why Choose Us?",
                    "subtitle": "Reliable feedstock.",
                    "imagePath": "/Images/why_us_illustration.png",
                    "points": [
                        { "icon": "CheckCircle", "title": "Low Contamination", "desc": "Strict checks." },
                        { "icon": "Clock", "title": "Consistent", "desc": "Steady volume." },
                        { "icon": "MapPin", "title": "Network", "desc": "Wide sourcing." },
                        { "icon": "DollarSign", "title": "Pricing", "desc": "Transparent." }
                    ]
                },
                "faqs": [
                    { "question": "Weight?", "answer": "100-150 kg." }
                ],
                "closing": "End use: flakes.",
                "buttonText": "Enquire"
            },
            {
                "id": "recycled-granules",
                "title": "Recycled Granules",
                "icon": "CircleDashed",
                "tagline": "High-quality granules.",
                "summary": "PP, LDPE, HDPE.",
                "materialBadges": ["PP", "LDPE", "HDPE"],
                "detailTagline": "High-quality granules.",
                "overviewDetails": gen_overview("Recycled Granules"),
                "gallery": gen_gallery(),
                "statsSection": gen_stats("Granules"),
                "features": gen_features(),
                "whyChooseUs": {
                    "title": "Why Choose Us?",
                    "subtitle": "Consistent quality.",
                    "imagePath": "/Images/why_us_illustration.png",
                    "points": [
                        { "icon": "CheckCircle", "title": "Consistency", "desc": "MFI." },
                        { "icon": "Clock", "title": "Clean", "desc": "Washed." },
                        { "icon": "MapPin", "title": "Sustainable", "desc": "Alternative." },
                        { "icon": "DollarSign", "title": "Cost", "desc": "Savings." }
                    ]
                },
                "faqs": [
                    { "question": "Injection?", "answer": "Yes." }
                ],
                "closing": "Sourcing to Supply.",
                "buttonText": "Enquire"
            },
            {
                "id": "plastic-grinding",
                "title": "Plastic Grinding",
                "icon": "Scissors",
                "tagline": "Quality chips.",
                "summary": "Chips and flakes.",
                "detailTagline": "Quality chips.",
                "overviewDetails": gen_overview("Plastic Grinding"),
                "gallery": gen_gallery(),
                "statsSection": gen_stats("Grinding"),
                "features": gen_features(),
                "whyChooseUs": {
                    "title": "Why Choose Us?",
                    "subtitle": "Ready feedstock.",
                    "imagePath": "/Images/why_us_illustration.png",
                    "points": [
                        { "icon": "CheckCircle", "title": "Size", "desc": "Uniform." },
                        { "icon": "Clock", "title": "Control", "desc": "Contamination." },
                        { "icon": "MapPin", "title": "Segregation", "desc": "Strict." },
                        { "icon": "DollarSign", "title": "Bulk", "desc": "Available." }
                    ]
                },
                "faqs": [
                    { "question": "Mixed?", "answer": "No." }
                ],
                "closing": "Clean chips.",
                "buttonText": "Enquire"
            },
            {
                "id": "industrial-scrap",
                "title": "Industrial Scrap Trading",
                "icon": "Box",
                "tagline": "Responsible sourcing.",
                "summary": "Metals, plastics, tyres.",
                "materialBadges": ["Copper", "Aluminium"],
                "detailTagline": "Responsible sourcing.",
                "overviewDetails": gen_overview("Scrap Trading"),
                "gallery": gen_gallery(),
                "statsSection": gen_stats("Scrap"),
                "features": gen_features(),
                "whyChooseUs": {
                    "title": "Why Choose Us?",
                    "subtitle": "Transparent.",
                    "imagePath": "/Images/why_us_illustration.png",
                    "points": [
                        { "icon": "CheckCircle", "title": "Valuation", "desc": "Fair." },
                        { "icon": "Clock", "title": "Lifting", "desc": "Prompt." },
                        { "icon": "MapPin", "title": "Compliance", "desc": "Driven." },
                        { "icon": "DollarSign", "title": "Diverse", "desc": "Handling." }
                    ]
                },
                "faqs": [
                    { "question": "Logistics?", "answer": "Yes." }
                ],
                "closing": "Circular economy.",
                "buttonText": "Enquire"
            }
        ]
    }
}

js_content = "export const psData = " + json.dumps(psData, indent=4) + ";\n"

with open("src/data/ProductsServicesData.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("ProductsServicesData.js updated successfully.")
