
# Step 1 — Simple Agent-Like Script (Vanilla Python)

## 📌 Summary
In this step you’ll **demystify “agents”** by building the simplest possible agent in **pure Python**—no frameworks.  
An agent is any system that can **perceive** (accept input), **reason** (decide what to do), and **act** (call a tool or function).  
You’ll implement a tiny agent that selects from a few tools (weather, calculator, random number, time) using naive keyword checks.  
This shows the **core idea**: agents are decision-making + tool use. In later steps we’ll replace naive logic with **LLM-driven reasoning**.

---

## 📂 File & Path
Create this file relative to the project root:

**`agents-mcp-bootcamp/src/amcp/step_1_simple_agent.py`**

```python
import random
import datetime


class SimpleAgent:
    def __init__(self):
        # Tools are just Python functions stored in a dictionary
        self.tools = {
            "weather": self.get_weather,
            "calculator": self.calculate,
            "random": self.get_random_number,
            "time": self.get_current_time,
        }

    # ----- Tools -----
    def get_weather(self, location="Yerevan"):
        return f"The weather in {location} is sunny and 28°C."

    def calculate(self, expression):
        try:
            return eval(expression)
        except Exception:
            return "Error in calculation"

    def get_random_number(self):
        return random.randint(1, 100)

    def get_current_time(self):
        now = datetime.datetime.now()
        return f"Current time: {now.strftime('%H:%M:%S')}"

    # ----- Core decision loop -----
    def act(self, task: str):
        \"\"\"
        Naive reasoning: check keywords in the input string,
        then call the corresponding tool.
        \"\"\"
        if "weather" in task.lower():
            return self.tools["weather"]()
        elif any(op in task for op in ["+", "-", "*", "/"]):
            return self.tools["calculator"](task)
        elif "random" in task.lower():
            return self.tools["random"]()
        elif "time" in task.lower():
            return self.tools["time"]()
        else:
            return "I don’t know how to do that yet."


# ----- Example usage -----
if __name__ == "__main__":
    agent = SimpleAgent()

    print(agent.act("What’s the weather in Yerevan?"))
    print(agent.act("2 + 2 * 3"))
    print(agent.act("Give me a random number"))
    print(agent.act("What time is it?"))
    print(agent.act("Tell me a joke"))
```

---

## 🔍 How It Works (Explanation)

### Imports
```python
import random
import datetime
```
- `random` enables a simple “random number” tool.  
- `datetime` enables a “current time” tool.

### Tools Dictionary
```python
self.tools = {
    "weather": self.get_weather,
    "calculator": self.calculate,
    "random": self.get_random_number,
    "time": self.get_current_time,
}
```
- The agent stores **callable tools** in a dictionary for easy lookup.  
- In real systems, tools are often **APIs**, **DB queries**, or **system commands**.

### Tool Functions
```python
def get_weather(self, location="Yerevan"): ...
def calculate(self, expression): ...
def get_random_number(self): ...
def get_current_time(self): ...
```
- Each tool is a plain Python function.  
- Here, `get_weather` is mocked; `calculate` uses `eval()` (okay for demo, unsafe in production); the others are standard library based.

### Decision Logic
```python
def act(self, task: str):
    if "weather" in task.lower():
        return self.tools["weather"]()
    elif any(op in task for op in ["+", "-", "*", "/"]):
        return self.tools["calculator"](task)
    elif "random" in task.lower():
        return self.tools["random"]()
    elif "time" in task.lower():
        return self.tools["time"]()
    else:
        return "I don’t know how to do that yet."
```
- The agent **parses the input string** and chooses a tool via naive keyword checks.  
- **Limitation:** brittle to phrasing (e.g., “What’s it like outside?” won’t match).  
- Later, you’ll replace this with **LLM-driven tool selection**.

### Example Usage
```python
if __name__ == "__main__":
    agent = SimpleAgent()
    ...
```
- Runs a few sample queries and prints results—one intentionally unsupported (“Tell me a joke”) to show the fallback path.

---

## 🧪 Try It
From the project root (`agents-mcp-bootcamp/`), run:

```bash
poetry run python src/amcp/step_1_simple_agent.py
```

You should see outputs for weather, calculator, random number, and time; the “joke” request will return the fallback message.

---

## 🧩 Extension Task (Optional)
- Add **one new tool** of your own (e.g., `greet(name)` → “Hello, <name>!” or `square(number)` → number²).  
- Update `act()` so it can route to your tool.  
- Re-run the script to test it.

---

## 🧠 Key Takeaways
- An agent = **Perceive → Reason → Act**.  
- Tools can be simple functions (and later, real APIs).  
- Today’s reasoning is naive; next, we’ll explore **LLM-driven** decision-making.
