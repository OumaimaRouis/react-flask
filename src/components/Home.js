import React, { Component } from 'react';


export default class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
            output : []
        };
      }
    
    componentDidMount() {
        fetch('http://localhost:5000/').then
                (res => res.json()
        ).then(
              data => {
              console.log(data)         
            this.setState({               
                output: data
              });
            
          });
      }
    
    render() {
       
        return (
        <div>
             <h1>This is the Homepage</h1>
              <p>{this.state.output.hello}</p>
              <p>{this.state.output.results}</p>
        </div>
        );
      }
}