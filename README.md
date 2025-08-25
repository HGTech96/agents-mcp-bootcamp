# Agents + MCP Bootcamp — README

## 📌 Summary
This bootcamp is a 20-step, day-by-day learning path to understand **AI Agents**, the **Model Context Protocol (MCP)**, and how to integrate them with a backend.  
We start from first principles (simple agent scripts), move through LangChain and MCP basics, and end by building a full **FastAPI + PostgreSQL backend** integrated with MCP and an agent that can log fitness/food data.  

The project is bare-metal (no Docker). Each step comes with detailed explanations of **what**, **why**, and **how**.

---

# 📚 Bootcamp Roadmap

## 🔹 Step 0 — Project Setup (Poetry · FastAPI · PostgreSQL)
**Summary:** Establish the foundation.  
- Initialize Poetry project with FastAPI, SQLAlchemy (async), Alembic, Postgres, Pydantic settings.  
- Create project structure (`src/amcp`).  
- Configure `.env`, Makefile, and Alembic.  
- Explain every file in detail: what, why, how.  
- Verify: `/health` endpoint works, Postgres accessible, Alembic runs.  

---

## 🔹 Step 1 — Simple Agent-Like Script (Vanilla Python)
**Summary:** Understand what an “agent” is in the simplest form.  
- Write a Python `SimpleAgent` that can call tools (weather, calculator, random).  
- Show how it chooses tools with `if-else`.  
- Realize limitations: no reasoning, no language understanding.  
- Task: Extend with one new tool.  

---

## 🔹 Step 2 — Agent with LLM Decision-Making (LangChain Intro)
**Summary:** Move from `if-else` to reasoning with an LLM.  
- Install LangChain (already in Poetry).  
- Build a minimal LangChain agent with 2 tools.  
- Compare: rule-based vs LLM-driven.  
- Task: Ask natural questions (“What’s 2+2?” / “What’s the weather?”).  

---

## 🔹 Step 3 — Tools & Actions
**Summary:** Learn how agents use external tools.  
- Add multiple tools: calculator, notes list, random generator.  
- Define what a “tool” is in LangChain.  
- Task: Teach the agent to add & list tasks.  

---

## 🔹 Step 4 — Intro to Model Context Protocol (MCP)
**Summary:** Understand MCP conceptually.  
- Why MCP exists: standardizing agent ↔ service communication.  
- Explain MCP architecture (server ↔ client).  
- Task: Write a short summary in your own words.  

---

## 🔹 Step 5 — Day Planner Agent (Mini Project)
**Summary:** Combine everything so far.  
- Agent can check weather, add tasks, do simple calculations.  
- CLI interface to interact with agent.  
- Task: Try “Plan my day” type queries.  

---

## 🔹 Step 6 — Memory (Short-Term Context)
**Summary:** Give the agent “memory.”  
- Add conversation buffer memory (LangChain).  
- Demonstrate sequential Q&A.  
- Task: Show difference between stateless vs memoryful agent.  

---

## 🔹 Step 7 — Memory (Semantic / Vector Intro)
**Summary:** Deeper memory concepts.  
- Explain embeddings, vector DBs (concept only).  
- Contrast buffer vs semantic memory.  
- Task: Write notes on use cases.  

---

## 🔹 Step 8 — First MCP Server
**Summary:** Run your first MCP service.  
- Install MCP SDK.  
- Write a server exposing a `create_note` command.  
- Test sending/receiving messages.  

---

## 🔹 Step 9 — Expanding MCP Server
**Summary:** Add real functionality.  
- Add `list_notes` command.  
- Explain why MCP is better than raw API calls (standard protocol, discoverability).  
- Task: Reflect on differences.  

---

## 🔹 Step 10 — Notes Assistant (Mini Project)
**Summary:** Combine MCP server + agent.  
- Agent can create and list notes via MCP.  
- Test with: “Remember to call mom.”  

---

## 🔹 Step 11 — FastAPI Backend Setup (Tasks API)
**Summary:** Begin backend integration.  
- Add `/tasks` endpoints in FastAPI (CRUD).  
- Verify with HTTP requests.  
- Task: Confirm working CRUD with Postgres.  

---

## 🔹 Step 12 — MCP Connector for Backend
**Summary:** Expose backend to agent via MCP.  
- Wrap `/tasks` endpoints in MCP server.  
- Verify: agent creates tasks via MCP.  

---

## 🔹 Step 13 — Persistence
**Summary:** Ensure data durability.  
- Add SQLAlchemy model for tasks.  
- Run Alembic migration.  
- Verify tasks survive restart.  

---

## 🔹 Step 14 — Authentication
**Summary:** Secure backend API.  
- Add API key header requirement.  
- Configure agent to include key.  

---

## 🔹 Step 15 — Task Manager Agent (Mini Project)
**Summary:** End-to-end integration.  
- Agent creates, lists, completes tasks via FastAPI backend + MCP.  
- Task: “Add buy milk, and list my tasks.”  

---

## 🔹 Step 16 — PostgreSQL Upgrade
**Summary:** Use a production-ready DB.  
- Switch from SQLite (if used earlier) to Postgres for all persistence.  
- Update connection strings, run migrations.  

---

## 🔹 Step 17 — Integration Patterns
**Summary:** Learn design approaches.  
- Agent as **service consumer** vs agent as **service provider**.  
- Discuss which fits our fitness logging use case.  

---

## 🔹 Step 18 — Observability
**Summary:** Add logging & tracing.  
- Log every agent ↔ backend call.  
- Show logs of one full conversation.  

---

## 🔹 Step 19 — Multi-Tool Reasoning
**Summary:** Make the agent more powerful.  
- Agent can call multiple tools: calendar, tasks, notes.  
- Task: “What’s on my calendar? Add a task to prepare.”  

---

## 🔹 Step 20 — Final Project: Fitness/Food Logging Assistant
**Summary:** Integrate everything into a demo.  
- Backend: FastAPI + Postgres stores meals & activities.  
- MCP: exposes `/food-entry` endpoints.  
- Agent: understands free text (“I ate 2 eggs and coffee”) → logs entry.  
- Demo: query calorie history.  
- Deliverable: Document setup, lessons learned, next steps.  

---

# 🎯 Outcome
By following all 20 steps you will:  
- Understand **agents conceptually & practically**.  
- Get hands-on with **MCP**.  
- Build and integrate a **FastAPI + PostgreSQL backend**.  
- Deliver a **final project** where an agent logs meals and queries calorie history via MCP.

