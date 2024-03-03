import UploadAndDisplayImage from "./profilePic.jsx";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";

function ProfileCard() {
  return (
    <Card style={{ width: "18rem" }}>
      <UploadAndDisplayImage />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
  );
}

export default ProfileCard;