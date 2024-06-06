import React from 'react';
import './Results.css';

const Results = ({ results }) => {
    return (
        <div className="results-container">
            {Object.keys(results).map((query) => (
                <div key={query}>
                    <h3>Results for: {query}</h3>
                    <table className="results-table">
                        <thead>
                            <tr>
                                <th>Title</th>
                                <th>Image</th>
                                <th>Price</th>
                                <th>Total Reviews</th>
                                <th>Creation Time Stamp</th>
                                <th>Updated Time Stamp</th>
                                
                            </tr>
                        </thead>
                        <tbody>
                            {results[query].map((product, index) => (
                                <tr key={index}>
                                    <td>{product.title}</td>
                                    <td>
                                        <img src={product.image_url} alt={product.title} className="product-image" />
                                    </td>
                                    <td>{product.price || 'N/A'}</td>
                                    <td>{product.total_reviews}</td>
                                    <td>{product.creation_timestamp}</td>
                                    <td>{product.update_timestamp}</td>

                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            ))}
        </div>
    );
};

export default Results;
