import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
    return (
        <footer className="footer" style={{ borderTop: '1px solid rgba(255,255,255,0.1)' }}>
            <div className="footer-bg-tree">
                <i className="fas fa-leaf"></i>
            </div>
            
            <div className="container footer-grid">
                <div className="footer-col">
                    <div className="footer-logo" style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                        <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="Plastroots Logo" style={{ height: '45px', filter: 'brightness(0) invert(1)' }} />
                        <span style={{ fontFamily: "var(--font-heading, 'Inter', sans-serif)", fontWeight: 700, fontSize: '1.75rem', letterSpacing: '1px', color: '#fff' }}>PLASTROOTS</span>
                    </div>
                    <p className="footer-desc" style={{ fontSize: '1rem', marginTop: '20px', paddingRight: '20px' }}>Re-rooting waste from linear to circular for a cleaner, greener and sustainable India.</p>
                    <div className="footer-social" style={{ marginTop: '24px' }}>
                        <a href="#"><i className="fab fa-facebook-f"></i></a>
                        <a href="#"><i className="fab fa-instagram"></i></a>
                        <a href="#"><i className="fab fa-linkedin-in"></i></a>
                        <a href="#"><i className="fa-brands fa-x-twitter"></i></a>
                    </div>
                </div>
                
                <div className="footer-col">
                    <h4>QUICK LINKS</h4>
                    <ul className="footer-links two-cols">
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/about">About Us</Link></li>
                        <li><Link to="/products-services">Services</Link></li>
                        <li><Link to="/products-services?category=products">Products</Link></li>
                        <li><Link to="/blog">Blog</Link></li>
                        <li><Link to="/careers">Career</Link></li>
                        <li><Link to="/contact">Contact</Link></li>
                    </ul>
                </div>
                
                <div className="footer-col">
                    <h4>OUR FOCUS</h4>
                    <ul className="footer-links">
                        <li><Link to="/products-services?category=corporate-compliance">Corporate Compliance & EPR</Link></li>
                        <li><Link to="/products-services?category=government-services">Government SWM Projects</Link></li>
                        <li><Link to="/products-services?category=products">Recycled Plastic Materials</Link></li>
                        <li><Link to="/products-services?category=government-services">Environmental Infrastructure</Link></li>
                    </ul>
                </div>
                
                <div className="footer-col">
                    <h4>CONTACT US</h4>
                    <ul className="footer-contact">
                        <li><i className="fas fa-phone-alt"></i> +91 7620094031<br/><span style={{marginLeft: '25px'}}>+91 7385837917</span></li>
                        <li><i className="fas fa-envelope"></i> <a href="mailto:info@plastroots.com">info@plastroots.com</a></li>
                        <li><i className="fas fa-map-marker-alt"></i> <span style={{lineHeight: 1.5}}>Plot no 12A, 1st Floor,<br/>Smruti Nagar Rd, Koradi,<br/>Bokara, Nagpur 441111</span></li>
                    </ul>
                </div>
            </div>

            <div className="footer-bottom" style={{ borderTop: '1px solid rgba(255,255,255,0.1)', marginTop: '50px', paddingTop: '25px', textAlign: 'center' }}>
                <div className="container" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px' }}>
                    <p style={{ margin: 0, opacity: 0.7, fontSize: '0.9rem' }}>&copy; {new Date().getFullYear()} Plastroots Waste Management Pvt Ltd. All rights reserved.</p>
                    <div className="footer-legal" style={{ display: 'flex', gap: '20px', opacity: 0.7, fontSize: '0.9rem' }}>
                        <Link to="#" style={{ color: '#fff', textDecoration: 'none' }}>Privacy Policy</Link>
                        <Link to="#" style={{ color: '#fff', textDecoration: 'none' }}>Terms of Service</Link>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
