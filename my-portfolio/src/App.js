import React from "react";
import "./App.css";

function App() {
  return (
    <div className="container">
      <header>
        <h1>John Martire</h1>
        <nav>
          <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </header>

      <section id="about">
        <h2>About Me</h2>
        <p>Hi, I'm John! An aspiring full-stack developer learning React and backend development.</p>
      </section>

      <section id="projects">
        <h2>Projects</h2>
        <div className="project">
          <h3>Project 1</h3>
          <p>Brief description of project.</p>
        </div>
        <div className="project">
          <h3>Project 2</h3>
          <p>Brief description of project.</p>
        </div>
      </section>

      <section id="contact">
        <h2>Contact Me</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <input type="text" placeholder="Your Name" required />
          <input type="email" placeholder="Your Email" required />
          <textarea placeholder="Your Message" required></textarea>
          <button type="submit">Send</button>
        </form>
      </section>

      <footer>
        <p>© 2025 John Martire. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;

