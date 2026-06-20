import React from 'react';

const About = () => {
    return (
        <section className="about-section" id="about">
            <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="" className="watermark-tree-about" />
            <div className="decor decor-left"></div>
            <div className="decor decor-right"></div>
            
            <div className="container about-grid">
                <div className="about-visual fade-in visible">
                    <div className="circle-infographic">
                        <div className="center-logo">
                            <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="Plastroots Center Logo" className="center-logo-img" />
                        </div>
                        
                        <div className="orbit-ring">
                            <div className="step-item step-1">
                                <div className="step-content">
                                    <div className="step-icon"><i className="fas fa-truck"></i></div>
                                    <span>COLLECTION</span>
                                </div>
                            </div>
                            <div className="step-item step-2">
                                <div className="step-content">
                                    <div className="step-icon"><i className="fas fa-trash-alt"></i></div>
                                    <span>SEGREGATION</span>
                                </div>
                            </div>
                            <div className="step-item step-3">
                                <div className="step-content">
                                    <div className="step-icon"><i className="fas fa-industry"></i></div>
                                    <span>PROCESSING</span>
                                </div>
                            </div>
                            <div className="step-item step-4">
                                <div className="step-content">
                                    <div className="step-icon"><i className="fas fa-recycle"></i></div>
                                    <span>RECYCLING</span>
                                </div>
                            </div>
                            <div className="step-item step-5">
                                <div className="step-content">
                                    <div className="step-icon"><i className="fas fa-leaf"></i></div>
                                    <span>REINTRODUCE</span>
                                </div>
                            </div>
                            
                            <div className="circle-arrows"></div>
                        </div>
                    </div>
                </div>

                <div className="about-content slide-in-right visible">
                    <h2 className="section-heading">ABOUT <span style={{ color: 'var(--primary-green)' }}>PLASTROOTS</span></h2>
                    
                    <p className="fade-up visible" style={{ animationDelay: '0.1s' }}>Plastroots is a social enterprise dedicated to transforming waste management in India by shifting from a linear to a circular model. Founded in 2019 by social entrepreneur Mr. Kapil Jangale, Plastroots Waste Management & Solutions Private Limited works to reduce carbon footprints and minimize landfill usage.</p>
                    <p className="fade-up visible" style={{ animationDelay: '0.2s' }}>We are committed to implementing effective waste management systems in remote areas to promote a circular economy. Our initiatives include awareness campaigns, training programs, and workshops designed to educate communities on sustainable practices.</p>
                    <p className="fade-up visible" style={{ animationDelay: '0.3s' }}>Plastroots focuses on professional waste aggregation and segregation, guided by the principles of Reduce, Reuse, and Recycle. Our primary objective is to address the lack of structured waste management in rural regions outside major cities, where nearly 75% of waste remains unsorted and contributes to environmental pollution. By introducing systematic solutions, we strive to build cleaner, healthier, and more sustainable communities.</p>
                </div>
            </div>

            <section className="vmv-section">
                <div className="container">
                    <div className="vmv-grid">
                        <div className="vmv-card vision-card fade-up visible" style={{ animationDelay: '0.1s' }}>
                            <div className="vmv-icon"><i className="fas fa-eye"></i></div>
                            <h3>Our Vision</h3>
                            <p>To become a leading management & resource recovery company, enabling a cleaner, circular & landfill-free future for India.</p>
                        </div>

                        <div className="vmv-card mission-card fade-up visible" style={{ animationDelay: '0.2s' }}>
                            <div className="vmv-icon"><i className="fas fa-bullseye"></i></div>
                            <h3>Our Mission</h3>
                            <p>To provide innovative & sustainable waste management solutions through collection, segregation, resource recovery, helping communities & organizations reduce environmental impact while creating value from waste.</p>
                        </div>

                        <div className="vmv-card values-card fade-up visible" style={{ animationDelay: '0.3s' }}>
                            <div className="vmv-icon"><i className="fas fa-heart"></i></div>
                            <h3>Our Values</h3>
                            <ul className="values-list">
                                <li><i className="fas fa-check"></i> Sustainability</li>
                                <li><i className="fas fa-check"></i> Responsibility</li>
                                <li><i className="fas fa-check"></i> Integrity</li>
                                <li><i className="fas fa-check"></i> Innovation</li>
                                <li><i className="fas fa-check"></i> Safety</li>
                                <li><i className="fas fa-check"></i> Resource Recovery</li>
                                <li><i className="fas fa-check"></i> Collaboration</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <section className="editorial-features-section">
                <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="" className="ed-bg-watermark" />
                <div className="container" style={{ padding: '80px 0', position: 'relative', zIndex: 2 }}>
                    <div className="editorial-feature-grid">
                        <div className="ed-feature-card fade-up visible" style={{ animationDelay: '0.1s' }}>
                            <div className="ed-card-header">
                                <span className="ed-index-mark">01 &mdash; FOOTPRINT</span>
                                <div className="ed-seal-container">
                                    <div className="ed-seal">
                                        <i className="fas fa-map-marked-alt"></i>
                                    </div>
                                    <svg className="ed-root-line" viewBox="0 0 10 100" preserveAspectRatio="none">
                                        <path d="M5,0 Q8,20 5,40 T5,80 L5,100" />
                                    </svg>
                                </div>
                            </div>
                            <div className="ed-card-body">
                                <h4>Our Footprint</h4>
                                <p>Headquartered in Nagpur, with regional facilities across India, we apply our specialist skills across all sectors—serving both private and public enterprises including ULBs, municipalities, industries, and commercial establishments. Our solutions are always fit for purpose, cost effective, and fully compliant with relevant legislation.</p>
                            </div>
                        </div>

                        <div className="ed-feature-card fade-up visible" style={{ animationDelay: '0.2s' }}>
                            <div className="ed-card-header">
                                <span className="ed-index-mark">02 &mdash; ROOTS</span>
                                <div className="ed-seal-container">
                                    <div className="ed-seal">
                                        <i className="fas fa-seedling"></i>
                                    </div>
                                    <svg className="ed-root-line" viewBox="0 0 10 100" preserveAspectRatio="none">
                                        <path d="M5,0 Q2,20 5,40 T5,80 L5,100" />
                                    </svg>
                                </div>
                            </div>
                            <div className="ed-card-body">
                                <h4>6 Years of Taking Root</h4>
                                <p>From our humble beginnings as a door-to-door waste collection service in 2019, we continue to drive the industry forward through innovation, advanced systems, and a world-class fleet. Our wealth of knowledge makes us a trusted partner in sustainable waste solutions, rooted in our local heritage.</p>
                            </div>
                        </div>

                        <div className="ed-feature-card fade-up visible" style={{ animationDelay: '0.3s' }}>
                            <div className="ed-card-header">
                                <span className="ed-index-mark">03 &mdash; IMPACT</span>
                                <div className="ed-seal-container">
                                    <div className="ed-seal">
                                        <i className="fas fa-chart-line"></i>
                                    </div>
                                    <svg className="ed-root-line" viewBox="0 0 10 100" preserveAspectRatio="none">
                                        <path d="M5,0 Q8,30 5,50 T5,90 L5,100" />
                                    </svg>
                                </div>
                            </div>
                            <div className="ed-card-body">
                                <h4>Towards Making a Difference</h4>
                                <p>We pride ourselves on setting new standards of compliance that guide the waste management industry toward a safer, more environmentally friendly future. With the lowest lost-time injury rate and facilities rated above 95% in environmental compliance, we demonstrate our commitment to excellence.</p>
                            </div>
                        </div>

                        <div className="ed-feature-card fade-up visible" style={{ animationDelay: '0.4s' }}>
                            <div className="ed-card-header">
                                <span className="ed-index-mark">04 &mdash; SOLUTIONS</span>
                                <div className="ed-seal-container">
                                    <div className="ed-seal">
                                        <i className="fas fa-lightbulb"></i>
                                    </div>
                                    <svg className="ed-root-line" viewBox="0 0 10 100" preserveAspectRatio="none">
                                        <path d="M5,0 Q2,25 5,45 T5,85 L5,100" />
                                    </svg>
                                </div>
                            </div>
                            <div className="ed-card-body">
                                <h4>Alternative Solutions</h4>
                                <p>For years, we have pioneered alternative waste management solutions, proudly leading the way toward a more sustainable future. Our broad spectrum of services includes non-hazardous waste transport, treatment and disposal, on-site waste management, industrial cleaning, and landfill facilities management.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </section>
    );
};

export default About;
