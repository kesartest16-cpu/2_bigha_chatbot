async function sendMessage() {
  let input = document.getElementById("userInput");
  let message = input.value;
  if (!message) return;

  let chatlog = document.getElementById("chatlog");
  chatlog.innerHTML += `<p class='user'>You: ${message}</p>`;
  input.value = "";

  let response = await fetch("/get", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });
  let data = await response.json();

  chatlog.innerHTML += `<p class='bot'>Bot: ${data.response}</p>`;
  chatlog.scrollTop = chatlog.scrollHeight;
}
