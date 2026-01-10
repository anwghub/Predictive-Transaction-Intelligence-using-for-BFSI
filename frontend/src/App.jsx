import React, { useState, useContext } from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Navbar from "./components/Navbar";
import NavbarLogged from "./components/NavbarLogged";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import ForgotPasswordPage from "./pages/ForgotPassword";
import ResetPasswordPage from "./pages/ResetPassowrd"
import Dashboard from "./pages/Dashboard";
import Predict from "./pages/Predict";
import Metrics from "./pages/Metrics";
import Alert from "./pages/Alert";
import History from "./pages/History";
import { AppContext } from "./context/AppContext";

function App() {
  const [darkMode, setDarkMode] = useState(true);
  const { isAuthenticated } = useContext(AppContext);

  return (
    <div
      className={`min-h-screen transition-all duration-500 ${darkMode
        ? "bg-[linear-gradient(#2C0F4B,#704E95,#2C0F4B)] text-white"
        : "bg-[linear-gradient(#C792FF,#FDFBFF,#C792FF)] text-black"
        }`}
    >
      {/* Navbar with darkMode toggle */}
      {isAuthenticated ? (
        <NavbarLogged darkMode={darkMode} setDarkMode={setDarkMode} />
      ) : (
        <Navbar darkMode={darkMode} setDarkMode={setDarkMode} />
      )}

      {/* Pages */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/forgot" element={<ForgotPasswordPage />} />
        <Route path="/reset" element={<ResetPasswordPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/predict" element={<Predict />} />
        <Route path="/metrics" element={<Metrics />} />
        <Route path="/alert" element={<Alert />} />
        <Route path="/history" element={<History />} />

      </Routes>
    </div>
  );
}

export default App;
