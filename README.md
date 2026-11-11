# ☕ Local Coffee Shop RAG Bot

Ever wanted to ask an AI if a coffee shop is *actually* good for Zoom meetings without it just guessing?

This project is a completely local Retrieval-Augmented Generation (RAG) pipeline designed to chat with a dataset of coffee shop reviews. Instead of relying on expensive cloud APIs, it runs entirely on your own hardware using Ollama. It reads the reviews, finds the most relevant ones based on your question, and synthesizes a direct answer.

## 🛠️ The Tech Stack

* **LLM Engine:** [Ollama](https://ollama.com/) (running `llama3.2` for text generation)
* **Embeddings:** `mxbai-embed-large` (optimized for semantic search)
* **Orchestration:** LangChain
* **Vector Database:** ChromaDB
* **Data Handling:** Pandas

## 📂 Project Structure

* `coffee_shop_reviews.csv`: The source dataset featuring 128 unique, realistic coffee shop reviews (including ratings, dates, and titles).
* `vector.py`: The filing cabinet. This script reads the CSV, chunks the data into individual documents, generates embeddings, and saves them locally into a Chroma database (`./chroma_langchain_db`).
* `main.py`: The chat interface. It takes your terminal input, searches the vector database for the 7 most relevant reviews, formats them into clean English, and hands them to Llama 3.2 to answer your question.

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python installed, and download [Ollama](https://ollama.com/download) for your operating system.

### 2. Install Dependencies

Open your terminal and install the required Python packages:

```bash
pip install langchain-ollama langchain-chroma langchain-core pandas

```

### 3. Pull the Local Models

Before running the code, you need to download the models into Ollama. This might take a few minutes depending on your internet connection.

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large

```

### 4. Build the Vector Database

Run the vector script first. This will parse the CSV and build your local Chroma database. You only need to run this once (or whenever you update the CSV).

```bash
python vector.py

```

### 5. Start Chatting

Fire up the main application.

```bash
python main.py

```

Once the prompt appears, you can ask it anything about the reviews. Try asking:

* *"What specific gluten-free pastries do they have?"*
* *"Is this a good place to study and take Zoom meetings?"*
* *"Are there any complaints about the barista's attitudes?"*

## 🧠 How the Prompt Injection Works

To prevent the LLM from getting confused by raw Python syntax, `main.py` intercepts the retrieved documents before they hit the prompt. It strips out the Python `Document()` wrappers and injects a clean, human-readable string (e.g., `Rating: 5/5 \n Review: Best cold brew...`). This saves tokens and drastically improves Llama 3.2's ability to synthesize contrasting reviews accurately.