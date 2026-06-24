import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import * as Icons from 'lucide-react';
import { psData } from '../data/ProductsServicesData';

const ProductsServices = () => {
    const [currentLevel, setCurrentLevel] = useState(1);
    const [activeCategory, setActiveCategory] = useState(null);
    const [activeService, setActiveService] = useState(null);
    const [activeTab, setActiveTab] = useState(0);

    const location = useLocation();
    const navigate = useNavigate();

    // Parse URL parameters for direct category access
    useEffect(() => {
        const params = new URLSearchParams(location.search);
        const categoryParam = params.get('category');
        
        if (categoryParam && psData[categoryParam]) {
            setActiveCategory(categoryParam);
            setCurrentLevel(2);
            setActiveTab(0);
            setActiveService(null);
        } else if (!activeCategory) {
            // Only reset to level 1 if we don't already have an active category
            setCurrentLevel(1);
        }
    }, [location.search]);

    // Scroll to top on level change
    useEffect(() => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }, [currentLevel]);

    const handleCategoryClick = (categoryId) => {
        navigate(`/products-services?category=${categoryId}`);
        setActiveCategory(categoryId);
        setActiveTab(0);
        setCurrentLevel(2);
    };

    const handleServiceClick = (serviceId) => {
        setActiveService(serviceId);
        setCurrentLevel(4);
    };

    const handleBack = () => {
        if (currentLevel === 4) {
            setActiveService(null);
            setCurrentLevel(2);
        } else if (currentLevel === 2) {
            navigate('/products-services', { replace: true });
            setActiveCategory(null);
            setCurrentLevel(1);
        }
    };

    const goHome = () => {
        navigate('/products-services', { replace: true });
        setCurrentLevel(1);
        setActiveCategory(null);
        setActiveService(null);
    };

    // Helper to render dynamic Lucide icons
    const renderIcon = (iconName) => {
        const IconComponent = Icons[iconName] || Icons.Circle;
        return <IconComponent size={24} strokeWidth={2} />;
    };

    // ----------------------------------------------------
    // BREADCRUMB
    // ----------------------------------------------------
    const renderBreadcrumb = () => {
        if (currentLevel === 1) return null;

        const categoryData = psData[activeCategory];
        const serviceData = currentLevel === 4 && activeService 
            ? (categoryData.services || []).find(s => s.id === activeService) || 
              (categoryData.sections || []).flatMap(sec => sec.services).find(s => s.id === activeService)
            : null;

        return (
            <div className="ps-breadcrumb fade-in">
                <span onClick={goHome}>Products & Services</span>
                <span className="ps-bc-separator">›</span>
                {currentLevel === 2 ? (
                    <span className="ps-bc-active">{categoryData.title}</span>
                ) : (
                    <>
                        <span onClick={() => handleBack()}>{categoryData.title}</span>
                        <span className="ps-bc-separator">›</span>
                        <span className="ps-bc-active">{serviceData?.title}</span>
                    </>
                )}
            </div>
        );
    };

    // ----------------------------------------------------
    // LEVEL 1: HUB
    // ----------------------------------------------------
    const renderLevel1 = () => (
        <div className="ps-view-container" key="level1">
            <div className="ps-hero-section ps-hub-hero" style={{ backgroundImage: 'url(/Images/ps_hub_hero.png)' }}>
                <div className="ps-hero-overlay"></div>
                <div className="ps-hero-content">
                    <h1>Products & Services</h1>
                    <p>From regulatory compliance to recycled materials — everything Plastroots offers.</p>
                </div>
            </div>

            <div className="ps-grid-3">
                {Object.values(psData).map(category => (
                    <div className={`ps-card theme-${category.theme}`} key={category.id}>
                        {category.image && (
                            <div 
                                className="ps-card-image" 
                                style={{ backgroundImage: `url(${category.image})` }}
                            >
                                <div className="ps-card-icon overlay">
                                    {renderIcon(category.icon)}
                                </div>
                            </div>
                        )}
                        {!category.image && (
                            <div className="ps-card-icon">
                                {renderIcon(category.icon)}
                            </div>
                        )}
                        <h3 style={{ marginTop: category.image ? '10px' : '0' }}>{category.title}</h3>
                        <p>{category.intro.substring(0, 150)}...</p>
                        
                        <div className="ps-badges">
                            {category.id === 'corporate-compliance' && (
                                <>
                                    <span className="ps-badge teal">EPR</span>
                                    <span className="ps-badge teal">Carbon Markets</span>
                                    <span className="ps-badge teal">ESG</span>
                                </>
                            )}
                            {category.id === 'government-services' && (
                                <>
                                    <span className="ps-badge neutral">Waste Management</span>
                                    <span className="ps-badge neutral">Environmental Projects</span>
                                    <span className="ps-badge neutral">Infrastructure</span>
                                </>
                            )}
                            {category.id === 'products' && (
                                <>
                                    <span className="ps-badge neutral">PET Bales</span>
                                    <span className="ps-badge neutral">Plastic Granules</span>
                                    <span className="ps-badge neutral">Industrial Scrap</span>
                                </>
                            )}
                        </div>

                        <button className="ps-btn-explore" onClick={() => handleCategoryClick(category.id)}>
                            Explore <Icons.ArrowRight size={16} />
                        </button>
                    </div>
                ))}
            </div>

            <div className="ps-global-cta">
                <p>"At Plastroots, every service and product is designed with one objective in mind — transforming waste into value while creating measurable environmental impact."</p>
                <Link to="/contact" className="ps-btn-primary">
                    Get in Touch <Icons.ArrowRight size={18} />
                </Link>
            </div>
        </div>
    );

    // ----------------------------------------------------
    // LEVEL 2 & 3: CATEGORY LANDING
    // ----------------------------------------------------
    const renderLevel2 = () => {
        const categoryData = psData[activeCategory];
        const heroMap = {
            'corporate-compliance': '/Images/cc_hero.png',
            'government-services': '/Images/gs_hero.png',
            'products': '/Images/prod_hero.png'
        };

        return (
            <div className="ps-view-container" key="level2">
                <button className="ps-back-btn" onClick={handleBack}>
                    <Icons.ArrowLeft size={18} /> Back
                </button>

                <div className="ps-hero-section" style={{ backgroundImage: `url(${heroMap[categoryData.id]})` }}>
                    <div className="ps-hero-overlay"></div>
                    <div className="ps-hero-content">
                        <h1>{categoryData.title}</h1>
                        <p>{categoryData.intro}</p>
                    </div>
                </div>

                {/* Handle flat services list (Corporate Compliance, Products) */}
                {categoryData.services && (
                    <div className="ps-grid-3">
                        {categoryData.services.map(service => (
                            <div className="ps-card" key={service.id}>
                                <div className="ps-card-icon">{renderIcon(service.icon)}</div>
                                <h3>{service.title}</h3>
                                <span className="ps-card-tagline">{service.tagline}</span>
                                <p>{service.summary}</p>

                                {service.materialBadges && (
                                    <div className="ps-badges">
                                        {service.materialBadges.map((badge, idx) => (
                                            <span key={idx} className="ps-badge neutral">{badge}</span>
                                        ))}
                                    </div>
                                )}

                                <button className="ps-btn-explore" onClick={() => handleServiceClick(service.id)}>
                                    Explore <Icons.ArrowRight size={16} />
                                </button>
                            </div>
                        ))}
                    </div>
                )}

                {/* Handle sectioned services (Government Services) with Tabs */}
                {categoryData.sections && (
                    <>
                        <div className="ps-tabs">
                            {categoryData.sections.map((section, idx) => (
                                <button 
                                    key={section.id} 
                                    className={`ps-tab ${activeTab === idx ? 'active' : ''}`}
                                    onClick={() => setActiveTab(idx)}
                                >
                                    <span className={`ps-tab-indicator ${section.badgeType}`}></span>
                                    {section.title}
                                </button>
                            ))}
                        </div>

                        <div className={`ps-section-content theme-${categoryData.sections[activeTab].badgeType}`}>
                            <div className="ps-section-header">
                                <h2>{categoryData.sections[activeTab].title}</h2>
                                <span className={`ps-badge ${categoryData.sections[activeTab].badgeType}`}>
                                    {categoryData.sections[activeTab].badgeText}
                                </span>
                            </div>
                            <p className="ps-section-desc">{categoryData.sections[activeTab].description}</p>
                            
                            <div className="ps-grid-3">
                                {categoryData.sections[activeTab].services.map(service => (
                                    <div className="ps-card ps-themed-card" key={service.id}>
                                        <div className="ps-card-icon">{renderIcon(service.icon)}</div>
                                        <h3>{service.title}</h3>
                                        <span className="ps-card-tagline">{service.tagline}</span>
                                        <p>{service.summary}</p>

                                        <div className="ps-badges">
                                            <span className={`ps-badge ${service.badgeType}`}>{service.badge}</span>
                                        </div>

                                        <button className="ps-btn-explore" onClick={() => handleServiceClick(service.id)}>
                                            Explore <Icons.ArrowRight size={16} />
                                        </button>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </>
                )}
            </div>
        );
    };

    // ----------------------------------------------------
    // LEVEL 4: DETAIL PAGE
    // ----------------------------------------------------
    const renderLevel4 = () => {
        const categoryData = psData[activeCategory];
        let serviceData = null;
        let parentCategoryTitle = categoryData.title;

        if (categoryData.services) {
            serviceData = categoryData.services.find(s => s.id === activeService);
        } else if (categoryData.sections) {
            for (const section of categoryData.sections) {
                const found = section.services.find(s => s.id === activeService);
                if (found) {
                    serviceData = found;
                    break;
                }
            }
        }

        if (!serviceData) return null;

        return (
            <div className="ps-view-container" key="level4">
                <button className="ps-back-btn" onClick={handleBack}>
                    <Icons.ArrowLeft size={18} /> Back
                </button>

                <div className="ps-detail-header">
                    <div className="ps-badges" style={{ marginBottom: '10px' }}>
                        <span className="ps-badge neutral">{parentCategoryTitle}</span>
                        {serviceData.badge && (
                            <span className={`ps-badge ${serviceData.badgeType}`}>{serviceData.badge}</span>
                        )}
                    </div>
                    <h1>{serviceData.title}</h1>
                    <h2>{serviceData.detailTagline}</h2>
                </div>

                <div className="ps-grid-2" style={{ gridTemplateColumns: '2fr 1fr' }}>
                    <div className="ps-detail-content" style={{ margin: 0 }}>
                        <h3>Overview</h3>
                        <p>{serviceData.about}</p>
                        
                        {serviceData.executionNote && (
                            <div className={`ps-execution-note ${serviceData.badgeType || 'green'}`}>
                                {serviceData.badgeType === 'green' ? <Icons.CheckCircle size={20} /> : <Icons.RefreshCw size={20} />}
                                {serviceData.executionNote}
                            </div>
                        )}
                    </div>

                    <div className="ps-detail-content" style={{ margin: 0 }}>
                        <h3>{serviceData.includedTitle || serviceData.includedListTitle || "Services Included"}</h3>
                        
                        {serviceData.included && (
                            <ul className="ps-detail-list">
                                {serviceData.included.map((item, idx) => (
                                    <li key={idx}>
                                        <strong>{item.title}</strong>
                                        {item.desc}
                                    </li>
                                ))}
                            </ul>
                        )}

                        {serviceData.includedList && (
                            <ul className="ps-detail-list">
                                {serviceData.includedList.map((item, idx) => (
                                    <li key={idx}>{item}</li>
                                ))}
                            </ul>
                        )}

                        {serviceData.includedListTitle2 && (
                            <>
                                <h3>{serviceData.includedListTitle2}</h3>
                                <ul className="ps-detail-list">
                                    {serviceData.includedList2.map((item, idx) => (
                                        <li key={idx}>{item}</li>
                                    ))}
                                </ul>
                            </>
                        )}
                    </div>
                </div>

                {serviceData.closing && (
                    <div className="ps-closing-text">{serviceData.closing}</div>
                )}

                <div style={{ textAlign: 'center', marginTop: '40px' }}>
                    <Link to="/contact" className="ps-btn-primary">
                        {serviceData.buttonText} <Icons.ArrowRight size={18} />
                    </Link>
                </div>
            </div>
        );
    };

    return (
        <section className="ps-page-container">
            {currentLevel > 1 && activeCategory === 'corporate-compliance' && (
                <div className="ps-fixed-doodles bg-corporate-compliance"></div>
            )}
            {currentLevel > 1 && activeCategory === 'government-services' && (
                <div className="ps-fixed-doodles bg-government-services"></div>
            )}
            {currentLevel > 1 && activeCategory === 'products' && (
                <div className="ps-fixed-doodles bg-products"></div>
            )}
            
            <div className="container">
                {renderBreadcrumb()}
                {currentLevel === 1 && renderLevel1()}
                {currentLevel === 2 && renderLevel2()}
                {currentLevel === 4 && renderLevel4()}
            </div>
        </section>
    );
};

export default ProductsServices;
