import re

file_path = r'D:\Plastroots_Website\src\data\ProductsServicesData.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def get_why_us(service_id):
    data = {
        'epr': {
            'title': 'Why Choose Plastroots for EPR?',
            'subtitle': 'Absolute precision in compliance.',
            'points': [
                {'icon': 'ShieldCheck', 'title': 'Regulatory Mastery', 'desc': 'Deep understanding of CPCB guidelines.'},
                {'icon': 'ClipboardList', 'title': 'End-to-End Support', 'desc': 'From registration to credit procurement.'},
                {'icon': 'CheckCircle', 'title': 'Audit-Ready', 'desc': 'Impeccable documentation standards.'}
            ]
        },
        'carbon-market': {
            'title': 'Why Choose Plastroots for Carbon Advisory?',
            'subtitle': 'Turning sustainability into measurable value.',
            'points': [
                {'icon': 'Leaf', 'title': 'Strategic Insight', 'desc': 'Expert guidance on voluntary and compliance markets.'},
                {'icon': 'LineChart', 'title': 'Accurate Baselines', 'desc': 'Rigorous GHG inventory and footprint assessments.'},
                {'icon': 'TrendingUp', 'title': 'Monetization', 'desc': 'End-to-end support in trading verified credits.'}
            ]
        },
        'esg-consulting': {
            'title': 'Why Choose Plastroots for ESG?',
            'subtitle': 'Building resilient and responsible operations.',
            'points': [
                {'icon': 'Target', 'title': 'Framework Alignment', 'desc': 'Seamless mapping to BRSR, GRI, and SASB.'},
                {'icon': 'BarChart', 'title': 'Data-Driven', 'desc': 'Developing measurable KPIs tailored to your industry.'},
                {'icon': 'Award', 'title': 'Stakeholder Trust', 'desc': 'Credible reporting that enhances brand value.'}
            ]
        },
        'swm': {
            'title': 'Why Choose Plastroots for SWM?',
            'subtitle': 'Integrated solutions for cleaner cities.',
            'points': [
                {'icon': 'Truck', 'title': 'Operational Scale', 'desc': 'Proven capacity to manage city-wide collection fleets.'},
                {'icon': 'Activity', 'title': 'Tech-Enabled', 'desc': 'Real-time GPS tracking and route optimization.'},
                {'icon': 'Users', 'title': 'Community Focus', 'desc': 'Effective IEC programs driving source segregation.'}
            ]
        },
        'env-projects': {
            'title': 'Why Choose Plastroots for Env. Projects?',
            'subtitle': 'Sustainable infrastructure built to last.',
            'points': [
                {'icon': 'Sprout', 'title': 'Circular Approach', 'desc': 'Converting waste streams into clean energy and compost.'},
                {'icon': 'Wrench', 'title': 'Technical Expertise', 'desc': 'Advanced design and commissioning capabilities.'},
                {'icon': 'CheckCircle', 'title': 'Reliable O&M', 'desc': 'Comprehensive maintenance ensuring long-term viability.'}
            ]
        },
        'supply-tenders': {
            'title': 'Why Choose Plastroots for Supply?',
            'subtitle': 'Dependable sourcing for municipal needs.',
            'points': [
                {'icon': 'ShieldCheck', 'title': 'Quality Assured', 'desc': 'Equipment meeting stringent government specifications.'},
                {'icon': 'Clock', 'title': 'Timely Delivery', 'desc': 'Robust logistics network ensuring deadlines are met.'},
                {'icon': 'ThumbsUp', 'title': 'After-Sales Support', 'desc': 'Dedicated assistance post-delivery.'}
            ]
        },
        'survey-it': {
            'title': 'Why Choose Plastroots for Consultancy?',
            'subtitle': 'Technical depth meets regulatory understanding.',
            'points': [
                {'icon': 'FileText', 'title': 'Robust DPRs', 'desc': 'Technically sound reports designed for rapid approval.'},
                {'icon': 'Monitor', 'title': 'Digital Enablement', 'desc': 'Seamless IT support for citizen and operational portals.'},
                {'icon': 'Briefcase', 'title': 'Strategic Advisory', 'desc': 'Expert guidance through complex project lifecycles.'}
            ]
        },
        'mrf-operations': {
            'title': 'Why Choose Plastroots for MRF Operations?',
            'subtitle': 'Maximizing resource recovery.',
            'points': [
                {'icon': 'Recycle', 'title': 'High Diversion Rates', 'desc': 'Advanced sorting protocols minimizing landfill waste.'},
                {'icon': 'Users', 'title': 'Vetted Partners', 'desc': 'Operations executed by highly qualified organizations.'},
                {'icon': 'FileCheck', 'title': 'Transparent Reporting', 'desc': 'Rigorous tracking of all recovered material streams.'}
            ]
        },
        'env-infra': {
            'title': 'Why Choose Plastroots for Env. Infra?',
            'subtitle': 'Reliable operation of critical facilities.',
            'points': [
                {'icon': 'Droplets', 'title': 'Compliance Focused', 'desc': 'Ensuring effluents consistently meet prescribed standards.'},
                {'icon': 'Settings', 'title': 'Preventative Maintenance', 'desc': 'Minimizing downtime through proactive care.'},
                {'icon': 'Shield', 'title': 'Health & Safety', 'desc': 'Strict adherence to operational safety protocols.'}
            ]
        },
        'civil-infra': {
            'title': 'Why Choose Plastroots for Civil Infra?',
            'subtitle': 'Building the foundations of urban life.',
            'points': [
                {'icon': 'Building', 'title': 'Quality Construction', 'desc': 'Adherence to the highest engineering standards.'},
                {'icon': 'Clock', 'title': 'On-Time Execution', 'desc': 'Rigorous project management ensuring timely delivery.'},
                {'icon': 'CheckSquare', 'title': 'Code Compliant', 'desc': 'Full alignment with national building codes.'}
            ]
        },
        'gardening': {
            'title': 'Why Choose Plastroots for Green Dev?',
            'subtitle': 'Creating healthier urban environments.',
            'points': [
                {'icon': 'Trees', 'title': 'Biodiversity Focus', 'desc': 'Selection of native and ecologically appropriate species.'},
                {'icon': 'Sprout', 'title': 'Expert Horticulture', 'desc': 'Specialized care for long-term plant health.'},
                {'icon': 'Sun', 'title': 'Aesthetic Excellence', 'desc': 'Beautifully designed public spaces.'}
            ]
        },
        'fire-smartcity': {
            'title': 'Why Choose Plastroots for Fire & Smart City?',
            'subtitle': 'Modern solutions for urban safety.',
            'points': [
                {'icon': 'Flame', 'title': 'NBC Compliant', 'desc': 'Systems designed to rigorous national safety codes.'},
                {'icon': 'Cpu', 'title': 'Smart Integration', 'desc': 'Seamlessly connected detection and response networks.'},
                {'icon': 'Search', 'title': 'Thorough Auditing', 'desc': 'Comprehensive assessments of existing infrastructure.'}
            ]
        },
        'pet-bale': {
            'title': 'Why Choose Plastroots for PET Bales?',
            'subtitle': 'Consistent, high-quality feedstock.',
            'points': [
                {'icon': 'MapPin', 'title': 'Pan-India Sourcing', 'desc': 'Extensive network of reliable collection partners.'},
                {'icon': 'CheckCircle', 'title': 'Rigorous QC', 'desc': 'Strict assessments minimizing contamination.'},
                {'icon': 'Package', 'title': 'Reliable Volumes', 'desc': 'Consistent supply to meet industrial demands.'}
            ]
        },
        'recycled-granules': {
            'title': 'Why Choose Plastroots Recycled Granules?',
            'subtitle': 'Sustainable alternatives without compromise.',
            'points': [
                {'icon': 'CircleDashed', 'title': 'High Consistency', 'desc': 'Uniform quality across every batch.'},
                {'icon': 'Settings', 'title': 'Advanced Processing', 'desc': 'State-of-the-art washing and extrusion technology.'},
                {'icon': 'Box', 'title': 'Versatile Applications', 'desc': 'Suitable for molding, pipes, and packaging.'}
            ]
        },
        'plastic-grinding': {
            'title': 'Why Choose Plastroots for Plastic Chips?',
            'subtitle': 'Premium pre-processed material.',
            'points': [
                {'icon': 'Scissors', 'title': 'Precision Grinding', 'desc': 'Uniform flake size for optimal downstream processing.'},
                {'icon': 'Layers', 'title': 'Clean Sourcing', 'desc': 'High-quality industrial off-cuts and rejects.'},
                {'icon': 'Truck', 'title': 'Bulk Capability', 'desc': 'Equipped to handle and supply massive volumes.'}
            ]
        },
        'industrial-scrap': {
            'title': 'Why Choose Plastroots for Industrial Scrap?',
            'subtitle': 'Responsible and transparent trading.',
            'points': [
                {'icon': 'Recycle', 'title': 'Diverse Portfolio', 'desc': 'Handling metals, plastics, rubber, and more.'},
                {'icon': 'FileCheck', 'title': 'Traceability', 'desc': 'Clear documentation supporting circular economy goals.'},
                {'icon': 'Handshake', 'title': 'Fair Value', 'desc': 'Competitive pricing driven by deep market knowledge.'}
            ]
        }
    }
    return data.get(service_id)

