import React, { useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { AuthContext } from '../contexts/AuthContext';

const ProtectedRoute: React.FC = () => {
  const authContext = useContext(AuthContext);
  const token = authContext?.token;

  return token ? <Outlet /> : <Navigate to="/login" />;
};

export default ProtectedRoute;