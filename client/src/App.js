import logo from "./logo.svg";
import { useState, useEffect } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { Container, Form, Row, Col, Card } from "react-bootstrap";
import { createClient } from "@supabase/supabase-js";
import { v4 as uuidv4 } from "uuid";

const supabase = createClient(
  "https://kbiicczvfwmduyungrpa.supabase.co",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtiaWljY3p2ZndtZHV5dW5ncnBhIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzY3MjQ0NzksImV4cCI6MTk5MjMwMDQ3OX0.6QgnUO6Gw54qmzvZyFdbfg-1hkWo2ZBvmOxIvVszW_E"
);



const CDNURL =
  "https://kbiicczvfwmduyungrpa.supabase.co/storage/v1/object/public/videos/";

function App() {
  const [videos, setVideos] = useState([]);

  async function getVideos() {
    const { data, error } = await supabase.storage.from("videos").list("");

    if (data !== null) {
      setVideos(data);
    } else {
      console.log(error);
      alert("Error grabbing files from supabase");
    }
  }

  useEffect(() => {
    getVideos();
  }, []);

  async function uploadFile(e) {
    const videoFile = e.target.files[0];
    // console.log("Upload!");
    const { error } = await supabase.storage
      .from("videos")
      .upload(uuidv4() + ".mp4", videoFile);
    if (error) {
      console.log(error);
      alert("error uploading file to supabase");
    }

    getVideos();
  }

  async function deleteVideo(event, video) {
    // console.log(video);
    const {data, error} = await supabase.storage.from("videos").remove([video.name]);
    getVideos();
  }

  // console.log(videos);

  return (
    <Container className="mt-5" style={{ width: "2000px" }}>
      <h1> Video Feed </h1>
      <Form.Group className="mb-3 mt-3">
        <Form.Label> Upload your Video here!</Form.Label>
        <Form.Control
          type="file"
          accept="video/mp4"
          onChange={(e) => uploadFile(e)}
        />
      </Form.Group>

      <Row xs={1} className="g-4">
        {videos.map((video) => {
          console.log(video.name);
          if (video.name === ".emptyFolderPlaceholder") return null;

          return (
            <Col key={video.name} md="6" lg="4">
              <Card>
                <video height="280px" controls>
                  <source src={CDNURL + video.name} type="video/mp4" />
                </video>
                <button onClick={(e) => {
                  deleteVideo(e, video)
                }}>Delete</button>
              </Card>
            </Col>
          );
        })}
      </Row>
    </Container>
  );
}

export default App;
