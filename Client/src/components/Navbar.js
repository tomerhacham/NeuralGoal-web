import React from 'react';
import '../CSS/Navbar.css';
import { Navbar, Nav } from 'react-bootstrap';
import { withRouter } from 'react-router-dom';

const Navigation = (props) => {
    console.log(props);
    return (
        <Navbar>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav>
                    <Nav.Link href="/" style={{color: "#CCD2D7",background: "none"}} >Upcoming Games</Nav.Link>
                    <Nav.Link href="/Stats" style={{color: "#CCD2D7",background: "none"}}>Stats For 20-21 Season</Nav.Link>
                    <Nav.Link href="/Foundation" style={{color: "#CCD2D7",background: "none"}} >Foundation</Nav.Link>
                    <Nav.Link href="/WinnerForm" style={{color: "#CCD2D7",background: "none"}}>Winner Form</Nav.Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default withRouter(Navigation);