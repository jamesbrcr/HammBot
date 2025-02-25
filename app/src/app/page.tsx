"use client";

import { useState } from 'react';
import Header from '../components/Header';

export default function Home() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Array<{ text: string; isUser: boolean }>>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    // add user message to the chat
    setMessages(prev => [...prev, { text: input, isUser: true }]);

    // TODO: send input to AI backend and get response
    // temporary: echo the input
    const aiResponse = `You said: ${input}`;

    // add AI response to the chat
    setMessages(prev => [...prev, { text: aiResponse, isUser: false }]);

    setInput('');
  };

  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-br from-[#262423] to-[#141413]">
      <Header />
      <main className="flex-1 p-4 flex flex-col items-center">
        <h1 className="text-2xl font-bold mb-4 text-orange-200">Have fun with Jared...</h1>
        <div className="max-w-2xl w-full bg-black bg-opacity-40 rounded-lg shadow-lg overflow-hidden">
          <div className="border border-orange-700 border-opacity-40 rounded-lg">
            <div className="h-[500px] overflow-y-auto p-4">
              {messages.map((message, index) => (
                <div key={index} className={`mb-4 ${message.isUser ? 'text-right' : 'text-left'}`}>
                  <span className={`inline-block p-2 rounded-lg ${
                    message.isUser ? 'bg-orange-600 bg-opacity-40 text-white' : 'bg-gray-200 text-gray-800'
                  }`}>
                    {message.text}
                  </span>
                </div>
              ))}
            </div>
            <div className="border-t border-orange-700 border-opacity-40 p-4">
              <form onSubmit={handleSubmit} className="flex items-center">
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  className="flex-1 p-2 border bg-orange-800 bg-opacity-20 border-gray-300 border-opacity-0 rounded-l-lg focus:outline-none focus:ring-0 focus:ring-orange-500"
                  placeholder="Talk to Jared Hamm..."
                />
                <button type="submit" className="bg-orange-800 text-white p-2 rounded-r-lg hover:bg-orange-600 focus:outline-none focus:ring-0 focus:ring-blue-500">
                  Send
                </button>
              </form>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}


