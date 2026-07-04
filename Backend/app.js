const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

const PORT = 3001;

app.get("/", (req, res) => {
    res.json({
        message: "Backend is running successfully!"
    });
});

app.get("/api/info", (req, res) => {
    res.json({
        application: "EKS CI/CD Demo",
        version: "1.0.0",
        service: "Backend",
        status: "Running"
    });
});

app.listen(PORT, () => {
    console.log(`Backend running on port ${PORT}`);
});
