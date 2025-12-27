const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/calculate", async (req, res) => {
  const response = await axios.post(
    "http://localhost:5000/predict",
    req.body
  );
  res.json(response.data);
});

app.listen(4000, () => {
  console.log("Node server running on port 4000");
});
