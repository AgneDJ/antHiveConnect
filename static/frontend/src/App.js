import React from "react";
// import "./App.css";
import { useState, useEffect } from "react";
import Register from "./components/registerForm";
import NavigationBar from "./components/navBar";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <NavigationBar />
        {/* You can add a navigation bar or other header content here */}
      </header>
      <main>
        <Register /> {/* This is where the Register component is rendered */}
      </main>
      <footer>{/* And a footer here, if you have one */}</footer>
    </div>
  );
}

export default App;

//   <Register />;
//   const [data, setData] = useState([{}]);

//   useEffect(() => {
//     fetch("/friends")
//       .then((res) => res.json())
//       .then((data) => {
//         setData(data);
//         console.log(data);
//       });
//   }, []);

//   return (
//     <div>
//       {typeof data.friends === "undefined" ? (
//         <p> Loading... </p>
//       ) : (
//         data.friends.map((friend, i) => (
//           <p>
//             {" "}
//             key={i}>{friend}
//           </p>
//         ))
//       )}
//     </div>x
//   );
// }

// export default App;
