import React, { useState, useEffect } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import * as Icons from 'lucide-react';
import { psData } from '../data/ProductsServicesData';

const ProductsServices = () => {
    const [currentLevel, setCurrentLevel] = useState(1);
    const [activeCategory, setActiveCategory] = useState(null);
    const [activeService, setActiveService] = useState(null);
    const [activeTab, setActiveTab] = useState(0);
    const [activeFaq, setActiveFaq] = useState(null);

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
        setActiveFaq(null);
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
            <div className="ps-hero-section ps-hub-hero" style={{ backgroundImage: 'url(/Images/Product&Services_hero.png)' }}>
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

                <div className="ps-overview-section">
                    {/* 1. Top Section */}
                    {serviceData.overviewDetails && (
                        <div className="ps-overview-top">
                            <div className="ps-overview-image">
                                <img src={serviceData.overviewDetails.imagePath} alt={serviceData.overviewDetails.title} />
                            </div>
                            <div className="ps-overview-text">
                                <h3>{serviceData.overviewDetails.title}</h3>
                                {serviceData.overviewDetails.paragraphs.map((p, idx) => (
                                    <p key={idx}>{p}</p>
                                ))}
                            </div>
                        </div>
                    )}

                    {/* Execution Note if present */}
                    {serviceData.executionNote && (
                        <div className={`ps-execution-note ${serviceData.badgeType || 'green'}`}>
                            {serviceData.badgeType === 'green' ? <Icons.CheckCircle size={20} /> : <Icons.RefreshCw size={20} />}
                            {serviceData.executionNote}
                        </div>
                    )}

                    {/* 2. Gallery Section */}
                    {serviceData.gallery && serviceData.gallery.length > 0 && (
                        <div className="ps-gallery">
                            {serviceData.gallery.map((item, idx) => (
                                <div key={idx} className="ps-gallery-item">
                                    <img src={item.img} alt={item.name} />
                                    <span>{item.name}</span>
                                </div>
                            ))}
                        </div>
                    )}

                    {/* 3. Advanced Dashboard Section */}
                    {serviceData.statsSection && (
                        <div className="ps-dashboard-section">
                            <div className="ps-dashboard-left">
                                <div className="ps-dashboard-eyebrow">
                                    <Icons.Leaf size={16} />
                                    <span>{serviceData.statsSection.eyebrow}</span>
                                </div>
                                <h2>{serviceData.statsSection.title}</h2>
                                <p>{serviceData.statsSection.description}</p>
                                
                                <div className="ps-dashboard-ministats">
                                    {serviceData.statsSection.miniStats.map((stat, idx) => (
                                        <div key={idx} className="ps-ministat-card">
                                            <span className="ps-ministat-label">{stat.label}</span>
                                            <div className="ps-ministat-value-wrapper">
                                                <span className="ps-ministat-value" style={{ color: stat.color || '#1a4a6e' }}>
                                                    {stat.value}
                                                </span>
                                                {stat.suffix && <span className="ps-ministat-suffix">{stat.suffix}</span>}
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                            
                            <div className="ps-dashboard-right">
                                <div className="ps-dashboard-circular-card">
                                    <div className="ps-circular-progress">
                                        <svg viewBox="0 0 100 100">
                                            <circle cx="50" cy="50" r="40" className="ps-circle-bg" />
                                            <circle 
                                                cx="50" 
                                                cy="50" 
                                                r="40" 
                                                className="ps-circle-fill" 
                                                style={{ strokeDashoffset: `calc(251.2 - (251.2 * ${serviceData.statsSection.circularProgress.value}) / 100)` }}
                                            />
                                        </svg>
                                        <div className="ps-circular-content">
                                            <span className="ps-circular-value">{serviceData.statsSection.circularProgress.value}%</span>
                                            <span className="ps-circular-label">{serviceData.statsSection.circularProgress.label}</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div className="ps-dashboard-barchart-card">
                                    <span className="ps-barchart-title">{serviceData.statsSection.barChart.title}</span>
                                    <div className="ps-barchart-container">
                                        {serviceData.statsSection.barChart.bars.map((bar, idx) => (
                                            <div key={idx} className="ps-barchart-column">
                                                <div className="ps-barchart-bar-wrapper">
                                                    <span className="ps-barchart-tooltip">{bar.height}</span>
                                                    <div className="ps-barchart-bar" style={{ '--target-height': bar.height, backgroundColor: bar.color }}></div>
                                                </div>
                                                <span className="ps-barchart-label">{bar.label}</span>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* 4. Features Grid */}
                    {serviceData.features && serviceData.features.length > 0 && (
                        <div className="ps-features-grid">
                            {serviceData.features.map((feature, idx) => {
                                const FeatureIcon = Icons[feature.icon] || Icons.CheckCircle;
                                return (
                                    <div key={idx} className="ps-feature-item">
                                        <div className="ps-feature-icon">
                                            <FeatureIcon size={32} />
                                        </div>
                                        <div className="ps-feature-text">
                                            <h4>{feature.title}</h4>
                                            <p>{feature.desc}</p>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    )}
                </div>

                {/* Why Choose Us Section */}
                {serviceData.whyChooseUs && (
                    <div className="ps-why-choose-us">
                        <div className="ps-why-header">
                            <span className="ps-why-eyebrow">Why Us</span>
                            <h3>{serviceData.whyChooseUs.title}</h3>
                            <p>{serviceData.whyChooseUs.subtitle}</p>
                        </div>
                        <div className="ps-why-content-wrapper">
                            <div className="ps-why-grid-column">
                                {serviceData.whyChooseUs.points.map((point, idx) => {
                                    const PointIcon = Icons[point.icon] || Icons.CheckCircle;
                                    return (
                                        <div key={idx} className="ps-why-card fade-up" style={{ animationDelay: `${idx * 0.1}s` }}>
                                            <div className="ps-why-card-icon">
                                                <PointIcon size={32} />
                                            </div>
                                            <div className="ps-why-card-text">
                                                <h4>{point.title}</h4>
                                                <p>{point.desc}</p>
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                            <div className="ps-why-image-side fade-up" style={{ animationDelay: '0.4s' }}>
                                <img src="/Images/Why_Choose_us.png" alt="Why Choose Us" />
                            </div>
                        </div>
                    </div>
                )}

                {/* FAQ Section */}
                {serviceData.faqs && (
                    <div className="ps-faq-section">
                        <h3>Frequently Asked Questions</h3>
                        <div className="ps-faq-list">
                            {serviceData.faqs.map((faq, idx) => (
                                <div 
                                    key={idx} 
                                    className={`ps-faq-item ${activeFaq === idx ? 'active' : ''}`}
                                    onClick={() => setActiveFaq(activeFaq === idx ? null : idx)}
                                >
                                    <div className="ps-faq-question">
                                        <h4>{faq.question}</h4>
                                        <div className="ps-faq-icon">
                                            {activeFaq === idx ? <Icons.Minus size={18} /> : <Icons.Plus size={18} />}
                                        </div>
                                    </div>
                                    <div className="ps-faq-answer">
                                        <p>{faq.answer}</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}

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
