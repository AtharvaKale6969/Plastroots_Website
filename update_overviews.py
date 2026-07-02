import re

file_path = r'D:\Plastroots_Website\src\data\ProductsServicesData.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Tailored paragraphs for each service
overview_texts = {
    'epr': [
        "Extended Producer Responsibility (EPR) mandates that producers, importers, and brand owners take accountability for the end-of-life management of their packaging and products. In India, this is strictly enforced under the Plastic and E-Waste Management Rules, requiring businesses to register, meet annual recycling targets, and file detailed compliance returns.",
        "Plastroots takes the complexity out of EPR. We act as your strategic compliance partner, seamlessly managing the entire lifecycle—from CPCB portal registration to the ethical procurement of EPR credits from verified recyclers. Our robust tracking and audit-ready documentation ensure your brand remains fully compliant while actively contributing to a circular economy."
    ],
    'carbon-market': [
        "The global transition toward a low-carbon economy has made carbon footprint management and credit trading a strategic necessity. Whether addressing mandatory compliance requirements under India's emerging Carbon Credit Trading Scheme (CCTS) or meeting voluntary corporate sustainability goals, organizations must proactively measure and mitigate their greenhouse gas (GHG) emissions.",
        "We provide end-to-end carbon advisory services designed to turn environmental responsibility into a competitive advantage. Our experts conduct rigorous GHG inventories across Scope 1, 2, and 3 emissions, develop actionable reduction strategies, and facilitate the transparent procurement and retirement of verified carbon credits, helping your organization achieve credible net-zero milestones."
    ],
    'esg-consulting': [
        "Environmental, Social, and Governance (ESG) metrics are no longer just optional disclosures; they are critical indicators of a company's resilience, risk management, and long-term value. With increasing pressure from investors, consumers, and regulatory bodies (such as SEBI's BRSR framework), businesses must demonstrate tangible, data-backed commitments to sustainable operations.",
        "Plastroots empowers organizations to build robust ESG frameworks tailored to their specific industry landscapes. We conduct comprehensive gap analyses, align your operations with global reporting standards like GRI and SASB, and develop measurable KPIs. Our strategic consulting ensures your sustainability narrative is both authentic and verifiable, driving stakeholder trust and operational excellence."
    ],
    'swm': [
        "Urbanization and population growth have placed immense pressure on municipal solid waste management infrastructure. Effective waste management is essential for public health, environmental protection, and urban aesthetics. Local bodies are tasked with the massive operational challenge of collecting, segregating, and processing thousands of tons of waste daily while adhering to strict environmental regulations.",
        "Plastroots partners with municipalities to design and execute integrated Solid Waste Management (SWM) systems. From deploying tech-enabled door-to-door collection fleets with real-time GPS tracking to operating mechanized street sweeping and managing Refuse Derived Fuel (RDF), we bring private-sector efficiency to public sanitation. Our community-focused IEC campaigns further ensure high source-segregation rates, drastically reducing landfill dependency."
    ],
    'env-projects': [
        "Building a sustainable future requires specialized infrastructure capable of converting municipal and industrial waste streams into valuable resources. From organic waste processing to plastic recycling, the successful execution of environmental projects demands a deep understanding of process engineering, regulatory compliance, and operational scalability.",
        "Our team excels in the turnkey design, establishment, and operation of high-impact sustainability projects. We specialize in setting up advanced biogas plants, mechanized composting units, and plastic waste recycling facilities for government bodies. By transforming liability waste into clean energy, biofuel, and nutrient-rich compost, we help cities achieve their zero-waste and circular economy mandates."
    ],
    'supply-tenders': [
        "Municipalities and public works departments require reliable, high-quality equipment to maintain daily sanitation and environmental operations. The procurement process via government tenders demands strict adherence to technical specifications, competitive pricing, and uncompromising post-delivery support to ensure public funds are utilized effectively.",
        "Plastroots is a trusted partner in fulfilling critical government supply tenders. We leverage our extensive supply chain network to deliver everything from heavy waste management machinery and specialized collection vehicles to color-coded segregation bins and operational supplies. Our commitment to quality assurance and timely logistics ensures that civic bodies have the exact tools they need to function efficiently."
    ],
    'survey-it': [
        "The successful implementation of large-scale urban and environmental projects requires meticulous planning, precise technical documentation, and modern digital oversight. Navigating the complex landscape of government approvals, budget allocations, and long-term project viability demands specialized consultancy and robust IT support frameworks.",
        "We bridge the gap between technical planning and execution by offering expert consultancy and IT services to government departments. Our team prepares highly detailed, technically sound Detailed Project Reports (DPRs) that accelerate funding approvals. Furthermore, we provide dedicated application support and digital monitoring solutions, bringing transparency and data-driven decision-making to municipal operations."
    ],
    'mrf-operations': [
        "Material Recovery Facilities (MRFs) are the beating heart of a circular economy. They serve as the critical infrastructure where mixed dry waste is systematically sorted, baled, and channeled to appropriate recycling industries. Without efficient MRFs, highly recyclable materials are tragically lost to overcrowded landfills, squandering immense economic and environmental value.",
        "Plastroots oversees the operation of high-capacity MRFs through a network of rigorously vetted and experienced partners. We implement advanced sorting protocols and stringent quality control measures to maximize resource recovery rates. By ensuring that clean, segregated streams of plastics, paper, glass, and metals are routed back into the manufacturing cycle, we actively close the loop on municipal waste."
    ],
    'env-infra': [
        "The continuous, reliable operation of environmental infrastructure—such as Sewage Treatment Plants (STPs) and large-scale waste processing facilities—is a non-negotiable requirement for modern urban centers. Any operational failure in these systems can lead to severe ecological damage, public health crises, and significant regulatory penalties.",
        "We coordinate the management of critical environmental infrastructure through specialized partner organizations, ensuring facilities run at peak efficiency around the clock. Our rigorous oversight protocols focus on preventative maintenance, strict adherence to effluent discharge standards, and comprehensive safety practices, guaranteeing that municipalities meet their environmental protection mandates without disruption."
    ],
    'civil-infra': [
        "Robust civil infrastructure is the backbone of urban development, directly impacting the quality of life, economic activity, and safety of citizens. The construction of roads, bridges, public buildings, and pedestrian pathways requires exacting engineering standards, high-quality materials, and flawless project management to ensure durability and public utility.",
        "Through our approved network of expert civil contractors, Plastroots facilitates the execution of vital municipal infrastructure works. From laying highly durable cement concrete roads to constructing institutional buildings and executing urban beautification projects, we ensure that every development strictly adheres to national building codes, is completed on schedule, and stands the test of time."
    ],
    'gardening': [
        "Green spaces are the lungs of any city, providing essential cooling, biodiversity, and recreational areas for residents. However, urban horticulture and green development require far more than simple planting; they demand expert knowledge of local ecology, soil management, and sustainable landscape design to thrive in challenging urban environments.",
        "Plastroots coordinates comprehensive urban greening initiatives alongside specialist horticultural partners. We oversee the development and maintenance of public parks, avenue plantations, and urban forests, meticulously selecting native and climate-appropriate species. Our initiatives not only elevate the aesthetic appeal of a city but actively combat urban heat islands and improve local air quality."
    ],
    'fire-smartcity': [
        "As cities grow denser and more complex, integrating advanced safety mechanisms and smart infrastructure becomes a paramount concern for civic authorities. Modern urban environments require rapid, automated responses to emergencies and intelligent systems that enhance public security, operational efficiency, and overall citizen well-being.",
        "We help municipalities future-proof their environments through the deployment of cutting-edge Fire and Smart City solutions. Working with certified experts, we coordinate the installation of NBC-compliant fire-fighting networks, advanced alarm systems, and smart surveillance infrastructure. Our comprehensive safety audits and intelligent integrations ensure cities are prepared, responsive, and secure."
    ],
    'pet-bale': [
        "Polyethylene Terephthalate (PET) is highly recyclable, yet securing a consistent, uncontaminated supply of PET waste remains a major challenge for the recycling industry. Manufacturers require massive, reliable volumes of high-quality PET feedstock to produce rPET flakes for use in sustainable textiles, packaging, and food-grade containers.",
        "Plastroots has established a formidable, pan-India sourcing network to bridge this supply gap. We procure PET waste directly from scrap aggregators and collection centers, implementing rigorous quality assessments at the source to minimize contamination. Our material is then expertly baled at our processing facilities, ensuring we provide leading recyclers with the dependable, high-grade feedstock they need to scale their operations."
    ],
    'recycled-granules': [
        "The manufacturing sector is increasingly pivoting away from virgin plastics in favor of sustainable alternatives, driven by both corporate ESG goals and regulatory pressures. However, finding recycled plastic granules that offer the same structural integrity, consistency, and performance as virgin materials is often difficult.",
        "We manufacture and supply premium recycled plastic granules—including PP, LDPE, and HDPE—engineered for high-performance industrial applications. Utilizing state-of-the-art washing, shredding, and extrusion technology, we transform post-consumer and post-industrial waste into uniform, high-quality pellets. Our granules serve as the perfect, sustainable raw material for injection molding, pipe extrusion, and flexible packaging industries."
    ],
    'plastic-grinding': [
        "The plastic recycling ecosystem relies heavily on pre-processed materials. Many secondary manufacturers and recyclers lack the massive capital infrastructure required to safely and efficiently break down large industrial plastic scrap into manageable, uniform pieces that are ready for immediate extrusion or molding.",
        "Plastroots solves this by operating specialized industrial grinding and shredding facilities. We source clean, industrial plastic off-cuts and rejects, processing them into high-quality chips and flakes of exact specifications. Our precision grinding operations provide a vital preprocessing service, allowing downstream manufacturers to seamlessly integrate our clean chips directly into their production lines."
    ],
    'industrial-scrap': [
        "Industrial manufacturing inherently generates massive quantities of scrap materials, including valuable metals, specialized plastics, and rubber. Historically, much of this material was mismanaged or undervalued. Today, responsible trading of industrial scrap is a cornerstone of the circular economy, returning critical raw materials back into the industrial supply chain.",
        "We operate a highly transparent and efficient industrial scrap trading division. Plastroots responsibly sources diverse recyclable materials—from copper and aluminum to tyre waste and industrial drums—directly from manufacturing estates. By offering fair market value and meticulous traceability, we ensure these valuable resources are diverted from landfills and channeled directly to verified processors for productive reuse."
    ]
}

