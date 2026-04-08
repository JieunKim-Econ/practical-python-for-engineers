# Practical Python for data engineers — files, APIs, and pipeline basics
Most Python tutorials focus on syntax. But real-world data engineering is about building **reliable and maintainable workflows**.

I created this repository to document practical Python examples covering common tasks such as file handling, API interaction, data transformation, and pipeline design. It covers the foundational patterns I wish I had known when I started — moving away from messy scripts toward structured, professional code.

## ✍️ Author's Note — [Jieun Kim](https://www.linkedin.com/in/jieunk101/)
This repository also serves as a living document of my commitment to writing clean and robust Python code.
Beyond making code work, I focus on writing scripts that can handle the realities of production — imperfect data, unexpected failures, and evolving requirements.

## 🎯 Focus Areas
This repo focuses on the essential best practices for any data engineer:

* **Configuration Management:** Using `.env` and environment variables for secure and flexible setup.
* **Defensive Programming:** Implementing robust error handling (`try-except`) for resilient API and file interactions.
* **Operational Visibility:** Moving beyond `print()` by implementing structured `logging` to track pipeline health and debugging.
* **Data Manipulation:** Practical usage of `pandas` and built-in modules to handle common data formats like CSV and JSON.

## 🛠 What's Inside
The examples in the `src/` directory are designed to be modular and easy to adapt for real-world tasks:

* **API Interaction:** How to fetch data while handling status codes and potential failures.
* **File I/O:** Best practices for reading and writing data efficiently and safely.
* **Data Transformation:** Essential patterns for cleaning and restructuring raw datasets.
* **Environment Setup:** Standardizing project environments to ensure code runs everywhere.

## 👤 Who This is For
* **Aspiring Data Engineers** who know basic syntax but want to learn how to structure a script properly.
* **Junior Developers** looking to adopt professional habits like logging and environment management.
