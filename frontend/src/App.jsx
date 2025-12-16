import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Navbar from "./components/Navbar";

function App() {
  const [darkMode, setDarkMode] = useState(true);

  return (
    <div
      className={`min-h-screen transition-all duration-500 ${
        darkMode
          ? "bg-[linear-gradient(#2C0F4B,#704E95,#2C0F4B)] text-white"
          : "bg-[linear-gradient(#C792FF,#FDFBFF,#C792FF)] text-black"
      }`}
    >
      {/* Navbar with darkMode toggle */}
      <Navbar darkMode={darkMode} setDarkMode={setDarkMode} />

      {/* Pages */}
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;
