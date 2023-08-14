from flask import Blueprint, request, jsonify
from controllers import chatgpt_controller

chatgpt_route = Blueprint('chatgpt_route', __name__)

@chatgpt_route.route('/api/v1/ask', methods=['POST'])
def ask():
    question = request.json['question']
    answer = chatgpt_controller.ask_gpt(question)
    return jsonify(answer=answer)
