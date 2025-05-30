import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Login from './components/Login';
import Register from './components/Register';
import AddFood from './components/AddFood';
import Report from './components/Report';
import Landing from './components/Landing';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/home" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/add-food" element={<AddFood />} />
      <Route path="/report" element={<Report />} />
    </Routes>
  );
}

export default App;
