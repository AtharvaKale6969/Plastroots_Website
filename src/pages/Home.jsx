import React from 'react';
import Hero from '../components/Hero';
import Stats from '../components/Stats';
import Process from '../components/Process';
import SustainabilityImpact from '../components/SustainabilityImpact';
import Testimonials from '../components/Testimonials';

const Home = () => {
  return (
    <>
      <Hero />
      <SustainabilityImpact />
      <Stats />
      <Process />
      <Testimonials />
    </>
  );
};

export default Home;
