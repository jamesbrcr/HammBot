const express = require('express');
const { OpenAI } = require('openai');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const client = new OpenAI({
  apiKey: "your-api-key-here"
});

app.post('/api/chat', async (req, res) => {
  const { message } = req.body;
  
  try {
    const response = await client.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        {"role": "system", "content": "You are HammBot, an AI assistant that responds like Jared Hamm, a guy known for his random, goofy responses that often don't directly align with what was asked."},
        {"role": "user", "content": message}
      ]
    });
    
    res.json({ reply: response.choices[0].message.content });
  } catch (error) {
    res.status(500).json({ error: 'An error occurred while processing your request.' });
  }
});

app.listen(3001, () => console.log('Server running on port 3001'));
