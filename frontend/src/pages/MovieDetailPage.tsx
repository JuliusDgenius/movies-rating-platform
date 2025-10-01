import React, { useState, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { useMovie } from '../hooks/useMovie';
import { submitReview, getReviews } from '../services/api';
import { AuthContext } from '../contexts/AuthContext';
import { Review } from '../types';

const MovieDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [rating, setRating] = useState<number>(0);
  const [comment, setComment] = useState<string>('');
  const authContext = useContext(AuthContext);

  const handleReviewSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!id || !authContext) return;
    try {
      await submitReview(id, { rating, comment });
      // Refresh reviews after submission
      const updatedReviews = await getReviews(id);
      setReviews(updatedReviews.data);
      setRating(0);
      setComment('');
    } catch (error) {
      console.error('Failed to submit review', error);
    }
  };

  const { movie, reviews, setReviews, isLoading, error } = useMovie(id as string);

  if (!id) {
    return <div>Movie ID not provided.</div>;
  }

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {(error as Error).message}</div>;
  }

  if (!movie) {
    return <div>Movie not found.</div>;
  }

  return (
    <div>
      <h2>{movie.title}</h2>
      <p><strong>Genre:</strong> {movie.genre}</p>
      <p><strong>Release Year:</strong> {movie.release_year}</p>

      <h3>Reviews</h3>
      <div className="review-list">
        {reviews.map((review: Review) => (
          <div key={review.id} className="review-card">
            <p><strong>Rating:</strong> {review.rating}/5</p>
            <p>{review.comment}</p>
          </div>
        ))}
      </div>

      {authContext?.token && (
        <form onSubmit={handleReviewSubmit}>
          <h3>Add a Review</h3>
          <input
            type="number"
            min="1"
            max="5"
            value={rating}
            onChange={(e) => setRating(parseInt(e.target.value))}
            required
          />
          <textarea
            placeholder="Your review"
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            required
          ></textarea>
          <button type="submit">Submit Review</button>
        </form>
      )}
    </div>
  );
};

export default MovieDetailPage;
