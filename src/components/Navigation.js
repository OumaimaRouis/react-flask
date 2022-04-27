import React from 'react';
import { Nav, NavLink} from 'reactstrap';

 
const Navigation = () => {
    return (
       //<div>
         // <NavLink to="/">Home</NavLink>       
       //</div>
       <Nav>
        <NavLink href="/">Home</NavLink> 
        <NavLink href="/login">Login</NavLink> 
      </Nav>


    );
}
 
export default Navigation;