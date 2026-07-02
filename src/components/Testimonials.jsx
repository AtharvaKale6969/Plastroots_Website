import React, { useState, useEffect, useRef } from 'react';
import { Users, Factory, UserCheck, HeartHandshake, Handshake, Building2, Quote, ChevronLeft, ChevronRight } from 'lucide-react';
import '../premium-testimonials.css';

const useIntersectionObserver = (options) => {
    const [isIntersecting, setIsIntersecting] = useState(false);
    const ref = useRef(null);
    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) setIsIntersecting(true);
        }, options);
        if (ref.current) observer.observe(ref.current);
        return () => { if (ref.current) observer.unobserve(ref.current); };
    }, [options]);
    return [ref, isIntersecting];
};

const categories = [
    { id: 'clients', label: 'Clients', icon: Users },
    { id: 'industry', label: 'Industry', icon: Factory },
    { id: 'advisors', label: 'Advisors', icon: UserCheck },
    { id: 'communities', label: 'Communities', icon: HeartHandshake },
    { id: 'csr', label: 'CSR Partners', icon: Handshake },
    { id: 'municipality', label: 'Municipality', icon: Building2 }
];

const testimonialsData = {
    clients: [
        {
            text: "Plastroots transformed our corporate waste management with transparent tracking and high-quality recycled output.",
            author: "Priya Sharma",
            title: "Sustainability Head",
            entity: "TechCorp India",
            logo: "https://images.unsplash.com/photo-1560179707-f14e90ef3623?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    industry: [
        {
            text: "Their recycled granules helped us achieve sustainable manufacturing without compromising product quality.",
            author: "Rajiv Desai",
            title: "Operations Director",
            entity: "EcoManufacture Ltd.",
            logo: "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    advisors: [
        {
            text: "Plastroots stands out in the circular economy for their operational excellence and genuine impact.",
            author: "Dr. Anil Menon",
            title: "Environmental Consultant",
            entity: "Green Future Advisory",
            logo: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    communities: [
        {
            text: "Thanks to their awareness programs, our streets are cleaner and waste pickers earn a stable income.",
            author: "Sunita Devi",
            title: "Community Leader",
            entity: "Nagpur Citizens Forum",
            logo: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    csr: [
        {
            text: "Partnering with Plastroots has been rewarding—we physically see the plastic diverted from landfills.",
            author: "Vikram Singh",
            title: "VP of CSR",
            entity: "Global Finance Bank",
            logo: "https://images.unsplash.com/photo-1556761175-4b46a572b786?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ],
    municipality: [
        {
            text: "A team of extraordinary entrepreneurs. Kapil and his team are just a phone call away for any waste management solutions.",
            author: "Mr. Harshal Gaikwad",
            title: "Chief Officer",
            entity: "Kalyan Dombivli Municipal Corp",
            logo: "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?ixlib=rb-4.0.3&auto=format&fit=crop&w=100&q=80"
        }
    ]
};

const Testimonials = () => {
    const [activeCategoryIndex, setActiveCategoryIndex] = useState(5);
    const [currentTestimonialIndex, setCurrentTestimonialIndex] = useState(0);
    const [ref, isIntersecting] = useIntersectionObserver({ threshold: 0.1 });

    const activeCategory = categories[activeCategoryIndex];
    const currentTestimonials = testimonialsData[activeCategory.id];
    const activeTestimonial = currentTestimonials[currentTestimonialIndex];

    useEffect(() => {
        const timer = setInterval(() => {
            handleNext();
        }, 6000);
        return () => clearInterval(timer);
    }, [activeCategoryIndex, currentTestimonialIndex]);

    const handleNext = () => {
        if (currentTestimonialIndex < currentTestimonials.length - 1) {
            setCurrentTestimonialIndex(prev => prev + 1);
        } else {
            const nextCategory = (activeCategoryIndex + 1) % categories.length;
            setActiveCategoryIndex(nextCategory);
            setCurrentTestimonialIndex(0);
        }
    };

    const handlePrev = () => {
        if (currentTestimonialIndex > 0) {
            setCurrentTestimonialIndex(prev => prev - 1);
        } else {
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
        <section className="premium-testimonials-section" ref={ref}>
            <div className={`premium-testimonials-container ${isIntersecting ? 'animate-fade-up' : 'opacity-0'}`} style={{ transition: 'opacity 0.6s ease-out, transform 0.6s ease-out' }}>
                <div className="premium-testimonials-header">
                    <span className="premium-badge" style={{ background: 'rgba(52, 211, 153, 0.15)', color: '#34d399', display: 'inline-block', padding: '8px 20px', borderRadius: '30px', fontSize: '0.85rem', fontWeight: '600', letterSpacing: '1.5px', textTransform: 'uppercase', marginBottom: '20px' }}>
                        Circular Trust Network
                    </span>
                    <h2>An Ecosystem of Trust</h2>
                    <p>Click on any segment to view the testimonial.</p>
                </div>

                <div className="premium-testimonials-layout">
                    {/* Left Side: Circular Network */}
                    <div className="premium-network-wrapper">
                        <div className="premium-network-container">
                            <div className="premium-network-ring"></div>
                            
                            <div className="premium-network-center">
                                <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="Plastroots Logo" />
                            </div>

                            {categories.map((cat, index) => {
                                const Icon = cat.icon;
                                const angle = (index / categories.length) * 360;
                                // 160px is the radius of the circle
                                const radius = 160;
                                return (
                                    <div 
                                        key={cat.id} 
                                        className={`premium-network-node ${index === activeCategoryIndex ? 'active' : ''}`}
                                        onClick={() => handleNodeClick(index)}
                                        style={{ 
                                            transform: `rotate(${angle}deg) translate(${radius}px) rotate(-${angle}deg)` 
                                        }}
                                    >
                                        <div className="premium-node-icon-box">
                                            <Icon className="premium-node-icon" strokeWidth={1.5} />
                                        </div>
                                        <span className="premium-node-label">{cat.label}</span>
                                    </div>
                                );
                            })}
                        </div>
                    </div>

                    {/* Right Side: Premium Testimonial Card */}
                    <div className="premium-testimonial-card-wrapper">
                        <div className="premium-testimonial-card">
                            <Quote className="premium-quote-icon" />
                            
                            <div className="premium-testimonial-content">
                                <p className="premium-testimonial-text">"{activeTestimonial.text}"</p>
                            </div>
                            
                            <div className="premium-testimonial-footer">
                                <img src={activeTestimonial.logo} alt={activeTestimonial.entity} className="premium-testimonial-avatar" />
                                <div className="premium-testimonial-author">
                                    <h4>{activeTestimonial.author}</h4>
                                    <span>{activeTestimonial.title}</span>
                                    <strong>{activeTestimonial.entity}</strong>
                                </div>
                            </div>
                            
                            <div className="premium-testimonial-controls">
                                <button className="premium-control-btn" onClick={handlePrev}>
                                    <ChevronLeft />
                                </button>
                                <button className="premium-control-btn" onClick={handleNext}>
                                    <ChevronRight />
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Testimonials;
