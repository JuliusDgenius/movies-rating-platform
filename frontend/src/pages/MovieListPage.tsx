import React from 'react';
import { useMovies } from '../hooks/useMovies';
import { Movie } from '../types';

const MovieListPage: React.FC = () => {
  const { movies, isLoading, error } = useMovies();

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h2>All Movies</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
        {movies.map((movie: Movie) => (
          <div key={movie.id} className="border rounded-lg p-4 shadow">
            <h3 className="text-lg font-bold">{movie.title}</h3>
            <p className="text-gray-600">{movie.genre}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MovieListPage;