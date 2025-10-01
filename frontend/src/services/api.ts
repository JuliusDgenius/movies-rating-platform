import axios, { InternalAxiosRequestConfig } from 'axios';

const apiClient = axios.create({
  baseURL: '/api',
});

apiClient.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const login = (email: string, password: string): Promise<any> => {
  return apiClient.post('/auth/login', { email, password });
};

export const register = (username: string, email: string, password: string): Promise<any> => {
  return apiClient.post('/auth/register', { username, email, password });
};

export const getMovies = (): Promise<any> => {
  return apiClient.get('/movies');
};

export const getMovie = (id: string): Promise<any> => {
  return apiClient.get(`/movies/${id}`);
};

export const getReviews = (movieId: string): Promise<any> => {
  return apiClient.get(`/movies/${movieId}/reviews`);
};

export const addMovie = (data: any): Promise<any> => {
  return apiClient.post('/movies', data);
};

export const submitReview = (movieId: string, data: any): Promise<any> => {
  return apiClient.post(`/movies/${movieId}/reviews`, data);
};

export default apiClient;
