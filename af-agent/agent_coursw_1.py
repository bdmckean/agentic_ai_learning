"""HF Agnet course quiz"""

# Flags to control which problems to run
RUN_PROBLEM_1 = False
RUN_PROBLEM_2 = False
RUN_PROBLEM_3 = True

# Q1 Make this code work
# Create a CodeAgent with DuckDuckGo search capability
"""
from smolagents import CodeAgent

agent = CodeAgent(
    tools=[],           # Add search tool here
    model=None          # Add model here
)
"""

if RUN_PROBLEM_1:
    # Create a CodeAgent with DuckDuckGo search capability
    from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel
    import os

    # Load environment variables if needed
    from dotenv import load_dotenv

    load_dotenv()

    # Create model with token if available
    model = InferenceClientModel(token=os.getenv("HF_TOKEN"))

    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],  # Add search tool here
        model=model,  # Use the model we created above
    )

    result = agent.run(
        "Search for the best music recommendations for a party at the Wayne's mansion."
    )
    print(f"\n=== Problem 1 Result ===\n{result}\n")

if RUN_PROBLEM_2:
    # Problem 2
    # Create web agent and manager agent structure
    # Web agent has correct tools configured
    # Manager agent properly references web agent
    # Appropriate max_steps value is set
    # Required imports are authorized

    """
    web_agent = ToolCallingAgent(
        tools=[],           # Add required tools
        model=None,         # Add model
        max_steps=5,        # Adjust steps
        name="",           # Add name
        description=""      # Add description
    )

    manager_agent = CodeAgent()
    """
    from smolagents import (
        ToolCallingAgent,
        CodeAgent,
        WebSearchTool,
        InferenceClientModel,
    )
    import os

    # Load environment variables
    from dotenv import load_dotenv

    load_dotenv()

    # Create model for both agents
    model = InferenceClientModel(token=os.getenv("HF_TOKEN"))

    # Create web agent and manager agent structure
    web_agent = ToolCallingAgent(
        tools=[WebSearchTool()],  # Add required tools
        model=model,  # Add model
        max_steps=5,  # Adjust steps
        name="web_agent",  # Add name (must be valid Python identifier)
        description="A web agent that will search the web for information",  # Add description
    )

    # Manager agent coordinates tasks using the web agent
    manager_agent = CodeAgent(
        managed_agents=[web_agent],  # Manager can use web agent (not tools!)
        model=model,
        name="manager_agent",
        description="A manager agent that will coordinate the web agent",
    )

    # Create a task for the manager agent to complete
    task = (
        "Search for the best music recommendations for a party at the Wayne's mansion."
    )

    # Run the manager agent with the task
    result = manager_agent.run(task)
    print(f"\n=== Problem 2 Result ===\n{result}\n")


# Problem 3
# Challenge:
# Configure Agent Security Settings
# Assessment Criteria:
# E2B sandbox is properly configured
# Authorized imports are appropriately limited
# Security settings are correctly implemented
# Basic agent configuration is maintained

# Set up secure code execution environment
"""
from smolagents import CodeAgent

agent = CodeAgent(
    tools=[],
    model=model
    # Add security configuration
)
"""
if RUN_PROBLEM_3:
    # Create a CodeAgent with secure configuration
    from smolagents import (
        CodeAgent,
        InferenceClientModel,
        WikipediaSearchTool,
        WebSearchTool,
    )
    import os
    from dotenv import load_dotenv

    load_dotenv()

    model = InferenceClientModel(token=os.getenv("HF_TOKEN"))

    # Configure secure CodeAgent with E2B sandbox and limited imports
    agent = CodeAgent(
        tools=[WikipediaSearchTool(), WebSearchTool()],  # Basic agent configuration
        model=model,
        executor_type="e2b",  # E2B sandbox ensures secure code execution
        additional_authorized_imports={
            "os",    # Only required built-in modules are allowed
            "json",
            "math"
        },
    )

    result = agent.run("Calculate 15 + 27 and print the result")
    print(f"\n=== Problem 3 Result ===\n{result}\n")
