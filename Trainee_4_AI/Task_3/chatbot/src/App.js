import React, { useState } from 'react';
import { OpenAI } from 'openai';
import "./App.css"

const App = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const openai = new OpenAI({
    apiKey: process.env.REACT_APP_OPENAI_API_KEY,
      dangerouslyAllowBrowser: true
  });

    const handleSendMessage = async () => {
        try {
            const response = await openai.chat.completions.create({
                model: 'gpt-3.5-turbo',
                messages: [
                    ...messages,
                    { role: 'system', content: 'You are going to help me get through this.' },
                    { role: 'user', content: input }
                ],
            });

            setMessages([
                ...messages,
                { role: 'user', content: input },
                { role: 'assistant', content: response.choices[0].message.content }
            ]);
            setInput('');
        } catch (error) {
            console.error('Error', error);
        }
    };
  return (
      <div className="main">
        <div className="chatbox">
          {messages.map((message, index) => (
              <div key={index} className={`message ${message.role}`}>
                {message.content}
              </div>
          ))}
        </div>
        <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
  );
};

export default App;