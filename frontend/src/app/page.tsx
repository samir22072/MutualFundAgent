"use client";

import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { chatService } from "../services/api";

type Message = {
  role: "user" | "advisor";
  content: string;
};

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "advisor",
      content: "Hello! I am your AI Financial Advisor. How can I help you with your mutual fund investments today?"
    }
  ]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setInput("");
    
    setMessages((prev) => [...prev, { role: "user", content: userMessage }]);
    setIsLoading(true);

    try {
      const data = await chatService.sendMessage(userMessage);
      setMessages((prev) => [...prev, { role: "advisor", content: data.response }]);
    } catch (error: any) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { role: "advisor", content: `I'm sorry, I encountered an error: ${error.message}. Please try again later.` }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="chat-container">
      <header className="chat-header">
        <h1>AI Financial Advisor</h1>
      </header>
      
      <div className="messages-area">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.role}`}>
            {msg.role === "advisor" ? (
              <div className="markdown-content">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>{msg.content}</ReactMarkdown>
              </div>
            ) : (
              <div>{msg.content}</div>
            )}
          </div>
        ))}
        {isLoading && (
          <div className="message advisor" style={{ width: 'fit-content' }}>
             <div className="loading-dots">
                <div className="dot"></div>
                <div className="dot"></div>
                <div className="dot"></div>
             </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <form onSubmit={handleSubmit} className="chat-form">
          <input
            type="text"
            className="chat-input"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="E.g., I want to invest in low-risk funds for 3 years..."
            disabled={isLoading}
          />
          <button 
            type="submit" 
            className="chat-submit"
            disabled={!input.trim() || isLoading}
          >
            Send
          </button>
        </form>
      </div>
    </main>
  );
}
