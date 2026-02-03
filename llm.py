from google import genai
client = genai.Client(api_key="AIzaSyDF5aBwrkhZfut4jWa1geQUPEE2yuaRSkg")

def study_assistant(user_prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = user_prompt
    )
    return response.text 

data = study_assistant("what is STRANGER THINGS")
print(data)