'use client';
import React, { useState } from 'react';
import { Send } from 'lucide-react';
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";

export function ChatAppComponent() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (input.trim()) {
      const newMessage = {
        id: Date.now(),
        text: input.trim(),
        sender: 'user',
      };
      setMessages(prev => [...prev, newMessage]);
      setInput('');

      try {
        const response = await fetch('http://localhost:5000/chat-bot', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ question: newMessage.text, context: messages }) // Only send the text
        });
  
        if (!response.ok) {
          throw new Error(`Error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        const assistantMessage = {
          id: Date.now(),
          text: data.answer || 'No response', // Fallback if no answer is received
          sender: 'assistant',
        };
        setMessages(prev => [...prev, assistantMessage]);

      } catch (error) {
        console.error('Error fetching assistant message:', error);

        // Add "No response" message if the fetch fails
        const assistantMessage = {
          id: Date.now(),
          text: 'No response', // Default message on error
          sender: 'assistant',
        };
        setMessages(prev => [...prev, assistantMessage]);
      }
    }
  };

  return (
    <div className="flex flex-col h-screen bg-[#D9D9D9] p-4">
      <h1 className="text-2xl font-bold mb-4 text-[#962929]">Chat Application</h1>
      <ScrollArea className="flex-grow mb-4 bg-white rounded-lg shadow-md p-4">
        {messages.map(message => (
          <div
            key={message.id}
            className={`mb-2 p-2 rounded-lg ${
              message.sender === 'user' ? 'bg-[#962929] text-white self-end' : 'bg-gray-200 text-black self-start'
            }`}
          >
            {message.text}
          </div>
        ))}
      </ScrollArea>
      <div className="flex space-x-2">
        <Input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Type your message..."
          className="flex-grow"
        />
        <Button
          onClick={handleSend}
          className="bg-[#962929] hover:bg-[#7a2121] text-white">
          <Send className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}
