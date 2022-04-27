import React, { Component } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import Error from './components/Error';
import Navigation from './components/Navigation';
 
class App extends Component {
  render() {
    return (      
       <BrowserRouter>
        <div>
          <Navigation />
            <Routes>
            <Route path="/" element={<Home/>}/>            
            <Route path="/*" element={<Error/>}/>
           </Routes>
        </div> 
      </BrowserRouter>
    );
  }
}
 
export default App;