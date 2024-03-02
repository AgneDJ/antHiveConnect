import React from "react";
import "./App.css";
import { useState, useEffect } from "react";

import Login from "./components/login_form.jsx";
import LikeButton from "./components/like_button.jsx";

const App = () => {
  return (
    <div>
      <Login />
      <LikeButton />
    </div>
  );
};

export default App;
