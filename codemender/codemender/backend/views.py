from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def analyze_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code')
        error_message = data.get('errorMessage')
        
        # Prepare the prompt for GPT
        prompt = f"""
        Analyze the following code and error message:
        
        Code:
        {code}
        
        Error Message:
        {error_message}
        
        Please provide a detailed explanation of why the code doesn't work and suggest possible fixes.
        """
        
        try:
            # Make the API call to OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",  
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that analyzes code and error messages."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500  
            )
            
            # Extract the response text
            analysis = response.choices[0].message['content'].strip()
            
            return JsonResponse({'response': analysis})
        
        except Exception as e:
            # Handle any errors that occur during the API call
            return JsonResponse({'error': str(e)}, status=500)

def health_check(request):
    print("Running health check...")
    return JsonResponse({'status': 'healthy'})
