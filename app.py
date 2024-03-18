

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()


def index():
    data = request.get_json()
    return data['challenge']

def index():
    request_secret = request.headers['Secret']
    if request_secret != os.environ['SECRET']:
        return ('Unauthorized', 401)
    
def index():
    data = request.get_json()
    return ('', 200)