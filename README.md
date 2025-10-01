<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gemini Pro Chatbot with Streamlit README</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            color: #e6edf3;
            background-color: #0d1117;
            padding: 20px 40px;
            max-width: 800px;
            margin: 0 auto;
        }
        h1, h2, h3 {
            border-bottom: 1px solid #30363d;
            padding-bottom: 0.3em;
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
        }
        h1 { font-size: 2.2em; }
        h2 { font-size: 1.8em; }
        h3 { font-size: 1.4em; }
        a {
            color: #58a6ff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        p, ul {
            margin-bottom: 16px;
        }
        ul {
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        code {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            font-size: 0.9em;
            background-color: #161b22;
            padding: 0.2em 0.4em;
            margin: 0;
            border-radius: 6px;
        }
        pre {
            background-color: #161b22;
            padding: 16px;
            border-radius: 6px;
            overflow: auto;
        }
        pre code {
            padding: 0;
            background-color: transparent;
            font-size: 0.85em;
        }
        strong {
            font-weight: 600;
        }
        .container {
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 20px;
        }
        .center {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 Gemini Pro Chatbot with Streamlit</h1>
        <p>A conversational AI chatbot built using Python, Streamlit, and the powerful Google Gemini Pro API. This application provides a clean, responsive user interface for interacting with the Gemini model, maintaining a full conversation history for context-aware responses.</p>
        
        <h3 class="center">✨ <a href="https://my-gemini-pro-chatbot.streamlit.app/"><strong>Live Demo on Streamlit Cloud</strong></a> ✨</h3>

        <h2>📖 About The Project</h2>
        <p>This project is a simple yet robust implementation of a Large Language Model (LLM) chatbot. The goal was to create a functional and easy-to-understand chatbot application that developers can easily clone, modify, and learn from.</p>
        
        <p><strong>Key Features:</strong></p>
        <ul>
            <li><strong>Conversational Memory:</strong> The chatbot remembers previous messages in the session to provide contextually relevant answers.</li>
            <li><strong>Clean User Interface:</strong> Built with Streamlit for a simple and intuitive chat experience.</li>
            <li><strong>Easy Setup:</strong> Requires minimal setup with a <code>.env</code> file for your API key.</li>
            <li><strong>Model Checker:</strong> Includes a utility script (<code>check_models.py</code>) to help you find the correct Gemini model name available for your specific API key, preventing common <code>404 Not Found</code> errors.</li>
        </ul>

        <h2>🛠️ Tech Stack</h2>
        <p>This project is built with the following technologies:</p>
        <ul>
            <li><strong>Python</strong></li>
            <li><strong>Streamlit:</strong> For creating the interactive web UI.</li>
            <li><strong>Google Generative AI API:</strong> For accessing the Gemini family of models.</li>
            <li><strong>python-dotenv:</strong> For managing environment variables securely.</li>
        </ul>

        <h2>📂 Project Structure</h2>
        <p>Here is a brief overview of the project's file structure:</p>
        <pre><code>gemini-chatbot/
├── .env                  # Stores your secret API key
├── .gitignore            # Specifies files for Git to ignore (like venv)
├── check_models.py       # Utility to list available models for your API key
├── main.py               # The main Streamlit application script
└── requirements.txt      # Lists all the Python dependencies
</code></pre>

        <h2>🚀 Getting Started</h2>
        <p>Follow these steps to set up and run the project on your local machine.</p>

        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.8 or higher installed on your system.</li>
            <li>A Google Account to create a Gemini API key.</li>
        </ul>

        <h3>Installation &amp; Setup</h3>
        <ol>
            <li><strong>Clone the Repository</strong>
                <pre><code>git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name</code></pre>
            </li>
            <li><strong>Create a Virtual Environment</strong>
                <p>It's a best practice to create a virtual environment to manage project dependencies.</p>
                <p><em># For Windows</em></p>
                <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
                <p><em># For macOS/Linux</em></p>
                <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
            </li>
            <li><strong>Install Dependencies</strong>
                <p>Install all the required packages from the <code>requirements.txt</code> file.</p>
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li><strong>Get Your Google Gemini API Key</strong>
                <ul>
                    <li>Go to <a href="https://aistudio.google.com/">Google AI Studio</a>.</li>
                    <li>Sign in with your Google account.</li>
                    <li>Click on <strong>"Get API key"</strong> &gt; <strong>"Create API key in new project"</strong>.</li>
                    <li>Copy the generated API key.</li>
                </ul>
            </li>
            <li><strong>Set Up Your Environment File</strong>
                <ul>
                    <li>Create a new file in the root of your project named <code>.env</code>.</li>
                    <li>Add your API key to this file as shown below:</li>
                </ul>
                <pre><code># .env file
GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"</code></pre>
            </li>
            <li><strong>(Optional but Recommended) Check Your Available Models</strong>
                <p>Google API keys can have access to different model names (e.g., <code>gemini-pro</code> vs. <code>gemini-pro-latest</code>). To avoid errors, run the included script to see which models your key can use.</p>
                <pre><code>python check_models.py</code></pre>
                <ul>
                    <li>The script will print a list of model names. Find the one you want to use (e.g., <code>gemini-pro-latest</code>) and make sure it's the one specified in <code>main.py</code>.</li>
                </ul>
            </li>
            <li><strong>Run the Streamlit App</strong>
                <p>You're all set! Run the following command in your terminal.</p>
                <pre><code>streamlit run main.py</code></pre>
                <ul>
                    <li>Your chatbot will now be running and accessible in your web browser.</li>
                </ul>
            </li>
        </ol>

        <h2>🔗 Connect with Me</h2>
        <p>Feel free to reach out if you have any questions or just want to connect!</p>
        <ul>
            <li><strong>Shubham Kumar</strong></li>
            <li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/shhshubham/">https://www.linkedin.com/in/shhshubham/</a></li>
        </ul>
    </div>
</body>
</html>
