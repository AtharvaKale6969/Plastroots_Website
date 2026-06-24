import React from 'react';

const Footer = () => {
    return (
        <footer className="footer">
            
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
                        <li><i className="fas fa-map-marker-alt"></i> Plot no 12A, 1st Floor, Smruti Nagar Rd, Smruti Nagar, Koradi, Bokara, Nagpur Maharashtra 441111</li>
                    </ul>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
