import React from 'react';

const ProductsServices = () => {
  return (
    <>
      <section className="hero products-hero-section">
        <div className="container hero-content fade-up visible" style={{ textAlign: 'center', margin: '0 auto', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <h1 className="hero-title" style={{ fontSize: '3rem', lineHeight: '1.2' }}>Products & Services</h1>
          <p className="hero-subtitle" style={{ fontSize: '1.2rem', opacity: 0.9 }}>
            Comprehensive waste management solutions and high-quality recycled materials.
          </p>
        </div>
      </section>

      <section style={{ padding: '100px 0', textAlign: 'center', backgroundColor: '#f4f0e6', color: 'var(--dark-green)', minHeight: '50vh', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
        <div className="container">
          <i className="fas fa-tools" style={{ fontSize: '4rem', color: 'var(--accent-green)', marginBottom: '30px' }}></i>
          <h2 style={{ fontSize: '2.5rem', marginBottom: '20px' }}>Under Construction</h2>
          <p style={{ fontSize: '1.2rem', maxWidth: '600px', margin: '0 auto', opacity: 0.8 }}>
            We are working hard to bring you a comprehensive list of our products and services. Detailed pages will be added soon!
          </p>
        </div>
      </section>
    </>
  );
};

export default ProductsServices;
