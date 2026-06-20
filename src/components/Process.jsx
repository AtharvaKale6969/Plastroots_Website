import React from 'react';

const Process = () => {
    return (
        <section className="process-section">
            <div className="si-wide-container">
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
