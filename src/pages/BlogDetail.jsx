import React, { useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { blogsData } from '../data/BlogData';
import '../products-services.css'; // Utilizing existing theme

const BlogDetail = () => {
  const { slug } = useParams();
  const navigate = useNavigate();
  
  // Find the blog that matches the slug
  const blog = blogsData.find(b => b.slug === slug);

  // Scroll to top when component mounts
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [slug]);

  if (!blog) {
    return (
      <div className="ps-page-container" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '60vh' }}>
        <div style={{ textAlign: 'center' }}>
          <h2>Article not found</h2>
          <button onClick={() => navigate('/blog')} className="ps-btn-primary" style={{ marginTop: '20px' }}>
            Back to Blogs
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="ps-page-container">
      {/* Immersive Hero Section */}
      <section 
        className="hero blog-hero-section ps-hero-section ps-hub-hero" 
        style={{ position: 'relative', margin: '0 5vw 50px 5vw', minHeight: '400px', overflow: 'hidden' }}
      >
        {/* Using an img tag instead of CSS background-image ensures it always loads on dynamic routes */}
        <img 
            src={blog.image} 
            alt={blog.title} 
            style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover', zIndex: 0 }} 
        />
        <div className="ps-hero-overlay" style={{ zIndex: 1 }}></div>
        <div className="container ps-hero-content fade-up visible" style={{ textAlign: 'left', maxWidth: '900px', margin: '0 auto', zIndex: 2, position: 'relative' }}>
          <button onClick={() => navigate('/blog')} className="ps-back-btn" style={{ color: '#fff', marginBottom: '30px' }}>
            <i className="fas fa-arrow-left"></i> Back to Blogs
          </button>
          <div className="ps-badges" style={{ marginBottom: '20px' }}>
             <span className="ps-badge green">Insights</span>
          </div>
          <h1 style={{ fontSize: '3rem', lineHeight: '1.2' }}>{blog.title}</h1>
          <p style={{ fontSize: '1rem', color: '#ccc', marginTop: '15px' }}>Published on: {blog.date}</p>
        </div>
      </section>

      {/* Main Content Area */}
      <section className="container" style={{ maxWidth: '800px', margin: '0 auto', marginBottom: '80px', padding: '0 20px' }}>
        <div className="ps-detail-content" style={{ fontSize: '1.15rem', color: '#444', lineHeight: '1.8' }}>
          {/* We render the HTML content directly */}
          <div dangerouslySetInnerHTML={{ __html: blog.content }} />
        </div>
      </section>
    </div>
  );
};

export default BlogDetail;
