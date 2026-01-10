import React, { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { SunIcon, MoonIcon } from "@heroicons/react/24/solid";
import { AppContext } from "../context/AppContext";

const NavbarLogged = ({ darkMode, setDarkMode }) => {
    const navigate = useNavigate();
    const { setIsAuthenticated } = useContext(AppContext);

    const handleLogout = () => {
        setIsAuthenticated(false);
        navigate('/');
    };

    return (
        <nav
            className={`fixed top-0 left-0 w-full z-50 flex items-center px-6 py-3.5 border-b border-white/10
        ${darkMode ? "bg-[linear-gradient(#2C0F4B,#704E95,#2C0F4B)] text-white"
                    : "bg-[linear-gradient(#C792FF,#FDFBFF,#C792FF)] text-black"
                }`}
        >
            <h1 className="font-bold text-2xl">ClarifAI</h1>

            <div className="hidden md:flex flex-1 justify-center gap-8 font-bold text-lg">
                <Link to="/dashboard">Dashboard</Link>
                <Link to="/predict">Predict</Link>
                <Link to="/metrics">Metrics</Link>
                <Link to="/alert">Alert</Link>
                <Link to="/history">History</Link>
            </div>

            <div className="hidden md:flex items-center justify-end gap-3">
                <button
                    onClick={() => setDarkMode(!darkMode)}
                    className={`p-2 rounded-full hover:scale-105 cursor-pointer transition ${darkMode ? "bg-gray-700 text-white" : "bg-gray-200 text-black"
                        }`}
                >
                    {darkMode ? <SunIcon className="h-5 w-5" /> : <MoonIcon className="h-5 w-5" />}
                </button>

                <button>
                    <span class="material-symbols-outlined">
                        face
                    </span>
                </button>

                <button onClick={handleLogout}
                    className={`px-6 py-2.5 rounded-full font-bold text-lg shadow-lg transition-all duration-300 bg-white text-black hover:bg-slate-200`}
                >
                    Logout
                </button>
            </div>
        </nav>
    );
};

export default NavbarLogged;
