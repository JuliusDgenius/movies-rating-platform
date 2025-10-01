export interface Movie {
  id: string;
  title: string;
  genre: string;
  release_year: number;
}

export interface Review {
  id: number;
  rating: number;
  comment: string;
}