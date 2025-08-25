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
        """
        Naive reasoning: check keywords in the input string,
        then call the corresponding tool.
        """
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
