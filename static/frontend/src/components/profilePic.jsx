import React, { useState, useEffect } from "react";

const UploadAndDisplayImage = () => {
  const [selectedImage, setSelectedImage] = useState(null);

  return (
    <div>
      <h1>Upload and Display Image</h1>

      {selectedImage && (
        <div>
          <img
            alt="not found"
            width={"250px"}
            src={URL.createObjectURL(selectedImage)}
          />
          <br />
          <button onClick={() => setSelectedImage(null)}>Remove</button>
        </div>
      )}

      <br />
      <br />

      <input
        type="file"
        name="myImage"
        onChange={(event) => {
          console.log(event.target.files[0]);
          setSelectedImage(event.target.files[0]);
        }}
      />
    </div>
  );
};

//   const Image = {
//     method: 'POST',
//     },
//     body: JSON.stringify(joke)
//   };
//   fetch('', options)
//     .then(response => response.json())
//     .then(data => console.log(data))
//     .catch(error => console.error(error));

// export default UploadAndDisplayImage;
