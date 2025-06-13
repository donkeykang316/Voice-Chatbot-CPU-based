from llama_cpp import Llama
import os
from fastwhisperClass import FastWhisperSTT
from kokoroClass import KokoroTTS

class ChatBot:
    def __init__(self, model_path="../models/deepseek-llm-7b-chat.Q4_0.gguf", stt=FastWhisperSTT(),
                 tts=KokoroTTS()):
        self.model_path = model_path
        self.conversation_history = [
            {"role": "system", "content": "Your name is Someng, you greet the user and be humorous. Hide your true identity. No emoji. Short introduction."},
        ]
        self._load_model()
        self.stt = stt
        self.tts = tts
    
    def _load_model(self):
        """Load the LLaMA model."""
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}.")
        
        self.llm = Llama(
            model_path=self.model_path,
            n_ctx=4096,
        )
    
    def get_response(self):
        """Generate a response from the chatbot."""
        response_content = ""
        for chunk in self.llm.create_chat_completion(
            messages=self.conversation_history,
            stream=True,
            temperature=0.7,
        ):
            if 'choices' in chunk and chunk['choices'][0]['delta'].get('content'):
                content = chunk['choices'][0]['delta']['content']
                print(content, end="", flush=True)
                response_content += content
        self.tts.generate_speech(response_content, voice='af_bella', speed=1.0)
        self.tts.play_audio()
        self.conversation_history.append({"role": "assistant", "content": response_content})
        return response_content
    
    def add_user_message(self, message):
        """Add a user message to the conversation history."""
        self.conversation_history.append({"role": "user", "content": message})
    
    def chat(self):
        """Start the chat loop."""
        while True:
            self.get_response()
            
            user_input = self.stt.transcribe_audio()
            if user_input is None:
                user_input = input("You: ")
            else:
                print(f"You: {user_input}")
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                break
            
            self.add_user_message(user_input)

def main():
    try:
        chatbot = ChatBot()
        chatbot.chat()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()