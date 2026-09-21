# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## Scenario Chosen

I selected a student marks management scenario. The private data contains marks of students stored locally in Python. Since the data is private, a public LLM does not know these values.

Example data:

* Abarna = 92
* Priya = 85
* Kavin = 78
* Rahul = 88

The objective is to answer questions related to student marks.

---

# Plain Chatbot

The plain chatbot uses only an LLM. It does not have access to the private student marks stored in the local system.

When a user asks for a student's mark, the chatbot generates a response using its training knowledge. Since the marks are private and not part of its training data, it cannot reliably answer the question.

The chatbot requires no tools and no predefined rules. It simply sends the user's message to the LLM and returns the generated response.

The limitation of this approach is that it cannot access private information and may produce incorrect or hallucinated answers.

---

# Rule-Based Workflow

The rule-based workflow uses predefined Python rules and conditions.

The workflow directly accesses the private marks dictionary stored in the program. It follows fixed if-else conditions to answer questions.

For example, if the user asks for Abarna's mark, the workflow checks the student name and returns the corresponding value.

This approach is reliable for predefined questions. However, it cannot handle unexpected requests outside the programmed rules.

The limitation is that every possible question type must be manually coded by the developer.

---

# AI Agent

The AI agent combines an LLM, tools, and a loop.

The agent uses tools that can access private student data and perform calculations. The LLM decides which tool to call based on the user's request.

The process follows:

1. Reason about the user's request.
2. Select an appropriate tool.
3. Execute the tool.
4. Observe the result.
5. Continue until a final answer is generated.

For example, if the user asks for the average mark, the agent can call a marks tool, retrieve the data, calculate the average, and return the result.

The agent can solve multi-step problems more effectively than a chatbot or workflow.

The limitation is that it depends on correct tool design and model tool-calling capability.

---

# Comparison Table

| Basis for Comparison     | Plain Chatbot | Rule-Based Workflow       | AI Agent                       |
| ------------------------ | ------------- | ------------------------- | ------------------------------ |
| Flexibility              | High          | Low                       | High                           |
| Decision-Making          | LLM-generated | Fixed rules               | LLM + tools                    |
| Tool Usage               | No            | No                        | Yes                            |
| Private Data Access      | No            | Yes                       | Yes                            |
| Multi-Step Task Handling | Limited       | Limited                   | Strong                         |
| Automation               | Low           | Medium                    | High                           |
| Reliability              | Medium        | High for predefined tasks | High when tools work correctly |

---

# Suitability Analysis

For the student marks scenario, the AI agent is the most suitable approach.

The chatbot cannot access private marks and may provide incorrect answers. The rule-based workflow can answer only predefined questions and cannot easily adapt to new requests.

The AI agent combines the reasoning capability of an LLM with access to tools that retrieve private data. It can handle complex and multi-step questions while still using accurate private information.

Therefore, the AI agent provides the best balance between flexibility, automation, and accuracy.

---

# Conclusion

A plain chatbot is suitable when general conversational responses are required and private data is not needed.

A rule-based workflow is suitable when tasks are predictable and follow fixed business rules.

An AI agent is suitable when tasks require reasoning, tool usage, private-data access, and multi-step decision making.

As problems become more dynamic and complex, the AI agent becomes the most effective solution because it combines LLM intelligence with external tools and iterative reasoning.
