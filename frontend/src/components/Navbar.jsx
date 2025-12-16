import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="fixed top-0 left-0 w-full z-50 flex items-center px-6 py-6 bg-black/20 backdrop-blur-md border-b border-white/10">
      {/* Left */}
      <h1 className="font-bold text-xl text-white">
        Fraudly
      </h1>

      {/* Center */}
      <div className="hidden md:flex flex-1 justify-center gap-8 font-bold text-white">
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/feat">Features</Link>
        <Link to="/services">Services</Link>
        <Link to="/contact">Contact</Link>
      </div>

      {/* Right */}
      <div className="hidden md:flex justify-end">
        <button className="px-6 py-2.5 text-black bg-white hover:bg-slate-200 active:scale-95 transition-all rounded-full text-lg font-bold">
          Login
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
