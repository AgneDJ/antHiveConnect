import React from "react";
import "./App.css";
import { useState, useEffect } from "react";
import Login from "./components/login_form.jsx";
import LikeButton from "./components/like_button.jsx";
import UploadAndDisplayImage from "./components/profilePic.jsx";
import NavigationBar from "./components/navBar.jsx";
import ProfileCard from "./components/profile.jsx";

const App = () => {
  return (
    <div>
      <NavigationBar />

      <Login />

      <LikeButton />

      <ProfileCard />
      <UploadAndDisplayImage />
    </div>
  );
};

export default App;
