import { useState } from "react";
import "./App.css";

import Header from "./components/Header";
import ChatBox from "./components/ChatBox";
import InputBar from "./components/InputBar";

function App() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Merhaba 👋 Ben BaşakGPT. Sana nasıl yardımcı olabilirim?"
    }
  ]);

  return (
    <div className="container">
      <Header />

      <ChatBox messages={messages} />

      <InputBar
        messages={messages}
        setMessages={setMessages}
      />
    </div>
  );
}

export default App;