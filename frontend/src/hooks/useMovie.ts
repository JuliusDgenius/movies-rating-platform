import { useState, useEffect } from 'react';
import { getMovie, getReviews } from '../services/api';
import { Movie, Review } from '../types';

export const useMovie = (id: string | undefined) => {
  const [movie, setMovie] = useState<Movie | null>(null);
  const [reviews, setReviews] = useState<Review[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<any>(null);

  useEffect(() => {
    if (!id) {
      setIsLoading(false);
      return;
    }

    const fetchMovieAndReviews = async () => {
      try {
        const [movieResponse, reviewsResponse] = await Promise.all([
          getMovie(id),
          getReviews(id),
        ]);
        setMovie(movieResponse.data);
        setReviews(reviewsResponse.data);
      } catch (err) {
        setError(err);
      } finally {
        setIsLoading(false);
      }
    };

    if (id) {
      fetchMovieAndReviews();
    }
  }, [id]);

  return { movie, reviews, setReviews, isLoading, error };
};
