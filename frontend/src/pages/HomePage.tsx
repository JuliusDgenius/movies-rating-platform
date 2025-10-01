import React from 'react';
import { Link } from 'react-router-dom';

const HomePage: React.FC = () => {
  return (
    <div className="container mx-auto mt-8 px-4 text-center">
      <h1 className="text-4xl font-bold mb-4">Welcome to the Movie Rating App</h1>
      <p className="text-lg mb-8">Here you can find and rate your favorite movies.</p>
      <nav className="flex justify-center space-x-4">
        <Link to="/movies" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          View All Movies
        </Link>
        <Link to="/add-movie" className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">Add a New Movie</Link>
      </nav>
    </div>
  );
};

export default HomePage;
