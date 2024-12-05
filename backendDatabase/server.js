const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();
const port = 3000;

// MongoDB connection URI (replace with your connection string for MongoDB Atlas or local instance)
const uri = "mongodb://localhost:27017";  // Local MongoDB URI
const client = new MongoClient(uri);

// Middleware to parse JSON
app.use(express.json());

// Connect to MongoDB
async function connectToDB() {
  try {
    await client.connect();
    console.log('Connected to MongoDB');
  } catch (err) {
    console.error(err);
  }
}

// Endpoint to fetch data from MongoDB
app.get('/data', async (req, res) => {
  try {
    const db = client.db('testdb');  // Name of the MongoDB database
    const collection = db.collection('testcollection');  // Name of the MongoDB collection
    const data = await collection.find({}).toArray();
    res.json(data);  // Send data to the frontend
  } catch (err) {
    res.status(500).send('Error retrieving data');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
  connectToDB();  // Connect to MongoDB when the server starts
});