def replacer(match):
    id_str = match.group(1)
    before_closing = match.group(2)
    # create the whyChooseUs JS object string
    wu = get_why_us(id_str)
    if not wu:
        return match.group(0)
    
    points_str = ",\n".join([f"                    {{ icon: '{p['icon']}', title: '{p['title']}', desc: '{p['desc']}' }}" for p in wu['points']])
    
    wu_str = f"""
                whyChooseUs: {{
                    title: "{wu['title']}",
                    subtitle: "{wu['subtitle']}",
                    points: [
{points_str}
                    ]
                }},"""
    return f'id: "{id_str}"{before_closing}{wu_str}'

# The regex matches id: "something", then everything until the last property before buttonText or closing.
# Actually, let's just find `buttonText: "..."` and inject it right before that.
# But we need to know the id of the current service.
# Let's split by `id: "` and process each block.
blocks = content.split('id: "')
new_blocks = [blocks[0]]

for block in blocks[1:]:
    # block starts with the id, e.g. epr",\n title: ...
    id_end = block.find('"')
    service_id = block[:id_end]
    
    wu = get_why_us(service_id)
    if wu:
        # find the last buttonText:
        bt_idx = block.rfind('buttonText:')
        if bt_idx != -1:
            points_str = ",\n".join([f"                    {{ icon: '{p['icon']}', title: '{p['title']}', desc: '{p['desc']}' }}" for p in wu['points']])
            wu_str = f"""whyChooseUs: {{
                    title: "{wu['title']}",
                    subtitle: "{wu['subtitle']}",
                    points: [
{points_str}
                    ]
                }},
                """
            block = block[:bt_idx] + wu_str + block[bt_idx:]
    new_blocks.append(block)

new_content = 'id: "'.join(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated successfully!")
