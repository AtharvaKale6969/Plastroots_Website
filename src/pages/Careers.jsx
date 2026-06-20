import React, { useState } from 'react';

const Careers = () => {
    const [openFaq, setOpenFaq] = useState(0);

    const toggleFaq = (index) => {
        setOpenFaq(openFaq === index ? -1 : index);
    };

    const faqs = [
        { q: "Do you offer internships?", a: "Yes, we offer internships across various departments including operations, sustainability, and HR. Keep an eye on our openings or reach out directly." },
        { q: "Are field roles available?", a: "Absolutely. Field operations are the backbone of our circular economy model. We regularly hire for on-ground roles." },
        { q: "Can freshers apply?", a: "Yes, we welcome fresh talent who are passionate about sustainability and eager to learn on the job." },
        { q: "Is prior waste management experience mandatory?", a: "For specific technical roles, yes. However, for many roles, a strong willingness to learn and passion for the environment is more important." },
        { q: "Where are the positions located?", a: "We have roles across our headquarters in Nagpur as well as regional facilities across India." }
    ];

    return (
        <div className="careers-page">
            {/* HERO SECTION */}
            <section className="careers-hero">
                <div className="careers-hero-overlay"></div>
                <div className="container">
                    <div className="careers-hero-content fade-up visible">
                        <h1>Build a Career<br/><span>That Creates Impact</span></h1>
                        <div className="careers-hero-divider">
                            <i className="fas fa-leaf"></i>
                        </div>
                        <p>Join Plastroots and be part of a mission that is re-rooting waste from linear to circular for a cleaner, greener tomorrow.</p>
                    </div>
                </div>
            </section>

            {/* WHY JOIN SECTION */}
            <section className="careers-why-join">
                <div className="container">
                    <div className="c-grid-2">
                        <div className="c-why-text">
                            <h2>Why Join Plastroots?</h2>
                            <p className="c-italic">At Plastroots, we believe waste is not a problem to be managed but a resource to be recovered. Every team member contributes to building sustainable waste management systems that create environmental, social, and economic impact.</p>
                            <p>We work closely with communities, local bodies, industries, and recycling partners to drive India's transition towards a circular economy.</p>
                        </div>
                        <div className="c-why-cards">
                            <div className="c-why-card">
                                <div className="c-why-icon"><i className="fas fa-leaf"></i></div>
                                <h4>Purpose-Driven Work</h4>
                                <p>Create measurable environmental impact every day.</p>
                            </div>
                            <div className="c-why-card">
                                <div className="c-why-icon"><i className="fas fa-sync-alt"></i></div>
                                <h4>Circular Economy Innovation</h4>
                                <p>Work on real-world waste management challenges.</p>
                            </div>
                            <div className="c-why-card">
                                <div className="c-why-icon"><i className="fas fa-users"></i></div>
                                <h4>Collaborative Culture</h4>
                                <p>Learn and grow with passionate and supportive teams.</p>
                            </div>
                            <div className="c-why-card">
                                <div className="c-why-icon"><i className="fas fa-chart-line"></i></div>
                                <h4>Career Growth</h4>
                                <p>Build skills across sustainability, operations, and business.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* CULTURE SECTION */}
            <section className="careers-culture bg-light">
                <div className="container">
                    <div className="c-grid-2">
                        <div className="c-who-look">
                            <h2>Who We Look For</h2>
                            <ul className="c-look-list">
                                <li><i className="far fa-check-circle"></i> Problem solvers</li>
                                <li><i className="far fa-check-circle"></i> Sustainability enthusiasts</li>
                                <li><i className="far fa-check-circle"></i> Community-driven individuals</li>
                                <li><i className="far fa-check-circle"></i> Operations and field professionals</li>
                                <li><i className="far fa-check-circle"></i> Innovative thinkers</li>
                                <li><i className="far fa-check-circle"></i> Team players</li>
                            </ul>
                        </div>
                        <div className="c-life">
                            <h2>Life at Plastroots</h2>
                            <div className="c-photo-grid">
                                <div className="c-photo-item">
                                    <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="Team Collaboration" />
                                    <span>Team Collaboration</span>
                                </div>
                                <div className="c-photo-item">
                                    <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="Field Visits" />
                                    <span>Field Visits</span>
                                </div>
                                <div className="c-photo-item">
                                    <img src="https://images.unsplash.com/photo-1531206715517-5c0ba140b2b8?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="Community Engagement" />
                                    <span>Community Engagement</span>
                                </div>
                                <div className="c-photo-item">
                                    <img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="Awareness Programs" />
                                    <span>Awareness Programs</span>
                                </div>
                                <div className="c-photo-item">
                                    <img src="https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="Facility Operations" />
                                    <span>Facility Operations</span>
                                </div>
                                <div className="c-photo-item">
                                    <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=500&q=80" alt="Training & Workshops" />
                                    <span>Training & Workshops</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* CURRENT OPENINGS */}
            <section className="careers-openings">
                <div className="container">
                    <div className="text-center mb-5" style={{ textAlign: 'center', marginBottom: '40px' }}>
                        <h2 className="c-section-title">Current Openings</h2>
                        <div className="c-title-divider"><i className="fas fa-leaf"></i></div>
                    </div>
                    
                    <div className="c-job-grid">
                        <div className="c-job-card">
                            <h3>Business Development Associate (EPR)</h3>
                            <div className="c-job-meta">
                                <span><i className="fas fa-map-marker-alt"></i> Nagpur, Maharashtra</span>
                                <span><i className="far fa-clock"></i> Full-Time</span>
                            </div>
                            <div className="c-job-reqs">
                                <h5>Key Responsibilities</h5>
                                <ul>
                                    <li>Identify and develop EPR partnership opportunities</li>
                                    <li>Engage with producers, recyclers and stakeholders</li>
                                    <li>Support in EPR compliance and documentation</li>
                                    <li>Achieve business development targets</li>
                                </ul>
                            </div>
                            <button className="c-btn">Apply Now <i className="fas fa-arrow-right"></i></button>
                        </div>

                        <div className="c-job-card">
                            <h3>Finance Associate</h3>
                            <div className="c-job-meta">
                                <span><i className="fas fa-map-marker-alt"></i> Nagpur, Maharashtra</span>
                                <span><i className="far fa-clock"></i> Full-Time</span>
                            </div>
                            <div className="c-job-reqs">
                                <h5>Key Responsibilities</h5>
                                <ul>
                                    <li>Assist in financial planning and reporting</li>
                                    <li>Maintain records of transactions and invoices</li>
                                    <li>Support budgeting, MIS and audits</li>
                                    <li>Coordinate with internal teams and vendors</li>
                                </ul>
                            </div>
                            <button className="c-btn">Apply Now <i className="fas fa-arrow-right"></i></button>
                        </div>

                        <div className="c-job-card">
                            <h3>HR Associate</h3>
                            <div className="c-job-meta">
                                <span><i className="fas fa-map-marker-alt"></i> Nagpur, Maharashtra</span>
                                <span><i className="far fa-clock"></i> Full-Time</span>
                            </div>
                            <div className="c-job-reqs">
                                <h5>Key Responsibilities</h5>
                                <ul>
                                    <li>Support end-to-end recruitment process</li>
                                    <li>Maintain employee records and documentation</li>
                                    <li>Coordinate training and development programs</li>
                                    <li>Assist in HR operations and engagement activities</li>
                                </ul>
                            </div>
                            <button className="c-btn">Apply Now <i className="fas fa-arrow-right"></i></button>
                        </div>
                    </div>

                    <div className="text-center mt-5" style={{ textAlign: 'center', marginTop: '40px' }}>
                        <button className="c-btn-dark">View All Openings</button>
                    </div>
                </div>
            </section>

            {/* PROCESS & FAQ */}
            <section className="careers-process-faq bg-light">
                <div className="container">
                    <div className="c-grid-2" style={{ gap: '60px' }}>
                        <div className="c-process">
                            <h2>Our Hiring Process</h2>
                            <div className="c-timeline-vertical">
                                <div className="c-timeline-step-v">
                                    <div className="c-t-icon-v"><i className="fas fa-file-signature"></i></div>
                                    <div className="c-t-text-v">
                                        <h6>Apply</h6>
                                        <p>Submit your application</p>
                                    </div>
                                </div>
                                <div className="c-timeline-step-v">
                                    <div className="c-t-icon-v"><i className="fas fa-search"></i></div>
                                    <div className="c-t-text-v">
                                        <h6>Resume Screening</h6>
                                        <p>We review your profile</p>
                                    </div>
                                </div>
                                <div className="c-timeline-step-v">
                                    <div className="c-t-icon-v"><i className="fas fa-users"></i></div>
                                    <div className="c-t-text-v">
                                        <h6>Interview</h6>
                                        <p>Connect with our team</p>
                                    </div>
                                </div>
                                <div className="c-timeline-step-v">
                                    <div className="c-t-icon-v"><i className="fas fa-clipboard-list"></i></div>
                                    <div className="c-t-text-v">
                                        <h6>Assessment (If Required)</h6>
                                        <p>Showcase your skills</p>
                                    </div>
                                </div>
                                <div className="c-timeline-step-v">
                                    <div className="c-t-icon-v"><i className="fas fa-handshake"></i></div>
                                    <div className="c-t-text-v">
                                        <h6>Offer</h6>
                                        <p>We make you an offer</p>
                                    </div>
                                </div>
                                <div className="c-timeline-step-v">
                                    <div className="c-t-icon-v"><i className="fas fa-seedling"></i></div>
                                    <div className="c-t-text-v">
                                        <h6>Join Us</h6>
                                        <p>Begin your journey with impact</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="c-faq">
                            <h2>Frequently Asked Questions</h2>
                            <div className="c-accordion">
                                {faqs.map((faq, idx) => (
                                    <div className={`c-accordion-item ${openFaq === idx ? 'active' : ''}`} key={idx}>
                                        <button className="c-accordion-header" onClick={() => toggleFaq(idx)}>
                                            {faq.q}
                                            <i className={`fas fa-chevron-${openFaq === idx ? 'up' : 'down'}`}></i>
                                        </button>
                                        <div className="c-accordion-body" style={{ maxHeight: openFaq === idx ? '200px' : '0' }}>
                                            <div className="c-accordion-content">{faq.a}</div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* APPLY SECTION */}
            <section className="careers-apply">
                <div className="container">
                    <div className="c-grid-2-apply">
                        <div className="c-form-container">
                            <h2 className="c-form-title">Apply Now <i className="fas fa-leaf text-green"></i></h2>
                            <form className="c-apply-form">
                                <div className="c-form-row">
                                    <div className="c-form-group">
                                        <label>First Name <span>*</span></label>
                                        <input type="text" placeholder="First Name" required />
                                    </div>
                                    <div className="c-form-group">
                                        <label>Last Name <span>*</span></label>
                                        <input type="text" placeholder="Last Name" required />
                                    </div>
                                </div>
                                <div className="c-form-row">
                                    <div className="c-form-group">
                                        <label>Mobile Number <span>*</span></label>
                                        <input type="tel" placeholder="Enter Mobile Number" required />
                                    </div>
                                    <div className="c-form-group">
                                        <label>Email <span>*</span></label>
                                        <input type="email" placeholder="Enter Email Address" required />
                                    </div>
                                </div>
                                <div className="c-form-row">
                                    <div className="c-form-group">
                                        <label>Upload Resume <span>*</span></label>
                                        <div className="c-file-upload">
                                            <i className="fas fa-cloud-upload-alt"></i>
                                            <span>Click or drag a file to this area to upload.</span>
                                            <input type="file" required />
                                        </div>
                                    </div>
                                    <div className="c-form-group">
                                        <label>Message <span>*</span></label>
                                        <textarea placeholder="Write your message here..." rows="3" required></textarea>
                                    </div>
                                </div>
                                <div className="mt-3" style={{ marginTop: '20px' }}>
                                    <button type="submit" className="c-btn-dark px-5">Submit</button>
                                </div>
                            </form>
                        </div>
                        
                        <div className="c-hr-contact">
                            <h3>HR Contact</h3>
                            <ul className="c-contact-list">
                                <li><i className="fas fa-phone-alt"></i> +91 77589 17078</li>
                                <li><i className="fas fa-envelope"></i> careers@plastroots.com</li>
                                <li><i className="far fa-clock"></i> Mon-Sat: 10:30 am - 6:30 pm<br/>Sunday off!</li>
                            </ul>
                            <p style={{ marginTop: '20px' }}>We'd love to hear from you. Reach out to us for any career related queries.</p>
                            <i className="fas fa-leaf c-contact-bg-icon"></i>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Careers;
