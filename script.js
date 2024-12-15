// DOM Elements
const sendButton = document.getElementById("sendButton");
const userMessage = document.getElementById("userMessage");
const chatBox = document.getElementById("chatBox");

// Function to display a single chat entry in the chat box
function displayChat(entry) {
    const userMessageHTML = `
        <div class="message">
            <p><strong class="user-message">You:</strong> ${entry.user}</p>
        </div>`;
    const botResponseHTML = `
        <div class="message">
            <p><strong class="bot-response">Bot:</strong> ${entry.bot}</p>
        </div>`;
    chatBox.innerHTML += userMessageHTML + botResponseHTML;

    // Auto-scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to send a message
async function sendMessage() {
    const message = userMessage.value;

    // Ensure the input is not empty
    if (!message.trim()) {
        alert("Please enter a message!");
        return;
    }

    try {
        // Send user message to the server
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        // Handle the server response
        if (response.ok) {
            const data = await response.json();
            if (data.chat) {
                displayChat(data.chat); // Add the chat data to the display
            }
        } else {
            console.error("Failed to send the message.");
        }
    } catch (error) {
        console.error("Error connecting to the server:", error);
    }

    // Clear the input field
    userMessage.value = "";
}

// Event listener for the send button
sendButton.addEventListener("click", sendMessage);

// Event listener for the "Enter" key
userMessage.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) { // Check for Enter key without Shift
        event.preventDefault(); // Prevent adding a new line in the textarea
        sendMessage(); // Send the message
    }
});
