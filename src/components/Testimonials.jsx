import React, { useState, useEffect } from 'react';

// The 6 nodes in the circular network
const categories = [
    { id: 'clients', label: 'Clients', icon: 'fas fa-users' },
    { id: 'industry', label: 'Industry', icon: 'fas fa-industry' },
    { id: 'advisors', label: 'Advisors', icon: 'fas fa-user-tie' },
    { id: 'communities', label: 'Communities', icon: 'fas fa-people-carry' },
    { id: 'csr', label: 'CSR Partners', icon: 'fas fa-handshake' },
    { id: 'municipality', label: 'Municipality', icon: 'fas fa-building' }
];

// Testimonial Data
const testimonialsData = {
    clients: [
        {
            text: "Plastroots has completely transformed how we handle our corporate waste. Their transparent tracking and high-quality recycled output exceeded our expectations.",
            author: "Priya Sharma",
            title: "Sustainability Head, TechCorp India",
            entity: "TechCorp India",
            logo: "https://images.unsplash.com/photo-1560179707-f14e90ef3623?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    industry: [
        {
            text: "The recycled granules provided by Plastroots have allowed us to reach our sustainable manufacturing goals without compromising on product quality.",
            author: "Rajiv Desai",
            title: "Operations Director",
            entity: "EcoManufacture Ltd.",
            logo: "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    advisors: [
        {
            text: "I've advised many startups in the circular economy space, but Plastroots stands out for their operational excellence and genuine on-the-ground impact.",
            author: "Dr. Anil Menon",
            title: "Environmental Consultant",
            entity: "Green Future Advisory",
            logo: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    communities: [
        {
            text: "Since Plastroots started their awareness programs here, our streets are cleaner and our local waste pickers are earning a stable, respectable income.",
            author: "Sunita Devi",
            title: "Community Leader",
            entity: "Nagpur Citizens Forum",
            logo: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    csr: [
        {
            text: "Partnering with Plastroots for our CSR initiatives has been incredibly rewarding. We can physically see the tons of plastic diverted from landfills every month.",
            author: "Vikram Singh",
            title: "VP of Corporate Social Responsibility",
            entity: "Global Finance Bank",
            logo: "https://images.unsplash.com/photo-1556761175-4b46a572b786?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    municipality: [
        {
            text: "Hi folks, Plastroots is a team of budding entrepreneurs with extraordinary zeal to make change in the recycling industry. The team lead Kapil is just a phone call away for all plastic waste management solutions required by any entity. My experience with Plastroots was fantastic and I would recommend connecting with them for consultation.",
            author: "Mr. Harshal Gaikwad",
            title: "Chief Officer",
            entity: "Kalyan Dombivli Municipal Corporation",
            logo: "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ]
};

const Testimonials = () => {
    const [activeCategoryIndex, setActiveCategoryIndex] = useState(5); // Default to municipality
    const [currentTestimonialIndex, setCurrentTestimonialIndex] = useState(0);

    const activeCategory = categories[activeCategoryIndex];
    const currentTestimonials = testimonialsData[activeCategory.id];
    const activeTestimonial = currentTestimonials[currentTestimonialIndex];

    // Auto-looping logic
    useEffect(() => {
        const timer = setInterval(() => {
            handleNext();
        }, 6000); // Change testimonial every 6 seconds

        return () => clearInterval(timer);
    }, [activeCategoryIndex, currentTestimonialIndex]);

    const handleNext = () => {
        if (currentTestimonialIndex < currentTestimonials.length - 1) {
            // Next testimonial in current category
            setCurrentTestimonialIndex(prev => prev + 1);
        } else {
            // Move to next category
            const nextCategory = (activeCategoryIndex + 1) % categories.length;
            setActiveCategoryIndex(nextCategory);
            setCurrentTestimonialIndex(0);
        }
    };

    const handlePrev = () => {
        if (currentTestimonialIndex > 0) {
            // Previous testimonial in current category
            setCurrentTestimonialIndex(prev => prev - 1);
        } else {
            // Move to previous category
            const prevCategory = (activeCategoryIndex - 1 + categories.length) % categories.length;
            setActiveCategoryIndex(prevCategory);
            setCurrentTestimonialIndex(testimonialsData[categories[prevCategory].id].length - 1);
        }
    };

    const handleNodeClick = (index) => {
        setActiveCategoryIndex(index);
        setCurrentTestimonialIndex(0);
    };

    return (
        <section className="testimonials-section" style={{ padding: 0, overflow: 'hidden' }}>
            {/* Top Header Area */}
            <div style={{ backgroundColor: '#4a6051', padding: '100px 0 60px 0', width: '100%' }}>
                <div className="container">
                    <div className="si-header text-center fade-up" style={{ textAlign: 'center', color: '#ffffff', maxWidth: '800px', margin: '0 auto' }}>
                        <h2 className="si-eyebrow" style={{ justifyContent: 'center', background: 'none', padding: 0, boxShadow: 'none', color: '#ffffff' }}>
                            Circular Trust Network
                        </h2>
                        <p style={{ maxWidth: '600px', margin: '15px auto 0', fontSize: '1.1rem', opacity: 0.9, color: '#ffffff' }}>
                            A circular ecosystem of trust. Click on any segment to view the testimonial.
                        </p>
                    </div>
                </div>
            </div>

            {/* Bottom Split Background Area */}
            <div className="testimonials-split-wrapper" style={{ padding: '80px 0 100px 0', width: '100%', margin: 0, boxSizing: 'border-box' }}>
                <div className="testimonials-flex-container" style={{ display: 'flex', width: '100%', margin: 0, padding: 0, boxSizing: 'border-box' }}>
                    {/* Left Side: Circular Network */}
                    <div className="network-wrapper fade-up" style={{ 
                        animationDelay: '0.2s', 
                        display: 'flex', 
                        justifyContent: 'center', 
                        alignItems: 'center',
                        width: '50%',
                        margin: 0,
                        padding: 0,
                        boxSizing: 'border-box'
                    }}>
                        <div className="network-container" style={{ margin: 0, padding: 0 }}>
                            <div className="network-ring"></div>
                            
                            <div className="network-center-logo">
                                <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="Plastroots Logo" />
                                <div style={{ fontSize: '0.7rem', color: '#16261d', fontWeight: 'bold', marginTop: '5px' }}>linear to circular</div>
                            </div>

                        {categories.map((cat, index) => (
                            <div 
                                key={cat.id} 
                                className={`network-node node-${index} ${index === activeCategoryIndex ? 'active' : ''}`}
                                onClick={() => handleNodeClick(index)}
                            >
                                <i className={cat.icon}></i>
                                <span className="node-label">{cat.label}</span>
                            </div>
                        ))}
                        </div>
                    </div>
                    {/* Right Side: Testimonial Card */}
                    <div className="testimonial-content-wrapper fade-up" style={{ 
                        animationDelay: '0.4s', 
                        display: 'flex', 
                        flexDirection: 'column',
                        justifyContent: 'center', 
                        alignItems: 'center',
                        width: '50%',
                        position: 'relative',
                        zIndex: 10,
                        margin: 0,
                        padding: '2rem 5rem',
                        boxSizing: 'border-box',
                        textAlign: 'center'
                    }}>
                        <i className="fas fa-quote-left quote-icon" style={{ marginBottom: '15px', color: 'var(--accent-green)', fontSize: '2rem' }}></i>
                        
                        <div className="testimonial-header" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginBottom: '20px' }}>
                            <img src={activeTestimonial.logo} alt={activeTestimonial.entity} className="testimonial-logo" style={{ marginBottom: '10px' }} />
                            <div className="testimonial-entity">
                                <h4 style={{ margin: 0, color: 'var(--dark-green)' }}>{activeTestimonial.entity}</h4>
                            </div>
                        </div>
                        
                        <div className="testimonial-body" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '20px' }}>
                            <p style={{ margin: 0, fontStyle: 'italic', fontSize: '1.1rem', color: 'var(--dark-green)' }}>"{activeTestimonial.text}"</p>
                        </div>
                        
                        <div className="testimonial-author" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginBottom: '30px' }}>
                            <strong style={{ color: 'var(--accent-green)', fontSize: '1.1rem' }}>{activeTestimonial.author}</strong>
                            <span style={{ fontSize: '0.9rem', color: 'var(--text-muted)' }}>{activeTestimonial.title}</span>
                        </div>

                        <div className="testimonial-controls" style={{ 
                            position: 'absolute', 
                            top: '50%', 
                            left: 0, 
                            right: 0, 
                            transform: 'translateY(-50%)', 
                            display: 'flex', 
                            justifyContent: 'space-between', 
                            pointerEvents: 'none',
                            padding: '0 30px'
                        }}>
                            <button className="t-control-btn prev" onClick={handlePrev} style={{ pointerEvents: 'auto' }}>
                                <i className="fas fa-chevron-left"></i>
                            </button>
                            <button className="t-control-btn next" onClick={handleNext} style={{ pointerEvents: 'auto' }}>
                                <i className="fas fa-chevron-right"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Testimonials;
