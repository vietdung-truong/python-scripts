import boto3
import json

prompt_data = """
what's up?
"""

bedrock = boto3.client(service_name="bedrock-runtime")
payload = {
    "promtp" : f"\n\nHuman: {prompt_data}\n\nAssistant:",
    "max_token_to_sample": 512,
    "temperature": 0.8,
    "top_p": 0.8,
}
body = json.dumps(payload)
model_id = "amazon.titan-text-express-v1"
response = bedrock.invoke_model(
    body=body,
    model_id=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completion")
print(response_text)