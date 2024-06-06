import React, { useState } from 'react';

const ScraperForm = ({ onResults }) => {
    const [queries, setQueries] = useState(['']);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleChange = (index, event) => {
        const newQueries = queries.slice();
        newQueries[index] = event.target.value;
        setQueries(newQueries);
    };

    const handleAddQuery = () => {
        setQueries([...queries, '']);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch('http://127.0.0.1:5000/scrape', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ queries })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            console.log(result);
            onResults(result);
        } catch (error) {
            console.error('Error during fetch:', error);
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {queries.map((query, index) => (
                <div key={index}>
                    <input 
                        type="text"
                        value={query}
                        onChange={(event) => handleChange(index, event)}
                    />
                </div>
            ))}
            <button type="button" onClick={handleAddQuery}>Add Query</button>
            <button type="submit">Scrape</button>
            {loading && <p>Loading...</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </form>
    );
};

export default ScraperForm;
