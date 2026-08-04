document.addEventListener("DOMContentLoaded", () => {
    const queryInput = document.getElementById("queryInput");
    const submitBtn = document.getElementById("submitBtn");
    const responseCard = document.getElementById("responseCard");
    const loader = document.getElementById("loader");
    const outputContent = document.getElementById("outputContent");
    const statusBadge = document.getElementById("statusBadge");

    async function triggerAgentExecution(queryText) {
        if (!queryText.trim()) return;

        // Reset UI states
        responseCard.classList.remove("hidden");
        loader.classList.remove("hidden");
        outputContent.classList.add("hidden");
        
        statusBadge.textContent = "Processing...";
        statusBadge.style.background = "rgba(245, 158, 11, 0.15)";
        statusBadge.style.color = "#f59e0b";
        
        submitBtn.disabled = true;
        submitBtn.textContent = "Analyzing...";

        try {
            const response = await fetch("/ask-agent", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ user_input: queryText })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || "An application error occurred.");
            }

            // Output generated answer
            outputContent.textContent = data.agent_response;
            statusBadge.textContent = "Completed";
            statusBadge.style.background = "rgba(16, 185, 129, 0.15)";
            statusBadge.style.color = "#10b981";

        } catch (error) {
            outputContent.textContent = `Error: ${error.message}`;
            statusBadge.textContent = "Failed";
            statusBadge.style.background = "rgba(239, 68, 68, 0.15)";
            statusBadge.style.color = "#ef4444";
        } finally {
            loader.classList.add("hidden");
            outputContent.classList.remove("hidden");
            submitBtn.disabled = false;
            submitBtn.textContent = "Execute Agent";
        }
    }

    // Submit via click execution
    submitBtn.addEventListener("click", () => {
        triggerAgentExecution(queryInput.value);
    });

    // Submit via Enter Key
    queryInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            triggerAgentExecution(queryInput.value);
        }
    });

    // Wire up prompt tags to automatically search on click
    document.querySelectorAll(".suggestion-tag").forEach(tag => {
        tag.addEventListener("click", () => {
            queryInput.value = tag.textContent;
            triggerAgentExecution(tag.textContent);
        });
    });
});
