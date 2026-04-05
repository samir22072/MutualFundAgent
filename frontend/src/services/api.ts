const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

export const chatService = {
  async sendMessage(query: string): Promise<{ response: string }> {
    const response = await fetch(`${backendUrl}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ detail: "Failed to fetch from backend" }));
      throw new Error(errorData.detail || "Failed to fetch from backend");
    }

    return response.json();
  }
};
