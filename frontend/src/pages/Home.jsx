import React from 'react'
import Navbar from '../components/Navbar';
import MainBanner from '../components/MainBanner';
import Footer from '../components/Footer';
import Feature from '../components/Feature';
import Services from '../components/Services';
import About from '../components/About';

const Home = () => {
  return (

    <div className=''>
      <Navbar />
      <MainBanner />
      <About />
      <Feature />
      <Services />
      <Footer />
      
    </div>

  )
}

export default Home




