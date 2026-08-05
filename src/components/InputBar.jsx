import { useState } from "react";
import { sendMessage as sendApiMessage } from "../api";

function InputBar({ messages, setMessages }) {

    const [input, setInput] = useState("");

    async function sendMessage() {

        if (input.trim() === "") return;

        const userMessage = { sender: "user", text: input };

        // Kullanıcı mesajını ekle
        setMessages((prev) => [...prev, userMessage]);
        setInput("");

        try {
            // API'ye gönder
            const response = await sendApiMessage(input);
            
            // Bot cevabını ekle
            setMessages((prev) => [
                ...prev,
                { sender: "bot", text: response.bot }
            ]);
        } catch (error) {
            console.error("Bot ile iletişim hatası:", error);
            setMessages((prev) => [
                ...prev,
                { sender: "bot", text: "⚠️ Sunucuya bağlanılamadı! Lütfen backend terminalinde uvicorn main:app --reload komutunun çalıştığından emin ol." }
            ]);
        }
    }

    return (

        <div className="input-bar">

            <input

                type="text"

                placeholder="Mesaj yaz..."

                value={input}

                onChange={(e) => setInput(e.target.value)}

                onKeyDown={(e) => e.key === 'Enter' && sendMessage()}

            />

            <button onClick={sendMessage}>

                Gönder

            </button>

        </div>

    )

}

export default InputBar;