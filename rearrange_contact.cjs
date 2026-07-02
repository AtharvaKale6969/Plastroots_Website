const fs = require('fs');

const content = fs.readFileSync('D:/Plastroots_Website/src/pages/Contact.jsx', 'utf-8');

// Use regex to extract sections
const heroMatch = content.match(/(<section className="contact-hero">[\s\S]*?<\/section>)/);
const deptCardsMatch = content.match(/(<section className="contact-cards-section">[\s\S]*?<\/section>)/);
const officeMapMatch = content.match(/(<section className="contact-office-section fade-up visible">[\s\S]*?<\/section>)/);
const stakeholdersMatch = content.match(/(<section className="contact-stakeholders fade-up visible">[\s\S]*?<\/section>)/);
const formFaqMatch = content.match(/(<section className="contact-bottom-section fade-up visible">[\s\S]*?<\/section>)/);

if (!heroMatch || !deptCardsMatch || !officeMapMatch || !stakeholdersMatch || !formFaqMatch) {
    console.error("Could not match all sections");
    process.exit(1);
}

const newReturnBlock = `
    <div className="contact-page-container">
      {/* 1. Hero Section */}
      ${heroMatch[1]}

      {/* 2. Stakeholders */}
      ${stakeholdersMatch[1]}

      {/* 3. Form & FAQ Grid */}
      ${formFaqMatch[1]}

      {/* 4. Department Cards */}
      ${deptCardsMatch[1]}

      {/* 5. Office & Map */}
      ${officeMapMatch[1]}
    </div>
`;

const startIdx = content.indexOf('<div className="contact-page-container">');
const endIdx = content.lastIndexOf(');');

if (startIdx !== -1 && endIdx !== -1) {
    const newContent = content.substring(0, startIdx) + newReturnBlock.trim() + "\n  );\n};\n\nexport default Contact;\n";
    fs.writeFileSync('D:/Plastroots_Website/src/pages/Contact.jsx', newContent, 'utf-8');
    console.log("Rearranged sections successfully!");
} else {
    console.error("Could not find start or end index.");
}
