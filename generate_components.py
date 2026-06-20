import os

components_dir = "src/components"
os.makedirs(components_dir, exist_ok=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

header_jsx = """import React, { useState, useEffect } from 'react';

const Header = () => {
    const [isSticky, setIsSticky] = useState(false);

    useEffect(() => {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                setIsSticky(true);
            } else {
                setIsSticky(false);
            }
        };
        window.addEventListener('scroll', handleScroll);
        return () => window.removeEventListener('scroll', handleScroll);
    }, []);

    return (
        <>
            <div className="top-bar">
                <div className="container top-bar-inner">
                    <div className="top-logo-area">
                        <img src="/Images/PWMSPL_Linear_to_Circular.png" alt="Plastroots Logo" className="main-logo" />
                    </div>
                    
                    <div className="top-contact">
                        <span>Make a call: +91 7620094031, +91 7385837917</span>
                    </div>
                    
                    <div className="top-social">
                        <a href="#"><i className="fab fa-facebook-f"></i></a>
                        <a href="#"><i className="fab fa-instagram"></i></a>
                        <a href="#"><i className="fab fa-linkedin-in"></i></a>
                        <a href="#"><i className="fa-brands fa-x-twitter"></i></a>
                    </div>
                    <div className="tree-logo-small">
                        <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="Tree Logo" className="tree-logo-img" />
                    </div>
                </div>
            </div>

            <header className={`navbar ${isSticky ? 'sticky' : ''}`} id="navbar">
                <div className="container nav-container">
                    <nav className="nav-links">
                        <a href="#" className="nav-link active">Home</a>
                        <a href="#about" className="nav-link">About Us</a>
                        <div className="dropdown">
                            <a href="#services" className="nav-link">Services <i className="fas fa-chevron-down text-xs"></i></a>
                        </div>
                        <div className="dropdown">
                            <a href="#products" className="nav-link">Products <i className="fas fa-chevron-down text-xs"></i></a>
                        </div>
                        <a href="#career" className="nav-link">Career</a>
                        <div className="dropdown">
                            <a href="#blog" className="nav-link">Blog <i className="fas fa-chevron-down text-xs"></i></a>
                        </div>
                        <a href="#contact" className="nav-link">Contact</a>
                    </nav>
                    <div className="nav-cta">
                        <a href="#contact" className="btn btn-dark">GET IN TOUCH</a>
                    </div>
                    <div className="mobile-menu-btn">
                        <i className="fas fa-bars"></i>
                    </div>
                </div>
            </header>
        </>
    );
};

export default Header;
"""
write_file(f"{components_dir}/Header.jsx", header_jsx)

hero_jsx = """import React from 'react';

const Hero = () => {
    return (
        <section className="hero">
            <img src="/Images/leaf_watermark.png" alt="" className="watermark-leaf-hero" />
            <div className="hero-overlay"></div>
            <div className="container hero-content fade-up visible">
                <h1 className="hero-title">About Us</h1>
                <p className="hero-subtitle">Re-rooting waste from linear to circular</p>
                <p className="hero-desc">Our mission is to reduce carbon footprints, minimize landfill usage, and drive India towards a sustainable circular economy.</p>
            </div>
            <div className="hero-tree-bg"><i className="fas fa-tree"></i></div>
        </section>
    );
};

export default Hero;
"""
write_file(f"{components_dir}/Hero.jsx", hero_jsx)

about_jsx = """import React from 'react';

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
                        
                        <div className="step-item step-1">
                            <div className="step-icon"><i className="fas fa-truck"></i></div>
                            <span>COLLECTION</span>
                        </div>
                        <div className="step-item step-2">
                            <div className="step-icon"><i className="fas fa-trash-alt"></i></div>
                            <span>SEGREGATION</span>
                        </div>
                        <div className="step-item step-3">
                            <div className="step-icon"><i className="fas fa-industry"></i></div>
                            <span>PROCESSING</span>
                        </div>
                        <div className="step-item step-4">
                            <div className="step-icon"><i className="fas fa-recycle"></i></div>
                            <span>RECYCLING</span>
                        </div>
                        <div className="step-item step-5">
                            <div className="step-icon"><i className="fas fa-leaf"></i></div>
                            <span>REINTRODUCE</span>
                        </div>
                        
                        <div className="circle-arrows"></div>
                    </div>
                </div>

                <div className="about-content slide-in-right visible">
                    <h2 className="section-heading">ABOUT <span style={{ color: 'var(--primary-green)' }}>PLASTROOTS</span></h2>
                    <h3 className="section-subheading">Re-rooting waste from linear to circular represents our established expertise :</h3>
                    
                    <p>Plastroots is a social enterprise dedicated to the waste management sector, with a mission to reduce carbon footprints and diminish landfill usage in India. Established in 2019 by Social Entrepreneur Mr. Kapil Jangale. Plastroots Waste Management & Solutions Private Limited is committed to implementing an effective in waste management system in remote areas to promote a circular economy. Our endeavors include conducting awareness campaigns, providing training programs, and organizing workshops to educate the public on efficient waste management practices.</p>
                    
                    <p>Plastroots is dedicated to instituting professional waste aggregation and segregation practices in remote regions, focusing on the principles of Reduce, Reuse, and Recycle. The organization's primary objective is to address the lack of structured waste management resources in rural areas outside major cities, where an estimated 75% of waste remains unsorted, contributing to environmental pollution. By introducing systematic waste management systems, we strive to combat this issue and advocate for a cleaner, more sustainable environment.</p>
                </div>
            </div>
        </section>
    );
};

export default About;
"""
write_file(f"{components_dir}/About.jsx", about_jsx)

stats_jsx = """import React, { useEffect, useRef, useState } from 'react';

const useIntersectionObserver = (options) => {
    const [isIntersecting, setIsIntersecting] = useState(false);
    const ref = useRef(null);

    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            setIsIntersecting(entry.isIntersecting);
        }, options);

        if (ref.current) {
            observer.observe(ref.current);
        }

        return () => {
            if (ref.current) {
                observer.unobserve(ref.current);
            }
        };
    }, [options]);

    return [ref, isIntersecting];
};

const AnimatedNumber = ({ target }) => {
    const [count, setCount] = useState(0);
    const [ref, isIntersecting] = useIntersectionObserver({ threshold: 0.1 });
    const [hasAnimated, setHasAnimated] = useState(false);

    useEffect(() => {
        if (isIntersecting && !hasAnimated) {
            setHasAnimated(true);
            let startTimestamp = null;
            const duration = 2000;
            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                setCount(Math.floor(progress * target));
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                }
            };
            window.requestAnimationFrame(step);
        }
    }, [isIntersecting, target, hasAnimated]);

    return <div className="stat-number" ref={ref}>{count}</div>;
};

const Stats = () => {
    return (
        <section className="stats-section">
            <div className="container stats-grid">
                <div className="stat-card fade-up visible" style={{ transitionDelay: '0.1s' }}>
                    <div className="stat-icon"><i className="fas fa-sync-alt"></i></div>
                    <div className="stat-info">
                        <AnimatedNumber target={2500} /><span className="stat-plus">+</span>
                        <div className="stat-label">Metric Tons<br/>Waste Processed</div>
                    </div>
                </div>
                <div className="stat-card fade-up visible" style={{ transitionDelay: '0.2s' }}>
                    <div className="stat-icon"><i className="fas fa-users"></i></div>
                    <div className="stat-info">
                        <AnimatedNumber target={50} /><span className="stat-plus">+</span>
                        <div className="stat-label">Communities<br/>Served</div>
                    </div>
                </div>
                <div className="stat-card fade-up visible" style={{ transitionDelay: '0.3s' }}>
                    <div className="stat-icon"><i className="fas fa-recycle"></i></div>
                    <div className="stat-info">
                        <AnimatedNumber target={75} /><span className="stat-plus">%</span>
                        <div className="stat-label">Waste Recovery<br/>Rate</div>
                    </div>
                </div>
                <div className="stat-card fade-up visible" style={{ transitionDelay: '0.4s' }}>
                    <div className="stat-icon"><i className="fas fa-bullhorn"></i></div>
                    <div className="stat-info">
                        <AnimatedNumber target={100} /><span className="stat-plus">+</span>
                        <div className="stat-label">Awareness<br/>Programs</div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Stats;
"""
write_file(f"{components_dir}/Stats.jsx", stats_jsx)

process_jsx = """import React from 'react';

const Process = () => {
    return (
        <section className="process-section">
            <div className="container">
                <div className="process-wrapper fade-in visible">
                    <div className="process-title">
                        <h3>OUR APPROACH</h3>
                    </div>
                    
                    <div className="process-flow">
                        <div className="process-step">
                            <div className="p-icon"><i className="fas fa-truck"></i></div>
                            <div className="p-label">COLLECT</div>
                        </div>
                        <div className="p-arrow"><i className="fas fa-long-arrow-alt-right"></i></div>
                        
                        <div className="process-step">
                            <div className="p-icon"><i className="fas fa-trash-alt"></i></div>
                            <div className="p-label">SEGREGATE</div>
                        </div>
                        <div className="p-arrow"><i className="fas fa-long-arrow-alt-right"></i></div>
                        
                        <div className="process-step">
                            <div className="p-icon"><i className="fas fa-cogs"></i></div>
                            <div className="p-label">RECOVER</div>
                        </div>
                        <div className="p-arrow"><i className="fas fa-long-arrow-alt-right"></i></div>
                        
                        <div className="process-step">
                            <div className="p-icon"><i className="fas fa-recycle"></i></div>
                            <div className="p-label">RECYCLE</div>
                        </div>
                        <div className="p-arrow"><i className="fas fa-long-arrow-alt-right"></i></div>
                        
                        <div className="process-step">
                            <div className="p-icon"><i className="fas fa-leaf"></i></div>
                            <div className="p-label">REINTRODUCE</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Process;
"""
write_file(f"{components_dir}/Process.jsx", process_jsx)

footer_jsx = """import React from 'react';

const Footer = () => {
    return (
        <footer className="footer">
            <img src="/Images/leaf_watermark.png" alt="" className="watermark-leaf-footer-left" />
            <img src="/Images/leaf_watermark.png" alt="" className="watermark-leaf-footer-right" />
            <div className="footer-bg-tree"><i className="fas fa-leaf"></i></div>
            
            <div className="container footer-grid">
                <div className="footer-col">
                    <div className="footer-logo">
                        <span style={{ fontFamily: "'Poppins', sans-serif", fontWeight: 700, fontSize: '1.5rem', letterSpacing: '1px' }}>PLASTROOTS</span>
                    </div>
                    <p className="footer-desc">Re-rooting waste from linear to circular for a cleaner, greener and sustainable India.</p>
                    <div className="footer-social">
                        <a href="#"><i className="fab fa-facebook-f"></i></a>
                        <a href="#"><i className="fab fa-instagram"></i></a>
                        <a href="#"><i className="fab fa-linkedin-in"></i></a>
                        <a href="#"><i className="fa-brands fa-x-twitter"></i></a>
                    </div>
                </div>
                
                <div className="footer-col">
                    <h4>QUICK LINKS</h4>
                    <ul className="footer-links two-cols">
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Career</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Services</a></li>
                        <li><a href="#">Contact</a></li>
                        <li><a href="#">Products</a></li>
                    </ul>
                </div>
                
                <div className="footer-col">
                    <h4>OUR SERVICES</h4>
                    <ul className="footer-links">
                        <li><a href="#">Waste Collection</a></li>
                        <li><a href="#">Waste Segregation</a></li>
                        <li><a href="#">Waste Recycling</a></li>
                        <li><a href="#">Awareness & Training Programs</a></li>
                    </ul>
                </div>
                
                <div className="footer-col">
                    <h4>CONTACT US</h4>
                    <ul className="footer-contact">
                        <li><i className="fas fa-phone-alt"></i> +91 7620094031, +91 7385837917</li>
                        <li><i className="fas fa-envelope"></i> <a href="mailto:info@plastroots.com">info@plastroots.com</a></li>
                        <li><i className="fas fa-map-marker-alt"></i> Pune, Maharashtra, India</li>
                    </ul>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
"""
write_file(f"{components_dir}/Footer.jsx", footer_jsx)

app_jsx = """import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Stats from './components/Stats';
import Process from './components/Process';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Hero />
        <About />
        <Stats />
        <Process />
      </main>
      <Footer />
    </div>
  );
}

export default App;
"""
write_file("src/App.jsx", app_jsx)
