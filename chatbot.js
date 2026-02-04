async function ask() {
     const chat = document.getElementById("chatt");
     const input = document.getElementById("q");
     try {
         const question = input.value.trim();
         if (!question) return;
         chat.textContent = "Thinking...";

         const res = await fetch("http://127.0.0.1:5000/ask", {
             method: "POST",
             headers: {
                 "Content-Type": "application/json"
             },
             body: JSON.stringify({
                 question
             })
         });
         const data = await res.json();
         chat.textContent = data.answer;
         input.value = "";
     } catch (err) {
         chat.textContent = "Error: " + err.message;
         console.error(err);
     }
 }