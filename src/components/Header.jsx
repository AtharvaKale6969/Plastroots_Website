import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

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
                    
                    <div className="top-contact" style={{ marginRight: '40px' }}>
                        <span>Make a call: +91 7620094031, +91 7385837917</span>
                    </div>
                    <div className="tree-logo-small">
                        <img src="/Images/PWMSPL_LOGO-removebg-preview.png" alt="Tree Logo" className="tree-logo-img" />
                    </div>
                </div>
            </div>

            <header className={`navbar ${isSticky ? 'sticky' : ''}`} id="navbar">
                <div className="container nav-container">
                    <nav className="nav-links">
                        <Link to="/" className="nav-link active">Home</Link>
                        <Link to="/about" className="nav-link">About Us</Link>
                        <div className="dropdown">
                            <Link to="/products-services" className="nav-link">Products & Services <i className="fas fa-chevron-down text-xs"></i></Link>
                        </div>
                        <Link to="/careers" className="nav-link">Career</Link>
                        <div className="dropdown">
                            <Link to="/blog" className="nav-link">Blog <i className="fas fa-chevron-down text-xs"></i></Link>
                        </div>
                        <Link to="/contact" className="nav-link">Contact</Link>
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
