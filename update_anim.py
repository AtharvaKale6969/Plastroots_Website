import re

# Update About.jsx
with open('src/components/About.jsx', 'r', encoding='utf-8') as f:
    about_jsx = f.read()

target = """<div className="step-item step-1">
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
                        
                        <div className="circle-arrows"></div>"""

replacement = """<div className="orbit-ring">
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
                        </div>"""

if target in about_jsx:
    about_jsx = about_jsx.replace(target, replacement)
    with open('src/components/About.jsx', 'w', encoding='utf-8') as f:
        f.write(about_jsx)

# Update index.css
with open('src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_orbit = """
/* Add Orbit Animations */
@keyframes orbit {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes counter-orbit {
    0% { transform: translate(-50%, -50%) rotate(0deg); }
    100% { transform: translate(-50%, -50%) rotate(-360deg); }
}

.orbit-ring {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    animation: orbit 40s linear infinite;
    z-index: 5;
}

.circle-infographic:hover .orbit-ring,
.circle-infographic:hover .step-item {
    animation-play-state: paused;
}
"""
if "/* Add Orbit Animations */" not in css:
    css = css.replace(".circle-infographic {", css_orbit + "\n.circle-infographic {")

css_step_item_old = """.step-item {
    position: absolute;
    text-align: center;
    width: 130px;
    font-family: var(--font-heading);
    font-size: 0.95rem;
    font-weight: 600;
}"""

css_step_item_new = """.step-item {
    position: absolute;
    text-align: center;
    width: 130px;
    font-family: var(--font-heading);
    font-size: 0.95rem;
    font-weight: 600;
    animation: counter-orbit 40s linear infinite;
    z-index: 10;
}

.step-content {
    transition: var(--transition-smooth);
}

.step-item:hover .step-content {
    transform: translateY(-5px) scale(1.05);
}"""
if css_step_item_old in css:
    css = css.replace(css_step_item_old, css_step_item_new)

css_hover_old = """.step-item:hover .step-icon {
    transform: translateY(-5px) scale(1.05);
    color: var(--accent-green);
    box-shadow: 0 8px 20px rgba(122, 158, 87, 0.2);
}"""

css_hover_new = """.step-item:hover .step-icon {
    color: var(--accent-green);
    box-shadow: 0 8px 20px rgba(122, 158, 87, 0.2);
}"""
if css_hover_old in css:
    css = css.replace(css_hover_old, css_hover_new)

with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)
