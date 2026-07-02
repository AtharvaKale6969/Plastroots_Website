import React from 'react';

const StrategicPartners = () => {
  const partners = [
    { 
        name: "Plastroots Foundation", 
        img: "/Images/PF_LOGO.png", 
        desc: "Driving community impact and awareness through widespread environmental education and social responsibility initiatives." 
    },
    { 
        name: "Shetahit Farm Solutions", 
        img: "/Images/Shetahit.webp", 
        desc: "Innovating agricultural sustainability by promoting organic compost and integrating eco-friendly farming practices." 
    },
    { 
        name: "Geoclaim Energy", 
        img: "/Images/Geoclaim_1.png", 
        desc: "Pioneering renewable energy solutions, specializing in advanced waste-to-energy conversion and biogas plant technologies." 
    }
  ];

  // We need enough items to scroll seamlessly. 
  // Three full sets of the original array (9 items) to act as the first half, 
  // and another three full sets (9 items) to act as the second half.
  // This ensures even very wide screens are covered.
  const displayPartners = [...partners, ...partners, ...partners, ...partners, ...partners, ...partners];

  return (
    <section className="flowup-partners-section" style={{ padding: '100px 0', backgroundColor: '#ffffff', position: 'relative', overflow: 'hidden' }}>
      {/* Background blurred orbs (Flow-up style) */}
      <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', overflow: 'hidden', pointerEvents: 'none', zIndex: 0 }}>
        <div style={{ position: 'absolute', top: '-20%', right: '10%', width: '50%', height: '50%', borderRadius: '50%', background: 'rgba(34, 197, 94, 0.05)', filter: 'blur(100px)' }}></div>
        <div style={{ position: 'absolute', bottom: '-20%', left: '10%', width: '50%', height: '50%', borderRadius: '50%', background: 'rgba(59, 130, 246, 0.04)', filter: 'blur(100px)' }}></div>
      </div>

      <div style={{ position: 'relative', zIndex: 10, maxWidth: '100%', margin: '0 auto' }}>
        {/* Header matching Flow-Up */}
        <div className="container fade-up visible" style={{ textAlign: 'center', marginBottom: '60px', display: 'flex', flexDirection: 'column', alignItems: 'center', padding: '0 24px' }}>
          <span style={{ display: 'block', marginBottom: '16px', color: '#16a34a', fontWeight: '600', letterSpacing: '0.1em', textTransform: 'uppercase', fontSize: '0.875rem' }}>
            Collaborations
          </span>
          <h2 style={{ fontSize: '3rem', fontWeight: '700', color: '#111827', marginBottom: '24px', lineHeight: '1.2', letterSpacing: '-0.02em' }}>
            Our Strategic Partners
          </h2>
          <div style={{ width: '80px', height: '4px', backgroundColor: '#16a34a', borderRadius: '9999px', marginBottom: '32px' }}></div>
          <p style={{ fontSize: '1.125rem', color: '#4b5563', maxWidth: '600px', margin: '0 auto', lineHeight: '1.7' }}>
            Collaborating with industry leaders who share our commitment to sustainability, innovation, and lasting environmental impact.
          </p>
        </div>

        {/* Marquee Container */}
        <div className="marquee-wrapper">
          <div className="marquee-track">
            {displayPartners.map((partner, index) => (
              <div key={index} className="flowup-partner-card">
                <div className="flowup-card-corner"></div>
                <div className="flowup-logo-container">
                  <img src={partner.img} alt={partner.name} className="flowup-partner-img" />
                </div>
                <h3 className="flowup-partner-title">{partner.name}</h3>
                <p className="flowup-partner-desc">{partner.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      <style>{`
        .marquee-wrapper {
          width: 100%;
          overflow: hidden;
          padding: 20px 0;
          position: relative;
        }

        /* Fade gradients on edges */
        .marquee-wrapper::before,
        .marquee-wrapper::after {
          content: "";
          position: absolute;
          top: 0;
          width: 150px;
          height: 100%;
          z-index: 2;
          pointer-events: none;
        }
        .marquee-wrapper::before {
          left: 0;
          background: linear-gradient(to right, #ffffff 0%, rgba(255,255,255,0) 100%);
        }
        .marquee-wrapper::after {
          right: 0;
          background: linear-gradient(to left, #ffffff 0%, rgba(255,255,255,0) 100%);
        }

        .marquee-track {
          display: flex;
          width: max-content;
          animation: marquee 40s linear infinite;
        }
        
        .marquee-track:hover {
          animation-play-state: paused;
        }

        .flowup-partner-card {
          position: relative;
          background: #ffffff;
          border: 1px solid #f3f4f6;
          border-radius: 24px;
          padding: 40px;
          box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
          transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
          overflow: hidden;
          cursor: pointer;
          display: flex;
          flex-direction: column;
          align-items: center;
          text-align: center;
          
          /* Fixed dimensions for infinite scroll track */
          width: 350px;
          margin-right: 32px;
          flex-shrink: 0;
        }

        .flowup-partner-card:hover {
          box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
          transform: translateY(-8px);
          border-color: rgba(34, 197, 94, 0.1);
        }

        .flowup-card-corner {
          position: absolute;
          top: 0;
          right: 0;
          width: 120px;
          height: 120px;
          background: rgba(34, 197, 94, 0.03);
          border-bottom-left-radius: 100px;
          z-index: 0;
          transition: background 0.5s ease;
        }

        .flowup-partner-card:hover .flowup-card-corner {
          background: rgba(34, 197, 94, 0.08);
        }

        .flowup-logo-container {
          position: relative;
          width: 100%;
          height: 140px;
          display: flex;
          align-items: center;
          justify-content: center;
          margin-bottom: 24px;
          z-index: 1;
        }

        .flowup-partner-img {
          max-width: 80%;
          max-height: 100%;
          object-fit: contain;
          transition: all 0.5s ease;
        }

        .flowup-partner-card:hover .flowup-partner-img {
          transform: scale(1.05);
        }

        .flowup-partner-title {
          font-family: var(--font-heading, 'Inter', sans-serif);
          font-size: 1.25rem;
          font-weight: 700;
          color: #111827;
          margin-bottom: 12px;
          position: relative;
          z-index: 1;
          transition: color 0.3s ease;
        }

        .flowup-partner-card:hover .flowup-partner-title {
          color: #16a34a;
        }

        .flowup-partner-desc {
          font-size: 0.95rem;
          color: #6b7280;
          line-height: 1.6;
          margin: 0;
          position: relative;
          z-index: 1;
        }

        @keyframes marquee {
          0% {
            transform: translateX(0);
          }
          100% {
            /* Transform exactly -50% to seamlessly loop */
            transform: translateX(calc(-50%));
          }
        }
        
        /* Mobile responsiveness */
        @media (max-width: 768px) {
          .marquee-wrapper::before,
          .marquee-wrapper::after {
            width: 50px;
          }
          .flowup-partner-card {
            width: 280px;
            margin-right: 20px;
            padding: 30px 20px;
          }
          .flowup-logo-container {
            height: 100px;
          }
        }
      `}</style>
    </section>
  );
};

export default StrategicPartners;
