import { useEffect, useRef } from "react";
import Message from "./Message";

function ChatBox({ messages }) {
    const endOfMessagesRef = useRef(null);

    // Mesajlar her değiştiğinde (yeni mesaj geldiğinde) en aşağıya kaydırır
    useEffect(() => {
        endOfMessagesRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages]);

    return (
        <div className="chat-box">
            {messages.map((msg, index) => (
                <Message
                    key={index}
                    sender={msg.sender}
                    text={msg.text}
                />
            ))}
            {/* Kaydırma işlemi için görünmez bir referans noktası */}
            <div ref={endOfMessagesRef} />
        </div>
    )
}

export default ChatBox;