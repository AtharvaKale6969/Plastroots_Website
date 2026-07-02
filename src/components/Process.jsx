import React, { useEffect, useRef, useState } from 'react';
import { Truck, BoxSelect, Cog, Recycle, Sprout, ArrowRight } from 'lucide-react';
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

const processSteps = [
  { icon: Truck, label: "COLLECT", desc: "Efficient waste gathering" },
  { icon: BoxSelect, label: "SEGREGATE", desc: "Precise sorting" },
  { icon: Cog, label: "RECOVER", desc: "Extracting value" },
  { icon: Recycle, label: "RECYCLE", desc: "Sustainable processing" },
  { icon: Sprout, label: "REINTRODUCE", desc: "Circular economy" }
];

const Process = () => {
  const [ref, isIntersecting] = useIntersectionObserver({ threshold: 0.2 });

  return (
    <section className="premium-process-section" ref={ref}>
      <div className="premium-process-container">
        <div 
          className={`premium-process-header ${isIntersecting ? 'animate-fade-up' : 'opacity-0'}`}
        >
          <span className="premium-badge">Our Approach</span>
          <h2>The Lifecycle of Sustainability</h2>
        </div>

        <div className="premium-process-flow">
          {processSteps.map((step, index) => {
            const Icon = step.icon;
            const delay = `${index * 0.15 + 0.2}s`;
            const connectorDelay = `${index * 0.15 + 0.3}s`;
            
            return (
            <React.Fragment key={index}>
              <div 
                className={`premium-process-step ${isIntersecting ? 'animate-scale-in' : 'opacity-0'}`}
                style={{ animationDelay: delay }}
              >
                <div className="premium-step-icon-box">
                  <Icon className="premium-step-icon" strokeWidth={1.5} />
                  <div className="premium-step-number">0{index + 1}</div>
                </div>
                <h3 className="premium-step-label">{step.label}</h3>
                <p className="premium-step-desc">{step.desc}</p>
              </div>

              {index < processSteps.length - 1 && (
                <div 
                  className={`premium-step-connector ${isIntersecting ? 'animate-expand' : 'opacity-0'}`}
                  style={{ animationDelay: connectorDelay }}
                >
                  <ArrowRight className="premium-connector-arrow" />
                </div>
              )}
            </React.Fragment>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default Process;
