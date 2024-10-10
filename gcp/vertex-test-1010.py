# Should uninstall previous sdk: pip uninstall -q -y vertexai google-cloud-aiplatform
# Should install specific version: pip install -q -U "vertexai==1.65.0" "google-cloud-aiplatform==1.65.0"

from vertexai.generative_models import GenerativeModel

model = GenerativeModel("gemini-pro")
# print(model.generate_content("Why is sky blue?"))

user_input = "Why is sky blue?"

print("##### \n User Input: \n", user_input)

response = model.generate_content(user_input)

# if response contains candidates, print the first candidate
if response.candidates:
    print("\n#### Response: \n", response.candidates[0].content.text, "\n#####\n")

