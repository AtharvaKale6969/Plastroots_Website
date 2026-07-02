import React from 'react';
import { Link } from 'react-router-dom';
import { blogsData } from '../data/BlogData';
import '../products-services.css';

const Blog = () => {
  return (
    <div className="ps-page-container">
      <section className="blog-hero-section ps-hero-section ps-hub-hero" style={{ backgroundImage: "url('/Images/Afforestation.png')", margin: '0 5vw 50px 5vw' }}>
        <div className="ps-hero-overlay"></div>
        <div className="container ps-hero-content fade-up visible" style={{ textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <h1>Insights & Updates</h1>
          <p>
            The latest news, thoughts, and stories from the circular economy.
          </p>
        </div>
      </section>

      <section className="container" style={{ marginBottom: '80px', padding: '0 20px' }}>
        <div className="ps-grid-3">
          {blogsData.map((blog, index) => (
            <Link 
              to={`/blog/${blog.slug}`} 
              className="ps-card theme-products ps-themed-card" 
              style={{ textDecoration: 'none', display: 'flex', flexDirection: 'column', animationDelay: `${index * 0.1}s` }} 
              key={index}
            >
              <div className="ps-card-image" style={{ backgroundImage: `url('${blog.image}')` }}></div>
              <span style={{ fontSize: '0.85rem', color: '#888', textTransform: 'uppercase', letterSpacing: '1px' }}>{blog.date}</span>
              <h3 style={{ fontSize: '1.4rem', marginTop: '10px', lineHeight: '1.4' }}>{blog.title}</h3>
              <p style={{ marginTop: '10px', marginBottom: '20px' }}>{blog.excerpt}</p>
              
              <div style={{ marginTop: 'auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div className="ps-badges" style={{ margin: 0 }}>
                  <span className="ps-badge green">Blog</span>
                </div>
                <span className="ps-btn-explore">
                  Read Article <i className="fas fa-arrow-right"></i>
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Blog;
