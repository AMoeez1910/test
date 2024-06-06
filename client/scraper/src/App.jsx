import React, { useState } from 'react';
import './App.css';
import ScraperForm from './components/ScraperForm/ScraperForm';
import Results from './components/Results/Results';

function App() {
    const [results, setResults] = useState({});

    return (
        <div className="App">
            <header className="App-header">
                <h1>Scraper App</h1>
            </header>
            <ScraperForm onResults={setResults} />
            <Results results={results} />
        </div>
    );
}

export default App;
