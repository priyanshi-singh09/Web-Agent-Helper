# 🔍 Web Intelligence Agent

A full-stack web search agent that provides concise, AI-powered answers to complex questions by intelligently searching the web, scraping content, and summarizing results.

## ✨ Features

- **Intelligent Query Classification**: Uses Gemini AI to validate and classify search queries
- **Smart Caching**: Implements Redis for exact matches and FAISS for semantic similarity search
- **Web Scraping**: Fetches and processes content from DuckDuckGo search results
- **AI Summarization**: Leverages Google's Gemini 2.5 Flash model for content summarization
- **Modern UI**: Clean, responsive React interface with Tailwind CSS
- **Fast Performance**: Vector-based caching reduces redundant API calls

## 🏗️ Architecture

### Backend (FastAPI)
- **agent.py**: Core logic for query processing, web scraping, and caching
- **main.py**: FastAPI server with CORS-enabled REST API
- **Technologies**: Python, FastAPI, Redis, FAISS, Sentence Transformers, BeautifulSoup

### Frontend (React + Vite)
- Modern React 19 application
- Tailwind CSS for styling
- Responsive design with gradient UI
- Real-time loading states

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- Redis server
- Google Gemini API key

## 🚀 Installation

### Backend Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd <project-directory>
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the backend directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
REDIS_URL=redis://localhost:6379
```

5. **Start Redis server**
```bash
redis-server
```

6. **Run the backend**
```bash
uvicorn main:app --reload --port 8000
```

### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Start development server**
```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 🔧 Configuration

### Backend Configuration

- **VECTOR_INDEX_PATH**: Path to store FAISS index (`vector.index`)
- **EMBEDDING_MODEL**: Sentence transformer model (`all-MiniLM-L6-v2`)
- **SIM_THRESHOLD**: Similarity threshold for cache hits (default: 0.75)

### Frontend Configuration

Update the API endpoint in `frontend/src/utils/handlesubmit.js` if deploying to production:
```javascript
const res = await fetch('YOUR_BACKEND_URL/query', {
    // ...
});
```
