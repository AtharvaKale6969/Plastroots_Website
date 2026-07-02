import React, { useEffect, useRef, useState } from 'react';
import Hero from '../components/Hero';
import Stats from '../components/Stats';
import Process from '../components/Process';
import SustainabilityImpact from '../components/SustainabilityImpact';
import Testimonials from '../components/Testimonials';
import StrategicPartners from '../components/StrategicPartners';

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

const AnimatedSection = ({ children }) => {
  const [ref, isIntersecting] = useIntersectionObserver({ threshold: 0.1 });
  return (
    <div 
      ref={ref} 
      className={isIntersecting ? 'animate-fade-up' : 'opacity-0'}
      style={{ transition: 'opacity 0.6s ease-out, transform 0.6s ease-out' }}
    >
      {children}
    </div>
  );
};

const Home = () => {
  return (
    <>
      <AnimatedSection>
        <Hero />
      </AnimatedSection>
      <AnimatedSection>
        <SustainabilityImpact />
      </AnimatedSection>
      <AnimatedSection>
        <Stats />
      </AnimatedSection>
      <AnimatedSection>
        <Process />
      </AnimatedSection>
      <AnimatedSection>
        <Testimonials />
      </AnimatedSection>
      <AnimatedSection>
        <StrategicPartners />
      </AnimatedSection>
    </>
  );
};

export default Home;
