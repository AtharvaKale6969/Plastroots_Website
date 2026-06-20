import React from 'react';
import About from '../components/About';
import Stats from '../components/Stats';

const AboutUs = () => {
  return (
    <div className="about-us-page-wrapper">
      <div className="watermark-floating watermark-1"><i className="fas fa-leaf"></i></div>
      <div className="watermark-floating watermark-2"><i className="fas fa-seedling"></i></div>
      <div className="watermark-floating watermark-3"><i className="fas fa-tree"></i></div>

      <section className="about-hero-section">
        <div className="container">
          <div className="about-hero-content fade-in visible">
            <h1>About Us</h1>
            <p>Empowering a cleaner, circular, and landfill-free future for India.</p>
          </div>
        </div>
      </section>

      <div style={{ paddingBottom: '60px' }}>
        <About />
      </div>
    </div>
  );
};

export default AboutUs;
