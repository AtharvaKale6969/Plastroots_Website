import React, { useEffect, useRef, useState } from 'react';

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
