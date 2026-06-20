import React from 'react';

const Contact = () => {
  return (
    <>
      <section className="hero contact-hero-section">
        <div className="container hero-content fade-up visible" style={{ textAlign: 'center', margin: '0 auto', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <h1 className="hero-title" style={{ fontSize: '3rem', lineHeight: '1.2' }}>Contact Us</h1>
          <p className="hero-subtitle" style={{ fontSize: '1.2rem', opacity: 0.9 }}>
            Reach out to our team to discuss waste management solutions for your organization.
          </p>
        </div>
      </section>

      <section style={{ padding: '100px 0', textAlign: 'center', backgroundColor: '#f4f0e6', color: 'var(--dark-green)', minHeight: '50vh', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
        <div className="container">
          <i className="fas fa-headset" style={{ fontSize: '4rem', color: 'var(--accent-green)', marginBottom: '30px' }}></i>
          <h2 style={{ fontSize: '2.5rem', marginBottom: '20px' }}>Under Construction</h2>
          <p style={{ fontSize: '1.2rem', maxWidth: '600px', margin: '0 auto', opacity: 0.8 }}>
            Our contact forms and detailed office locations are being set up. Full page will be live soon!
          </p>
          <div style={{ marginTop: '40px', fontSize: '1.2rem', fontWeight: 'bold' }}>
            In the meantime, call us at: +91 7620094031
          </div>
        </div>
      </section>
    </>
  );
};

export default Contact;
