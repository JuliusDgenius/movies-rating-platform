import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { AuthContext } from '../contexts/AuthContext';

const Navbar = () => {
  const authContext = useContext(AuthContext);

  if (!authContext) {
    return null; // Or some fallback UI
  }

  const { token, logout } = authContext;

  return (
    <nav className="bg-gray-800 p-4 shadow-md">
      <ul className="flex space-x-4 list-none">
        <li><Link to="/" className="text-white hover:text-gray-300">Home</Link></li>
        <li><Link to="/movies" className="text-white hover:text-gray-300">Movies</Link></li>
        {token ? (
          <>
            <li><Link to="/add-movie" className="text-white hover:text-gray-300">Add Movie</Link></li>
            <li><button onClick={logout} className="text-white hover:text-gray-300 focus:outline-none">Logout</button></li>
          </>
        ) : (
          <>
            <li><Link to="/login" className="text-white hover:text-gray-300">Login</Link></li>
            <li><Link to="/register" className="text-white hover:text-gray-300">Register</Link></li>
          </>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
