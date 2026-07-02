import React, { useEffect, useRef, useState } from 'react';
import { Leaf, Users, Recycle, Megaphone } from 'lucide-react';
import '../premium-sections.css';

const useIntersectionObserver = (options) => {
    const [isIntersecting, setIsIntersecting] = useState(false);
    const ref = useRef(null);
    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) setIsIntersecting(true);
        }, options);
        if (ref.current) observer.observe(ref.current);
        return () => { if (ref.current) observer.unobserve(ref.current); };
    }, [options]);
    return [ref, isIntersecting];
};

const AnimatedNumber = ({ target }) => {
    const [count, setCount] = useState(0);
    const [ref, isIntersecting] = useIntersectionObserver({ threshold: 0.1 });
    useEffect(() => {
        if (isIntersecting) {
            let startTimestamp = null;
            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / 2000, 1);
                setCount(Math.floor(progress * target));
                if (progress < 1) window.requestAnimationFrame(step);
            };
            window.requestAnimationFrame(step);
        }
    }, [isIntersecting, target]);
    return <span ref={ref}>{count}</span>;
};

const statsData = [
  { icon: Leaf, count: 2500, suffix: "+", label: "Metric Tons", subLabel: "Waste Processed", delay: '0.1s' },
  { icon: Users, count: 50, suffix: "+", label: "Communities", subLabel: "Served", delay: '0.2s' },
  { icon: Recycle, count: 75, suffix: "%", label: "Waste Recovery", subLabel: "Rate", delay: '0.3s' },
  { icon: Megaphone, count: 100, suffix: "+", label: "Awareness", subLabel: "Programs", delay: '0.4s' }
];

const Stats = () => {
  const [ref, isIntersecting] = useIntersectionObserver({ threshold: 0.1 });

  return (
    <section className="premium-stats-section" ref={ref}>
      <div className="premium-stats-container">
        <div 
          className={`premium-stats-header ${isIntersecting ? 'animate-fade-up' : 'opacity-0'}`}
        >
          <span className="premium-badge" style={{ background: 'rgba(34, 197, 94, 0.15)', color: '#34d399' }}>Our Impact</span>
          <h2>Driving Change at Scale</h2>
        </div>
        <div className="premium-stats-grid">
          {statsData.map((stat, index) => {
            const Icon = stat.icon;
            return (
            <div 
              key={index}
              className={`premium-stat-card ${isIntersecting ? 'animate-fade-up' : 'opacity-0'}`}
              style={{ animationDelay: stat.delay, opacity: isIntersecting ? 1 : 0 }}
            >
              <div className="premium-stat-icon-wrapper">
                <Icon className="premium-stat-icon" strokeWidth={1.5} />
              </div>
              <div className="premium-stat-content">
                <div className="premium-stat-number">
                  <AnimatedNumber target={stat.count} />
                  <span className="premium-stat-suffix">{stat.suffix}</span>
                </div>
                <div className="premium-stat-text">
                  <span className="premium-stat-label">{stat.label}</span>
                  <span className="premium-stat-sublabel">{stat.subLabel}</span>
                </div>
              </div>
            </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Stats;
