import React, { useState } from 'react';
import '../contact.css';
import { 
  Recycle, Flame, Headset, MapPin, Phone, Mail, Globe, 
  Clock, Building2, Landmark, Package, Factory, 
  GraduationCap, Handshake, Users, Leaf, Send, Plus, Minus 
} from 'lucide-react';

const Contact = () => {
  const [activeFaq, setActiveFaq] = useState(null);

  const toggleFaq = (index) => {
    setActiveFaq(activeFaq === index ? null : index);
  };

  const faqs = [
    { question: "What services does Plastroots provide?", answer: "We offer end-to-end waste management, EPR compliance, and alternative fuel resource services." },
    { question: "Do you work with industries and businesses?", answer: "Yes, we collaborate extensively with industries to manage industrial scrap and ensure regulatory compliance." },
    { question: "Can Plastroots assist with EPR compliance?", answer: "Absolutely. We specialize in providing EPR certificates and complete audit trails for brands." },
    { question: "Do you work with municipal bodies and communities?", answer: "Yes, we partner with ULBs and communities to build sustainable local waste recovery ecosystems." },
    { question: "How quickly can I expect a response?", answer: "Our team typically responds to all inquiries within 24 business hours." },
    { question: "How do I apply for a job at Plastroots?", answer: "Please visit our Careers page to view current openings, or send your resume to careers@plastroots.com." }
  ];

  const stakeholders = [
    { icon: <Building2 size={28} strokeWidth={1.5} />, label: "Municipal Corporations" },
    { icon: <Landmark size={28} strokeWidth={1.5} />, label: "Urban Local Bodies (ULBs)" },
    { icon: <Package size={28} strokeWidth={1.5} />, label: "Producers & Brand Owners" },
    { icon: <Factory size={28} strokeWidth={1.5} />, label: "Industries & Manufacturing" },
    { icon: <GraduationCap size={28} strokeWidth={1.5} />, label: "Educational Institutions" },
    { icon: <Handshake size={28} strokeWidth={1.5} />, label: "CSR & Development" },
    { icon: <Users size={28} strokeWidth={1.5} />, label: "Communities & Residents" },
    { icon: <Recycle size={28} strokeWidth={1.5} />, label: "Recycling Partners" }
  ];

  return (
    <div className="contact-page-container">
      {/* 1. Hero Section */}
      <section className="contact-hero" style={{ paddingBottom: '120px', justifyContent: 'center' }}>
        <div className="contact-hero-content fade-up visible" style={{ textAlign: 'center', margin: '0 auto', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <h1 className="contact-hero-title contact-heading-serif" style={{ textAlign: 'center' }}>Get In Touch</h1>
          <p className="contact-hero-subtitle" style={{ textAlign: 'center' }}>
            Whether you're looking for waste management solutions, EPR compliance support, AFR services, recycling partnerships, or sustainability initiatives, our team is here to help.
          </p>
          <p className="contact-hero-subtitle" style={{ textAlign: 'center' }}>
            Let's work together to create practical solutions that reduce landfill dependency and drive a circular economy.
          </p>
        </div>
      </section>

      {/* 2. Bento Grid Layout */}
      <section className="contact-bento-grid fade-up visible">
        
        {/* Department Card 1 */}
        <div className="bento-card span-4">
          <div className="bento-card-inner">
            <div className="contact-card-header">
              <div className="contact-card-icon"><Recycle size={24} /></div>
              <div>
                <h3 style={{ margin: '0 0 5px 0', fontSize: '1.25rem', color: 'var(--contact-heading)' }}>EPR Compliance</h3>
                <p style={{ margin: 0, fontSize: '0.95rem', color: 'var(--contact-text)' }}>Producers, importers, brand owners.</p>
              </div>
            </div>
            <div className="contact-card-info" style={{ marginTop: 'auto', paddingTop: '15px', borderTop: '1px solid var(--contact-border)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div className="contact-info-item"><Phone size={18} color="var(--contact-accent)" /> <span>+91 72489 17078</span></div>
              <div className="contact-info-item"><Clock size={18} color="var(--contact-accent)" /> <span>Mon – Sat: 11 AM – 7 PM</span></div>
            </div>
          </div>
        </div>

        {/* Department Card 2 */}
        <div className="bento-card span-4">
          <div className="bento-card-inner">
            <div className="contact-card-header">
              <div className="contact-card-icon"><Flame size={24} /></div>
              <div>
                <h3 style={{ margin: '0 0 5px 0', fontSize: '1.25rem', color: 'var(--contact-heading)' }}>AFR Services</h3>
                <p style={{ margin: 0, fontSize: '0.95rem', color: 'var(--contact-text)' }}>Alt. Fuel & Raw Material solutions.</p>
              </div>
            </div>
            <div className="contact-card-info" style={{ marginTop: 'auto', paddingTop: '15px', borderTop: '1px solid var(--contact-border)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div className="contact-info-item"><Phone size={18} color="var(--contact-accent)" /> <span>+91 73858 37917</span></div>
              <div className="contact-info-item"><Clock size={18} color="var(--contact-accent)" /> <span>Mon – Sat: 11 AM – 6 PM</span></div>
            </div>
          </div>
        </div>

        {/* Department Card 3 */}
        <div className="bento-card span-4">
          <div className="bento-card-inner">
            <div className="contact-card-header">
              <div className="contact-card-icon"><Headset size={24} /></div>
              <div>
                <h3 style={{ margin: '0 0 5px 0', fontSize: '1.25rem', color: 'var(--contact-heading)' }}>General Queries</h3>
                <p style={{ margin: 0, fontSize: '0.95rem', color: 'var(--contact-text)' }}>Partnerships & general inquiries.</p>
              </div>
            </div>
            <div className="contact-card-info" style={{ marginTop: 'auto', paddingTop: '15px', borderTop: '1px solid var(--contact-border)', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div className="contact-info-item"><Phone size={18} color="var(--contact-accent)" /> <span>+91 77589 17078</span></div>
              <div className="contact-info-item"><Clock size={18} color="var(--contact-accent)" /> <span>Mon – Sat: 11 AM – 6 PM</span></div>
            </div>
          </div>
        </div>

        {/* Contact Form Card */}
        <div className="bento-card span-7">
          <div className="contact-form-header" style={{ padding: '25px', background: 'var(--contact-dark-green)', color: 'white' }}>
            <h2 style={{ margin: '0 0 10px 0', fontSize: '1.5rem', display: 'flex', alignItems: 'center', gap: '10px' }}>Send Us a Message <Leaf size={20} color="#aed581" /></h2>
            <p style={{ margin: 0, opacity: 0.9, fontSize: '0.95rem' }}>Fill out the form below and our team will get back to you.</p>
          </div>
          <div className="contact-form-body" style={{ padding: '25px', position: 'relative' }}>
            <form onSubmit={(e) => e.preventDefault()}>
              <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px', marginBottom: '15px' }}>
                <div className="form-group" style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                  <label style={{ fontSize: '0.85rem', fontWeight: 600 }}>First Name <span style={{ color: 'red' }}>*</span></label>
                  <input type="text" placeholder="First Name" required style={{ padding: '10px', border: '1px solid var(--contact-border)', borderRadius: '6px' }} />
                </div>
                <div className="form-group" style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                  <label style={{ fontSize: '0.85rem', fontWeight: 600 }}>Last Name <span style={{ color: 'red' }}>*</span></label>
                  <input type="text" placeholder="Last Name" required style={{ padding: '10px', border: '1px solid var(--contact-border)', borderRadius: '6px' }} />
                </div>
              </div>
              <div className="form-row" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px', marginBottom: '15px' }}>
                <div className="form-group" style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                  <label style={{ fontSize: '0.85rem', fontWeight: 600 }}>Mobile <span style={{ color: 'red' }}>*</span></label>
                  <input type="tel" placeholder="Mobile Number" required style={{ padding: '10px', border: '1px solid var(--contact-border)', borderRadius: '6px' }} />
                </div>
                <div className="form-group" style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                  <label style={{ fontSize: '0.85rem', fontWeight: 600 }}>Email <span style={{ color: 'red' }}>*</span></label>
                  <input type="email" placeholder="Email Address" required style={{ padding: '10px', border: '1px solid var(--contact-border)', borderRadius: '6px' }} />
                </div>
              </div>
              <div className="form-group" style={{ display: 'flex', flexDirection: 'column', gap: '5px', marginBottom: '15px' }}>
                <label style={{ fontSize: '0.85rem', fontWeight: 600 }}>Service Interested In <span style={{ color: 'red' }}>*</span></label>
                <select required style={{ padding: '10px', border: '1px solid var(--contact-border)', borderRadius: '6px' }}>
                  <option value="">Select Service</option>
                  <option value="epr">EPR Compliance</option>
                  <option value="afr">AFR Services</option>
                  <option value="general">General Inquiry</option>
                </select>
              </div>
              <div className="form-group" style={{ display: 'flex', flexDirection: 'column', gap: '5px', marginBottom: '20px' }}>
                <label style={{ fontSize: '0.85rem', fontWeight: 600 }}>Message <span style={{ color: 'red' }}>*</span></label>
                <textarea rows="3" placeholder="Write your message..." required style={{ padding: '10px', border: '1px solid var(--contact-border)', borderRadius: '6px' }}></textarea>
              </div>
              <button type="submit" className="contact-submit-btn" style={{ background: 'var(--contact-dark-green)', color: 'white', padding: '12px 25px', border: 'none', borderRadius: '6px', fontWeight: 600, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Send size={18} /> Send Message
              </button>
            </form>
            <Leaf className="form-watermark" size={150} color="var(--contact-light-green)" style={{ position: 'absolute', bottom: '10px', right: '10px', opacity: 0.2, pointerEvents: 'none' }} />
          </div>
        </div>

        {/* FAQ Sidebar */}
        <div className="span-5" style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
          {/* FAQ Card */}
          <div className="bento-card" style={{ flexGrow: 1 }}>
            <div className="bento-card-inner">
              <h3 style={{ margin: '0 0 15px 0', fontSize: '1.25rem', display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--contact-dark-green)' }}>FAQ <Leaf size={20} color="var(--contact-accent)" /></h3>
              <div className="faq-list">
                {faqs.map((faq, idx) => (
                  <div key={idx} className={`faq-item ${activeFaq === idx ? 'active' : ''}`} style={{ borderBottom: '1px solid rgba(0,0,0,0.1)', padding: '16px 0' }}>
                    <div className="faq-question" onClick={() => toggleFaq(idx)} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', cursor: 'pointer', fontWeight: 600, fontSize: '1.05rem', color: 'var(--contact-heading)' }}>
                      {faq.question}
                      {activeFaq === idx ? <Minus size={18} color="var(--contact-accent)" /> : <Plus size={18} color="var(--contact-accent)" />}
                    </div>
                    <div className="faq-answer" style={{ maxHeight: activeFaq === idx ? '150px' : 0, overflow: 'hidden', transition: 'max-height 0.3s ease', fontSize: '0.95rem', color: 'var(--contact-text)', marginTop: activeFaq === idx ? '10px' : 0, lineHeight: 1.6 }}>
                      {faq.answer}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Stakeholders Card */}
        <div className="bento-card span-12">
          <div className="bento-card-inner" style={{ textAlign: 'center', alignItems: 'center' }}>
            <h2 style={{ fontSize: '1.8rem', margin: '0 0 10px 0', display: 'inline-flex', alignItems: 'center', gap: '10px', color: 'var(--contact-heading)' }}>Who We Work With <Leaf size={24} color="var(--contact-accent)" /></h2>
            <p style={{ maxWidth: '600px', margin: '0 auto 30px', color: 'var(--contact-text)', fontSize: '0.95rem' }}>We collaborate with a wide range of stakeholders to build sustainable waste management systems and promote circular economy practices.</p>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '40px 20px', justifyItems: 'center', width: '100%' }}>
              {stakeholders.map((item, idx) => (
                <div key={idx} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '10px' }}>
                  <div style={{ width: '50px', height: '50px', borderRadius: '50%', background: 'var(--contact-light-green)', color: 'var(--contact-dark-green)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    {item.icon}
                  </div>
                  <span style={{ fontSize: '0.8rem', fontWeight: 600, color: 'var(--contact-heading)' }}>{item.label}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Map Card */}
        <div className="bento-card span-8 bento-map" style={{ minHeight: '350px' }}>
          <iframe 
            src="https://maps.google.com/maps?q=21.2166221,79.079491&t=&z=16&ie=UTF8&iwloc=&output=embed" 
            width="100%" 
            height="100%" 
            style={{ border: 0, minHeight: '350px' }} 
            allowFullScreen="" 
            loading="lazy" 
            referrerPolicy="no-referrer-when-downgrade"
            title="Plastroots Office Map"
          ></iframe>
        </div>

        {/* Head Office Card */}
        <div className="bento-card span-4">
          <div className="bento-card-inner">
            <h3 style={{ margin: '0 0 15px 0', fontSize: '1.25rem', display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--contact-dark-green)' }}>Head Office <Leaf size={20} color="var(--contact-accent)" /></h3>
            <p style={{ margin: '0 0 10px 0', fontWeight: 600, color: 'var(--contact-heading)' }}>Plastroots Waste Management & Solutions Pvt. Ltd.</p>
            <div style={{ display: 'flex', gap: '10px', color: 'var(--contact-text)', fontSize: '0.95rem', lineHeight: 1.6 }}>
              <MapPin size={18} color="var(--contact-accent)" style={{ flexShrink: 0, marginTop: '3px' }} />
              <span>Plot no 12A, 1st Floor,<br/>Smruti Nagar Rd, Koradi, Bokara,<br/>Nagpur, Maharashtra 441111</span>
            </div>
            
            <div style={{ marginTop: 'auto', paddingTop: '20px', borderTop: '1px solid var(--contact-border)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px', fontSize: '0.95rem' }}><Mail size={18} color="var(--contact-accent)" /> info@plastroots.com</div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '0.95rem' }}><Globe size={18} color="var(--contact-accent)" /> www.plastroots.com</div>
            </div>
          </div>
        </div>

      </section>
    </div>
  );
};

export default Contact;