def replace_overview_paragraphs(match):
    service_id = match.group(1)
    # The regex matches from the ID up to the `paragraphs: [` array
    # We want to replace the contents of the array.
    
    # We'll use a second regex just on the block to find and replace the paragraphs array.
    block = match.group(0)
    
    if service_id in overview_texts:
        paras = overview_texts[service_id]
        new_paras_str = ",\n                        ".join([f'"{p}"' for p in paras])
        
        # Replace the old paragraphs array with the new one
        # Look for "paragraphs": [ ... ]
        pattern = r'("paragraphs":\s*\[)(.*?)(\])'
        
        # We need to make sure we don't replace too much, re.DOTALL is needed for the inner match
        new_block = re.sub(pattern, rf'\g<1>\n                        {new_paras_str}\n                    \g<3>', block, flags=re.DOTALL)
        return new_block
    
    return block

# The regex will match id: "service-id" and capture it, then match everything up to the end of the overviewDetails object
# Since we might have multiple overviewDetails, it's safer to split by id: " like we did before.

blocks = content.split('id: "')
new_blocks = [blocks[0]]

for block in blocks[1:]:
    id_end = block.find('"')
    service_id = block[:id_end]
    
    if service_id in overview_texts:
        paras = overview_texts[service_id]
        new_paras_str = ",\n                        ".join([f'"{p}"' for p in paras])
        
        pattern = r'("paragraphs":\s*\[)(.*?)(\])'
        
        # Replace only the first occurrence which belongs to this service
        block = re.sub(pattern, rf'\g<1>\n                        {new_paras_str}\n                    \g<3>', block, count=1, flags=re.DOTALL)
        
    new_blocks.append(block)

new_content = 'id: "'.join(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Overview paragraphs updated successfully!")
