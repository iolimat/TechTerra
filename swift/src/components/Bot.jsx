import { useState, useEffect, useRef } from 'react';
import '../css/ChatbotDesign.css';
import botImage from '../assets/bot.png';
import inputImage from '../assets/user.png';
import axios from 'axios';

const Bot = ({ showContent }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([{ message: "Hello, I'm TechTerra. Please provide me with the context.", sender: 'bot' }]);
  const [toggleBtnVisible, setToggleBtnVisible] = useState(true);
  const chatHistoryRef = useRef(null); // Ref to the chat history container

  // Effect to toggle chatbot visibility based on showContent prop
  useEffect(() => {
    setIsOpen(showContent); 
    setToggleBtnVisible(!showContent); 
  }, [showContent]);

  // Effect to scroll chat history to bottom when it updates
  useEffect(() => {
    if (chatHistoryRef.current) {
      chatHistoryRef.current.scrollTop = chatHistoryRef.current.scrollHeight;
    }
  }, [chatHistory]);

  // Function to toggle chatbot visibility
  const toggleChatbot = () => {
    setIsOpen(!isOpen);
    setToggleBtnVisible(false);
  };

  // Function to close the chatbot
  const closeChatbot = () => {
    setIsOpen(false);
    setToggleBtnVisible(!showContent); 
    setToggleBtnVisible(true);
  };

  // Function to handle input change
  const handleInputChange = (e) => {
    setMessage(e.target.value);
  };

  // Function to handle sending a message
  const handleSendMessage = async () => {
    if (message.trim() !== '') {
      // Add user's message to the chat history
      const updatedChatHistory = [...chatHistory, { message, sender: 'user' }];
      setChatHistory(updatedChatHistory);
      setMessage('');

      try {
        // Send message to the server and get response
        const response = await axios.post('http://192.168.66.190:8000/api/user_request', { message });
        const responseData = response.data; 
        // Add bot's response to the chat history
        const updatedChatHistoryWithResponse = [...updatedChatHistory, { message: responseData, sender: 'bot' }];
        setChatHistory(updatedChatHistoryWithResponse);
      } catch (error) {
        console.error('Error:', error.message);
        // If an error occurs, add error message to the chat history
        const updatedChatHistoryWithError = [...updatedChatHistory, { message: 'Sorry, I encountered an error. Please try again later.', sender: 'bot' }];
        setChatHistory(updatedChatHistoryWithError);
      }
    }
  };

  // Function to handle key down event (e.g., pressing Enter to send message)
  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  // Function to handle toggling chatbot visibility
  const handleToggle = () => {
    setIsOpen(!isOpen); 
    setToggleBtnVisible(false);
  };

  return (
    <div className="chatbot">
      {toggleBtnVisible && (
        <button className="chatbot-toggle-btn" onClick={handleToggle}></button>
      )}
      {isOpen && (
        <div className="chatbot-container">
          <div className="chatbot-header">
            <h3></h3>
            <button className="close-btn" onClick={closeChatbot}>
              X
            </button>
          </div>
          <div className="chat-history" ref={chatHistoryRef}>
            {chatHistory.map((item, index) => (
              <div key={index} className={`message ${item.sender}`}>
                {item.sender === 'bot' && <img src={botImage} alt="Bot" className="avatar" />}
                {item.sender === 'user' && <img src={inputImage} alt="User" className="avatar user" />}
                <div className="message-text">{item.message}</div>
              </div>
            ))}
          </div>
          <div className="input-container">
            <input
              type="text"
              placeholder="Type a message..."
              value={message}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown} 
              name="Prompt"
            />
            <button className="send-btn" onClick={handleSendMessage}>
              Send
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Bot;
