# Mistral CLI Interface for `mistral-large`

This project is a Command-Line Interface (CLI) tool designed to interact with the latest Mistral model, `mistral-large`. It allows users to perform various tasks, such as generating text or querying the model for specific outputs, directly from the terminal.

## Features

- Interact with the `mistral-large` model via simple CLI commands.
- Input text and receive generated responses based on the model’s understanding.
- Flexible and customizable options for controlling the generation process (e.g., temperature, max tokens).

## Installation

To use this project, you'll need to install the required dependencies and set up your environment.

### Prerequisites

- Python 3.8+ installed on your machine.
- A working internet connection to download model weights.

### Install Dependencies

1. Clone this repository:

   ```bash
   git clone https://github.com/MohamTahaB/mistral_project.git
   cd mistral-cli
   ```

2. Set up a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

3. Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Add an API key in a `.env` file (see [Mistral's open API documentation](https://docs.mistral.ai/)):
   ```bash
   MISTRAL_API_KEY="*************"
   ```

## Usage

Once the environment is set up, you can run the CLI tool to interact with `mistral-large`.

```bash
python main.py
```
