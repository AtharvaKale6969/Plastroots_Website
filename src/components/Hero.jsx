import React from 'react';

const Hero = () => {
    return (
        <section className="hero">
            <div className="hero-overlay"></div>
            <div className="container hero-content fade-up visible" style={{ textAlign: 'center', margin: '0 auto', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <h1 className="hero-title" style={{ fontSize: '2.5rem', lineHeight: '1.2' }}>Transforming Waste.<br/>Empowering Communities.</h1>
                <p className="hero-desc" style={{ fontSize: '1.1rem', maxWidth: '800px', margin: '15px auto 0' }}>Creating sustainable livelihoods through plastic waste management, recycling, and environmental awareness.</p>
                <div className="hero-buttons" style={{ display: 'flex', justifyContent: 'center', gap: '15px' }}>
                    <button className="hero-btn hero-btn-primary">Explore Our Initiatives</button>
                    <button className="hero-btn hero-btn-secondary">Get Involved</button>
                </div>
            </div>

        </section>
    );
};

export default Hero;
