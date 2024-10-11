from flask import Flask, render_template, request

app = Flask(__name__)

# Define the available options for agents, types, and interactions
agents = ['Agent 1', 'Agent 2', 'Agent 3']
types = ['Type A', 'Type B', 'Type C']
interactions = ['Interaction X', 'Interaction Y', 'Interaction Z']

@app.route('/')
def index():
    return render_template('index.html', agents=agents, types=types, interactions=interactions)

@app.route('/submit', methods=['POST'])
def submit():
    selected_agent = request.form.get('agent')
    selected_type = request.form.get('type')
    selected_interaction = request.form.get('interaction')

    # Process the selected options
    return f'Selected Agent: {selected_agent}, Type: {selected_type}, Interaction: {selected_interaction}'

@app.route('/add_agent', methods=['POST'])
def add_agent():
    new_agent = request.form.get('new_agent')
    agents.append(new_agent)
    return f'Added new agent: {new_agent}'

@app.route('/edit_agent', methods=['POST'])
def edit_agent():
    # Implement edit agent functionality here (example, placeholder)
    edited_agent = request.form.get('edit_agent')
    return f'Edited agent: {edited_agent}'

if __name__ == '__main__':
    app.run(debug=True)
