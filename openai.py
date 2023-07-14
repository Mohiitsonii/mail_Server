import openai
import mailbody

openai.api_key = "YOUR_OPENAI_API_KEY"


def generate_email_body():
    prompt = """Write the content for your email:\nSubject: {}\n\n""".format(
        mailbody.subject)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        n=1,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    email_body = response.choices[0].text.strip()
    return email_body


if mailbody.set_attachment:
    # Add your code for attaching the file here
    pass

# Rest of your code for sending the email with the generated body
# ...
