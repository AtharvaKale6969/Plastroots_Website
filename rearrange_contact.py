import re

with open('D:/Plastroots_Website/src/pages/Contact.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract sections
hero = re.search(r'(<section className="contact-hero">.*?</section>)', content, re.DOTALL).group(1)
dept_cards = re.search(r'(<section className="contact-cards-section">.*?</section>)', content, re.DOTALL).group(1)
office_map = re.search(r'(<section className="contact-office-section fade-up visible">.*?</section>)', content, re.DOTALL).group(1)
stakeholders = re.search(r'(<section className="contact-stakeholders fade-up visible">.*?</section>)', content, re.DOTALL).group(1)
form_faq = re.search(r'(<section className="contact-bottom-section fade-up visible">.*?</section>)', content, re.DOTALL).group(1)

# Ensure all matched
if not (hero and dept_cards and office_map and stakeholders and form_faq):
    print("Could not match all sections")
    exit(1)

# Build the new return block
new_return_block = f"""
    <div className="contact-page-container">
      {{/* 1. Hero Section */}}
      {hero}

      {{/* 2. Stakeholders */}}
      {stakeholders}

      {{/* 3. Form & FAQ Grid */}}
      {form_faq}

      {{/* 4. Department Cards */}}
      {dept_cards}

      {{/* 5. Office & Map */}}
      {office_map}
    </div>
"""

# Replace the original return block
# We find everything from <div className="contact-page-container"> to the last </div> before );
# Since regex can be tricky with nested divs, we'll replace the chunk from <div className="contact-page-container"> to the end of the file, then append ); } export default Contact;

start_idx = content.find('<div className="contact-page-container">')
end_idx = content.rfind(');')

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_return_block.strip() + "\n  );\n};\n\nexport default Contact;\n"
    with open('D:/Plastroots_Website/src/pages/Contact.jsx', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Rearranged sections successfully!")
else:
    print("Could not find start or end index.")
