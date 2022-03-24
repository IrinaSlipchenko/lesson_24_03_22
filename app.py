from flask import Flask, request, jsonify

from tools.misc import make_resp, check_keys
from users.repo import InMemoryUserRepo

app = Flask(__name__)
app.user_repo = InMemoryUserRepo


@app.route("/")
def root():
    return app.send_static_file("index.html")


@app.route("/api/register", methods=['POST'])
def user_register():
    in_json = request.json()
    if not in_json:
        return make_resp(jsonify({"message": "Empty request"}), 400)
    elif not check_keys(request.json(), {"username", "password"}):
        return make_resp(jsonify({"message": "Bad request"}), 400)
    created_user = app.user_repo.request_create(**in_json)
    if not created_user:
        return make_resp(jsonify({"message": "Duplicated user"}), 400)


if __name__ == "__main__":
    app.run()

