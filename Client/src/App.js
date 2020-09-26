import React from 'react';
import './CSS/App.css';
import Navigation from './components/Navbar';
import Routes from './Routes/Routes';

function App() {
  return (
    <div>
      <div className={"header"}>
        <h1>Neural Goal</h1>
      </div>
      <div className={"navbar"}>
        <Navigation />
      </div>
      <div className={"routerWindows"}>
        <Routes />
      </div>
    </div>
  );
}

export default App;
