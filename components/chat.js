import { useState } from "react";
import axios from "axios";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input) return;
    const newMessages = [...messages, { role: "user", content: input }];
    setMessages(newMessages);

    const res = await axios.post("http://localhost:8000/chat", {
      message: input,
      history: messages,
    });

    setMessages([
      ...newMessages,
      { role: "assistant", content: res.data.answer },
    ]);
    setInput("");
  };

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto" }}>
      <div style={{ border: "1px solid #ccc", padding: "10px", height: "400px", overflowY: "auto" }}>
        {messages.map((m, i) => (
          <p key={i}><b>{m.role}:</b> {m.content}</p>
        ))}
      </div>
      <input
        style={{ width: "80%", padding: "10px" }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Tulis pesan..."
      />
      <button onClick={sendMessage} style={{ padding: "10px" }}>
        Kirim
      </button>
    </div>
  );
}
