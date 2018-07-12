from flask import Flask, request, Response

from src.spotify.spotify import is_related


def create_app(debug=True):
    """
    Simple application factory and the API route and response
    """
    app = Flask(__name__)

    @app.route('/related', methods=['GET'])
    def relation():
        first = request.args['first_artist']
        second = request.args['second_artist']

        check = is_related(first, second)

        if check is True:
            return Response("Artists are related", status=200)
        else:
            return Response("Artists are not related", status=404)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
