# 🛡️ RedSentinel: Multi-Agent Cybersecurity SOC Dashboard

> A concurrent multi-agent system where autonomous AI agents run simultaneously to analyze, simulate, and defend against security anomalies in real-time.

---

## 🎯 Overview

**RedSentinel** is a next-generation Security Operations Center (SOC) dashboard designed for advanced threat telemetry and automated defense simulation. Built for hackathons and enterprise demonstration, it leverages a multi-agent "Cyber Range" architecture powered by Google Gemini to orchestrate offensive maneuvers, defensive responses, and compliance auditing simultaneously.

---

## 🏗️ Architecture & Multi-Agent Pipeline

The core logic revolves around three specialized autonomous agents operating in sync:

1. **🔴 Red Team Agent**: Simulates offensive tactics, attack vectors, and penetration testing payloads to test system resilience.
2. **🔵 Blue Team Agent**: Analyzes incoming telemetry to generate real-time mitigation rules, patches, and defensive postures.
3. **⚖️ Auditor / Compliance Agent**: Evaluates the simulated engagement against security frameworks and generates concise compliance and risk reports.

---

## 🚀 Tech Stack

* **Frontend / Dashboard**: Streamlit (Python)
* **AI Engine**: Google Gemini (`gemini-3.5-flash`) via Mozaik-AI (`@mozaik-ai/core`)
* **Core Logic**: Python & TypeScript
* **Resilience**: Built-in silent automatic retry logic for handling API instabilities (503/429 throttling).

---

## ⚙️ Installation & Setup

### Prerequisites
* Python 3.10+
* Node.js & npm (for TypeScript modules)
* A valid Google Gemini API Key

### 1. Clone the Repository

git clone [https://github.com/cristandergt/RedSentinel.git](https://github.com/cristandergt/RedSentinel.git)
cd RedSentinel

2. Configure Environment Secrets

Create a Streamlit secrets file for your API credentials:

mkdir -p .streamlit
touch .streamlit/secrets.toml

Add your Gemini API key inside .streamlit/secrets.toml:

GEMINI_API_KEY = "api_key"

3. Run the Dashboard:

 streamlit run app.py


## 🔒 Security & Best Practices
Zero Credentials Leak: Sensitive files (.env, .streamlit/secrets.toml, and dependencies like node_modules/ or venv/) are strictly excluded via .gitignore.

Clean UI: Debug telemetry and raw API status alerts are suppressed for an end-user-ready presentation experience.
