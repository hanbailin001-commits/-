import React from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Login from './pages/Login'

export default function App(){
  return (
    <BrowserRouter>
      <div style={{padding:20}}>
        <h2>Telegram WebApp Skeleton</h2>
        <Routes>
          <Route path="/" element={<Login/>} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}
