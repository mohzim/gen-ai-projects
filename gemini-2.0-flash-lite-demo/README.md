Explanation:

    Import Libraries:
        google.generativeai: For interacting with the Gemini API.
        textwrap: For formatting the output text (wrapping long lines).

    summarize_text_with_gemini(text, api_key, model_name, max_output_tokens) Function:
        Configures the Gemini API with your API key using genai.configure(api_key=api_key).
        Initializes the Gemini model using genai.GenerativeModel(model_name). The default model is set to "gemini-2.0-flash-lite".
        Constructs a prompt that includes the text to be summarized, providing clear instructions to the model.
        Calls the model.generate_content() method to get the summary. The generation_config parameter limits the output length.
        Handles potential errors (e.g., API issues) with a try...except block.
        Returns the summarized text (stripped of extra whitespace) or None if there's an error.

    main() Function:
        Sets the api_key variable. You must replace "YOUR_API_KEY" with your actual API key.
        Defines the text_to_summarize. You can replace this with any text you want to summarize.
        Calls the summarize_text_with_gemini() function.
        Prints the original text and the generated summary, formatting the output for better readability.

Key Points:

    API Key: You must replace "YOUR_API_KEY" with your actual Google Cloud API key. This is essential for the code to work. See How to Get a Google Cloud API Key for instructions.
    Model Selection: The code defaults to "gemini-2.0-flash-lite", but you can change the model_name parameter to use other Gemini models if needed.
    Prompt Engineering: The prompt is crucial for getting good results. You can experiment with different prompts to see how they affect the summary. For example, you could add instructions like "Summarize in three sentences" or "Focus on the key events."
    Error Handling: The code includes basic error handling, but you might want to add more sophisticated error logging or retry mechanisms in a production environment.
    Output Formatting: The textwrap module is used to make the output more readable by wrapping long lines.

To Run This Code:

    Install the Google Generative AI library:
    Bash

pip install google-generativeai

Replace "YOUR_API_KEY" with your actual API key.
Run the Python script:
Bash

python your_script_name.py