import os
import google.generativeai as genai
import textwrap

def summarize_text_with_gemini(text, api_key, model_name="gemini-2.0-flash-lite", max_output_tokens=500):
    """
    Summarizes the given text using the specified Gemini model.

    Args:
        text (str): The text to be summarized.
        api_key (str): Your Google Cloud API key.
        model_name (str, optional): The name of the Gemini model to use.
            Defaults to "gemini-2.0-flash-lite".
        max_output_tokens (int, optional): The maximum number of tokens in the summary.
            Defaults to 500.

    Returns:
        str: The summarized text, or None if an error occurs.
    """
    # Set the API key for Google Generative AI
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(model_name)

    prompt = f"""
    Summarize the following text, focusing on the key points:

    {text}
    """

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_output_tokens
            ),
        )
        # Check if a valid response and text are available
        if response and response.text:
            return response.text.strip()  # Remove leading/trailing spaces
        else:
            print("Error: No text generated in the response.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to run the text summarization.
    """
    # Replace with your actual API key
    # api_key = ""  #  <-----------------------  Replace this
    
    # Ensure the API key is set in the environment variable
    api_key = os.getenv("GOOGLE_CLOUD_API_KEY") 

    # Example text to summarize (replace with your text)
    text_to_summarize = """
    The Hubble Space Telescope is a space telescope that was launched into low Earth orbit in 1990 and remains in operation. It was not the first space telescope, but it is one of the largest and most versatile. It is well known as both a vital research tool and a public relations boon for astronomy.

    Hubble was built by U.S. space agency NASA with contributions from the European Space Agency. It was named after astronomer Edwin Hubble. The telescope comprises a 2.4-meter (7 ft 10 in) reflecting telescope, and five main instruments. Hubble's five main instruments observe in the ultraviolet, visible, and near-infrared regions of the electromagnetic spectrum. The telescope is operated by NASA's Goddard Space Flight Center.

    Repair missions were crucial to the telescope's success. Five Space Shuttle missions repaired, upgraded, and replaced systems on the Hubble Space Telescope, including installing corrective optics to compensate for the primary mirror's defect. The fifth mission in 2009 installed the Wide Field Camera 3 and the Cosmic Origins Spectrograph.
    """

    if not api_key:
        print("Error: Please provide your Google Cloud API key.  You need to replace 'YOUR_API_KEY' with your key.")
        return

    print("Text to Summarize:")
    print(textwrap.fill(text_to_summarize, width=80))
    print("\n")

    summary = summarize_text_with_gemini(text_to_summarize, api_key)

    if summary:
        print("Summary:")
        print(textwrap.fill(summary, width=80))
    else:
        print("Failed to generate summary.")


if __name__ == "__main__":
    main()
