import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


def generate():
    import google.auth.credentials
    from google.oauth2 import service_account
    credentials = service_account.Credentials.from_service_account_file(
        "path/to/your/service_account_key.json"
    )

    vertexai.init(project="gcp-xxx", location="us-central1", credentials=credentials)

    model = GenerativeModel(
        # "gemini-1.5-flash-002",
        "gemini-2.0-flash-exp",
    )
    responses = model.generate_content(
        [text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

text1 = """You are a title generation bot. Your task is to create engaging and relevant titles for books based on the provided logline and genre.

Instructions:

1. Carefully consider the logline and genre.
2. Generate five creative title options that capture the essence of the story and appeal to the target audience.
3. Present the titles in a numbered list.

Logline: 

Genre: 

Optional Example: (If you have a specific style or tone in mind, provide an example title here. Otherwise, leave this section blank.)


Output your generated titles here:"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()