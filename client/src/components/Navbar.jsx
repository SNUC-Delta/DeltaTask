import React from "react";
import "../assets/css/Navbar.css";

function Navbar() {
  return (
    <div className="main_nav__container">
      <nav className="main_nav">
        <div className="nav_logo">Delta Tasks</div>
        <button className="nav_cta__button">Sign Up</button>
      </nav>
    </div>
  );
}

export default Navbar;
