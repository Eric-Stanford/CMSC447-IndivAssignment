import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import createInput from './createInput.js'

function App() {
  const [placeholder, setPlaceholder] = useState('Hi');
  const [placeholder2, setPlaceholder2] = useState('Hello');

  useEffect(() => {
    fetch('/hello').then(res => res.json()).then(data => {
      setPlaceholder(data.result);
    });
  }, []);
 

  return (
    <div className="App">
      <header className="App-header">
        <div dangerouslySetInnerHTML = {{__html: placeholder}} />
      </header>
    </div>
  );
}

export default App;