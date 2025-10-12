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
